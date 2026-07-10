# PCAP-Kompendium: Exceptions

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Exception | Laufzeitfehlerobjekt |
| Exception hierarchy | Vererbungshierarchie der Exception-Klassen |
| Handler | `except`-Block, der eine Exception behandelt |
| Re-raise | aktuelle Exception mit `raise` erneut werfen |
| Assertion | Prüfung mit `assert`, wirft bei `False` `AssertionError` |
| Custom exception | selbst definierte Exception-Klasse |

## Grundform

```python
try:
    risky()
except ValueError as error:
    print(error)
else:
    print("no exception")
finally:
    print("cleanup")
```

Reihenfolge:

1. `try`
2. passender `except`, falls Exception
3. `else`, falls keine Exception
4. `finally`, fast immer

## `except`

```python
except ValueError:
    ...
```

Mehrere Typen:

```python
except (TypeError, ValueError):
    ...
```

Falsch in Python 3:

```python
except TypeError, ValueError:
    ...
```

Das ist ein `SyntaxError`.

## Reihenfolge der Handler

Spezifisch vor allgemein:

```python
try:
    1 / 0
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arithmetic")
```

`ZeroDivisionError` erbt von `ArithmeticError`. Wird `ArithmeticError` zuerst abgefangen, erreicht Python den spezifischeren Block nicht mehr.

## `raise`

Neue Exception werfen:

```python
raise ValueError("bad value")
```

Aktuelle Exception erneut werfen:

```python
try:
    int("x")
except ValueError:
    raise
```

`raise` ohne aktive Exception ist ein Fehler.

## `assert`

```python
assert score >= 0
assert score >= 0, "score must not be negative"
```

Wenn die Bedingung `False` ist, entsteht ein `AssertionError`.

## Wichtige Exception-Klassen

| Exception | Typischer Auslöser |
| --- | --- |
| `BaseException` | Wurzel fast aller Exceptions |
| `Exception` | Basisklasse für normale Programmfehler |
| `ArithmeticError` | Basisklasse mathematischer Fehler |
| `ZeroDivisionError` | Division durch `0` |
| `ValueError` | richtiger Typ, aber ungültiger Wert |
| `TypeError` | falscher Typ oder falsche Signatur |
| `NameError` | Name nicht definiert |
| `UnboundLocalError` | lokaler Name vor Zuweisung gelesen |
| `AttributeError` | Attribut existiert nicht |
| `IndexError` | ungültiger Sequenzindex |
| `KeyError` | Schlüssel fehlt |
| `OSError` | Betriebssystem-/Dateifehler |
| `FileNotFoundError` | Datei nicht gefunden |
| `AssertionError` | `assert` fehlgeschlagen |
| `StopIteration` | Iterator ist erschöpft |

## Eigene Exceptions

```python
class InvalidScoreError(Exception):
    pass
```

Mit eigener Initialisierung:

```python
class InvalidScoreError(Exception):
    def __init__(self, score):
        super().__init__(f"invalid score: {score}")
        self.score = score
```

Gültige Varianten zum Aufruf von `Exception.__init__`:

```python
super().__init__(message)
Exception.__init__(self, message)
super(MyError, self).__init__(message)
```

Falsch:

```python
super.__init__(message)
```

## `args`

```python
error = ValueError("spam", "ham")
print(error.args)  # ("spam", "ham")
```

Exceptions speichern übergebene Argumente in `.args`.

## Mini-Checks

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
    `A`, `C`, `D`

```python
try:
    raise OSError
finally:
    print("cleanup")
```

??? success "Lösung"
    Erst `cleanup`, danach bleibt `OSError` unbehandelt.
