#!/usr/bin/env python3
"""Extract an EPUB into a local intermediate format.

The EPUB used for the PCAP preparation stores many code snippets as images.
This extractor therefore keeps text blocks and image references, and can copy
the referenced images into the output directory.

Output structure:

    output/
      manifest.json
      chapters/
        OEBPS_part0007.json
        OEBPS_part0007.md
      assets/
        image_rsrcF6A.jpg
      mock_tests.json
      mock_tests.md
"""

from __future__ import annotations

import argparse
import html.parser
import json
import posixpath
import re
import shutil
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


XHTML_NS = "{http://www.w3.org/1999/xhtml}"
NCX_NS = "{http://www.daisy.org/z3986/2005/ncx/}"


@dataclass
class Block:
    type: str
    text: str | None = None
    level: int | None = None
    items: list[str] | None = None
    src: str | None = None
    alt: str | None = None
    page_id: str | None = None
    class_name: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v not in (None, [], "")}


class XHTMLBlockParser(html.parser.HTMLParser):
    BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[Block] = []
        self._tag_stack: list[tuple[str, dict[str, str]]] = []
        self._text_stack: list[list[str]] = []
        self._list_stack: list[list[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: v or "" for k, v in attrs}
        self._tag_stack.append((tag, attr))

        if tag in self.BLOCK_TAGS:
            self._text_stack.append([])

        if tag in {"ol", "ul"}:
            self._list_stack.append([])

        if tag == "img":
            src = attr.get("src", "")
            alt = attr.get("alt", "")
            self.blocks.append(
                Block(
                    type="image",
                    src=src,
                    alt=alt,
                    class_name=attr.get("class", ""),
                )
            )

        if "id" in attr and attr["id"].startswith("page_"):
            self.blocks.append(Block(type="page", page_id=attr["id"]))

    def handle_endtag(self, tag: str) -> None:
        if tag in self.BLOCK_TAGS and self._text_stack:
            text = normalize_text("".join(self._text_stack.pop()))
            if text:
                if tag == "li" and self._list_stack:
                    self._list_stack[-1].append(text)
                elif tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
                    self.blocks.append(Block(type="heading", level=int(tag[1]), text=text))
                else:
                    self.blocks.append(Block(type="paragraph", text=text))

        if tag in {"ol", "ul"} and self._list_stack:
            items = self._list_stack.pop()
            if items:
                self.blocks.append(Block(type="list", items=items))

        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._text_stack:
            self._text_stack[-1].append(data)


def normalize_text(text: str) -> str:
    return " ".join(text.replace("\xa0", " ").split())


def read_text(zip_file: zipfile.ZipFile, name: str) -> str:
    return zip_file.read(name).decode("utf-8", "ignore")


def parse_nav(zip_file: zipfile.ZipFile) -> list[dict[str, str]]:
    if "OEBPS/nav.xhtml" in zip_file.namelist():
        root = ElementTree.fromstring(read_text(zip_file, "OEBPS/nav.xhtml"))
        nav_items: list[dict[str, str]] = []
        for nav in root.iter(f"{XHTML_NS}nav"):
            if nav.attrib.get("{http://www.idpf.org/2007/ops}type") == "toc":
                for link in nav.iter(f"{XHTML_NS}a"):
                    href = link.attrib.get("href", "")
                    title = normalize_text("".join(link.itertext()))
                    if href and title:
                        nav_items.append({"title": title, "href": posixpath.join("OEBPS", href)})
                return nav_items

    if "OEBPS/toc.ncx" in zip_file.namelist():
        root = ElementTree.fromstring(read_text(zip_file, "OEBPS/toc.ncx"))
        nav_items = []
        for point in root.iter(f"{NCX_NS}navPoint"):
            label = point.find(f".//{NCX_NS}text")
            content = point.find(f"{NCX_NS}content")
            if label is not None and content is not None:
                src = content.attrib.get("src", "")
                nav_items.append({"title": normalize_text(label.text or ""), "href": posixpath.join("OEBPS", src)})
        return nav_items

    return []


def parse_chapter(zip_file: zipfile.ZipFile, href: str) -> dict[str, Any]:
    parser = XHTMLBlockParser()
    parser.feed(read_text(zip_file, href))
    title = next((b.text for b in parser.blocks if b.type == "heading"), href)
    return {
        "source": href,
        "title": title,
        "blocks": [block.as_dict() for block in parser.blocks],
    }


def chapter_file_stem(source: str) -> str:
    return source.replace("/", "_").replace(".xhtml", "")


def block_to_markdown(block: dict[str, Any], asset_prefix: str = "../assets") -> str:
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
        return f"![{alt}]({asset_prefix}/{posixpath.basename(src)})"
    if block_type == "page":
        return f"<!-- {block.get('page_id')} -->"
    return ""


def write_chapter_files(chapter: dict[str, Any], output_dir: Path) -> None:
    chapters_dir = output_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)
    stem = chapter_file_stem(chapter["source"])

    json_path = chapters_dir / f"{stem}.json"
    json_path.write_text(json.dumps(chapter, ensure_ascii=False, indent=2), encoding="utf-8")

    md_blocks = [block_to_markdown(block) for block in chapter["blocks"]]
    md_path = chapters_dir / f"{stem}.md"
    md_path.write_text("\n\n".join(block for block in md_blocks if block), encoding="utf-8")


