# Mutable, Immutable und Referenzen

## Theorie

Variablen in Python speichern nicht direkt den Wert. Eine Variable ist ein Name, der auf ein Objekt zeigt.

```python
x = [1, 2, 3]
```

`x` ist der Name. Die Liste `[1, 2, 3]` ist das Objekt.

## Mutable und immutable

Mutable Objekte können verändert werden, ohne dass ein neues Objekt entsteht.

Typische mutable Typen:

- `list`
- `dict`
- `set`
- `bytearray`

Immutable Objekte können nicht in-place verändert werden. Bei einer scheinbaren Änderung entsteht ein neues Objekt.

Typische immutable Typen:

- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `bytes`

## Zuweisung ist keine Kopie

Bei einer Zuweisung wird normalerweise nicht das Objekt kopiert. Es wird nur ein weiterer Name auf dasselbe Objekt gesetzt.

```python
a = [1, 2]
b = a

b.append(3)
print(a)
```

Ausgabe:

```python
[1, 2, 3]
```

`a` und `b` zeigen auf dieselbe Liste.

Bei immutable Objekten wirkt es oft wie eine Kopie:

```python
a = 10
b = a
b += 1

print(a)
print(b)
```

Ausgabe:

```python
10
11
```

`b += 1` verändert nicht die alte `10`, sondern bindet `b` an ein neues Integer-Objekt.

## Kopien von Collections

Eine flache Kopie einer Liste geht zum Beispiel so:

```python
b = a.copy()
b = a[:]
b = list(a)
```

Aber: Eine flache Kopie kopiert nur die äußere Collection. Verschachtelte mutable Objekte bleiben geteilt.

```python
a = [[1], [2]]
b = a.copy()

b[0].append(99)
print(a)
```

Ausgabe:

```python
[[1, 99], [2]]
```

Für verschachtelte Strukturen braucht man bei Bedarf `copy.deepcopy()`.

## Funktionen und Argumente

Beim Funktionsaufruf bekommt der Parameter eine Referenz auf dasselbe Objekt.

```python
def change(values):
    values.append(4)

numbers = [1, 2, 3]
change(numbers)
print(numbers)
```

Ausgabe:

```python
[1, 2, 3, 4]
```

Bei immutable Typen kann die Funktion das ursprüngliche Objekt nicht in-place verändern:

```python
def change(number):
    number += 1
    print("innen:", number)

value = 10
change(value)
print("außen:", value)
```

Ausgabe:

```python
innen: 11
außen: 10
```

`number += 1` erzeugt ein neues Integer-Objekt. Der lokale Name `number` zeigt danach auf `11`, aber der äußere Name `value` zeigt weiterhin auf `10`.

Das gleiche Prinzip gilt auch für Strings:

```python
def change(text):
    text += "!"
    print("innen:", text)

message = "Hallo"
change(message)
print("außen:", message)
```

Ausgabe:

```python
innen: Hallo!
außen: Hallo
```

Wird der Parameter aber neu zugewiesen, zeigt nur der lokale Name auf ein anderes Objekt:

```python
def change(values):
    values = [99]

numbers = [1, 2, 3]
change(numbers)
print(numbers)
```

Ausgabe:

```python
[1, 2, 3]
```

Merksatz:

```text
Mutation am Objekt sieht man außen.
Neue Zuweisung des lokalen Namens sieht man außen nicht.
```

## Aufgaben

### Aufgabe 1: Referenz oder Kopie?

Was wird ausgegeben?

```python
a = [1, 2]
b = a

b.append(3)
print(a)
print(b)
```

??? success "Lösung"
    Ausgabe:

    ```python
    [1, 2, 3]
    [1, 2, 3]
    ```

    `a` und `b` zeigen auf dieselbe Liste.

### Aufgabe 2: Immutable Integer

Was wird ausgegeben?

```python
a = 5
b = a

b += 2
print(a)
print(b)
```

??? success "Lösung"
    Ausgabe:

    ```python
    5
    7
    ```

    Integer sind immutable. `b += 2` erzeugt ein neues Objekt und bindet `b` daran.

### Aufgabe 3: Funktion mit Liste

Was wird ausgegeben?

```python
def add_item(items):
    items.append("x")

data = ["a", "b"]
add_item(data)
print(data)
```

