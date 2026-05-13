# Kursplan: Python Programmierung – Vorbereitung PCEP / PCAP
**Zertifikat:** PCAP-31-03  
**Dauer:** 8 Wochen | 5 Tage/Woche | 10 UE/Tag (à 45 min) = **400 UE gesamt**  
**Zielgruppe:** Umschüler mit Java- und Python-Vorkenntnissen, gemischtes Niveau  
**Struktur:** 5 Wochen Inhalt (Spiralcurriculum) + 3 Wochen Projekte & Prüfungsvorbereitung

---

## Legende

| Symbol | Bedeutung |
|--------|-----------|
| 🔵 | PCEP-relevant |
| 🟠 | PCAP-zusätzlich |
| 🔄 | Spirale – Thema wird vertieft (Verweis auf Ersteinführung) |
| 🛠️ | Werkzeug / Methodik |

---

## Überblick: Themenspirale

| Thema | Ersteinführung | Vertiefung 1 | Vertiefung 2 |
|-------|---------------|--------------|--------------|
| Funktionen & Type Hints | Woche 1 | Woche 3 | Woche 5 (als Methoden) |
| Exceptions | Woche 1 (try/except) | Woche 4 (Hierarchie, eigene) | Woche 7 (in Projekten) |
| Datentypen & Strukturen | Woche 1–2 | Woche 3 (Comprehensions) | Woche 4 (mit Dateien) |
| OOP | Woche 3 (einfache Klasse) | Woche 5 (Vererbung, Dunder) | Woche 7 (Projekt) |
| Module & pip | Woche 1 (import) | Woche 4 (Pakete, pip, venv) | – |
| Debugger | Woche 1 | durchgehend | – |

---

## WOCHE 1 – Python-Einstieg & Grundwerkzeuge

**Schwerpunkt:** Lauffähige Programme schreiben von Tag 1. Debugger als Lernwerkzeug einführen. Erste Funktionen und Type Hints zeigen.

**PCAP-Syllabus:** Grundlagen, Datentypen, Operatoren, erste Module

---

### Tag 1 – Umgebung, erste Programme, Debugger

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Entwicklungsumgebung einrichten (VS Code + Python Extension), erste Ausführung | 🔵 🛠️ |
| 3–4 | Python-Syntax im Vergleich zu Java: Einrückung, keine Semikolons, keine Typendeklaration | 🔵 |
| 5–6 | **Debugger einführen:** Breakpoints setzen, Variablenwerte beobachten, Step-over/into | 🛠️ |
| 7–8 | Variablen, Zuweisung, `print()`, `input()` | 🔵 |
| 9–10 | Übung: Kleines Programm schreiben, mit Debugger Schritt für Schritt durchgehen | 🔵 🛠️ |

---

### Tag 2 – Datentypen & Operatoren

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Datentypen: `int`, `float`, `str`, `bool`, `NoneType` – dynamische Typisierung verstehen | 🔵 |
| 3–4 | Typumwandlung: `int()`, `float()`, `str()`, `bool()` | 🔵 |
| 5–6 | Arithmetische Operatoren inkl. `//`, `%`, `**` | 🔵 |
| 7–8 | Vergleichs- und logische Operatoren (`==`, `!=`, `and`, `or`, `not`) | 🔵 |
| 9–10 | Übung: Taschenrechner mit Debugger analysieren | 🔵 🛠️ |

---

### Tag 3 – Strings & Type Hints

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Strings: Literale, Escape-Zeichen, f-Strings | 🔵 |
| 3–4 | String-Operationen: Konkatenation, Wiederholung, Indexierung, Slicing | 🔵 |
| 5–6 | **Type Hints einführen:** `x: int = 5`, Nutzen in der IDE zeigen | 🔵 🛠️ |
| 7–8 | **Erste Funktionen:** `def`, Parameter mit Type Hints, Rückgabewert | 🔵 |
| 9–10 | Übung: Funktionen mit Type Hints schreiben, IDE-Feedback beobachten | 🔵 🛠️ |

---

### Tag 4 – Kontrollstrukturen I

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | `if`, `elif`, `else` | 🔵 |
| 3–4 | `while`-Schleife, `break`, `continue` | 🔵 |
| 5–6 | `for`-Schleife mit `range()` | 🔵 |
| 7–8 | **Erste Exceptions:** `try/except` als praktisches Werkzeug bei Nutzereingaben | 🔵 |
| 9–10 | Übung: Eingabevalidierung mit try/except und Debugger | 🔵 🛠️ |

