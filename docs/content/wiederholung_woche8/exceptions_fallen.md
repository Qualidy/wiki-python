# Exception-Fallen für PCAP

Diese Einheit wiederholt nicht nur eigene Exceptions, sondern vor allem Prüfungsfallen: Reihenfolge, `else`, `finally`, nacktes `raise` und mehrere Exception-Typen.

## Reihenfolge von `except`

Spezifische Exceptions müssen vor allgemeinen stehen.

```python
try:
    int("x")
except Exception:
    print("general")
except ValueError:
    print("value")
```

`ValueError` wird nie erreicht, weil `Exception` vorher alles abfängt.

## Mehrere Exception-Typen

In Python 3 müssen mehrere Typen als Tupel geschrieben werden.

```python
try:
    raise ValueError
except (TypeError, ValueError):
    print("handled")
```

Falsch:

```python
except TypeError, ValueError:
    ...
```

Das ist ein `SyntaxError`.

## `else`

Der `else`-Block läuft nur, wenn im `try`-Block keine Exception geworfen wurde.

```python
try:
    print("try")
except ValueError:
    print("except")
else:
    print("else")
```

Ausgabe:

```text
try
else
```

## `finally`

`finally` läuft fast immer, egal ob eine Exception passiert oder nicht.

```python
try:
    raise OSError
finally:
    print("cleanup")
```

Erst wird `cleanup` ausgegeben, danach bleibt `OSError` unbehandelt.

## `raise` ohne Argument

`raise` ohne Argument funktioniert nur innerhalb eines `except`-Blocks. Es wirft die aktuelle Exception erneut.

```python
try:
    open("missing.txt")
except OSError:
    raise
```

## Eigene Exception mit `Exception.__init__`

Diese Varianten rufen den Konstruktor der Basisklasse korrekt auf:

```python
class SpamException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
```

```python
class SpamException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message
```

```python
class SpamException(Exception):
    def __init__(self, message):
        super(SpamException, self).__init__(message)
        self.message = message
```

## Aufgaben

### Aufgabe 1: `else`

Was wird ausgegeben?

```python
try:
    print("A")
except Exception:
    print("B")
else:
    print("C")
finally:
    print("D")
```

??? success "Lösung"
    ```text
    A
    C
    D
    ```

### Aufgabe 2: `finally` mit Exception

Was passiert?

```python
try:
    raise OSError
finally:
    print("done")
```

??? success "Lösung"
    `done` wird ausgegeben. Danach bleibt `OSError` unbehandelt.

### Aufgabe 3: Mehrere Exception-Typen

Korrigiere den Code.

```python
try:
    raise ValueError
except TypeError, ValueError:
    print("handled")
```

??? success "Lösung"
    ```python
    try:
        raise ValueError
    except (TypeError, ValueError):
        print("handled")
    ```

### Aufgabe 4: `raise` ohne Argument

Warum ist dieser Code falsch?

```python
raise
```

??? success "Lösung"
    Außerhalb eines aktiven `except`-Blocks gibt es keine aktuelle Exception, die erneut geworfen werden könnte.

### Aufgabe 5: Welche Ausgabe?

```python
try:
    1 / 0
except ArithmeticError:
    print("A")
except ZeroDivisionError:
    print("Z")
```

??? success "Lösung"
    `A`, weil `ZeroDivisionError` von `ArithmeticError` erbt und der allgemeinere Block zuerst kommt.

### Aufgabe 6: Custom Exception

Welche Varianten rufen `Exception.__init__` korrekt auf?

```python
super().__init__(message)
Exception.__init__(self, message)
super(MyError, self).__init__(message)
super.__init__(message)
```

??? success "Lösung"
    Die ersten drei Varianten sind korrekt. `super.__init__(message)` ist falsch.