??? success "Lösung"
    Ausgabe:

    ```python
    ['a', 'b', 'x']
    ```

    Die Funktion verändert die übergebene Liste in-place.

### Aufgabe 4: Funktion mit Neuzuweisung

Was wird ausgegeben?

```python
def replace_items(items):
    items = ["new"]

data = ["old"]
replace_items(data)
print(data)
```

??? success "Lösung"
    Ausgabe:

    ```python
    ['old']
    ```

    `items = ["new"]` bindet nur den lokalen Namen `items` neu. Die äußere Liste bleibt unverändert.

### Aufgabe 5: Funktion mit immutable Typ

Was wird ausgegeben?

```python
def increase(number):
    number += 10
    print("innen:", number)

value = 5
increase(value)
print("außen:", value)
```

??? success "Lösung"
    Ausgabe:

    ```python
    innen: 15
    außen: 5
    ```

    `int` ist immutable. `number += 10` verändert nicht das ursprüngliche Integer-Objekt, sondern bindet den lokalen Namen `number` an ein neues Objekt.

### Aufgabe 6: Flache Kopie

Was wird ausgegeben?

```python
a = [[1], [2]]
b = a[:]

b.append([3])
b[0].append(99)

print(a)
print(b)
```

??? success "Lösung"
    Ausgabe:

    ```python
    [[1, 99], [2]]
    [[1, 99], [2], [3]]
    ```

    `b.append([3])` verändert nur die äußere Liste `b`. `b[0].append(99)` verändert aber die innere Liste, die `a` und `b` gemeinsam nutzen.

### Aufgabe 7: String ist immutable

Was passiert?

```python
text = "Python"
text[0] = "J"
print(text)
```

??? success "Lösung"
    Es entsteht ein `TypeError`, weil Strings immutable sind. Richtig wäre zum Beispiel:

    ```python
    text = "J" + text[1:]
    ```

### Aufgabe 8: Mutable Default Argument

Was wird ausgegeben?

```python
def collect(value, bucket=[]):
    bucket.append(value)
    return bucket

print(collect(1))
print(collect(2))
print(collect(3, []))
print(collect(4))
```

??? success "Lösung"
    Ausgabe:

    ```python
    [1]
    [1, 2]
    [3]
    [1, 2, 4]
    ```

    Das Default-Argument `bucket=[]` wird nur einmal beim Definieren der Funktion erzeugt und danach wiederverwendet.

### Aufgabe 9: Bessere Variante für Defaults

Repariere die Funktion aus Aufgabe 8.

```python
def collect(value, bucket=[]):
    bucket.append(value)
    return bucket
```

??? success "Lösung"
    ```python
    def collect(value, bucket=None):
        if bucket is None:
            bucket = []
        bucket.append(value)
        return bucket
    ```

### Aufgabe 10: Tuple mit mutable Inhalt

Was wird ausgegeben?

```python
t = ([1, 2], "a")
t[0].append(3)

print(t)
```

??? success "Lösung"
    Ausgabe:

    ```python
    ([1, 2, 3], 'a')
    ```

    Das Tuple selbst ist immutable: Man kann `t[0]` nicht neu zuweisen. Die Liste im Tuple ist aber mutable und kann verändert werden.

### Aufgabe 11: Quizfragen

Beantworte ohne Ausführen.

| Frage | Antwortmöglichkeiten |
| --- | --- |
| Welche Typen sind mutable? | A `list`, B `str`, C `dict`, D `tuple` |
| Welche Zuweisung kopiert eine Liste flach? | A `b = a`, B `b = a[:]`, C `b = a.copy()`, D `b = list(a)` |
| Was sieht der Aufrufer nach `parameter.append(...)`? | A keine Änderung, B Änderung am Original, C immer `TypeError` |
| Was sieht der Aufrufer nach `parameter = [...]`? | A Original wird ersetzt, B nur lokaler Name wird neu gebunden, C Programm endet immer |

??? success "Lösung"
    - Mutable Typen: A und C.
    - Flache Kopien: B, C und D.
    - `parameter.append(...)`: Änderung am Original, wenn dasselbe mutable Objekt übergeben wurde.
    - `parameter = [...]`: Nur der lokale Name wird neu gebunden.
