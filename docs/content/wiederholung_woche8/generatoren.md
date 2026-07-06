# Generatoren

## Theorie

Die Grundlagen sind bereits gut abgedeckt:

- [Generatoren im Skript](../funktionen_fortgeschritten/generatoren/generatoren.md)

Wichtig für die Wiederholung:

- Eine Generatorfunktion enthält `yield`.
- Generatoren merken sich ihren Zustand.
- `next(generator)` liefert den nächsten Wert.
- Ein verbrauchter Generator liefert keine neuen Werte.

## Aufgaben

### Aufgabe 1: Verbrauch vorhersagen

```python
def letters():
    yield "A"
    yield "B"
    yield "C"

gen = letters()
print(next(gen))
print(list(gen))
print(list(gen))
```

??? success "Lösung"
    Erst `"A"`, dann `["B", "C"]`, danach `[]`.

### Aufgabe 2: Generator schreiben

Schreibe `even_numbers(limit)`. Der Generator soll alle geraden Zahlen von `0` bis einschließlich `limit` liefern.

??? success "Lösung"
    ```python
    def even_numbers(limit):
        current = 0
        while current <= limit:
            yield current
            current += 2
    ```

### Aufgabe 3: `return` in Generatoren

Was passiert, wenn eine Generatorfunktion `return` erreicht?

??? success "Lösung"
    Der Generator endet. Intern entsteht `StopIteration`.

### Aufgabe 4: Generator Expression

Was wird ausgegeben?

```python
gen = (x * 2 for x in range(3))
print(next(gen))
print(list(gen))
```

??? success "Lösung"
    Erst `0`, danach `[2, 4]`.

### Aufgabe 5: Verbrauch in `sum`

Was wird ausgegeben?

```python
gen = (x for x in [1, 2, 3])
print(sum(gen))
print(list(gen))
```

??? success "Lösung"
    Erst `6`, danach `[]`, weil `sum()` den Generator verbraucht.

### Aufgabe 6: Filter-Generator schreiben

Schreibe einen Generator `only_long(words, min_length)`, der nur Wörter liefert, deren Länge mindestens `min_length` ist.

??? success "Lösung"
    ```python
    def only_long(words, min_length):
        for word in words:
            if len(word) >= min_length:
                yield word
    ```
