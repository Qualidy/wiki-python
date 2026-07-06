# Listen, Slices und Sortieren

## Theorie

Die Grundlagen sind bereits gut abgedeckt:

- [Listen & List-Methoden](../wiederholung/list_wiederholung.md)
- [Listen im Skript](../datenstrukturen/lists/lists.md)

Wichtig für die Wiederholung:

- Slices erzeugen neue Listen.
- `list.sort()` sortiert in-place und gibt `None` zurück.
- `sorted(...)` erzeugt eine neue sortierte Liste.
- Negative Indizes und Schrittweiten müssen sauber gelesen werden.

## Aufgaben

### Aufgabe 1: Slices auswerten

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

a = numbers[1:5:2]
b = numbers[::-1]
c = numbers[2:-1]
numbers.sort()
```

Bestimme `a`, `b`, `c` und `numbers`.

??? success "Lösung"
    `a == [1, 1]`, `b == [2, 9, 5, 1, 4, 1, 3]`, `c == [4, 1, 5, 9]`, `numbers == [1, 1, 2, 3, 4, 5, 9]`.

### Aufgabe 2: `sort()` reparieren

```python
values = [4, 2, 7, 1]
result = values.sort()
```

Warum ist `result` `None`? Schreibe den Code so um, dass `values` unverändert bleibt.

??? success "Lösung"
    `result = sorted(values)`

### Aufgabe 3: Sortierschlüssel

Sortiere nach Länge, dann alphabetisch.

```python
words = ["pear", "fig", "apple", "kiwi"]
```

??? success "Lösung"
    `sorted(words, key=lambda word: (len(word), word))`

### Aufgabe 4: Slice-Zuweisung

Was enthält `values` danach?

```python
values = [1, 2, 3, 4, 5]
values[1:4] = [20, 30]
```

??? success "Lösung"
    `[1, 20, 30, 5]`

### Aufgabe 5: Kopie oder Referenz

Was wird ausgegeben?

```python
a = [[1], [2]]
b = a[:]
b[0].append(99)
print(a)
```

??? success "Lösung"
    `[[1, 99], [2]]`. Der Slice kopiert nur die äußere Liste, nicht die inneren Listen.

### Aufgabe 6: Reverse sortieren

Sortiere die Zahlen absteigend, ohne `values` zu verändern.

```python
values = [5, 1, 9, 2]
```

??? success "Lösung"
    `result = sorted(values, reverse=True)`
