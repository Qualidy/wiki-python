# Projektaufgabe: PCEP Quiz-Engine

**Dauer:** 1-1.5 Tage (4 UE Vorbereitung + Arbeitsphase + 2 UE Integration/Präsentation)

**Ziel:** Ein funktionales Quiz-Programm entwickeln, das Fragen stellt, Antworten validiert und Statistiken anzeigt. Das Programm soll später mit echten PCEP/PCAP-Prüfungsfragen erweitert werden.

---

## 📋 Anforderungen

### Must-Haves (Pflicht):

1. **Fragen-Datenbank (`questions.py`)**
   - Mindestens 10 Fragen als Liste von Dictionaries
   - Jede Frage mit: `question`, `options`, `correct_index`, `explanation`, `category`
   - Fragen aus verschiedenen Kategorien (z.B. Datentypen, Operatoren, Kontrollstrukturen, Syntax, Exceptions)

2. **Quiz-Engine (`quiz_engine.py`)**
   - `run_quiz(questions: list[dict]) -> dict` – Hauptschleife für Quiz
   - `display_question(question: dict, num: int, total: int) -> None` – Frage anzeigen
   - `get_answer(question: dict) -> int` – Antwort vom Nutzer holen (mit Validierung!)
   - `check_answer(answer: int, question: dict) -> bool` – Antwort prüfen
   - `display_results(results: dict) -> None` – Ergebnisse anzeigen
   - **Type Hints überall!**
   - **Try/except für Eingabevalidierung** (nur Zahlen, nur gültiger Bereich)

3. **Hauptprogramm (`main.py`)**
   - Menu mit Optionen: "Quiz starten", "Statistik", "Beenden"
   - Quiz mit zufällig gemischten Fragen starten
   - Ergebnisse speichern (in einfacher Variable/Liste, **keine Dateien!**)
   - Statistik anzeigen: Gesamt-Punkte, Richtig/Falsch, Best/Worst Category

4. **Git-Workflow**
   - Repository clonen oder initialisieren
   - Mindestens 3-5 sinnvolle Commits mit aussagekräftigen Messages
   - Am Ende: `git log` zeigen

### Nice-to-Haves (Optional, Bonuspunkte):

- [ ] **Schwierigkeitsstufen:** Quiz nur mit einfachen (level 1) oder schwierigen (level 3+) Fragen
- [ ] **Kategorien-Filter:** Nutzer wählt Kategorie aus, nur diese Fragen spielen
- [ ] **Highscore-System:** Beste Scores tracken und anzeigen
- [ ] **Timed Mode:** Zeit-Limit pro Frage (mit `time`-Modul)
- [ ] **Prozentanzeige:** Echtzeit-Fortschrittsanzeige während Quiz
- [ ] **Formatierung:** Schöne Ausgabe mit Farben oder Symbolen (Unicode: ✓ ✗ ★)

---

## 🏗️ Projekt-Struktur

```
pcep-quiz/
├── main.py              # Hauptprogramm mit Menu-Loop
├── quiz_engine.py       # Kernfunktionen (run_quiz, display, etc.)
├── questions.py         # Fragen-Datenbank (hardcodiert)
├── stats.py             # (Optional) Statistik & Highscore
├── README.md            # Kurze Dokumentation
└── .gitignore           # (Optional) z.B. __pycache__, .pyc
```

---

## 🔧 Technische Vorgaben (Woche 1!)

- **Nur Woche-1-Inhalte verwenden:**
  - ✅ Funktionen mit Type Hints (`def func(...) -> type:`)
  - ✅ Datentypen: `int`, `str`, `bool`, `list`, `dict`
  - ✅ Kontrollstrukturen: `if/elif/else`, `while`, `for`, `range()`
  - ✅ Operatoren: arithmetisch, Vergleich, logisch
  - ✅ String-Operationen und f-Strings
  - ✅ `try/except` für Fehlerbehandlung
  - ✅ `import`/`from`: `random`, `time` (optional), mögl. `questions`
  - ❌ **KEINE:** Klassen, Dateioperationen, Comprehensions, OOP

- **Codequalität:**
  - Type Hints bei allen Funktionen
  - Aussagekräftige Funktionsnamen
  - Kurze, fokussierte Funktionen
  - Kommentare nur wo nötig (Code sollte self-documenting sein)

---

## 📝 Beispiel-Struktur

### `questions.py`:

```python
questions = [
    {
        'question': "Welcher Datentyp ist 5.0?",
        'options': ["int", "float", "str", "bool"],
        'correct_index': 1,
        'explanation': "5.0 hat einen Dezimalpunkt, daher float",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was gibt `3 // 2` aus?",
        'options': ["1", "1.5", "2", "Error"],
        'correct_index': 0,
        'explanation': "// ist Floor Division (Ganzzahldivision)",
        'category': "Operatoren",
        'difficulty': 1
    },
    # ... mindestens 10 Fragen
]
```

### `quiz_engine.py` (Grundgerüst):

```python
from typing import Optional