---

### Tag 5 – Imports & Wochenabschluss

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | `import` und `from ... import`, Standardbibliothek: `math`, `random` | 🔵 |
| 3–4 | Namensräume: warum `import math` vs. `from math import sqrt` | 🔵 🟠 |
| 5–7 | Wiederholung & Lücken schließen | 🔵 |
| 8–10 | **Mini-Aufgabe:** Zahlenratespiel (Funktionen, Schleife, try/except, random) | 🔵 |

---

## WOCHE 2 – Datenstrukturen & Kontrollstrukturen II

**Schwerpunkt:** Die vier Kernstrukturen sicher beherrschen. Iteration vertiefen.

**PCAP-Syllabus:** Listen, Tupel, Dicts, Sets, Sequenzoperationen

---

### Tag 1 – Listen

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Listen: Erstellen, Indexierung, Slicing, Ändern | 🔵 |
| 4–5 | Listen-Methoden: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()` | 🔵 |
| 6–7 | Iteration über Listen mit `for` | 🔵 |
| 8–10 | Übung: Notenverwaltung mit Liste und Funktionen | 🔵 |

---

### Tag 2 – Tupel & Sets

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Tupel: Unveränderlichkeit, wann sinnvoll, Entpacken (unpacking) | 🔵 |
| 4–6 | Sets: Mengenoperationen, `in`-Operator, Duplikat-Filterung | 🔵 |
| 7–8 | Vergleich: Liste vs. Tupel vs. Set – wann welche Struktur? | 🔵 |
| 9–10 | Übung mit Debugger: Unterschiede live beobachten | 🔵 🛠️ |

---

### Tag 3 – Dictionaries

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Dicts: Erstellen, Zugriff, Ändern, Löschen | 🔵 |
| 4–5 | Dict-Methoden: `keys()`, `values()`, `items()`, `get()` | 🔵 |
| 6–7 | Iteration über Dicts | 🔵 |
| 8–10 | Übung: Telefonbuch als Dict mit Funktionen und Type Hints | 🔵 |

---

### Tag 4 – Verschachtelte Strukturen & Kontrollstrukturen II

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Verschachtelte Listen und Dicts (Matrix, JSON-ähnliche Strukturen) | 🔵 |
| 4–5 | Mehrfachzuweisung, `enumerate()`, `zip()` | 🔵 🟠 |
| 6–7 | `for`/`while` mit `else` | 🟠 |
| 8–10 | Übung: Schülernotenliste als verschachtelte Struktur | 🔵 |

---

### Tag 5 – Wiederholung & Übungsaufgaben

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | PCEP-typische Aufgaben zu Datenstrukturen | 🔵 |
| 4–6 | Häufige Fehler: Mutable vs. Immutable, Referenzen vs. Kopien | 🔵 🟠 |
| 7–10 | **Mini-Aufgabe:** Einkaufsliste mit Dict und Funktionen, Eingabevalidierung | 🔵 |

---

## WOCHE 3 – Funktionen vertieft, Comprehensions, OOP-Einstieg

**Schwerpunkt:** 🔄 Funktionen auf das PCAP-Niveau heben. List Comprehensions. Erste Klasse als praktisches Konzept einführen.

**PCAP-Syllabus:** Funktionen (Scope, *args, **kwargs, Lambda), Comprehensions, OOP-Grundlagen

---

### Tag 1 – Funktionen vertieft (🔄 Woche 1)

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Scope: lokal, global, `global`-Keyword | 🔵 🟠 |
| 3–4 | Default-Parameter, Keyword-Argumente | 🔵 |
| 5–6 | `*args` und `**kwargs` | 🟠 |
| 7–8 | Type Hints vertieft: komplexe Typen (`list[int]`, `dict[str, float]`, `Optional`) | 🟠 🛠️ |
| 9–10 | Übung: Funktionen mit verschiedenen Argumenttypen | 🟠 |

---

### Tag 2 – Lambda, Closures, Higher-Order Functions

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Lambda-Funktionen: Syntax, wann sinnvoll | 🟠 |
| 4–5 | `map()`, `filter()` | 🟠 |
| 6–7 | Closures: Funktion gibt Funktion zurück | 🟠 |
| 8–10 | Übung: Sortieren mit Lambda, filter auf Listen anwenden | 🟠 |

---

### Tag 3 – List/Dict/Set Comprehensions

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | List Comprehensions: Syntax, mit Bedingung | 🟠 |
| 4–5 | Dict- und Set-Comprehensions | 🟠 |
| 6–7 | Vergleich: Comprehension vs. klassische Schleife (Lesbarkeit, Performance) | 🟠 |
| 8–10 | Übung: Datenbereinigung und Transformation mit Comprehensions | 🟠 |

---

### Tag 4 – OOP-Einstieg: Klasse als besseres Dict

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Motivation: warum OOP? Klasse als Datencontainer | 🔵 🟠 |
| 3–5 | Klasse definieren, `__init__`, Attribute, erste Methoden | 🟠 |
| 6–7 | `self` verstehen, Instanzen erstellen | 🟠 |
| 8–10 | Übung: Klasse `Student` mit Attributen und Methode `vorstellen()` | 🟠 |

---

### Tag 5 – Wiederholung & PCAP-Aufgaben

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | PCAP-typische Aufgaben: Funktionen und Comprehensions | 🟠 |
| 4–6 | Häufige Fehler: Scope-Probleme, mutable Default-Argumente | 🟠 |
| 7–10 | **Mini-Aufgabe:** Klasse `Warenkorb` mit Methoden und Type Hints | 🟠 |

---

## WOCHE 4 – Exceptions vertieft, Dateien, Module & pip

**Schwerpunkt:** 🔄 Exceptions auf PCAP-Niveau. Dateioperationen. Paketstruktur verstehen.

**PCAP-Syllabus:** Exception-Hierarchie, eigene Exceptions, Dateien, os, pip, venv

---

### Tag 1 – Exceptions vertieft (🔄 Woche 1)

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Exception-Hierarchie: `BaseException` → `Exception` → konkrete Typen | 🟠 |
| 3–4 | `try/except/else/finally` vollständig | 🟠 |
| 5–6 | Mehrere `except`-Blöcke, Exception-Objekt nutzen (`as e`) | 🟠 |
| 7–8 | Eigene Exception-Klassen definieren und `raise` | 🟠 |
| 9–10 | Übung: Eigene Exception in der `Warenkorb`-Klasse aus Woche 3 | 🟠 |

---

### Tag 2 – Dateioperationen

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | `open()`, Modi (`r`, `w`, `a`, `rb`), `close()`, `with`-Statement | 🟠 |
| 3–4 | Textdateien lesen und schreiben | 🟠 |
| 5–6 | Zeilenweise lesen, `readlines()`, `readline()` | 🟠 |
| 7–8 | Binärdateien, Byte-Operationen | 🟠 |
| 9–10 | Übung: Kontaktliste in Datei speichern und laden | 🟠 |

---

### Tag 3 – os & datetime

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | `os`-Modul: `os.path`, `os.listdir()`, `os.getcwd()`, `os.makedirs()` | 🟠 |
| 4–6 | `datetime`-Modul: `date`, `datetime`, `timedelta`, Formatierung | 🟠 |
| 7–8 | Kombination: Datei mit Zeitstempel anlegen | 🟠 |
| 9–10 | Übung: Logdatei mit Zeitstempel | 🟠 |

---

### Tag 4 – Module, Pakete, pip & venv

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | 🔄 Eigene Module: `.py`-Datei als Modul, `__name__ == "__main__"` | 🟠 |
| 3–4 | Pakete: Ordner mit `__init__.py`, Importpfade | 🟠 |
| 5–6 | `pip`: installieren, deinstallieren, `requirements.txt` | 🟠 |
| 7–8 | Virtuelle Umgebungen: `venv` erstellen, aktivieren, nutzen | 🟠 |
| 9–10 | Übung: Eigenes Mini-Paket erstellen und importieren | 🟠 |

---

### Tag 5 – Wiederholung & PCAP-Aufgaben

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | PCAP-typische Aufgaben: Exceptions und Dateien | 🟠 |
| 4–6 | Häufige Fehler: Datei nicht geschlossen, falsche Exception abgefangen | 🟠 |
| 7–10 | **Mini-Aufgabe:** Aufgabenverwaltung mit Datei-Persistenz und eigenen Exceptions | 🟠 |

---

## WOCHE 5 – OOP vertieft

**Schwerpunkt:** 🔄 OOP vollständig auf PCAP-Niveau bringen. Schwergewichtigste PCAP-Sektion (45% der Prüfung).

**PCAP-Syllabus:** Vererbung, MRO, Dunder-Methoden, abstrakte Klassen, Polymorphismus, Kapselung

---

### Tag 1 – Vererbung & Polymorphismus

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Vererbung: `class Kind(Eltern)`, `super()`, Methoden überschreiben | 🟠 |
| 4–5 | Polymorphismus: gleiche Methode, unterschiedliches Verhalten | 🟠 |
| 6–7 | `isinstance()`, `issubclass()` | 🟠 |
| 8–10 | Übung: Klassenstruktur `Tier → Hund / Katze` | 🟠 |

---

### Tag 2 – Mehrfachvererbung & MRO

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Mehrfachvererbung: Syntax, Konflikte | 🟠 |
| 4–6 | Method Resolution Order (MRO): `__mro__`, C3-Linearisierung verstehen | 🟠 |
| 7–8 | Diamond-Problem und Lösung durch MRO | 🟠 |
| 9–10 | Übung: MRO mit `__mro__` und Debugger nachvollziehen | 🟠 🛠️ |

---

### Tag 3 – Dunder-Methoden & Operatorüberladung

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | `__str__`, `__repr__` | 🟠 |
| 3–4 | `__len__`, `__eq__`, `__lt__` (Vergleichsoperatoren) | 🟠 |
| 5–6 | `__add__`, `__mul__` (Arithmetik) | 🟠 |
| 7–8 | `__getitem__`, `__setitem__` (Sequenzprotokoll) | 🟠 |
| 9–10 | Übung: Klasse `Vektor` mit Dunder-Methoden | 🟠 |

---

### Tag 4 – Kapselung, Eigenschaften & abstrakte Klassen

| UE | Inhalt | Level |
|----|--------|-------|
| 1–2 | Kapselung: `_privat`, `__name_mangling` | 🟠 |
| 3–4 | `@property`, Getter und Setter | 🟠 |
| 5–7 | Abstrakte Klassen: `abc`, `ABC`, `@abstractmethod` | 🟠 |
| 8–10 | Übung: Abstrakte Klasse `Form` → `Kreis`, `Rechteck` | 🟠 |

---

### Tag 5 – OOP Gesamtwiederholung & PCAP-Aufgaben

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | PCAP-typische OOP-Aufgaben (Syllabus-nah) | 🟠 |
| 4–6 | Häufige Fehler: MRO-Überraschungen, fehlende `super()`-Aufrufe | 🟠 |
| 7–10 | **Mini-Aufgabe:** Klassenhierarchie für Projekt 1 entwerfen | 🟠 |

---

## WOCHE 6 – Projekt 1

**Schwerpunkt:** Alle Inhalte aus Wochen 1–5 in einem zusammenhängenden Programm anwenden.

**Projektthema:** CLI-Anwendung nach Wahl aus vorgegebener Liste (z.B. Aufgabenverwaltung, Kontaktbuch, einfaches Kassensystem)

**Pflichtbestandteile:**
- Mindestens 2 Klassen mit Vererbung
- Eigene Exception-Klasse
- Datei-Persistenz (Speichern und Laden)
- Type Hints durchgehend
- Fehlerbehandlung für alle Nutzereingaben

**PCEP-Kandidaten:** Umsetzung prozedural (mit Funktionen, ohne OOP-Pflicht), Schwerpunkt auf sauberem Code und Fehlerbehandlung

---

| Tag | Inhalt |
|-----|--------|
| 1 | Anforderungen verstehen, Struktur planen, Klassen/Funktionen entwerfen |
| 2 | Kernfunktionalität implementieren |
| 3 | Fehlerbehandlung und Datei-Persistenz einbauen |
| 4 | Testen, Debuggen, Refactoring |
| 5 | Code Review in Paaren, kurze Präsentation (5 min pro Gruppe) |

---

## WOCHE 7 – Projekt 2 & Lücken schließen

**Schwerpunkt:** Projekt 1 erweitern oder refactoren. Gezielt PCAP-Lücken schließen. PCEP-Kandidaten: Übungsaufgaben und Vertiefung.

**Projektthema:** Erweiterung von Projekt 1 um:
- Generatoren (`yield`) für große Datensätze
- Dekoratoren (z.B. Logging, Zugriffskontrolle)
- Erweiterte OOP-Struktur

---

### Tag 1 – Generatoren

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | `yield`, Generator-Funktionen vs. normale Funktionen | 🟠 |
| 4–6 | Generator-Expressions, `next()`, `StopIteration` | 🟠 |
| 7–10 | Einbau in Projekt 2 | 🟠 |

---

### Tag 2 – Dekoratoren

| UE | Inhalt | Level |
|----|--------|-------|
| 1–3 | Dekoratoren verstehen: Funktion die Funktion wrапpt | 🟠 |
| 4–5 | `@decorator`-Syntax, `functools.wraps` | 🟠 |
| 6–7 | Praktische Beispiele: Logging, Zeitmessung | 🟠 |
| 8–10 | Einbau in Projekt 2 | 🟠 |

---

### Tag 3–4 – Projektarbeit & individuelle Lücken

| UE | Inhalt | Level |
|----|--------|-------|
| 1–5 | Projekt 2 fertigstellen | 🟠 |
| 6–10 | Gezielte Nacharbeit je nach Gruppe: PCAP-Schwachstellen identifizieren und üben | 🔵 🟠 |

---

### Tag 5 – Projektabschluss

| UE | Inhalt |
|-----|--------|
| 1–5 | Abschlusspräsentation Projekt 2 |
| 6–10 | Gemeinsame Reflexion: Was war schwer? Was kommt in der Prüfung? |

---

## WOCHE 8 – Prüfungsvorbereitung

**Schwerpunkt:** Systematische Wiederholung nach Prüfungsgewicht. Probeklausuren. Gezielte Schwachstellenarbeit.

**PCAP-Prüfungsgewichte zur Orientierung:**

| Sektion | Thema | Gewicht |
|---------|-------|---------|
| 1 | Module, Pakete, pip | 12% |
| 2 | Strings, Exceptions | 18% |
| 3 | OOP Grundlagen | 25% |
| 4 | OOP Fortgeschritten | 20% |
| 5 | Dateien, os, datetime | 25% |

---

### Tag 1 – Wiederholung: Sektionen 1 & 2

| UE | Inhalt |
|----|--------|
| 1–4 | Module, Pakete, pip, venv – typische Prüfungsfragen |
| 5–8 | Strings, String-Methoden, Exceptions – typische Prüfungsfragen |
| 9–10 | Kurzer Diagnosetest |

---

### Tag 2 – Wiederholung: Sektionen 3 & 4 (OOP)

| UE | Inhalt |
|----|--------|
| 1–5 | OOP Grundlagen: Klassen, `__init__`, Methoden, Instanzen |
| 6–10 | OOP Fortgeschritten: Vererbung, MRO, Dunder, abstrakte Klassen |

---

### Tag 3 – Wiederholung: Sektion 5 & Probeklausur

| UE | Inhalt |
|----|--------|
| 1–4 | Dateien, os, datetime – typische Prüfungsfragen |
| 5–10 | **Probeklausur 1** (PCEP-Format für PCEP-Kandidaten, PCAP-Format für PCAP-Kandidaten) |

---

### Tag 4 – Auswertung & gezielte Nacharbeit

| UE | Inhalt |
|----|--------|
| 1–3 | Probeklausur gemeinsam auswerten, häufige Fehler besprechen |
| 4–7 | Individuelle Schwachstellen nacharbeiten |
| 8–10 | **Probeklausur 2** |

---

### Tag 5 – Finale Vorbereitung

| UE | Inhalt |
|----|--------|
| 1–3 | Probeklausur 2 auswerten |
| 4–6 | Letzte offene Fragen klären |
| 7–8 | Prüfungsstrategie: Zeitmanagement, Fragentypen, häufige Fallen |
| 9–10 | Abschluss: Fragen, Motivation, organisatorische Infos zur Prüfung |

---

## Häufige Prüfungsfallen (PCAP-31-03)

Diese Themen führen erfahrungsgemäß zu den meisten Fehlern:

1. **MRO bei Mehrfachvererbung** – Reihenfolge nicht intuitiv, muss geübt werden
2. **Mutable Default-Argumente** – `def f(x=[])` ist eine klassische Falle
3. **Scope und `global`/`nonlocal`** – besonders in verschachtelten Funktionen
4. **Exception-Hierarchie** – welche Exception fängt welche ab?
5. **`__str__` vs. `__repr__`** – wann wird welche aufgerufen?
6. **Datei-Modi** – `r+` vs. `w+` vs. `a`
7. **Generatoren** – `yield` vs. `return`, Erschöpfung eines Generators
8. **Comprehension-Scope** – Variablen in Comprehensions "leaken" in Python 2, nicht in Python 3
9. **`isinstance()` vs. `type()`** – Unterschied bei Vererbung
10. **pip und venv** – Prüfung fragt nach konkreten Befehlen

---

*Stand: PCAP-31-03 Syllabus | Erstellt für internen Gebrauch*
