# Mathematische Operationen
In Python können wir alle einfachen mathematischen Operationen durchführen. Dieses sind grundlegend für die Entwicklung 
von Algorithmen und der Lösung von Problemen. In diesem Abschnitt soll es nur um mathematische Operationen gehen,
die wir mit Ganzzahlen und Fließkommazahlen verwenden können.

## Grundoperationen

[//]: # ([30min])

{{ youtube_video("https://www.youtube.com/embed/b62k5bR3fsY?si=zcEu6Ef2CEEP9jcS") }}

**Addition (`+`)**: Addiert zwei Zahlen.
```python
summe = 5 + 3  # Ergibt 8
```
**Subtraktion (`-`)**: Subtrahiert eine Zahl von einer anderen.

```python
differenz = 10 - 2  # Ergibt 8
```

**Multiplikation (`*`)**: Multipliziert zwei Zahlen.

```python
produkt = 4 * 2  # Ergibt 8
```

**Division (`/`)**: Teilt eine Zahl durch eine andere.

```python
quotient = 16 / 2  # Ergibt 8
```

**Ganzzahlige Division (`//`)**: Teilt eine Zahl durch eine andere und rundet das Ergebnis auf die nächste ganze Zahl ab.

```python
ganzzahliger_quotient = 17 // 2  # Ergibt 8
```

**Modulo (`%`)**: Gibt den Rest einer Division zurück.

```python
rest = 18 % 10  # Ergibt 8
```

**Potenzierung (`**`)**: Erhebt eine Zahl in die Potenz einer anderen.

```python
potenz = 2 ** 3  # Ergibt 8
```

## Erweiterte Operationen

[//]: # ([30min])

{{ youtube_video("https://www.youtube.com/embed/ZntIVAUqqII?si=Aw37qj3b9AnxH67D") }}

Für komplexere mathematische Operationen wie Wurzeln oder trigonometrische Funktionen benötigst Du das `math`-Modul, 
das viele nützliche Funktionen bietet. 

Um das `math`-Modul nutzen zu können, muss es importiert werden:
```python
import math
```

Hier sind einige Beispiele:

**Quadratwurzel (`math.sqrt(x)`)**: Berechnet die Quadratwurzel einer Zahl.

```python
import math
wurzel = math.sqrt(64)  # Ergibt 8
```

**Exponentialfunktion (`math.exp(x)`)**: Berechnet e^x, wobei e ~ 2,718282... die Eulersche Zahl ist.

```python
import math
exponent = math.exp(3)  # Berechnet e^3
```

**Logarithmus (`math.log(x, base)`)**: Berechnet den Logarithmus einer Zahl zu einer bestimmten Basis.

```python
import math
log_nat = math.log(8, 2)  # Berechnet den Logarithmus von 8 zur Basis 2
```

## Reihenfolge der Operationen

[//]: # ([30min])

{{ youtube_video("https://www.youtube.com/embed/dJh7L2rlYlE?si=jX4efDDlf8oEU1ST") }}

In Python, wie in den meisten Programmiersprachen, ist die Reihenfolge der mathematischen Operationen wichtig und folgt 
etablierten mathematischen Konventionen. Diese Reihenfolge bestimmt, in welcher Reihenfolge die Operationen in einem 
Ausdruck ausgeführt werden.

1. **Klammern (`()`)** haben die höchste Priorität und werden zuerst ausgewertet. Sie können verwendet werden, um die 
Ausführungsreihenfolge zu ändern. Zum Beispiel wird in `(3 + 4) * 5` zuerst die Addition innerhalb der Klammern 
durchgeführt und dann die Multiplikation.

2. **Potenzierung (`**`)** wird als nächstes ausgeführt. Sie hat eine höhere Priorität als Multiplikation und Division.

3. **Multiplikation (`*`) und Division (`/`)** folgen danach. Sie haben die gleiche Priorität und werden von links nach
rechts ausgeführt.

4. **Addition (`+`) und Subtraktion (`-`)** haben die niedrigste Priorität und werden zuletzt ausgeführt, ebenfalls von 
links nach rechts.

Es ist wichtig, sich die Reihenfolge der Operationen zu merken, um Fehler in Berechnungen zu vermeiden und den Code 
klar und präzise zu gestalten. Die gute Nachricht: Die Reihenfolge entspricht exakt dem was wir aus der normalen 
Mathematik kennen!

Üben wir das Ganze:

# Aufgaben
[30min]

Berechne und gib jeweils das Ergebnis aus:

{{ task(file="tasks/python_grundlagen/math_operations/math_operations/01_addition.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/02_subtraktion.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/03_multiplikation.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/04_division.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/05_ganzzahlige_division.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/06_modulo.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/07_potenzierung.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/08_quadratwurzel.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/09_exponentialfunktion.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/10_naturlicher_logarithmus.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/11_komplexe_rechnung.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/12_vergleich.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/13_runden.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/14_negative_zahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/15_variable_in_rechnung.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/16_verschiedene_operationen.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/17_einsatz_von_klammern.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/18_potenzierung_und_division.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/19_mehrere_operationen.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/20_komplexer_ausdruck.yaml") }}
# Anspruchsvolle Aufgaben
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/21_zinsrechner.yaml") }}
{{ task(file="tasks/python_grundlagen/math_operations/math_operations/22_umrechner_fur_temperaturen.yaml") }}
