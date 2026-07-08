import os
import re
import yaml
import html
import json
import uuid
import base64


def define_env(env):
    @env.macro
    def task(file=None, **parameter):
        params = dict()

        if file:
            file_path = os.path.join(env.project_dir, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                params.update(yaml.safe_load(file))

        params.update(parameter)

        return create_task(**params)

    @env.macro
    def quiz(file=None, **parameter):
        params = dict()

        if file:
            file_path = os.path.join(env.project_dir, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                params.update(yaml.safe_load(file))

        params.update(parameter)

        return create_quiz(**params)

    @env.macro
    def youtube_video(inner_url, title='Video'):
        return youtube_video_admonition(inner_url, title)

    @env.macro
    def python_tutor(code_string, title="Code im Debugger"):
        return generate_pythontutor_iframe(code_string, title=title)

    @env.macro
    def python_tutor_button(code_string, title="Code im Debugger ansehen"):
        return generate_pythontutor_button(code_string, title=title)
    
    @env.macro
    def link(text="", url="", new_tab=True, icon=":fontawesome-solid-external-link:"):
        result = f'[{icon} {text}]({url})'
        if new_tab:
            result +='{ target=_blank rel="noopener noreferrer" }'
        return result


def youtube_video_admonition(inner_url, title='Video'):
    return f'''??? video "{title}"

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{inner_url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>'''


def create_task(title="Aufgabe",
                question="⚠QUESTION_TEXT_MISSING⚠",
                solution="",
                tip="",
                difficulty=0,
                difficulty_icon='🌶',
                collapsed=False,
                solution_video=None,
                question_video=None):
    question = render_embedded_macros(question)
    tip = render_embedded_macros(tip)
    solution = render_embedded_macros(solution)

    difficulty_icons = difficulty * difficulty_icon + (" " if difficulty else "")
    collapsed_symbol = "" if collapsed else "+"

    result = f'???{collapsed_symbol} question "{difficulty_icons}{title}"\n'
    if question_video:
        result += add_tabs(youtube_video_admonition(question_video))

    result += add_tabs(question)
    if tip:
        result += add_tabs(f'??? info "Tipp"\n') + add_tabs(tip, 2)
    if solution:
        result += add_tabs(f'??? success "Lösung"\n')
        if solution_video:
            result += add_tabs(youtube_video_admonition(solution_video, "Lösungsvideo"), 2)
        result += add_tabs(solution, 2)
    return result


def create_quiz(
    title="Quiz",
    questions=None,
    description="",
    collapsed=False,
    exam_mode=False,
    duration_minutes=None,
    passing_score=None,
):
    questions = questions or []
    quiz_id = f"quiz-{uuid.uuid4().hex}"
    escaped_title = html.escape(title)
    escaped_description = html.escape(description)
    open_attr = "" if collapsed else " open"
    duration = int(duration_minutes) if duration_minutes else None

    result_parts = [
        f'<details class="question"{open_attr}>',
        f'<summary>{escaped_title}</summary>',
    ]
    if description:
        result_parts.append(f'<p>{escaped_description}</p>')

    result_parts.append(
        f'<form class="interactive-quiz" id="{quiz_id}" '
        f'data-exam-mode="{str(bool(exam_mode)).lower()}"'
        f'{f" data-duration-minutes=\"{duration}\"" if duration else ""}'
        f'{f" data-passing-score=\"{passing_score}\"" if passing_score is not None else ""}>'
    )
    if exam_mode and duration:
        result_parts.append(
            '<div class="quiz-exam-bar">'
            '<span class="quiz-timer" aria-live="polite">Zeit: --:--</span>'
            '</div>'
        )

    def render_option_label(option, fallback):
        label_text = str(option.get("label", fallback))
        if option.get("code"):
            match = re.match(r"^([A-Z]\.\s*)(.*)$", label_text, re.S)
            if match:
                prefix = html.escape(match.group(1))
                body = html.escape(match.group(2)).replace("\n", "<br>")
                return f'<span class="quiz-option-prefix">{prefix}</span><code>{body}</code>'
            body = html.escape(label_text).replace("\n", "<br>")
            return f'<code>{body}</code>'

        return html.escape(label_text).replace("\n", "<br>")

    answers = []
    for index, question in enumerate(questions):
        q_type = question.get("type", "text")
        prompt = html.escape(str(question.get("prompt", ""))).replace("\n", "<br>")
        code = question.get("code")
        explanation = html.escape(str(question.get("explanation", "")))
        answer = question.get("answer")
        options = question.get("options", [])
        points = question.get("points", 1)
        q_name = f"{quiz_id}-q{index}"

        answers.append({
            "type": q_type,
            "answer": answer,
            "explanation": explanation,
            "points": points,
        })

        result_parts.append('<div class="quiz-question">')
        result_parts.append(f'<p><strong>{index + 1}. {prompt}</strong></p>')
        if code is not None:
            result_parts.append(
                f'<pre><code>{html.escape(str(code))}</code></pre>'
            )
        post_prompt = question.get("post_prompt")
        if post_prompt:
            result_parts.append(
                f'<p>{html.escape(str(post_prompt)).replace(chr(10), "<br>")}</p>'
            )

        if q_type == "single":
            for option_index, option in enumerate(options):
                option_id = f"{q_name}-{option_index}"
                value = html.escape(str(option.get("value", option.get("label", ""))))
                label = render_option_label(option, value)
                result_parts.append(
                    f'<label class="quiz-option" for="{option_id}">'
                    f'<input id="{option_id}" type="radio" name="{q_name}" value="{value}"> '
                    f'{label}</label>'
                )
        elif q_type == "multiple":
            for option_index, option in enumerate(options):
                option_id = f"{q_name}-{option_index}"
                value = html.escape(str(option.get("value", option.get("label", ""))))
                label = render_option_label(option, value)
                result_parts.append(
                    f'<label class="quiz-option" for="{option_id}">'
                    f'<input id="{option_id}" type="checkbox" name="{q_name}" value="{value}"> '
                    f'{label}</label>'
                )
        elif q_type == "output":
            placeholder = html.escape(str(question.get("placeholder", "Expected Output eingeben")))
            result_parts.append(
                f'<textarea class="quiz-text-input quiz-output-input" name="{q_name}" '
                f'placeholder="{placeholder}" rows="4"></textarea>'
            )
        else:
            placeholder = html.escape(str(question.get("placeholder", "Antwort eingeben")))
            result_parts.append(
                f'<input class="quiz-text-input" type="text" name="{q_name}" '
                f'placeholder="{placeholder}" autocomplete="off">'
            )

        if not exam_mode:
            result_parts.append(
                f'<button type="button" class="md-button quiz-check-one" '
                f'data-question-index="{index}">Diese Frage prüfen</button>'
            )
        result_parts.append('<p class="quiz-feedback" aria-live="polite"></p>')
        result_parts.append('</div>')

    check_label = "Test auswerten" if exam_mode else "Prüfen"
    result_parts.append(f'<button type="button" class="md-button md-button--primary quiz-check">{check_label}</button>')
    result_parts.append('<button type="reset" class="md-button quiz-reset">Zurücksetzen</button>')
    result_parts.append('<p class="quiz-summary" aria-live="polite"></p>')
    result_parts.append('</form>')

    result_parts.append('''<style>
.interactive-quiz {
  display: grid;
  gap: 1rem;
}
.quiz-question {
  border-left: 0.2rem solid var(--md-accent-fg-color);
  padding: 0.6rem 0.8rem;
  background: var(--md-code-bg-color);
}
.quiz-exam-bar {
  display: flex;
  justify-content: flex-end;
  position: sticky;
  top: 3rem;
  z-index: 2;
}
.quiz-timer {
  padding: 0.35rem 0.6rem;
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 0.2rem;
  background: var(--md-default-bg-color);
  font-weight: 700;
}
.quiz-option {
  display: block;
  margin: 0.35rem 0;
}
.quiz-option-prefix {
  display: inline-block;
  min-width: 1.6rem;
}
.quiz-option code {
  white-space: pre-wrap;
  vertical-align: top;
}
.quiz-text-input {
  width: min(100%, 32rem);
  padding: 0.45rem 0.55rem;
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 0.2rem;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
}
.quiz-output-input {
  font-family: var(--md-code-font-family);
  min-height: 6rem;
}
.quiz-check-one {
  margin-top: 0.55rem;
}
.quiz-feedback {
  margin: 0.45rem 0 0;
  font-weight: 600;
}
.quiz-feedback.correct {
  color: #2e7d32;
}
.quiz-feedback.incorrect {
  color: #c62828;
}
.quiz-summary {
  font-weight: 700;
}
</style>''')

    payload = base64.b64encode(json.dumps(answers, ensure_ascii=False).encode("utf-8")).decode("ascii")
    result_parts.append(f'<script type="application/json" id="{quiz_id}-answers">{payload}</script>')
    result_parts.append(f'''<script>
(function() {{
  const form = document.getElementById("{quiz_id}");
  const dataNode = document.getElementById("{quiz_id}-answers");
  if (!form || !dataNode) return;
  const answers = JSON.parse(decodeURIComponent(escape(atob(dataNode.textContent))));
  const examMode = form.dataset.examMode === "true";
  const durationMinutes = Number(form.dataset.durationMinutes || 0);
  const passingScore = form.dataset.passingScore ? Number(form.dataset.passingScore) : null;
  let finished = false;
  let timerInterval = null;

  function normalize(value) {{
    return String(value ?? "").trim().toLowerCase().replace(/\\s+/g, " ");
  }}

  function arraysEqual(a, b) {{
    const left = [...a].map(normalize).sort();
    const right = [...b].map(normalize).sort();
    return left.length === right.length && left.every((value, index) => value === right[index]);
  }}

  function checkQuestion(index, reveal = true) {{
    const question = answers[index];
    const name = "{quiz_id}-q" + index;
    const container = form.querySelectorAll(".quiz-question")[index];
    const feedback = container.querySelector(".quiz-feedback");

    let correct = false;
    if (question.type === "single") {{
      const selected = form.querySelector('input[name="' + name + '"]:checked');
      correct = selected && normalize(selected.value) === normalize(question.answer);
    }} else if (question.type === "multiple") {{
      const selected = Array.from(form.querySelectorAll('input[name="' + name + '"]:checked')).map(input => input.value);
      correct = arraysEqual(selected, Array.isArray(question.answer) ? question.answer : [question.answer]);
    }} else {{
      const input = form.querySelector('[name="' + name + '"]');
      const validAnswers = Array.isArray(question.answer) ? question.answer : [question.answer];
      correct = input && validAnswers.some(answer => normalize(input.value) === normalize(answer));
    }}

    if (reveal) {{
      if (correct) {{
        feedback.textContent = "Richtig.";
        feedback.className = "quiz-feedback correct";
      }} else {{
        feedback.textContent = "Nicht richtig." + (question.explanation ? " " + question.explanation : "");
        feedback.className = "quiz-feedback incorrect";
      }}
    }}

    return correct;
  }}

  function finishQuiz() {{
    if (finished) return;
    finished = true;
    let score = 0;
    let total = 0;

    answers.forEach(function(question, index) {{
      total += Number(question.points || 1);
      if (checkQuestion(index, true)) {{
        score += Number(question.points || 1);
      }}
    }});

    let summary = "Ergebnis: " + score + " von " + total + " Punkten.";
    if (passingScore !== null) {{
      summary += score >= passingScore ? " Bestanden." : " Nicht bestanden.";
    }}
    form.querySelector(".quiz-summary").textContent = summary;
    if (examMode) {{
      form.querySelectorAll("input, textarea, button").forEach(node => {{
        if (!node.classList.contains("quiz-reset")) node.disabled = true;
      }});
    }}
  }}

  function startTimer() {{
    if (!examMode || !durationMinutes) return;
    const timer = form.querySelector(".quiz-timer");
    if (!timer) return;
    if (timerInterval) clearInterval(timerInterval);
    let remaining = durationMinutes * 60;
    const render = function() {{
      const minutes = Math.floor(remaining / 60);
      const seconds = remaining % 60;
      timer.textContent = "Zeit: " + String(minutes).padStart(2, "0") + ":" + String(seconds).padStart(2, "0");
    }};
    render();
    timerInterval = setInterval(function() {{
      if (finished) {{
        clearInterval(timerInterval);
        return;
      }}
      remaining -= 1;
      render();
      if (remaining <= 0) {{
        clearInterval(timerInterval);
        finishQuiz();
      }}
    }}, 1000);
  }}

  form.querySelectorAll(".quiz-check-one").forEach(button => {{
    button.addEventListener("click", function() {{
      const index = Number(button.dataset.questionIndex);
      checkQuestion(index);
      form.querySelector(".quiz-summary").textContent = "";
    }});
  }});

  form.querySelector(".quiz-check").addEventListener("click", function() {{
    finishQuiz();
  }});

  form.addEventListener("reset", function() {{
    setTimeout(function() {{
      form.querySelectorAll(".quiz-feedback").forEach(node => {{
        node.textContent = "";
        node.className = "quiz-feedback";
      }});
      form.querySelector(".quiz-summary").textContent = "";
      finished = false;
      form.querySelectorAll("input, textarea, button").forEach(node => {{
        node.disabled = false;
      }});
      startTimer();
    }}, 0);
  }});
  startTimer();
}})();
</script>''')
    result_parts.append('</details>')
    return "\n".join(result_parts)


def add_tabs(text, tabs=1):
    return ('\n' + text).replace('\n', '\n' + '\t' * tabs)


embedded_youtube_re = re.compile(
    r'\{\{\s*youtube_video\(\s*([\'"])(.*?)\1\s*(?:,\s*([\'"])(.*?)\3\s*)?\)\s*\}\}'
)


def render_embedded_macros(text):
    if not text:
        return text

    def replace_youtube(match):
        return youtube_video_admonition(match.group(2), match.group(4) or "Video")

    return embedded_youtube_re.sub(replace_youtube, text)


import urllib.parse


def generate_pythontutor_iframe(code_string, title='Python Tutor'):
    base_url = "https://pythontutor.com/iframe-embed.html"

    # Encoding des Codes
    encoded_code = urllib.parse.quote(code_string)

    # Dynamische Berechnung der Höhe basierend auf der Anzahl der Zeilen im Code
    line_count = code_string.count('\n') + 1
    code_div_height = max(line_count * 25, 400)  # Mindestens 400 px, ansonsten 25 px pro Zeile

    # Parameter für den Hash-Teil der URL
    hash_params = {
        "code": encoded_code,
        "cumulative": "false",
        "curInstr": "0",
        "heapPrimitives": "nevernest",
        "origin": "opt-frontend.js",
        "py": "3",
        "rawInputLstJSON": "[]",
        "textReferences": "false",
        "codeDivHeight": str(code_div_height),
        "codeDivWidth": "350"  # Feste Breite für den Code-Editor
    }

    # Hash-String zusammenbauen
    hash_string = "&".join(f"{key}={value}" for key, value in hash_params.items())
    full_url = f"{base_url}#{hash_string}"

    # Generieren des iframe-Tags im Container
    iframe_tag = f'''!!! python_tutor "{title}"

    <div class="python_tutor_container">
        <iframe src="{full_url}" title="{title}" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin" allowfullscreen
        style="width: 100%; height: {code_div_height}px;">
        </iframe>
    </div>
    '''

    return iframe_tag


def generate_pythontutor_button(code_string, title='Python Tutor'):
    base_url = "https://pythontutor.com/render.html"

    # Encoding des Codes
    encoded_code = urllib.parse.quote(code_string)

    # Parameter für den Hash-Teil der URL
    hash_params = {
        "code": encoded_code,
        "cumulative": "false",
        "curInstr": "0",
        "heapPrimitives": "nevernest",
        "origin": "opt-frontend.js",
        "py": "3",
        "rawInputLstJSON": "[]",
        "textReferences": "false"
    }

    # Hash-String zusammenbauen
    hash_string = "&".join(f"{key}={value}" for key, value in hash_params.items())
    full_url = f"{base_url}#{hash_string}"

    # Generieren des Button-Tags im Container
    button_tag = f'<a href="{full_url}" target="_blank" class="md-button" rel="noopener noreferrer">{title}</a>'

    return button_tag
