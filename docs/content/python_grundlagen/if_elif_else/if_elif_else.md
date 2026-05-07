# Verzweigungen
Verzweigungen sind ein wesentlicher Bestandteil der Programmierung. Sie ermöglichen es, Entscheidungen auf Basis 
bestimmter Bedingungen zu treffen. 

In Python verwenden wir dafür `if`, `elif` (else if) und `else` zur Steuerung des Programmflusses:

## Grundstruktur
{{ youtube_video("https://www.youtube.com/embed/GA8Oj97qUXM?si=Ne0kUbnFBrmg-w0a") }}

[//]: # ([20min])
Die grundlegende Struktur einer `if-else`-Verzweigung in Python sieht folgendermaßen aus:

```python
if bedingung:
    # Anweisungen, wenn Bedingung wahr ist
else:
    # Anweisungen, wenn Bedingung falsch ist
```

Die `bedingung` ist ein Ausdruck, der entweder wahr (`True`) oder falsch (`False`) ergibt. Die Anweisungen müssen eingerückt sein! Dies ist ein fundamentales Prinzip in Python, mit dem wir sehr schnell vertraut sein werden.

### Bedingungen

[//]: # ([50min])
In Python werden Bedingungen in `if`-Abfragen verwendet, um zu bestimmen, ob bestimmte Anweisungen ausgeführt werden 
sollen oder nicht. Diese Bedingungen können auf unterschiedliche Weise formuliert werden, um die Logik des Programms 
zu steuern. 

Eine grundlegende Bedingung in einer `if`-Abfrage könnte so einfach sein wie der Vergleich zweier Werte. Zum Beispiel 
überprüft `if alter >= 18:` ob das Alter einer Person 18 Jahre oder älter ist. Hierbei wird ein Gleichheits- oder 
Ungleichheitsoperator verwendet, um zu entscheiden, ob der Code innerhalb des `if`-Blocks ausgeführt wird.

Komplexere Bedingungen können durch die Verwendung logischer Operatoren wie `and`, `or` und `not` erstellt werden. 
Eine solche Bedingung könnte lauten `if alter >= 18 and student == True:`, was bedeutet, dass der Code nur ausgeführt 
wird, wenn die Person 18 Jahre oder älter ist und gleichzeitig ein Student ist.

Python ermöglicht auch die Überprüfung von Mitgliedschaften mit dem `in`-Operator in Bedingungen. Ein Beispiel wäre 
`if frucht in ['Apfel', 'Banane', 'Kirsche']:`. Diese Bedingung prüft, ob der Wert der Variablen `frucht` in der 
angegebenen Liste enthalten ist. Dies ist eine sehr mächtige Bedingung, die man häufig praktisch verwenden kann 
und ein gutes Beispiel für 'pythonic' Code sind.

Bedingungen können auch komplexere Ausdrücke beinhalten, wie z.B. Funktionsaufrufe oder kombinierte Vergleiche. Zum 
Beispiel kann `if ist_regnerisch() and temperatur < 20:` eine Bedingung sein, die wahr ist, wenn die Funktion 
`ist_regnerisch()` `True` zurückgibt und die Temperatur unter 20 Grad liegt.

Insgesamt erlauben Bedingungen in `if`-Abfragen in Python, sehr flexible und leistungsfähige Kontrollstrukturen in 
Programmen zu erstellen, von einfachen Vergleichen bis hin zu komplexen logischen Ausdrücken.

Die Bausteine dafür sehen wir hier:

- Vergleichsoperatoren: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logische Operatoren: `and`, `or`, `not`
- Überprüfung auf Null/None: `is None`, `is not None`

**Beispiel**:
```python
alter = 18
if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")
```

##  if-elif-else-Abfragen

{{ youtube_video("https://www.youtube.com/embed/r-OHMDZNyzQ?si=2lp4Dxp_TS4immP2") }}

[//]: # ([30min])
Oft benötigen wir mehr als zwei Zweige, zum Beispiel wenn wir für verschiedene Altersklassen andere Aktionen ausführen 
müssen oder wollen.

`elif` erlaubt es, mehrere Bedingungen nacheinander zu überprüfen.

**Grundstruktur**
```python
if bedingung1:
    # Anweisungen, wenn bedingung1 wahr ist
elif bedingung2:
    # Anweisungen, wenn bedingung2 wahr ist
else:
    # Anweisungen, wenn keine Bedingung wahr ist
```

Es können beliebig viele Zweige entstehen. Hat der Code sehr viele Zweige, sollte man sich jedoch fragen, ob man das 
nicht anders lösen kann. Je mehr Einrückungsebenen es gibt, desto schwieriger wird es für andere den Code zu lesen.

**Beispiel**
```python
zahl = 15
if zahl > 10:
    print("Die Zahl ist größer als 10.")
elif zahl == 10:
    print("Die Zahl ist genau 10.")
else:
    print("Die Zahl ist kleiner als 10.")
```

Die Verwendung von `if`, `elif` und `else` in Python ermöglicht es, basierend auf Bedingungen unterschiedliche Wege im 
Programm einzuschlagen. Das findet man eigentlich in jedem Programm, da die Unterscheidung von Aktionen basierend auf
einer oder mehrere Bedingungen ein zentraler Bestandteil der Softwareentwicklung ist.

# Aufgaben

[//]: # ([70min])
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/01_einfache_if_abfrage.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/02_if_else.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/03_negativ_oder_positiv.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/04_groer_oder_kleiner.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/05_alter_uberprufen.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/06_passwortuberprufung.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/07_maximalwert.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/08_bewertung.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/09_temperaturen.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/10_einfache_rechnung.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/11_jahreszeiten.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/12_teilbarkeit.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/13_einkaufsliste.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/14_grote_von_drei_zahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/15_rabattaktion.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/16_lichtschalter.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/17_fahrzeugklasse.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/18_kinotag.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/19_schaltjahr.yaml") }}
# Anspruchsvolle Aufgaben

[//]: # ([30min])
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/20_benutzereingaben_filtern_und_sortieren.yaml") }}
{{ task(file="tasks/python_grundlagen/if_elif_else/if_elif_else/21_entwickle_ein_textbasiertes_rollenspiel.yaml") }}
