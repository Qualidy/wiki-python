#!/usr/bin/env python3
"""Import extracted PCAP mock tests into MkDocs pages.

Input is the intermediate directory created by extract_pcap_epub.py.
The script writes:

    docs/content/pcap/testexam_1.md
    docs/content/pcap/testexam_2.md
    docs/assets/pcap_exam/<images>
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any


def block_to_markdown(block: dict[str, Any], asset_prefix: str) -> str:
    block_type = block.get("type")
    if block_type == "heading":
        level = min(int(block.get("level", 2)), 6)
        return f"{'#' * level} {block.get('text', '')}"
    if block_type == "paragraph":
        return block.get("text", "")
    if block_type == "list":
        return "\n".join(f"- {item}" for item in block.get("items", []))
    if block_type == "image":
        src = block.get("src", "")
        alt = block.get("alt", "")
        return f"![{alt}]({asset_prefix}/{Path(src).name})"
    if block_type == "page":
        return f"<!-- {block.get('page_id')} -->"
    return ""


def extract_answer_letters(answer_text: str) -> list[str]:
    return re.findall(r"\b[A-Z]\b", answer_text.partition(":")[2])


def find_answer_index(blocks: list[dict[str, Any]]) -> int | None:
    for index, block in enumerate(blocks):
        if block.get("type") == "paragraph" and block.get("text", "").strip().startswith("Answer:"):
            return index
    return None


def find_option_index(blocks: list[dict[str, Any]], answer_index: int) -> int | None:
    for index in range(answer_index - 1, -1, -1):
        if blocks[index].get("type") == "list":
            return index
    return None


def render_blocks(blocks: list[dict[str, Any]], asset_prefix: str) -> list[str]:
    rendered: list[str] = []
    for block in blocks:
        md = block_to_markdown(block, asset_prefix)
        if md:
            rendered.append(md)
    return rendered


def render_quiz_options(items: list[str], answer_letters: list[str]) -> str:
    answer_value = ",".join(answer_letters)
    options: list[str] = [
        f'<div class="pcap-options" data-answer="{html.escape(answer_value)}">'
    ]
    for index, item in enumerate(items):
        letter = chr(ord("A") + index)
        options.append(
            '<label class="pcap-option">'
            f'<input type="checkbox" value="{letter}"> '
            f'<span class="pcap-option-letter">{letter}.</span> '
            f'<span>{html.escape(item)}</span>'
            '</label>'
        )
    options.extend(
        [
            '<button type="button" class="pcap-check">Antwort prüfen</button>',
            '<p class="pcap-feedback" aria-live="polite"></p>',
            '</div>',
        ]
    )
    return "\n".join(options)


def render_question(question: dict[str, Any], asset_prefix: str) -> list[str]:
    blocks = question.get("blocks", [])
    answer_index = find_answer_index(blocks)
    if answer_index is None:
        return render_blocks(blocks[1:], asset_prefix)

    answer_text = blocks[answer_index].get("text", "")
    answer_letters = extract_answer_letters(answer_text)
    option_index = find_option_index(blocks, answer_index)

    if option_index is None:
        question_blocks = blocks[1:answer_index]
        option_items: list[str] = []
    else:
        question_blocks = blocks[1:option_index]
        option_items = blocks[option_index].get("items", [])

    rendered: list[str] = render_blocks(question_blocks, asset_prefix)

    if option_items and answer_letters:
        rendered.append(render_quiz_options(option_items, answer_letters))
        rendered.append('<details class="pcap-solution" hidden markdown="1">')
        rendered.append('<summary>Lösung und Erklärung</summary>')
    else:
        rendered.append("!!! warning \"Hinweis\"")
        rendered.append("    Bei dieser Frage wurden die Antwortoptionen nicht sauber als Liste erkannt.")
        rendered.append("")
        rendered.append('<button type="button" class="pcap-reveal">Lösung anzeigen</button>')
        rendered.append('<details class="pcap-solution" hidden markdown="1">')
        rendered.append('<summary>Lösung und Erklärung</summary>')
        rendered.extend(render_blocks(blocks[1:answer_index], asset_prefix))

    rendered.append(f"**{answer_text}**")
    rendered.extend(render_blocks(blocks[answer_index + 1 :], asset_prefix))
    rendered.append("</details>")

    return rendered


def write_test_page(test: dict[str, Any], number: int, docs_dir: Path) -> None:
    page_path = docs_dir / "content" / "pcap" / f"testexam_{number}.md"
    asset_prefix = "../../assets/pcap_exam"

    parts: list[str] = [
        f"# Testexam {number}",
        "Kreuze die passende Antwort an. Die Lösung und Erklärung wird erst nach dem Prüfen angezeigt.",
        "",
        "!!! note \"Hinweis\"",
        "    Einige Code-Snippets liegen als Bilder vor, weil sie im Ausgangsmaterial als Bild gespeichert sind.",
        "",
    ]

    for question in test.get("questions", []):
        parts.append(f"## Question {question['number']}")
        parts.extend(render_question(question, asset_prefix))

    page_path.write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")


def copy_assets(extract_dir: Path, docs_dir: Path) -> None:
    source_assets = extract_dir / "assets"
    target_assets = docs_dir / "assets" / "pcap_exam"
    target_assets.mkdir(parents=True, exist_ok=True)
    if not source_assets.exists():
        return
    for source in source_assets.iterdir():
        if source.is_file():
            shutil.copy2(source, target_assets / source.name)


def main() -> None:
    parser = argparse.ArgumentParser(description="Import extracted PCAP mock tests into the wiki docs.")
    parser.add_argument("extract_dir", type=Path, help="Directory produced by extract_pcap_epub.py")
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"), help="MkDocs docs directory")
    args = parser.parse_args()

    mock_tests_path = args.extract_dir / "mock_tests.json"
    tests = json.loads(mock_tests_path.read_text(encoding="utf-8"))
    if len(tests) < 2:
        raise SystemExit(f"Expected at least 2 mock tests in {mock_tests_path}, found {len(tests)}")

    copy_assets(args.extract_dir, args.docs_dir)
    for index, test in enumerate(tests[:2], start=1):
        write_test_page(test, index, args.docs_dir)

    print(f"Imported {min(len(tests), 2)} testexam page(s) into {args.docs_dir / 'content' / 'pcap'}")


if __name__ == "__main__":
    main()
