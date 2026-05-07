# PEP 8, PEP 20 und PEP 257
## Python-Style-Guide, Zen of Python und Docstrings
[240min]

In der Python-Community gibt es Richtlinien und Prinzipien, um den Code einheitlich und lesbar zu gestalten. Diese werden in sogenannten PEPs (Python Enhancement Proposals) festgehalten. Hier sind drei wichtige PEPs, die eine Rolle in Bezug auf den Code-Stil und die Dokumentation spielen: PEP 8, PEP 20 und PEP 257.

## PEP 8: Style Guide for Python Code 🌶️️

PEP 8 ist der Style Guide für Python-Code. Er legt Konventionen für die Formatierung von Code, einschließlich Einrückungen, Zeilenlängen, Importen und Namenskonventionen, fest. Einige wichtige Punkte sind:

```python
# Verwende 4 Leerzeichen pro Einrückungsebene
def example_function():
    # Begrenze Zeilen auf 79 Zeichen für Code und 72 Zeichen für Docstrings
    long_variable_name = "This is a long string that exceeds the recommended line length"

    # Verwende sprechende Namen für Variablen, Funktionen und Module
    meaningful_variable_name = 42
```

Weitere Details findest du [hier](https://www.python.org/dev/peps/pep-0008/).

## PEP 20: The Zen of Python 🌶️️

PEP 20 enthält 19 Grundsätze, die als "The Zen of Python" bekannt sind. Diese Grundsätze bieten Richtlinien für das Schreiben von Python-Code und betonen Lesbarkeit und Einfachheit. Einige davon sind:

```python
# Schönheit zählt
beautiful_code = readable + simple

# Explizit ist besser als implizit
explicit_code = explicit_function()

# Flach ist besser als verschachtelt
flat_code = not_nested()
```

Du kannst sie dir in der Python-Shell anzeigen lassen, indem du `import this` ausführst.

## PEP 257: Docstring Conventions 🌶️️

PEP 257 legt Konventionen für Docstrings fest. Docstrings sind mehrzeilige Zeichenketten, die an den Anfang von Modulen, Funktionen, Klassen und Methoden platziert werden, um deren Verwendung zu dokumentieren. Wichtige Punkte sind:

```python
def example_function(param1, param2):
    """Kurze Zusammenfassung.

    Eine detaillierte Beschreibung dieses Beispiels und seiner Parameter.

    Args:
        param1: Erklärung des ersten Parameters.
        param2: Erklärung des zweiten Parameters.

    Returns:
        Der Rückgabewert dieser Funktion.
    """
    return result
```

Weitere Details findest du [hier](https://www.python.org/dev/peps/pep-0257/).

# Aufgaben:
[120min]

{{ task(file="tasks/python_grundlagen/13_pep/01_pep_8_konformitat.yaml") }}

{{ task(file="tasks/python_grundlagen/13_pep/02_umsetzung_des_zen_of_python.yaml") }}

{{ task(file="tasks/python_grundlagen/13_pep/03_docstrings_fur_funktionen_und_klassen.yaml") }}