def display_question(question: dict, num: int, total: int) -> None:
    """Zeigt Frage mit Nummern und Optionen"""
    pass

def get_answer(question: dict) -> int:
    """Liest Antwort vom Nutzer (mit Validierung!)"""
    pass

def check_answer(answer: int, question: dict) -> bool:
    """Prüft ob Antwort richtig ist"""
    pass

def run_quiz(questions: list[dict]) -> dict:
    """Durchläuft ein komplettes Quiz"""
    pass

def display_results(results: dict) -> None:
    """Zeigt Ergebnisse an"""
    pass
```

### `main.py` (Grundgerüst):

```python
from questions import questions
import quiz_engine
import random

def main() -> None:
    """Hauptprogramm mit Menu"""
    all_results = []

    while True:
        print("\n=== PCEP Quiz ===")
        print("1. Quiz starten")
        print("2. Meine Ergebnisse anzeigen")
        print("3. Beenden")

        # ...

if __name__ == '__main__':
    main()
```

---

## 🔄 Git-Workflow

### Start (gemeinsam):

```bash
# Repo erstellen/clonen
git clone <repo-url>
cd pcep-quiz

# Initialisieren (falls neu)
git config user.name "Dein Name"
git config user.email "deine@email.com"
```

### Pro Gruppe:

```bash
# Feature-Branch erstellen (z.B. für questions, quiz_engine, main, stats)
git checkout -b feature/quiz-engine

# Code entwickeln, testen
# ...

# Änderungen committen
git add .
git commit -m "feat: add quiz_engine with run_quiz and display functions"

# Push
git push origin feature/quiz-engine

# Pull Request auf GitHub (oder später mergen)
```

### Commits sollten sein:

- `feat: add ...` (neue Funktion)
- `fix: bug in ...` (Bugfix)
- `refactor: improve ...` (Code verbessern)
- `docs: add ...` (Dokumentation)

---

## 📅 Zeitplan (1-1.5 Tage)

| Zeit                         | Aktivität                                  | UE    |
| ---------------------------- | ------------------------------------------ | ----- |
| **Tag 1 Start**              | Briefing & Anforderungen klären            | 0.5   |
|                              | Repo setup & Git intro                     | 0.5   |
|                              | Code-Struktur planen (gemeinsam)           | 0.5   |
| **Arbeitsphase 1**           | Entwicklung: questions.py + quiz_engine.py | 2–2.5 |
|                              | Regelmäßige Commits machen                 |       |
| **Tag 1 Ende / Tag 2 Start** | Testing & Debugging                        | 1     |
| **Arbeitsphase 2**           | main.py & optionale Features               | 1–1.5 |
|                              | Code-Review in Paaren                      | 0.5   |
| **Finale Phase**             | Integration, Git `log` zeigen              | 0.5   |
|                              | Demo/Präsentation (3–5 Min)                | 0.5   |

---

## ✅ Abgabe & Evaluation

Jede Gruppe zeigt:

1. **Funktionales Programm:** Quiz läuft, Fragen erscheinen, Scoring stimmt
2. **Code-Qualität:** Type Hints, Try/Except, aussagekräftige Funktionsnamen
3. **Git-Geschichte:** `git log` mit mindestens 3–5 Commits
4. **Optional:** Bonus-Features (Kategorien-Filter, Schwierigkeit, etc.)

---

## 🚀 Nächste Schritte (nach diesem Projekt)

- **Woche 2:** Fragen-Kategorien erweitern
- **Woche 4:** `questions.py` durch YAML/JSON-Dateioperationen ersetzen
- **Woche 8:** Echte PCEP/PCAP-Fragen einspielen, separates Fragen-Repo
- **Optional später:** Web-UI, Datenbank, Multiplayer-Modus

---

## 💡 Tipps

- **Debugger verwenden:** Häufig eine Schleife nicht verlassen? Debugger starten und Step-by-step gehen
- **Testen während Entwicklung:** Nicht erst am Schluss testen!
- **Funktionen klein halten:** Eine Funktion = eine Aufgabe
- **Type Hints früh:** Macht die IDE besser und Code lesbarer
- **Commits oft:** Nach jeder fertigen Funktion committen, nicht erst am Ende!

---

## 📚 Ressourcen

- Python Docs: https://docs.python.org/3/
- Type Hints: https://docs.python.org/3/library/typing.html
- Git Basics: https://git-scm.com/book/en/v2/Getting-Started-The-Basics
- Debugging in VS Code: F5 or Run → Start Debugging

---

**Viel Erfolg! 🚀**