def collect_asset_paths(chapters: list[dict[str, Any]]) -> set[str]:
    assets: set[str] = set()
    for chapter in chapters:
        source_dir = posixpath.dirname(chapter["source"])
        for block in chapter["blocks"]:
            if block.get("type") == "image" and block.get("src"):
                assets.add(posixpath.normpath(posixpath.join(source_dir, block["src"])))
    return assets


def copy_assets(zip_file: zipfile.ZipFile, asset_paths: set[str], output_dir: Path) -> None:
    assets_dir = output_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    names = set(zip_file.namelist())
    for asset in sorted(asset_paths):
        if asset not in names:
            continue
        target = assets_dir / posixpath.basename(asset)
        with zip_file.open(asset) as src, target.open("wb") as dst:
            shutil.copyfileobj(src, dst)


def extract_questions(chapter: dict[str, Any]) -> list[dict[str, Any]]:
    questions: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    pattern = re.compile(r"^Question\s+(\d+):?$", re.IGNORECASE)

    for block in chapter["blocks"]:
        text = block.get("text", "")
        match = pattern.match(text)
        if match:
            if current is not None:
                questions.append(current)
            current = {
                "number": int(match.group(1)),
                "source": chapter["source"],
                "chapter_title": chapter["title"],
                "blocks": [block],
            }
        elif current is not None:
            current["blocks"].append(block)

    if current is not None:
        questions.append(current)
    return questions


def write_mock_tests(chapters: list[dict[str, Any]], output_dir: Path) -> None:
    tests = []
    for chapter in chapters:
        if "Mock Tests" not in chapter.get("title", ""):
            continue
        tests.append(
            {
                "source": chapter["source"],
                "title": chapter["title"],
                "questions": extract_questions(chapter),
            }
        )

    (output_dir / "mock_tests.json").write_text(json.dumps(tests, ensure_ascii=False, indent=2), encoding="utf-8")

    parts: list[str] = []
    for test in tests:
        parts.append(f"# {test['title']}")
        for question in test["questions"]:
            parts.append(f"## Question {question['number']}")
            parts.extend(block_to_markdown(block, "assets") for block in question["blocks"][1:])
    (output_dir / "mock_tests.md").write_text("\n\n".join(part for part in parts if part), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract PCAP EPUB content into JSON/Markdown intermediate files.")
    parser.add_argument("epub", type=Path, help="Path to the EPUB file")
    parser.add_argument("-o", "--output", type=Path, default=Path("epub_extract"), help="Output directory")
    parser.add_argument("--mock-tests-only", action="store_true", help="Only extract chapters whose title contains 'Mock Tests'")
    parser.add_argument("--no-assets", action="store_true", help="Do not copy image assets")
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(args.epub) as zip_file:
        nav = parse_nav(zip_file)
        if args.mock_tests_only:
            nav = [item for item in nav if "Mock Tests" in item["title"]]

        chapters = [parse_chapter(zip_file, item["href"]) for item in nav]

        manifest = {
            "source_epub": str(args.epub),
            "chapters": [{"title": chapter["title"], "source": chapter["source"]} for chapter in chapters],
        }
        (args.output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

        for chapter in chapters:
            write_chapter_files(chapter, args.output)

        if not args.no_assets:
            copy_assets(zip_file, collect_asset_paths(chapters), args.output)

        write_mock_tests(chapters, args.output)

    print(f"Extracted {len(chapters)} chapter(s) to {args.output}")


if __name__ == "__main__":
    main()
