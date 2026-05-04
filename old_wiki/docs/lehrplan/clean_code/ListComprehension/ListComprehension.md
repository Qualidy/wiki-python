# List Comprehensions
[30 min]

List comprehensions sind ein sehr nützliches Werkzeug, das Python bietet, um Listen zu erstellen. Sie sind oft schneller als normale Schleifen, da sie in C geschrieben wurden. List comprehensions sind in der Regel kompakter als normale Schleifen, da sie in einer Zeile geschrieben werden können. Sie sind nicht immer leicht zu lesen, aber sie sind ein guter Weg, um zu zeigen, wie mächtig Python ist! Im Folgenden werden einige Beispiele für die Verwendung von List Comprehensions gezeigt.

**Beispiel 1**

Zunächst ein klassisches Beispiel, um eine Liste zu erstellen, die die Quadratzahlen von 1 bis 10 enthält.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
squared_evens = []
for x in numbers:
    if x % 2 == 0 and x < 10:
        squared_evens.append(x**2)
```
Diese Schleife kann in eine List-Comprehension umgewandelt werden, um den Code kompakter und in vielen Fällen lesbarer zu machen.

```python
squared_evens = [x**2 for x in numbers if x % 2 == 0 and x < 10]
```

In dieser List-Comprehension wird für jedes Element x in der Liste numbers überprüft, ob es gerade ist (x % 2 == 0) und kleiner als 10 (x < 10). Wenn beide Bedingungen erfüllt sind, wird das Quadrat von x (x**2) in die neue Liste squared_evens aufgenommen.

Dieser Ansatz ist oft bevorzugt, wenn die Operationen relativ einfach sind und die Klarheit des Codes davon profitiert.

**Beispiel 2**

Angenommen, wir haben einen Satz:
```python
sentence = "The quick brown fox jumps over the lazy dog"
```

Wir möchten eine Liste erstellen, die die Länge jedes Wortes in diesem Satz enthält, aber nur, wenn das Wort länger als drei Buchstaben ist. List-Comprehension Ansatz:

```python
word_lengths = [len(word) for word in sentence.split() if len(word) > 3]
```

**Vorteile von List Comprehensions:**
* **Kompakter Code:** List Comprehensions ermöglichen es, komplexe Operationen in einer einzigen, kompakten Zeile zu schreiben, was den Code kürzer und oft leichter lesbar macht. 
* **Verbesserte Lesbarkeit:** Für Personen, die mit der Syntax vertraut sind, können List Comprehensions die Absicht des Codes klarer machen als eine entsprechende Schleife.
* **Höhere Ausführungsgeschwindigkeit:** List Comprehensions können in einigen Fällen schneller ausgeführt werden als äquivalente Schleifen, da die Iteration intern optimiert ist.
* **Direkte Nutzung von Funktionen und Bedingungen:** In List Comprehensions können Funktionen und bedingte Logik direkt verwendet werden, was die Notwendigkeit separater Schleifen oder bedingter Anweisungen reduziert.
* **Reduzierung des Bedarfs an temporären Variablen:** List Comprehensions erlauben es, ohne zusätzliche temporäre Listen oder Variablen auszukommen, was den Speicherverbrauch reduzieren kann.
* **Förderung eines funktionalen Programmierstils:** List Comprehensions unterstützen einen funktionalen Ansatz, bei dem Datenverarbeitungsvorgänge oft klarer und konziser ausgedrückt werden können.
* **Einfache Integration mehrerer Iteratoren:** Komplexe List Comprehensions können mehrere Iteratoren und verschachtelte Schleifen in einer einzigen Zeile integrieren, was in traditionellen Schleifenstrukturen oft umständlicher ist.
* **Gute Unterstützung in der Python-Community:** List Comprehensions sind ein beliebtes Feature in Python und werden von der Community gut unterstützt, was bedeutet, dass viele Ressourcen und Beispiele zur Verfügung stehen.

### Aufgabe 1: Filtern und Umwandeln von Zahlen 🌶️🌶️
[15 min]
Gegeben ist eine Liste von Zahlen. Erstelle eine neue Liste, die das Quadrat jeder ungeraden Zahl aus der ursprünglichen Liste enthält, sofern die Zahl größer als 10 ist.

Beispiel-Liste: `numbers = [9, 12, 17, 21, 28, 33, 35]`

[Lösung](solution.md#lsung-aufgabe-1)

### Aufgabe 2: Extrahieren von Anfangsbuchstaben 🌶️
[10min]
Gegeben ist eine Liste von Namen. Erstelle eine neue Liste, die den ersten Buchstaben jedes Namens enthält.

Beispiel-Liste: `names = ["Alice", "Bob", "Charlie", "Diana"]`

[Lösung](solution.md#lsung-aufgabe-2)

### Aufgabe 3: Temperaturkonverter 🌶️🌶️
[15 min]
Du hast eine Liste von Temperaturen in Grad Celsius. Konvertiere jede Temperatur in Grad Fahrenheit und erstelle eine neue Liste mit den konvertierten Werten. Die Formel zur Umrechnung ist: Fahrenheit = (Celsius * 9/5) + 32.

Beispiel-Liste: `celsius = [0, 10, 20, 30, 40]`

[Lösung](solution.md#lsung-aufgabe-3)

