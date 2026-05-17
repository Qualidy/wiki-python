# Navigation Structure

This document defines the menu hierarchy for the wiki. Content will be unlocked progressively via git branches, following the course timeline (weeks 1-8).

## Structure Overview: 1-3 Top-Level Items per Week

### Week 1: Python Grundlagen

1. **Python Grundlagen**
   - Variables, types, operators, control flow, imports, debugger introduction

2. **Funktionen & Fehlerbehandlung**
   - Basic functions, type hints, parameters, try/except basics

---

### Week 2: Datenstrukturen

1. **Datenstrukturen**
   - Lists, tuples, sets, dicts, nested structures, enumerate(), zip()

---

### Week 3: Funktionen & OOP-Einstieg

1. **Funktionen Vertiefung**
   - Scope (local, global), *args, **kwargs, lambda, closures, map/filter

2. **Comprehensions**
   - List/dict/set comprehensions, data transformation, comparison to loops

3. **OOP Grundlagen**
   - Classes, `__init__`, methods, attributes, self, object instantiation

---

### Week 4: Fehlerbehandlung & Dateisystem

1. **Exceptions Vertiefung**
   - Exception hierarchy, try/except/else/finally, custom exceptions, raise

2. **Dateien & Dateisystem**
   - File I/O (read/write/append modes), os module, datetime, path handling, with statement

3. **Module, Pakete & pip**
   - Custom modules, packages, `__name__ == "__main__"`, pip, venv, requirements.txt

---

### Week 5: Objektorientierte Programmierung Vertiefung

1. **Vererbung & Polymorphismus**
   - Inheritance, super(), method override, isinstance(), issubclass()

2. **MRO & Mehrfachvererbung**
   - Method Resolution Order (__mro__), C3 linearization, diamond problem

3. **Dunder-Methoden & Kapselung**
   - `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`, `__getitem__`, `__setitem__`
   - Private attributes (`_private`, `__mangling`), @property, abstract classes (@abstractmethod)

---

### Week 6: Projekt

1. **Projekt 1: CLI-Anwendung**
   - Hands-on project applying weeks 1-5 content
   - Requirements: 2+ classes with inheritance, custom exceptions, file persistence, type hints, error handling

---

### Week 7: Projekt & Fortgeschrittene Konzepte

1. **Generatoren & Dekoratoren**
   - `yield`, generator functions vs normal functions, generator expressions
   - Decorator pattern, `@decorator` syntax, functools.wraps, practical examples

2. **Projekt 2: Erweiterte CLI**
   - Enhancement of Projekt 1 with generators, decorators, and advanced patterns

---

### Week 8: Prüfungsvorbereitung

1. **Prüfungsvorbereitung PCAP-31-03**
   - Mock exams (PCEP / PCAP format depending on path)
   - Review by exam weight: Modules/pip (12%), Strings/Exceptions (18%), OOP Basics (25%), OOP Advanced (20%), Files/os/datetime (25%)
   - Exam strategy, common pitfalls, time management

---

## Implementation Notes

- **Disabled state:** Items are shown in the menu but disabled until their corresponding week/content is ready
- **Branch unlocking:** Content is merged when ready, enabling the menu item
- **Progressive disclosure:** Students see the full learning path upfront but can only access current/past content
- **Lookup friendly:** Topic names are descriptive enough that students can find what they need later without remembering week numbers

## Future Renaming

Item names may be refined as content develops. This serves as the initial structure and reference point.
