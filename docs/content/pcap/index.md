# PCAP Vorbereitung

Diese Sektion buendelt die letzte Wiederholungswoche vor dem PCAP-Exam.
Der Schwerpunkt liegt auf Pruefungsformat, Themengewichtung und gezielter Wiederholung.

## Pruefungsformat

Die folgenden Eckdaten beziehen sich auf das PCAP - Certified Associate Python
Programmer Exam (`PCAP-31-03`) und sollten vor der echten Pruefung noch einmal
auf der offiziellen Python-Institute-Seite geprueft werden:
[PCAP - Certified Associate Python Programmer](https://pythoninstitute.org/pcap).

| Punkt | Wert |
|-------|------|
| Pruefung | PCAP - Certified Associate Python Programmer |
| Exam-Code | `PCAP-31-03` |
| Fragen | 40 |
| Zeit | 65 Minuten |
| Bestehensgrenze | 70% |
| Fragetypen | Single Choice, Multiple Choice, Luecken/Drag-and-Drop je nach Plattform |
| Sprache | Englisch |

!!! warning "Wichtig"
    In der Vorbereitung sind Probetests nur dann sinnvoll, wenn danach sauber
    ausgewertet wird. Nicht nur Punkte zaehlen, sondern jede falsche Antwort
    einem Thema zuordnen.

## Testexamen

- [Testfragen 1](testexam_1.md)
- [Testfragen 2](testexam_2.md)
- [Testexam 3 (PCAP-31-02)](testexam_3.md): basiert auf der Vorgaengerversion `PCAP-31-02`
- [Testexam 4 (PCAP-31-03)](testexam_4.md)

## Überblick

- PCAP ist eine Associate-Zertifizierung des Python Institute.
- Der Fokus liegt auf Python-Grundlagen mit klarer Vertiefung in Richtung fortgeschrittener Programmierung.
- Besonders wichtig sind objektorientierte Programmierung, Module und Packages, Exceptions, Strings, Comprehensions, Lambdas, Generatoren, Closures und Dateioperationen.
- Die Zertifizierung richtet sich an Lernende, Quereinsteiger, Junior-Developer, Tester, Data-Analyst-Einsteiger und technische Rollen, die Python als Grundlage brauchen.
- Nach bestandener Pruefung soll man mehrmodulige Python-Programme entwerfen, entwickeln und verbessern koennen.
- Die Pruefung prueft nicht nur Syntaxwissen, sondern auch Anwendung auf realistische Programmieraufgaben.
- Empfohlen werden solide Grundlagen in Variablen, Datentypen, Kontrollstrukturen, Funktionen, Modulen, Algorithmen und Datenstrukturen.
- Praktische Erfahrung mit Entwicklungsumgebungen, dem Ausfuehren von Programmen, Libraries, Modulen und Debugging ist wichtig.
- Keine formalen Voraussetzungen, lebenslange Gueltigkeit, 65 Minuten, 40 Fragen, 70 Prozent Bestehensgrenze, Pearson-VUE Online-Proctoring.

### The Candidate's Profile

The test candidate who has passed the PCAP-31-0x exam demonstrates the following proficiency in Python programming:

- an ability to design, develop and improve multi-module computer applications coded in Python
- an ability to analyze and model real-life problems in OOP categories
- experience allowing her/him to take a job as a junior developer
- sufficient skills to create and develop her/his own programming portfolio
- the potential to use Python in everyday life applications including DIY activities

## Domains Covered

### Section 1: Modules and Packages (12%)

Objectives covered by the block (6 exam items)

**PCAP-31-03 1.1 - Import and use modules and packages**

!!! info "Relevante Skriptstellen"
    - [Imports Einführung](../python_grundlagen/module/module.md)
    - [Pakete](../module_pakete_pip/pakete/pakete.md)
    - [Pip und Venv](../module_pakete_pip/pip_venv/pip_venv.md)
    - [Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md)
    - [Wiederholung Woche 8: Module, Imports und Standardmodule](../wiederholung/module_imports_wiederholung.md#weitere-pcap-relevante-standardmodule)

- import variants: `import`, `from import`, `import as`, `import *`
- advanced qualifying for nested modules
- the `dir()` function
- the `sys.path` variable

**PCAP-31-03 1.2 - Perform evaluations using the `math` module**

!!! info "Relevante Skriptstellen"
    - [Mathematische Operationen](../python_grundlagen/math_operations/math_operations.md)
    - [Operatoren und Precedence](../wiederholung_woche8/operatoren_precedence.md)

- functions: `ceil()`, `floor()`, `trunc()`, `factorial()`, `hypot()`, `sqrt()`

**PCAP-31-03 1.3 - Generate random values using the `random` module**

!!! info "Relevante Skriptstellen"
    - [Imports Einführung](../python_grundlagen/module/module.md)
    - [Pakete](../module_pakete_pip/pakete/pakete.md)
    - [Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md)

- functions: `random()`, `seed()`, `choice()`, `sample()`

**PCAP-31-03 1.4 - Discover host platform properties using the `platform` module**

!!! info "Relevante Skriptstellen"
    - [Imports Einführung](../python_grundlagen/module/module.md)
    - [Pakete](../module_pakete_pip/pakete/pakete.md)
    - [Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md)

- functions: `platform()`, `machine()`, `processor()`, `system()`, `version()`, `python_implementation()`, `python_version_tuple()`

**PCAP-31-03 1.5 - Create and use user-defined modules and packages**

!!! info "Relevante Skriptstellen"
    - [Imports Einführung](../python_grundlagen/module/module.md)
    - [Pakete](../module_pakete_pip/pakete/pakete.md)
    - [Pip und Venv](../module_pakete_pip/pip_venv/pip_venv.md)
    - [Module und Imports Wiederholung](../wiederholung/module_imports_wiederholung.md)

- idea and rationale
- the `__pycache__` directory
- the `__name__` variable
- public and private variables
- the `__init__.py` file
- searching for/through modules/packages
- nested packages vs. directory trees

### Section 2: Exceptions (14%)

Objectives covered by the block (5 exam items)

**PCAP-31-03 2.1 - Handle errors using Python-defined exceptions**

!!! info "Relevante Skriptstellen"
    - [Try-Except](../python_grundlagen/try_except/try_except.md)
    - [Exceptions Vertiefung](../exceptions/index.md)
    - [Exceptions Wiederholung](../wiederholung/exceptions.md)
    - [Eigene Exceptions](../wiederholung_woche8/eigene_exceptions.md)

- `except`, `except`-`except`, `except`-`else`, `except (e1, e2)`
- the hierarchy of exceptions
- `raise`, `raise ex`
- `assert`
- event classes
- `except E as e`
- the `arg` property

**PCAP-31-02 2.2 - Extend the Python exceptions hierarchy with self-defined exceptions**

!!! info "Relevante Skriptstellen"
    - [Exceptions Vertiefung](../exceptions/index.md)
    - [Exceptions Wiederholung](../wiederholung/exceptions.md)
    - [Eigene Exceptions](../wiederholung_woche8/eigene_exceptions.md)

- self-defined exceptions
- defining and using self-defined exceptions

### Section 3: Strings (18%)

Objectives covered by the block (8 exam items)

**PCAP-31-03 3.1 - Understand machine representation of characters**

!!! info "Relevante Skriptstellen"
    - [Strings](../python_grundlagen/strings/strings.md)
    - [chr und ord](../wiederholung_woche8/chr_ord.md)

- encoding standards: ASCII, UNICODE, UTF-8, code points, escape sequences

**PCAP-31-03 3.2 - Operate on strings**

!!! info "Relevante Skriptstellen"
    - [Strings](../python_grundlagen/strings/strings.md)
    - [chr und ord](../wiederholung_woche8/chr_ord.md)
    - [Mutable, Immutable und Referenzen](../wiederholung_woche8/mutable_immutable_referenzen.md)

- functions: `ord()`, `chr()`
- indexing, slicing, immutability
- iterating through strings, concatenating, multiplying, comparing against strings and numbers
- operators: `in`, `not in`

**PCAP-31-03 3.3 - Employ built-in string methods**

!!! info "Relevante Skriptstellen"
    - [Strings](../python_grundlagen/strings/strings.md)
    - [Listen](../datenstrukturen/lists/lists.md)
    - [Listen Wiederholung](../wiederholung/list_wiederholung.md)
    - [Listen, Slices und Sortieren](../wiederholung_woche8/listen_slices_sortieren.md)

- methods: `.isxxx()`, `.join()`, `.split()`, `.sort()`, `sorted()`, `.index()`, `.find()`, `.rfind()`

### Section 4: Object-Oriented Programming (34%)

Objectives covered by the block (12 exam items)

**PCAP-31-03 4.1 - Understand the Object-Oriented approach**

!!! info "Relevante Skriptstellen"
    - [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)
    - [OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md)
    - [Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md)
    - [Quiz OOP Grundlagen](../oop_vertiefung_teil2/quiz_oop_grundlagen.md)

- ideas and notions: class, object, property, method, encapsulation, inheritance, superclass, subclass, identifying class components

**PCEP-31-03 4.2 - Employ class and object properties**

!!! info "Relevante Skriptstellen"
    - [Attribute](../oop_grundlagen/attributes/attributes.md)
    - [Protected & Private](../oop_vertiefung/protected_private/protected_private.md)
    - [Getter & Setter](../oop_vertiefung/getter_setter/getter_setter.md)
    - [Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md)
    - [Mutable, Immutable und Referenzen](../wiederholung_woche8/mutable_immutable_referenzen.md)

- instance vs. class variables: declarations and initializations
- the `__dict__` property: objects vs. classes
- private components: instances vs. classes
- name mangling

**PCAP-31-03 4.3 - Equip a class with methods**

!!! info "Relevante Skriptstellen"
    - [Methoden](../oop_grundlagen/methods/methods.md)
    - [Class- & Staticmethod](../oop_vertiefung/class_static_methods/class_static_methods.md)
    - [Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md)
    - [super() in Klassen](../wiederholung_woche8/super_init_methoden.md)

- declaring and using methods
- the `self` parameter

**PCAP-31-03 4.4 - Discover the class structure**

!!! info "Relevante Skriptstellen"
    - [Polymorphismus & Introspection](../oop_vertiefung_teil2/polymorphismus_introspection.md)
    - [OOP Wiederholung](../oop_vertiefung_teil2/oop_wiederholung.md)
    - [Quiz Polymorphismus & Introspection](../oop_vertiefung_teil2/quiz_polymorphismus_introspection.md)
    - [Quiz Wochenreview](../oop_vertiefung_teil2/quiz_wochenreview.md)

- introspection and the `hasattr()` function: objects vs. classes
- properties: `__name__`, `__module__`, `__bases__`

**PCAP-31-03 4.5 - Build a class hierarchy using inheritance**

!!! info "Relevante Skriptstellen"
    - [Vererbung](../oop_vertiefung/vererbung_polymorphismus/vererbung/vererbung.md)
    - [Magic Methods](../oop_vertiefung/magic_methods/magic_methods.md)
    - [Komposition, Vererbung & Mixins](../oop_vertiefung_teil2/komposition_mixins.md)
    - [Mehrfachvererbung, MRO & Diamond](../oop_vertiefung_teil2/mro_diamond.md)
    - [Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md)
    - [super() in Klassen](../wiederholung_woche8/super_init_methoden.md)
    - [Quiz Komposition, Mixins & MRO](../oop_vertiefung_teil2/quiz_komposition_mixins_mro.md)

- single and multiple inheritance
- the `isinstance()` function
- overriding
- operators:
- `not is`, `is`
- polymorphism
- overriding the `__str__()` method
- diamonds

**PCAP-31-03 4.6 - Construct and initialize objects**

!!! info "Relevante Skriptstellen"
    - [Klassen definieren](../oop_grundlagen/define_classes/define_classes.md)
    - [Methoden](../oop_grundlagen/methods/methods.md)
    - [Klassen, super() und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md)
    - [super() in Klassen](../wiederholung_woche8/super_init_methoden.md)

- declaring and invoking constructors

### Section 5: Miscellaneous (22%)

Scope: List Comprehensions, Lambdas, Closures, and I/O Operations

Objectives covered by the block (9 exam items)

**PCAP-31-03 5.1 - Build complex lists using list comprehension**

!!! info "Relevante Skriptstellen"
    - [List Comprehensions](../comprehensions/list_comp/list_comp.md)
    - [Listen](../datenstrukturen/lists/lists.md)
    - [Comprehensions Wiederholung](../wiederholung/comprehension_wiederholung.md)
    - [Listen, Slices und Sortieren](../wiederholung_woche8/listen_slices_sortieren.md)

- list comprehensions: the `if` operator, nested comprehensions

**PCAP-31-03 5.2 - Embed lambda functions into the code**

!!! info "Relevante Skriptstellen"
    - [Lambda](../funktionen_fortgeschritten/lambda/lambda.md)
    - [Funktionen](../python_grundlagen/functions/functions.md)
    - [map, filter und lambda](../wiederholung_woche8/map_filter_lambda.md)

- lambdas: defining and using lambdas
- self-defined functions taking lambdas as arguments
- functions: `map()`, `filter()`

**PCAP-31-03 5.3 - Define and use closures**

!!! info "Relevante Skriptstellen"
    - [Scopes](../funktionen_vertiefung/scopes/scopes.md)
    - [Funktionen](../python_grundlagen/functions/functions.md)
    - [Scope, Closure & Variablen](../wiederholung/function_scopes_and_closure.md)
    - [Scope und Closure](../wiederholung_woche8/scope_closure.md)

- closures: meaning and rationale
- defining and using closures

**PCAP-31-03 5.4 - Understand basic Input/Output terminology**

!!! info "Relevante Skriptstellen"
    - [Ein- und Ausgabe](../python_grundlagen/input_output/input_output.md)
    - [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)
    - [Dateien lesen und schreiben](../wiederholung_woche8/dateien.md)

- I/O modes
- predefined streams
- handles vs. streams
- text vs. binary modes

**PCAP-31-03 5.5 - Perform Input/Output operations**

!!! info "Relevante Skriptstellen"
    - [Dateioperationen](../dateien_dateisystem/dateioperationen/dateioperationen.md)
    - [Dateien lesen und schreiben](../wiederholung_woche8/dateien.md)
    - [bytearray](../wiederholung_woche8/bytearray.md)

- the `open()` function
- the `errno` variable and its values
- functions: `close()`, `.read()`, `.write()`, `.readline()`, `readlines()`
- using `bytearray` as input/output buffer
