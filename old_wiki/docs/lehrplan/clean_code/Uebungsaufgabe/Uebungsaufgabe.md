# Übungsaufgabe: Verwaltung von Büchereidaten
🌶️🌶️🌶️

[90 min]

**Ziel:** Entwickeln Sie ein Python-Programm, das eine JSON-Datei mit Büchereidaten einliest, die Daten manipuliert und das Ergebnis in eine neue Datei schreibt. Dabei sollen diverse Python-Konzepte angewandt werden.

**Vorgaben:**

* JSON-Datei Einlesen: Die JSON-Datei enthält eine Liste von Büchern. Jedes Buch ist ein Objekt mit den Eigenschaften titel, autor, jahr und seitenzahl.
* Manipulation der Objekte: Fügen Sie jedem Buchobjekt ein neues Attribut lesezeit hinzu, das auf der Seitenzahl basiert (angenommen, eine Seite wird durchschnittlich in 2 Minuten gelesen).
* `with` Statements: Verwenden Sie With Statements, um die JSON-Dateien zu öffnen und zu schreiben.
* Klassenkonzept: Definieren Sie eine Klasse Buecherei, die Methoden zur Verwaltung der Buchdaten enthält.
* Docstrings und Typhinweise: Fügen Sie allen Methoden und Funktionen sinnvolle Docstrings hinzu und verwenden Sie Typhinweise, um die Datentypen der Parameter und Rückgabewerte zu spezifizieren.
* List Comprehensions: Nutzen Sie List Comprehensions, um die Daten effizient zu manipulieren.

**Beispiel für die JSON-Datei (buecher.json):**

```json
[
    {"titel": "Python Programmierung", "autor": "Max Muster", "jahr": 2020, "seitenzahl": 300},
    {"titel": "Datenanalyse mit Python", "autor": "Erika Beispiel", "jahr": 2018, "seitenzahl": 250}
]
```
**Aufgabenstellung:**

* Schreiben Sie eine Python-Klasse Buecherei, die Methoden zum Einlesen der Bücher aus einer JSON-Datei, zum Hinzufügen der lesezeit zu jedem Buch und zum Schreiben der manipulierten Daten in eine neue Datei enthält.
* Die Methode zum Hinzufügen der lesezeit sollte eine List Comprehension verwenden, um die lesezeit für jedes Buch zu berechnen und hinzuzufügen.
* Implementieren Sie die Ein- und Ausgabe von Dateien mithilfe von With Statements.
* Jede Methode und Funktion sollte einen Docstring im Numpy-Stil enthalten, der ihren Zweck, ihre Parameter und ihre Rückgabewerte beschreibt. Verwenden Sie auch Typhinweise, um die Datentypen der Parameter und Rückgabewerte anzugeben.
 
**Erwartetes Ergebnis:** Ein Python-Skript, das die vorgegebene JSON-Datei einliest, die Daten entsprechend der Aufgabenstellung manipuliert und das Ergebnis in einer neuen JSON-Datei speichert. Der Code sollte klar und gut dokumentiert sein, um das Verständnis und die Wiederverwendbarkeit zu erleichtern.

[Lösung](solution.md)