# Objektorientierte vs. Funktionale Programmierung
[120min]

## Funktionale Programmierung

Die funktionale Programmierung ist ein Paradigma, das auf der Verwendung von Funktionen als grundlegenden Bausteinen basiert. Im Vergleich zur objektorientierten Programmierung liegt der Fokus stärker auf deklarativen Beschreibungen dessen, "was" erreicht werden soll, anstatt imperativer Anweisungen, "wie" es erreicht werden soll.

**Warum funktionale Programmierung?** 

Funktionale Programmierung bietet oft klare und elegante Lösungen für komplexe Probleme. Programme sind in der Regel kürzer, lesbarer und leichter zu warten. Funktionale Programme neigen dazu, weniger Fehler zu enthalten und sind einfacher parallelisierbar, was die Leistung verbessern kann.

## Unterschiede zwischen OOP und Funktionaler Programmierung

Wir kennen bereits das Paradigma der Objektorientierte Programmierung (OOP). Python ist eine sog. Multi-paradigmensprache d.h. man kann in Python sowohl objektorientiert programmieren als auch funktional. Hier die Unterschiede der beiden Paradigmen im Vergleich:

| Eigenschaft                     | Objektorientierte Programmierung (OOP)  | Funktionale Programmierung |
|---------------------------------|------------------------------------------|-----------------------------|
| Zustand und Veränderlichkeit     | Objekte können ihren Zustand ändern.     | Betont Unveränderlichkeit.  |
| Nebenwirkungen                  | Methoden können Nebenwirkungen haben.    | Strebt nach vermeidbaren Nebenwirkungen. |
| Daten und Verhalten              | Kapselt Daten und Verhalten in Objekten. | Trennt Daten und Verhalten. |
| Typische Struktur                | Klassen, Objekte, Vererbung.              | Funktionen, Unveränderlichkeit.   |
| Beispiele                        | Java, Python                 | Python, Haskell, Lisp, Scala.       |

## Funktionale Programmierung in Schritten erklärt

### 1. Funktionen als First-Class Citizens

In der funktionalen Programmierung sind Funktionen "first-class citizens", was bedeutet, dass sie wie Daten behandelt werden können.

Sehen wir uns ein Beispiel an:

```python
# Beispiel: Funktionen als Variablen zuweisen
add = lambda x, y: x + y
multiply = lambda x, y: x * y

# Funktionen als Argumente übergeben
def apply_operation(operation, x, y):
    return operation(x, y)

result_add = apply_operation(add, 3, 5)  # Ergebnis: 8
result_multiply = apply_operation(multiply, 3, 5)  # Ergebnis: 15
```

Dieses Codebeispiel zeigt die Verwendung von Lambda-Funktionen (anonymen Funktionen) sowie die Möglichkeit, Funktionen als Variablen zu behandeln und als Argumente an andere Funktionen zu übergeben.

Hier sind die Schritte im Detail:

1. **Definition von Lambda-Funktionen:**
   ```python
   add = lambda x, y: x + y
   multiply = lambda x, y: x * y
   ```
   Hier werden zwei Lambda-Funktionen definiert. Die `add`-Funktion nimmt zwei Argumente `x` und `y` und gibt ihre Summe zurück. Die `multiply`-Funktion nimmt ebenfalls zwei Argumente und gibt deren Produkt zurück.

2. **Funktion zum Anwenden von Operationen:**
   ```python
   def apply_operation(operation, x, y):
       return operation(x, y)
   ```
   Hier wird eine Funktion namens `apply_operation` definiert, die drei Argumente akzeptiert: `operation` (eine Funktion), `x` und `y`. Die Funktion ruft die übergebene Operation mit den Argumenten `x` und `y` auf und gibt das Ergebnis zurück.

3. **Anwenden der Operationen:**
   ```python
   result_add = apply_operation(add, 3, 5)  # Ergebnis: 8
   result_multiply = apply_operation(multiply, 3, 5)  # Ergebnis: 15
   ```
   Hier werden die zuvor definierten Lambda-Funktionen `add` und `multiply` an die Funktion `apply_operation` übergeben. Das Ergebnis wird in den Variablen `result_add` und `result_multiply` gespeichert. In diesem Fall wird `add` mit den Argumenten 3 und 5 aufgerufen, was zu 8 führt, und `multiply` wird mit den gleichen Argumenten aufgerufen, was zu 15 führt.

### 2. Anonyme Funktionen (Lambda)

**Lambda-Funktionen** sind anonyme Funktionen, die oft für kurze, einfache Operationen verwendet werden.

Nehmen wir an wir schreiben eine Funktion so:
```python
def double:
    x: x * 2
```
Und verwenden sie dann anschließend so:
```python
result = double(4)  # Ergebnis: 8
```
Alternativ könnte man als anonyme Funktionen, mittels `lambda` Schlüsselwort, Folgendes schreiben:

```python
# Beispiel: Lambda-Funktion zur Verdopplung
double = lambda x: x * 2
result = double(4)  # Ergebnis: 8
```

Wenn wir nun die Zwischenvariable `double` noch weglassen wollen und entsprechend Klammern setzen, sieht das ganze so aus:

```python
result = (lambda x: x * 2)(4)  # Ergebnis: 8
```

### 3. Funktionen höherer Ordnung

Funktionen, die andere Funktionen als Argumente akzeptieren oder Funktionen zurückgeben, werden als Funktionen höherer Ordnung bezeichnet.

```python
# Beispiel: Funktion höherer Ordnung
def apply_twice(operation, x):
    return operation(operation(x))

square = lambda x: x * x
result = apply_twice(square, 3)  # Ergebnis: 81
```

### 4. Rekursion

Rekursion ist ein häufig verwendetes Konzept in der funktionalen Programmierung.

```python
# Beispiel: Rekursive Berechnung der Fakultät
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
result = factorial(5)  # Ergebnis: 120
```

### 5. Lambda-Schlüsselwort

Das `lambda`-Schlüsselwort wird verwendet, um anonyme Funktionen zu erstellen. Es ermöglicht die Definition von Funktionen ohne eine explizite `def`-Anweisung.

```python
# Beispiel: Vergleich von normaler Funktion und Lambda
def square_function(x):
    return x ** 2

square_lambda = lambda x: x ** 2
```

# Aufgaben:
[100min]

## 1. **Fakultät berechnen 🌶️️🌶️️** 

Implementiere eine Funktion zur Berechnung der Fakultät einer Zahl unter Verwendung der funktionalen Programmierung und Rekursion. Teilschritte:
   - Schreibe eine Lambda-Funktion für die Fakultät.
   - Implementiere eine Funktion höherer Ordnung zur Anwendung der Lambda-Funktion.
   - Teste die Funktionalität mit verschiedenen Eingaben.

## 2. **Wortliste sortieren 🌶️️🌶️️🌶️️**
 Erstelle eine Liste von Wörtern und sortiere sie nach der Länge unter Verwendung der Funktionen `sorted` und `len` im funktionalen Stil. Teilschritte:
   - Definiere eine Liste von Wörtern.
   - Verwende die `sorted`-Funktion mit einer Lambda-Funktion als Schlüssel für die Sortierung. [Dokumentation](https://docs.python.org/3/howto/sorting.html#sorting-how-to)
   - Gib die sortierte Liste aus.
