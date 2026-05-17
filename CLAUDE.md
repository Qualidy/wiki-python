# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a MkDocs-based documentation website for the **PCEP/PCAP-31-03 Python Certification Course**. It's an 8-week intensive training program (400 hours total: 5 days/week, 10 hours/day) designed for participants with Java and Python background. The course follows a spiral curriculum structure and features interactive educational content built with custom Python macros, deployed to GitHub Pages with CI/CD automation.

### Course Structure

- **Weeks 1-5:** Content delivery following a spiral curriculum (topics introduced → deepened across multiple weeks)
- **Weeks 6-7:** Project-based learning (2 CLI projects applying all learned concepts)
- **Week 8:** Examination preparation with practice tests

### Certification & Target Audience

- **Certification:** PCAP-31-03 (Certified Associate Python Programmer)
- **Audience:** Career changers with Java and Python background, mixed skill levels
- **Exam Emphasis:** OOP (45%), Strings & Exceptions (18%), Files/os/datetime (25%), Modules/pip (12%)

## Spiral Curriculum (Content Organization)

The course uses a **spiral curriculum** where topics are introduced at a basic level and then deepened in subsequent weeks. The wiki should reflect this structure:

| Topic | Week 1 | Week 3 | Week 5 | Exam Weight |
|-------|--------|--------|--------|------------|
| **Funktionen & Type Hints** | Introduction, basic functions | Scope, *args, **kwargs | Methods in OOP | 12% |
| **Exceptions** | try/except basics | Exception hierarchy, custom exceptions | In projects | 18% |
| **Datentypen & Strukturen** | int, float, str, bool | Comprehensions (list/dict/set) | Working with complex data | varies |
| **OOP** | Simple classes | Inheritance, polymorphism | Vererbung, MRO, Dunder, abstract classes | 45% |
| **Module & pip** | `import` basics | Packages, pip, venv | N/A | 12% |
| **Debugging** | Debugger introduction | Used continuously | N/A | N/A |

**Legend for difficulty levels in content:**
- 🔵 PCEP-relevant (basic level)
- 🟠 PCAP-additional (advanced level)
- 🔄 Spiral notation (deepening of previously introduced concept)
- 🛠️ Tool/methodology focus

## Architecture

### Core Components

- **main.py**: MkDocs macros plugin that extends markdown with custom functionality:
  - `task()`: Renders interactive question/solution blocks (supports difficulty levels, tips, solution videos)
  - `youtube_video()`: Embeds YouTube videos in styled admonition blocks
  - `python_tutor()`: Embeds interactive Python Tutor (code debugger) in iframes
  - `python_tutor_button()`: Creates button links to Python Tutor
  - `link()`: Creates styled external links with icons

- **mkdocs.yml**: Central configuration file with:
  - Navigation structure (extensive Python fundamentals curriculum)
  - Material Design theme with custom CSS/JS
  - Markdown extensions (Mermaid diagrams, math equations, emoji support, syntax highlighting)
  - Plugins (search, macros via main.py)
  - Watch configuration for hot-reloading tasks/ directory

- **docs/**: Content structure
  - `index.md`: Landing page
  - `content/`: Markdown content organized by topic (python_grundlagen/, begriffe/, checklists/)
  - `assets/`: Images (logo, favicon)
  - `stylesheets/`: Custom CSS for interactive elements
  - `javascripts/`: Custom JS (mathjax for math rendering)

- **tasks/**: YAML files containing task definitions (referenced in mkdocs.yml watch, used as input to task() macro)

## Common Development Commands

**Setup** (one-time):
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

**Run locally with hot-reload**:
```bash
source venv/bin/activate
mkdocs serve
```

**Build static site**:
```bash
mkdocs build
```

**Deploy to GitHub Pages** (CI/CD runs automatically on push to main/master):
```bash
mkdocs gh-deploy --force
```

## Weekly Content Structure (PCAP_Kursplan.md)

Refer to `PCAP_Kursplan.md` in the root for the complete 8-week course plan. Key structure:

**Weeks 1-5 (Content):**
- Each week is organized into 5 days with 10 teaching units (UE) per day
- Each day focuses on a specific topic area
- Content includes introduction, deepening, practice exercises, and mini-projects
- Topics are marked with difficulty levels (PCEP 🔵 vs PCAP-extended 🟠)

**Week 6:** Projekt 1 (CLI application with required OOP, exception handling, file persistence)
**Week 7:** Projekt 2 (Project 1 enhanced with generators, decorators)
**Week 8:** Exam prep (practice tests, review by exam weight percentages)

**Important:** The wiki's `docs/content/` structure should align with week-by-week progression. When adding content, indicate which week(s) it covers.

## Development Workflow

1. **Edit content**: Modify or create markdown files in `docs/content/` following the course weekly structure
2. **Link content to weeks**: When creating content, document which week(s) it addresses (use frontmatter or comments)
3. **Add educational tasks**: Create YAML files in `tasks/` directory with question/solution content, then reference via `{{ task('tasks/filename.yaml') }}` macro in markdown
4. **Preview locally**: Run `mkdocs serve` and view at http://localhost:8000
5. **Commit and push**: Changes to main branch automatically trigger GitHub Actions deployment (typically live within 30-50 seconds)

## Key Customization Notes

- **Task macro**: Supports `title`, `question`, `solution`, `tip`, `difficulty` (0-3 as difficulty_icon count), `collapsed` (boolean, default=False for expanded), `solution_video`, `question_video`
- **Embedded macros**: Task content supports nested YouTube video embeds using `{{ youtube_video('url', 'title') }}` syntax
- **Custom styling**: Interactive elements use custom CSS in `stylesheets/` (e.g., python_tutor_container, video_admonition)
- **Theme**: Material Design with amber primary color and deep orange accent
- **Extensions used**: pymdownx.keys, admonition, superfences (Mermaid), toc, emoji, arithmatex (math), highlight with line numbers

## Common Exam Pitfalls (PCAP-31-03)

When creating or updating content, emphasize these areas where learners commonly struggle:

1. **MRO in Multiple Inheritance** – Order of method resolution not intuitive
2. **Mutable Default Arguments** – `def f(x=[])` creates shared state across calls
3. **Scope & global/nonlocal** – Especially in nested functions
4. **Exception Hierarchy** – Which exception catches which?
5. **__str__ vs __repr__** – When each is called
6. **File Modes** – Differences between r+, w+, a
7. **Generators** – yield vs return, generator exhaustion
8. **isinstance() vs type()** – Behavior with inheritance
9. **pip & venv** – Specific commands and workflows
10. **Comprehension Scope** – Variable leaking (Python 2 vs 3)

Content should include explicit examples and debugging exercises for these topics.

## GitHub Actions CI/CD

File: `.github/workflows/ci.yml`

- Triggers on push to main/master branches
- Runs Python 3.x setup, installs dependencies, builds, and deploys via `mkdocs gh-deploy --force`
- Pages automatically published to GitHub Pages from gh-pages branch
