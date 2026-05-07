# Exkurs: Einführung in Type Hints in Python

{{ youtube_video("https://www.youtube.com/embed/ZgNRVwTY-v8?si=gQPKZ5pvzuRB2Jg0") }}

Type Hints sind in Python seit der Version 3.5 offiziell verfügbar und stellen eine optionale Erweiterung für die
Sprache dar. Sie ermöglichen es Entwicklern, den **erwarteten Datentyp** von Parametern und Rückgabewerten in Funktionen
anzugeben. 

Type Hints sind dabei lediglich **ein Hinweis** für andere Programmierer und werden nicht 
ohne automatisch durch Python nicht überprüft. Dafür gibt es allerdings frei verfügbare Tools, um dies zu tun.

Type Hints können nach Variablen oder Parametern mit einem `:` hinter dem Variablennamen angegeben werden.
Den Rückgabetyp von Funktonen wird nach den Parameterklammern nach einem `->` gesetzt.

```python
def addiere(a: int, b: int) -> int:
    return a + b

num1: int = 3
num2: int = 4
result: int = addiere(num1, num2)
```

### Statische Typüberprüfung

Eine der Hauptmethoden zum Testen von Type Hints ist die statische Typüberprüfung. Hier sind einige Tools, die dabei
helfen können:

**mypy**: `mypy` ist ein beliebtes Open-Source-Tool, das die statische Typüberprüfung in Python unterstützt. Es kann
als Teil des Entwicklungsprozesses verwendet werden, um sicherzustellen, dass Type Hints konsistent angewendet werden
und der Code den angegebenen Typen entspricht.

- Installation: `pip install mypy`
- Verwendung: `mypy script.py`

**pyright**: `pyright` ist ein statischer Typüberprüfer für Python, entwickelt von Microsoft. Er ist schneller
als `mypy` und kann ebenfalls als Teil des Entwicklungsworkflows integriert werden.

- Installation: `npm install -g pyright`
- Verwendung: `pyright script.py`

**PyCharm**: Die integrierte Entwicklungsumgebung (IDE) PyCharm von JetBrains bietet eingebaute Unterstützung für
Type Hints und die statische Typüberprüfung. PyCharm hebt Typkonflikte hervor und bietet Korrekturvorschläge während
der Entwicklung.

**Pylance**: Pylance ist eine Erweiterung für Visual Studio Code, die auf Pyright basiert. Sie verbessert die
Python-Unterstützung in VS Code durch Features wie schnelle und umfassende statische Typüberprüfung.

{{ task(file="tasks/python_grundlagen/type_hints/type_hints/01_typehints_betrachten.yaml") }}
{{ task(file="tasks/python_grundlagen/type_hints/type_hints/02_basistypen_bestimmen.yaml") }}
## Wichtigkeit von Type Hints

[//]: # ([40min])

* **Verbesserte Lesbarkeit und Wartbarkeit**: Type Hints machen den Code für andere Entwickler (oder auch für den Autor
   selbst zu einem späteren Zeitpunkt) leichter verständlich.

* **Fehlervermeidung**: Sie helfen dabei, Fehler zu identifizieren, indem sie sicherstellen, dass Funktionen mit den
   erwarteten Datentypen verwendet werden.

* **Unterstützung durch Entwicklungswerkzeuge**: Moderne Entwicklungsumgebungen nutzen Type Hints, um
   potenzielle Laufzeitfehler zu erkennen.

* **Verbesserte Refactoring-Unterstützung**: Type Hints erleichtern das Refactoring von Code, da Tools präziser
   erkennen können, wie bestimmte Variablen und Funktionen verwendet werden.

* **Dokumentation**: Sie dienen als eine Form der Dokumentation, die es neuen Nutzern des Codes erleichtert, die
   Funktionsweise und den Zweck von Funktionen zu verstehen.

## Weitere Beispiele

{{ youtube_video("https://www.youtube.com/embed/CBhga84SM3s?si=PKe3QHd1p4PNeh9_") }}

[//]: # ([25min])

Im einfachsten Fall nutzen wir einfach nur die uns bekannten primitiven Datentypen 

```python
def begruesse(name: str, alter: int) -> str:
    return f"Hallo {name}, du bist {alter} Jahre alt."
```

Viele der in Python vorimplementierten komplexen Datentypen können über das Modul `typing` importiert
und beim Typehinting genutzt werden:

```python
from typing import List, Dict, Tuple

def get_min_max(daten: List[int]) -> Dict[str, int]:
    return {"max": max(daten), "min": min(daten)}

def create_dict(data: List[Tuple[str, int]]) -> Dict[str, int]:
    result = {}
    for item in data:
        result[item[0]] = item[1]
    return result

def print_in_reverse(text: str) -> None:
    print(text[::-1])
```

# Aufgaben

[//]: # ([25min])

{{ task(file="tasks/python_grundlagen/type_hints/type_hints/03_typen_finden.yaml") }}
