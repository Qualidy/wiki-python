# Projekt: PCEP Quiz-Engine

**Woche 1** | Dauer: 1-1.5 Tage | Schwerpunkt: 🔵 PCEP-relevant + 🛠️ Git & Zusammenarbeit

---

## 📌 Übersicht

Ein praktisches Projekt zum Abschluss von Woche 1, das alle bisherigen Konzepte zusammenbringt:

- **Funktionen mit Type Hints** – Code strukturieren
- **Try/Except** – Eingabevalidierung
- **Datenstrukturen** – `dict` und `list` für Fragen & Ergebnisse
- **Kontrollstrukturen** – Schleifen, if/elif/else
- **String-Operationen** – Formatierung und Ausgabe
- **Module** – `random` zum Mischen von Fragen
- **Git & GitHub** – Echte Zusammenarbeit & Versionskontrolle

Das Quiz-Programm ist **später erweiterbar** mit echten PCEP/PCAP-Prüfungsfragen für Woche 8.

---

## 📚 Inhalte

- **[Projektaufgabe](aufgabe.md)** – Anforderungen, Struktur, Code-Beispiele, Zeitplan
- **[Git Cheat Sheet](git_cheatsheet.md)** – Schnelle Referenz für Git-Befehle

---

## 🎯 Lernziele

Nach diesem Projekt können die Teilnehmer:

✅ Ein Programm aus mehreren Funktionen strukturieren
✅ Benutzereingaben sicher validieren (try/except)
✅ Komplexe Datenstrukturen nutzen und verarbeiten
✅ Mit Git arbeiten: clone, branches, commits, push
✅ Code-Review mit Peers durchführen

---

## 🚀 Schnelleinstieg

1. **Aufgabe lesen:** [Projektaufgabe](aufgabe.md)
2. **Git-Befehle pauken:** [Git Cheat Sheet](git_cheatsheet.md)
3. **Repository klonen** und losarbeiten!
4. **Commits machen** – mindestens nach jeder fertigen Funktion
5. **Präsentation** – Demo + Git-Historiy zeigen

---

## 📝 Projekt-Struktur

```
pcep-quiz/
├── main.py              # Hauptprogramm mit Menu-Loop
├── quiz_engine.py       # Kernfunktionen (run_quiz, display, etc.)
├── questions.py         # Fragen-Datenbank (hardcodiert)
├── stats.py             # (Optional) Statistik & Highscore
├── README.md            # Dokumentation
└── .gitignore           # (Optional)
```

---

## 💡 Wichtige Konzepte aus Woche 1

| Konzept | Im Projekt | Beispiel |
|---------|-----------|----------|
| **Funktionen** | Modularität | `run_quiz()`, `display_question()` |
| **Type Hints** | Codequalität | `def run_quiz(questions: list[dict]) -> dict:` |
| **Try/Except** | Fehlerbehandlung | `int(input())` mit ValueError-Handling |
| **Dict & List** | Datenmanagement | Fragen als `list[dict]`, Results als `dict` |
| **For/While** | Schleifen | Quiz-Schleife, Menu-Loop |
| **String Ops** | Formatierung | f-Strings für Ausgabe |
| **Random** | Gameplay | `random.shuffle(questions)` |
| **Import** | Modularität | `from questions import questions` |

---

## ✨ Bonusfeatures

Optional für ambitionierte Gruppen:

- 🎯 **Kategorien-Filter** – nur Fragen einer Kategorie
- 📊 **Statistik** – Highscores, best/worst Kategorien
- ⏱️ **Timed Mode** – Zeit-Limit pro Frage
- 🎨 **Formatierung** – Schöne Ausgabe mit Unicode-Symbolen
- 📈 **Schwierigkeit** – Einfach/Mittel/Schwer-Filter

---

## 🔗 Weitere Ressourcen

- [Python 3 Dokumentation](https://docs.python.org/3/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-The-Basics)
- [VS Code Debugging](https://code.visualstudio.com/docs/editor/debugging)

---

**Bereit? Los geht's! 🚀**
