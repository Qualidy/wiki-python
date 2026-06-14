# OOP Vertiefung Teil 2

In dieser Woche werden die bekannten OOP-Grundlagen wiederholt und danach
schrittweise vertieft. Der Schwerpunkt liegt auf den Themen, die in PCAP-Aufgaben
häufig in Codebeispielen geprüft werden:

- Klassen, Objekte, Attribute und Methoden sicher erkennen
- Instanzattribute und Klassenattribute unterscheiden
- Konstruktoren und `super()` verstehen
- Overriding und Polymorphismus anwenden
- Klassen und Objekte mit Introspection untersuchen
- Vererbung, Komposition und Mixins unterscheiden
- Mehrfachvererbung, MRO und Diamond Problem nachvollziehen
- ein eigenes OOP-Projekt planen, dokumentieren und umsetzen

## Wiederholung: bekannte OOP-Konzepte

Die Wiederholung dient dazu, die wichtigsten Begriffe wieder sauber zu ordnen:

| Begriff | Kurzbeschreibung |
|---------|------------------|
| Klasse | Bauplan für Objekte |
| Objekt / Instanz | konkretes Exemplar einer Klasse |
| Attribut | Eigenschaft eines Objekts oder einer Klasse |
| Methode | Funktion, die zu einer Klasse gehört |
| `self` | Referenz auf das aktuelle Objekt |
| Konstruktor | `__init__`, initialisiert ein neues Objekt |
| Klassenattribut | Attribut auf Klassenebene, geteilt über Instanzen |
| Instanzattribut | Attribut eines konkreten Objekts |
| Kapselung | Daten und Verhalten werden in Klassen zusammengefasst |
| Vererbung | Unterklassen übernehmen Verhalten von Oberklassen |
| Overriding | Unterklasse ersetzt Methode der Oberklasse |

## Vertiefung: neue Schwerpunkte

Die neuen Themen bauen auf dieser Wiederholung auf. Besonders wichtig ist,
Code nicht nur schreiben, sondern auch **vorhersagen** zu können:

- Welche Methode wird ausgeführt?
- Wo liegt ein Attribut wirklich?
- Was steht in `obj.__dict__`?
- Warum ist `isinstance()` bei Vererbung oft besser als `type()`?
- In welcher Reihenfolge sucht Python bei Mehrfachvererbung?
