# `map()`, `filter()` und `lambda`

## Theorie

`lambda` erzeugt eine kleine anonyme Funktion mit genau einem Ausdruck.

```python
double = lambda x: x * 2
print(double(4))
```

`map(function, iterable)` wendet eine Funktion auf jedes Element an.

```python
result = map(lambda x: x * 2, [1, 2, 3])
print(list(result))
```

`filter(function, iterable)` behält nur Elemente, für die die Funktion truthy zurückgibt.

```python
result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(result))
```

Wichtig:

- `map()` und `filter()` liefern Iteratoren.
- Iteratoren sind nach dem Durchlaufen verbraucht.
- `lambda` enthält einen Ausdruck, keinen Anweisungsblock.

## Aufgaben

### Aufgabe 1: Ergebnis bestimmen

```python
values = map(lambda x: x + 1, [1, 2, 3])
print(list(values))
print(list(values))
```

??? success "Lösung"
    Erst `[2, 3, 4]`, danach `[]`, weil der Iterator verbraucht ist.

### Aufgabe 2: Gerade Zahlen quadrieren

Erzeuge aus dieser Liste das Ergebnis `[4, 16, 36]`.

```python
numbers = [1, 2, 3, 4, 5, 6]
```

??? success "Lösung"
    `list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))`

### Aufgabe 3: Ohne `lambda`

Schreibe Aufgabe 2 mit normalen Funktionen statt mit `lambda`.

??? success "Lösung"
    ```python
    def is_even(number):
        return number % 2 == 0

    def square(number):
        return number ** 2

    result = list(map(square, filter(is_even, numbers)))
    ```

### Aufgabe 4: Wahrheitswerte bei `filter`

Was wird ausgegeben?

```python
items = ["", "Python", [], [1], 0, 3]
print(list(filter(lambda x: x, items)))
```

??? success "Lösung"
    `["Python", [1], 3]`, weil leere Strings, leere Listen und `0` falsy sind.

### Aufgabe 5: Zwei Listen verarbeiten

Nutze `map()` und `lambda`, um die Werte paarweise zu addieren.

```python
a = [1, 2, 3]
b = [10, 20, 30]
```

Erwartet:

```python
[11, 22, 33]
```

??? success "Lösung"
    `list(map(lambda x, y: x + y, a, b))`

### Aufgabe 6: Reihenfolge erklären

Was wird ausgegeben?

```python
numbers = [1, 2, 3, 4]
result = filter(lambda x: x > 4, map(lambda x: x * 2, numbers))
print(list(result))
```

??? success "Lösung"
    `[6, 8]`. Erst werden die Zahlen verdoppelt: `2, 4, 6, 8`. Danach bleiben Werte größer als `4`.
