# Projekt dokumentieren mit Markdown

Zu einem Softwareprojekt gehört nicht nur Code. Andere Personen müssen verstehen,
was das Projekt macht, wie man es startet und wie der Code grob aufgebaut ist.

Dafür wird häufig eine Datei namens `README.md` verwendet. Die Endung `.md`
steht für **Markdown**.

## Was ist Markdown?

Markdown ist eine einfache Schreibweise für formatierte Texte. Man schreibt
normalen Text und ergänzt wenige Zeichen für Überschriften, Listen, Links,
Codeblöcke und Tabellen.

Markdown wird zum Beispiel verwendet in:

- GitHub-Repositories
- technischen Dokumentationen
- Projektbeschreibungen
- Aufgabenblättern
- Wikis und Lernmaterialien

## Grundsyntax

### Überschriften

```markdown
# Hauptüberschrift
## Abschnitt
### Unterabschnitt
```

### Listen

```markdown
- erster Punkt
- zweiter Punkt
- dritter Punkt
```

### Nummerierte Schritte

```markdown
1. Projekt herunterladen
2. Virtuelle Umgebung erstellen
3. Abhängigkeiten installieren
4. Programm starten
```

### Code im Text

```markdown
Starte das Programm mit `python main.py`.
```

### Codeblock

````markdown
```python
def greet(name):
    return f"Hallo {name}"
```
````

### Link

```markdown
[Python Dokumentation](https://docs.python.org/3/)
```

### Tabelle

```markdown
| Datei | Aufgabe |
|-------|---------|
| main.py | Einstiegspunkt |
| game.py | Spiellogik |
```

## Was gehört in eine README?

Eine gute Projekt-Dokumentation beantwortet mindestens diese Fragen:

| Abschnitt | Frage |
|-----------|-------|
| Projektname | Wie heißt das Projekt? |
| Kurzbeschreibung | Was macht das Programm? |
| Features | Was kann das Programm? |
| Installation | Was muss vorher installiert werden? |
| Start | Wie führt man das Programm aus? |
| Bedienung | Wie benutzt man es? |
| Projektstruktur | Welche Dateien sind wichtig? |
| Beispiele | Wie sieht eine typische Nutzung aus? |
| Bekannte Grenzen | Was funktioniert noch nicht? |
| Ausblick | Was könnte man verbessern? |

## README-Vorlage
### **Github**-Beispiel: 
https://github.com/SadikshyaBashyal/Hangman-Game
```markdown
"
# Projektname

Kurze Beschreibung des Projekts in 2-4 Sätzen.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation


```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```.
## Start

```bash
python main.py
```.

## Bedienung

Beschreibe kurz, wie man das Programm benutzt.

## Projektstruktur

| Datei / Ordner | Bedeutung |
|----------------|-----------|
| main.py | startet das Programm |
| src/ | enthält den Quellcode |

## Beispiel

```text
Beispielausgabe oder Beispielablauf
```.

## Bekannte Grenzen

- Punkt 1
- Punkt 2

## Ausblick

- mögliche Erweiterung 1
- mögliche Erweiterung 2

```

!!! warning "Codeblock in Codeblock"
    Wenn du eine Markdown-Vorlage zeigst, die selbst Codeblöcke enthält,
    brauchst du außen mehr Backticks als innen. Deshalb wurde oben außen
    ein längerer Markdown-Codeblock verwendet.

## Mini-Präsentation

Für die Vorstellung eines Projekts reicht oft eine klare Struktur:

1. Was war die Idee?
2. Was kann das Programm?
3. Welche Datei ist der Einstiegspunkt?
4. Welche Stelle im Code ist besonders wichtig?
5. Was war schwierig?
6. Was würdest du als Nächstes verbessern?

{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/00_markdown_readme.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/18_markdown_code_review.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/19_readme_installation_abschnitt.yaml") }}
