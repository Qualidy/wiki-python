# Mathematische Operationen
In Python können wir alle einfachen mathematischen Operationen durchführen. Dieses sind grundlegend für die Entwicklung 
von Algorithmen und der Lösung von Problemen. In diesem Abschnitt soll es nur um mathematische Operationen gehen,
die wir mit Ganzzahlen und Fließkommazahlen verwenden können.

## Grundoperationen

[//]: # ([30min])

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/b62k5bR3fsY?si=zcEu6Ef2CEEP9jcS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

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

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZntIVAUqqII?si=Aw37qj3b9AnxH67D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

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

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dJh7L2rlYlE?si=jX4efDDlf8oEU1ST" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

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

### 1. **Addition**🌶️️
Addiere 5 und 3. 
### 2. **Subtraktion**🌶️️
Subtrahiere 2 von 10. 
### 3. **Multiplikation**🌶️
Multipliziere 4 mit 2. 
### 4. **Division**🌶️
Teile 16 durch 2. 
### 5. **Ganzzahlige Division**🌶️
Führe eine ganzzahlige Division von 17 durch 2 durch. 
### 6. **Modulo**🌶️
Finde den Rest der Division von 18 durch 10. 
### 7. **Potenzierung**🌶️
Erhebe 2 in die 3. Potenz. 
### 8. **Quadratwurzel**🌶️🌶️
Berechne die Quadratwurzel von 64. 
### 9. **Exponentialfunktion**🌶️🌶️
Berechne $e^3$ ($e$ ist die Basis des natürlichen Logarithmus). 
### 10. **Natürlicher Logarithmus**🌶️🌶️
Berechne den natürlichen Logarithmus von 8. 
### 11. **Komplexe Rechnung**🌶️
Berechne das Ergebnis von (3 + 4) * 5. 
### 12. **Vergleich**: 🌶️
Überprüfe, ob das Produkt von 2 und 3 gleich 6 ist. 
### 13. **Runden**: 🌶️🌶️
Runde die Zahl 2.7 auf die nächste ganze Zahl. 
### 14. **Negative Zahlen**: 🌶️
Berechne das Produkt von -3 und 3. 
### 15. **Variable in Rechnung**: 🌶️
Definiere eine Variable `x` mit dem Wert 5 und berechne `x * x`. 
### 16. **Verschiedene Operationen**: 🌶️
Berechne das Ergebnis von `2 + 3 * 5`.
### 17. **Einsatz von Klammern**: 🌶️
Ändere den Ausdruck `2 + 3 * 5` so ab, dass zuerst die Addition und dann die 
Multiplikation ausgeführt wird.
### 18. **Potenzierung und Division**: 🌶️
Berechne das Ergebnis von `4 ** 2 / 8`.
### 19. **Mehrere Operationen**: 🌶️
Finde das Ergebnis von `3 + 4 * 2 - 1`.
### 20. **Komplexer Ausdruck**: 🌶️
Berechne den Wert von `(3 + 4) * (5 - 2) ** 2`.

[Lösungen](solutions.md)

# Anspruchsvolle Aufgaben
### **Zinsrechner**🌶️🌶️🌶️

[40 min] 

Aufgabenstellung:

- Schreibe ein Python-Programm, das als einfacher Zinsrechner fungiert. 
- Das Programm soll vom Benutzer das Anfangskapital (Hauptsumme), den Zinssatz (in Prozent) und die Anlagedauer in 
Jahren abfragen. 
- Berechne die Endsumme, die sich aus der Formel Endsumme = Anfangskapital * (1 + Zinssatz/100 * Jahre) ergibt. 
- Gib das berechnete Ergebnis aus.

### **Umrechner für Temperaturen**🌶️🌶️🌶️

[40 min]

Aufgabenstellung:

- Erstelle ein Python-Programm zur Umrechnung von Temperaturen zwischen Celsius und Fahrenheit. 
- Das Programm soll zuerst nach der Eingabetemperatur (als Zahl) fragen und dann, ob diese in Celsius oder Fahrenheit ist. 
- Führe die entsprechende Umrechnung durch: Von Celsius nach Fahrenheit (`F = C * 9/5 + 32`) oder von Fahrenheit nach 
- Celsius (`C = (F - 32) * 5/9`).
- Gib das Ergebnis der Umrechnung aus.

