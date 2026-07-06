# PCEP Vorbereitung

Diese Sektion buendelt die wichtigsten Informationen zum PCEP-Exam.
Der Schwerpunkt liegt auf Pruefungsformat, Themengewichtung und gezielter Wiederholung der Python-Grundlagen.

## Pruefungsformat

Die folgenden Eckdaten beziehen sich auf das PCEP - Certified Entry-Level Python
Programmer Exam (`PCEP-30-02`). Da `PCEP-30-02` laut Python Institute am
31. August 2026 zur Ablösung vorgesehen ist und `PCEP-30-03` fuer Q3 2026
angekuendigt ist, sollten die Angaben vor einer echten Anmeldung noch einmal
auf der offiziellen Seite geprueft werden:
[PCEP - Certified Entry-Level Python Programmer](https://pythoninstitute.org/pcep).

| Punkt | Wert |
|-------|------|
| Pruefung | PCEP - Certified Entry-Level Python Programmer |
| Exam-Code | `PCEP-30-02` |
| Status | Live & Active |
| Fragen | 30 |
| Zeit | 40 Minuten Exam + 5 Minuten NDA/Tutorial |
| Bestehensgrenze | 70% |
| Fragetypen | Single Choice, Multiple Choice, Drag-and-Drop, Gap Fill, Sort, Code Fill, Code Insertion, interaktive und szenariobasierte Aufgaben |
| Sprache | Englisch, Spanisch, Portugiesisch, Polnisch, Japanisch |
| Voraussetzungen | Keine |
| Gueltigkeit | Lifetime fuer `PCEP-30-02`; 8 Jahre fuer `PCEP-30-03` |

!!! warning "Wichtig"
    PCEP prueft Grundlagen, aber nicht nur Definitionen. Viele Aufgaben sind
    Code-Vorhersagen: Was ist die Ausgabe? Welcher Ausdruck ist gueltig?
    Welche Schleife laeuft wie oft? Deshalb immer mit kleinen Codebeispielen
    wiederholen, nicht nur Begriffe lesen.

## Überblick

- PCEP ist die Entry-Level-Zertifizierung des Python Institute.
- Der Fokus liegt auf universellen Programmiergrundlagen und Python-Basics.
- Besonders wichtig sind Datentypen, Operatoren, Kontrollfluss, Schleifen, Collections, Funktionen und einfache Exceptions.
- Die Pruefung ist ein sinnvoller Zwischenschritt vor PCAP.
- PCEP richtet sich an Lernende, angehende Entwickler, Data-Analyst-Einsteiger, Tester und technische Rollen, die Python-Grundlagen nachweisen wollen.
- Nach bestandener Pruefung soll man einfache Python-Programme lesen, schreiben und typische Einsteigerprobleme loesen koennen.
- Die Pruefung prueft Syntax, Semantik, Ablaufverstaendnis und Grundbegriffe der Programmlogik.
- Praktische Erfahrung mit kleinen Programmen, Konsoleneingabe, Bedingungen, Schleifen, Listen, Dictionaries und Funktionen ist wichtiger als Auswendiglernen.

### The Candidate's Profile

Eine Person, die PCEP besteht, sollte insbesondere zeigen koennen:

- grundlegende Programmierbegriffe sicher zu verwenden
- einfache Python-Programme zu lesen und zu schreiben
- Variablen, Literale, Operatoren und Datentypen passend einzusetzen
- Kontrollfluss mit Bedingungen und Schleifen zu modellieren
- Daten mit Listen, Tupeln, Dictionaries und Strings zu verarbeiten
- Funktionen zu definieren, aufzurufen und mit Parametern/Rueckgabewerten zu arbeiten
- einfache Exceptions zu erkennen und mit `try`/`except` zu behandeln
- auf PCAP-Niveau weiterlernen zu koennen

## Domains Covered

### Section 1: Computer Programming and Python Fundamentals (18%)

Objectives covered by the block: 7 exam items.

**PCEP-30-02 1.1 - Fundamental terms and definitions**

- Interpreter vs. Compiler
- Interpretation vs. Compilation
- Lexis, Syntax und Semantik

**PCEP-30-02 1.2 - Python logic and structure**

- Keywords
- Instructions
- Indentation
- Comments

**PCEP-30-02 1.3 - Literals, variables and numeral systems**

- Boolean, Integer und Float
- Scientific notation
- Strings
- Binary, octal, decimal and hexadecimal notation
- Variables
- Naming conventions
- PEP 8 basics

**PCEP-30-02 1.4 - Operators and data types**

- Numeric operators: `**`, `*`, `/`, `%`, `//`, `+`, `-`
- String operators: `*`, `+`
- Assignment and shortcut operators
- Unary and binary operators
- Operator precedence and binding
- Bitwise operators: `~`, `&`, `^`, `|`, `<<`, `>>`
- Boolean operators: `not`, `and`, `or`
- Boolean expressions
- Relational operators: `==`, `!=`, `>`, `>=`, `<`, `<=`
- Floating-point accuracy
- Type casting

**PCEP-30-02 1.5 - Console Input/Output**

- `print()` and `input()`
- `sep=` and `end=`
- `int()` and `float()`

### Section 2: Control Flow - Conditional Blocks and Loops (29%)

Objectives covered by the block: 8 exam items.

**PCEP-30-02 2.1 - Decisions with `if`**

- `if`, `if`-`else`, `if`-`elif`, `if`-`elif`-`else`
- Multiple conditional statements
- Nested conditional statements

**PCEP-30-02 2.2 - Iteration**

- `pass`
- `while`, `for`, `range()` and `in`
- Iterating through sequences
- `while`-`else` and `for`-`else`
- Nested loops and nested conditions
- `break` and `continue`

### Section 3: Data Collections - Tuples, Dictionaries, Lists and Strings (25%)

Objectives covered by the block: 7 exam items.

**PCEP-30-02 3.1 - Lists**

- Constructing vectors
- Indexing and slicing
- `len()`
- List methods such as `.append()`, `.insert()`, `.index()`
- `sorted()`
- `del`
- Iterating through lists
- Initializing loops
- `in` and `not in`
- List comprehensions
- Copying and cloning
- Nested lists: matrices and cubes

**PCEP-30-02 3.2 - Tuples**

- Indexing and slicing
- Building tuples
- Immutability
- Similarities and differences compared to lists
- Lists inside tuples and tuples inside lists

**PCEP-30-02 3.3 - Dictionaries**

- Building dictionaries
- Indexing by key
- Adding and removing keys
- Iterating through keys and values
- Checking whether a key exists
- `.keys()`, `.items()`, `.values()`

**PCEP-30-02 3.4 - Strings**

- Constructing strings
- Indexing and slicing
- Immutability
- Escaping with `\`
- Quotes and apostrophes inside strings
- Multi-line strings
- Basic string functions and methods

### Section 4: Functions and Exceptions (28%)

Objectives covered by the block: 8 exam items.

**PCEP-30-02 4.1 - Functions**

- Defining and invoking user-defined functions
- Generators at beginner level
- `return`
- Returning results
- `None`
- Recursion

**PCEP-30-02 4.2 - Function/environment interaction**

- Parameters vs. arguments
- Positional arguments
- Keyword arguments
- Mixed argument passing
- Default parameter values
- Scopes
- Name hiding / shadowing
- `global`

**PCEP-30-02 4.3 - Built-in exception hierarchy**

- `BaseException`
- `Exception`
- `SystemExit`
- `KeyboardInterrupt`
- Abstract exception categories
- `ArithmeticError`
- `LookupError`
- `IndexError`
- `KeyError`
- `TypeError`
- `ValueError`

**PCEP-30-02 4.4 - Basic exception handling**

- `try`/`except`
- `try`/`except Exception`
- Ordering `except` branches
- Propagating exceptions through function boundaries
- Delegating responsibility for handling exceptions

## Quellen

- [PCEP - Certified Entry-Level Python Programmer](https://pythoninstitute.org/pcep)
- [PCEP-30-02 Exam Syllabus](https://pythoninstitute.org/assets/627e61bc29de3989767095.pdf)
