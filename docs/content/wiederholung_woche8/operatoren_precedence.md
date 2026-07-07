# Operatoren und Precedence

## Theorie

Operator Precedence bedeutet: Python entscheidet nach festen Regeln, welcher Teil eines Ausdrucks zuerst ausgewertet wird.

Für boolsche Logik ist diese Reihenfolge besonders wichtig:

| Rang | Operator | Bedeutung |
| ---: | --- | --- |
| 1 | Vergleiche wie `<`, `>`, `==`, `in`, `is` | erzeugen meist `True` oder `False` |
| 2 | `not` | logische Negation |
| 3 | `and` | beide Seiten müssen truthy sein |
| 4 | `or` | mindestens eine Seite muss truthy sein |

Beispiel:

```python
x = True
y = False
z = False

result = not x or y and not z
```

Python liest das so:

```python
result = (not x) or (y and (not z))
```

und nicht so:

```python
result = ((not x or y) and not z)
```

Wichtig:

- Klammern schlagen Precedence. Wenn es unklar wirkt, setze Klammern.
- `and` und `or` geben in Python nicht zwingend `True` oder `False` zurück, sondern einen der beteiligten Werte.
- Python wertet kurzschließend aus: Bei `and` wird rechts nur geprüft, wenn links truthy ist. Bei `or` wird rechts nur geprüft, wenn links falsy ist.

## Wahrheitstabellen

| `a` | `b` | `a and b` | `a or b` |
| --- | --- | --- | --- |
| `False` | `False` | `False` | `False` |
| `False` | `True` | `False` | `True` |
| `True` | `False` | `False` | `True` |
| `True` | `True` | `True` | `True` |

## Beispiel: Precedence macht einen Unterschied

```python
a = True
b = True
c = False

print(a or b and c)
print((a or b) and c)
```

Ausgabe:

```python
True
False
```

Ohne Klammern wird `and` zuerst ausgewertet:

```python
a or b and c
a or (b and c)
True or (True and False)
True or False
True
```

Mit Klammern wird zuerst `a or b` ausgewertet:

```python
(a or b) and c
(True or True) and False
True and False
False
```

## Aufgaben

### Aufgabe 1: Precedence ohne Klammern

Was wird ausgegeben?

```python
x = True
y = False
z = False

print(not x or y or not y and x)
```

??? success "Lösung"
    Ausgabe: `True`

    Auswertung:

    ```python
    (not x) or y or ((not y) and x)
    False or False or (True and True)
    False or False or True
    True
    ```

### Aufgabe 2: `and` vor `or`

Was wird ausgegeben?

```python
print(False or True and False)
```

??? success "Lösung"
    Ausgabe: `False`

    `and` wird vor `or` ausgewertet:

    ```python
    False or (True and False)
    False or False
    False
    ```

### Aufgabe 3: Vergleiche zuerst

Was wird ausgegeben?

```python
x = 3
y = 5

print(x < 4 and y > 10 or x == 3)
```

??? success "Lösung"
    Ausgabe: `True`

    ```python
    (x < 4) and (y > 10) or (x == 3)
    True and False or True
    False or True
    True
    ```

### Aufgabe 4: `not` bindet stark

Was wird ausgegeben?

```python
value = 0

print(not value == 0)
print((not value) == 0)
```

??? success "Lösung"
    Ausgabe:

    ```python
    False
    False
    ```

    Beim ersten Ausdruck wird zuerst verglichen:

    ```python
    not (value == 0)
    not True
    False
    ```

    Beim zweiten Ausdruck wird zuerst `not value` ausgewertet:

    ```python
    (not 0) == 0
    True == 0
    False
    ```

### Aufgabe 5: Short-Circuit

Was wird ausgegeben?

```python
def check(name):
    print(name)
    return name == "B"

print(check("A") and check("B"))
print(check("B") or check("C"))
```

??? success "Lösung"
    Ausgabe:

    ```python
    A
    False
    B
    True
    ```

    Bei `and` wird `check("B")` nicht mehr aufgerufen, weil `check("A")` schon `False` liefert.

    Bei `or` wird `check("C")` nicht mehr aufgerufen, weil `check("B")` schon `True` liefert.

### Aufgabe 6: Rückgabewerte von `and` und `or`

Was wird ausgegeben?

```python
print("Python" and 42)
print("" or "fallback")
print([] or [1, 2])
print([0] and "done")
```

??? success "Lösung"
    Ausgabe:

    ```python
    42
    fallback
    [1, 2]
    done
    ```

    `and` gibt den ersten falsy Wert zurück, sonst den letzten Wert. `or` gibt den ersten truthy Wert zurück, sonst den letzten Wert.

### Aufgabe 7: Klammern verändern alles

Welche Zeilen geben `True` aus?

```python
a = True
b = False
c = False

print(a or b and c)
print((a or b) and c)
print(a or (b and c))
```

??? success "Lösung"
    Zeile 1 und 3 geben `True` aus. Zeile 2 gibt `False` aus.

    ```python
    a or b and c      # True or (False and False) -> True
    (a or b) and c    # (True or False) and False -> False
    a or (b and c)    # True or (False and False) -> True
    ```

### Aufgabe 8: Trick mit `not in`

Was wird ausgegeben?

```python
items = ["a", "b", "c"]

print("a" not in items or "d" in items)
print(not "a" in items or "d" in items)
```

??? success "Lösung"
    Ausgabe:

    ```python
    False
    False
    ```

    Beide Ausdrücke bedeuten hier dasselbe:

    ```python
    ("a" not in items) or ("d" in items)
    False or False
    False
    ```
