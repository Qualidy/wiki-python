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


def create_quiz(title="Quiz", questions=None, description="", collapsed=False):
    questions = questions or []
    quiz_id = f"quiz-{uuid.uuid4().hex}"
    escaped_title = html.escape(title)
    escaped_description = html.escape(description)
    open_attr = "" if collapsed else " open"

    result_parts = [
        f'<details class="question"{open_attr}>',
        f'<summary>{escaped_title}</summary>',
    ]
    if description:
        result_parts.append(f'<p>{escaped_description}</p>')

    result_parts.append(f'<form class="interactive-quiz" id="{quiz_id}">')

    answers = []
    for index, question in enumerate(questions):
        q_type = question.get("type", "text")
        prompt = html.escape(str(question.get("prompt", "")))
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

        if q_type == "single":
            for option_index, option in enumerate(options):
                option_id = f"{q_name}-{option_index}"
                value = html.escape(str(option.get("value", option.get("label", ""))))
                label = html.escape(str(option.get("label", value)))
                result_parts.append(
                    f'<label class="quiz-option" for="{option_id}">'
                    f'<input id="{option_id}" type="radio" name="{q_name}" value="{value}"> '
                    f'{label}</label>'
                )
        elif q_type == "multiple":
            for option_index, option in enumerate(options):
                option_id = f"{q_name}-{option_index}"
                value = html.escape(str(option.get("value", option.get("label", ""))))
                label = html.escape(str(option.get("label", value)))
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

        result_parts.append('<p class="quiz-feedback" aria-live="polite"></p>')
        result_parts.append('</div>')

    result_parts.append('<button type="button" class="md-button md-button--primary quiz-check">Prüfen</button>')
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
.quiz-option {
  display: block;
  margin: 0.35rem 0;
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

  function normalize(value) {{
    return String(value ?? "").trim().toLowerCase().replace(/\\s+/g, " ");
  }}

  function arraysEqual(a, b) {{
    const left = [...a].map(normalize).sort();
    const right = [...b].map(normalize).sort();
    return left.length === right.length && left.every((value, index) => value === right[index]);
  }}

  form.querySelector(".quiz-check").addEventListener("click", function() {{
    let score = 0;
    let total = 0;

    answers.forEach(function(question, index) {{
      const name = "{quiz_id}-q" + index;
      const container = form.querySelectorAll(".quiz-question")[index];
      const feedback = container.querySelector(".quiz-feedback");
      total += Number(question.points || 1);

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
        correct = validAnswers.some(answer => normalize(input.value) === normalize(answer));
      }}

      if (correct) {{
        score += Number(question.points || 1);
        feedback.textContent = "Richtig.";
        feedback.className = "quiz-feedback correct";
      }} else {{
        feedback.textContent = "Noch nicht richtig." + (question.explanation ? " " + question.explanation : "");
        feedback.className = "quiz-feedback incorrect";
      }}
    }});

    form.querySelector(".quiz-summary").textContent = "Ergebnis: " + score + " von " + total + " Punkten.";
  }});

  form.addEventListener("reset", function() {{
    setTimeout(function() {{
      form.querySelectorAll(".quiz-feedback").forEach(node => {{
        node.textContent = "";
        node.className = "quiz-feedback";
      }});
      form.querySelector(".quiz-summary").textContent = "";
    }}, 0);
  }});
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
