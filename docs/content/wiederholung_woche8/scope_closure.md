# Scope und Closure

## Theorie

Die Grundlagen sind bereits gut abgedeckt:

- [Scope, Closure & Variablen](../wiederholung/function_scopes_and_closure.md)

Wichtig für die Wiederholung:

- Namen werden nach LEGB gesucht: Local, Enclosing, Global, Built-in.
- `global` wird gebraucht, wenn eine globale Variable innerhalb einer Funktion neu zugewiesen werden soll.
- `nonlocal` wird gebraucht, wenn eine Variable aus einer äußeren, aber nicht globalen Funktion verändert werden soll.
- Ein Closure entsteht, wenn eine innere Funktion Variablen aus dem enclosing scope weiter benutzt.

## Aufgaben

### Aufgabe 1: Output vorhersagen

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        print(x)

    inner()

outer()
print(x)
```

??? success "Lösung"
    Ausgabe: `outer`, danach `global`. `inner()` findet `x` im enclosing scope von `outer`.

### Aufgabe 2: Zähler reparieren

Ergänze genau ein Schlüsselwort.

```python
def make_counter():
    count = 0

    def counter():
        # Ergänzen
        count += 1
        return count

    return counter
```

??? success "Lösung"
    In `counter()` muss `nonlocal count` stehen.

### Aufgabe 3: Erklären

Warum erzeugt dieser Code einen Fehler?

```python
value = 10

def change():
    value += 1
    return value
```

??? success "Lösung"
    Durch `value += 1` behandelt Python `value` als lokale Variable. Vor der Zuweisung wurde diese lokale Variable aber noch nicht initialisiert.

### Aufgabe 4: Closure bauen

Schreibe `make_multiplier(factor)`. Die Funktion soll eine innere Funktion zurückgeben, die eine Zahl mit `factor` multipliziert.

```python
times_three = make_multiplier(3)
print(times_three(4))  # 12
```

??? success "Lösung"
    ```python
    def make_multiplier(factor):
        def multiply(number):
            return number * factor
        return multiply
    ```

### Aufgabe 5: `global` oder `nonlocal`

Entscheide für jede Lücke, ob `global`, `nonlocal` oder nichts gebraucht wird.

```python
total = 0

def outer():
    count = 0

    def inner():
        # Lücke 1
        count += 1
        return count

    return inner

def add_to_total(value):
    # Lücke 2
    total += value
```

??? success "Lösung"
    Lücke 1: `nonlocal count`. Lücke 2: `global total`.

### Aufgabe 6: Ausgabe und Scope begründen

```python
x = 1

def outer():
    x = 2

    def inner():
        x = 3
        return x

    return inner(), x

print(outer())
print(x)
```

??? success "Lösung"
    Ausgabe: `(3, 2)` und danach `1`. Jede Zuweisung erzeugt in ihrer Funktion einen lokalen Namen.
