# PCAP-Kompendium: Miscellaneous

Dieser Block enthält die typischen PCAP-Themen, die nicht sauber in die anderen Blöcke passen: Comprehensions, Lambdas, Closures, Generatoren und Datei-I/O.

## List Comprehensions

Form:

```python
[expression for item in iterable if condition]
```

Beispiele:

```python
[x * 2 for x in range(3)]          # [0, 2, 4]
[x for x in range(10) if x % 2]    # [1, 3, 5, 7, 9]
[[c for c in range(r)] for r in range(3)]
```

Fallen:

- Reihenfolge lesen: erst `for`, dann optional `if`, dann Ausdruck vorne.
- `range(5, 1)` ist leer, weil der Standard-Step `+1` ist.

## `lambda`

Form:

```python
lambda parameters: expression
```

Beispiele:

```python
f = lambda x, y: x + y
print(f(2, 3))  # 5
```

Falsch in Python 3:

```python
lambda (x, y): x + y
```

## `map()`

Signatur:

```python
map(function, iterable, *iterables)
```

Ergebnis: Iterator.

```python
list(map(lambda x: x * 2, range(3)))  # [0, 2, 4]
```

## `filter()`

Signatur:

```python
filter(function, iterable)
```

Ergebnis: Iterator mit Elementen, für die die Funktion truthy ist.

```python
list(filter(lambda x: x % 2, range(10)))  # [1, 3, 5, 7, 9]
```

## Closures

Eine Closure entsteht, wenn eine innere Funktion Namen aus einem umschließenden Scope bindet.

```python
def make_adder(amount):
    def add(value):
        return value + amount
    return add


add_10 = make_adder(10)
print(add_10(5))  # 15
```

`nonlocal` erlaubt Änderungen an Namen im umschließenden Funktionsscope:

```python
def counter():
    value = 0

    def inc():
        nonlocal value
        value += 1
        return value

    return inc
```

## Generatoren

Eine Funktion mit `yield` ist eine Generatorfunktion.

```python
def squares():
    for x in range(3):
        yield x * x
```

```python
for value in squares():
    print(value)
```

Ausgabe:

```text
0
1
4
```

Wichtige Begriffe:

| Begriff | Bedeutung |
| --- | --- |
| Iterator | Objekt, das Werte nacheinander liefert |
| Iterable | Objekt, über das iteriert werden kann |
| `__iter__()` | gibt Iterator zurück |
| `__next__()` | liefert nächsten Wert oder wirft `StopIteration` |
| `yield` | pausiert Generator und liefert Wert |
| `StopIteration` | Ende eines Iterators |

Eigener Iterator:

```python
class Spam:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.text):
            raise StopIteration
        value = self.text[self.index]
        self.index += 1
        return value
```

## Datei-I/O

### `open()`

Signatur stark vereinfacht:

```python
open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None)
```

Wichtige Modi:

| Modus | Bedeutung |
| --- | --- |
| `"r"` | lesen, Datei muss existieren |
| `"w"` | schreiben, überschreibt |
| `"a"` | anhängen |
| `"x"` | exklusiv erstellen, Fehler wenn Datei existiert |
| `"b"` | binary mode |
| `"t"` | text mode |
| `"+"` | lesen und schreiben |

Kombinationen:

```python
"rt"
"wb"
"r+"
"a+"
"r+b"
```

### Methoden

| Methode | Bedeutung |
| --- | --- |
| `file.read(size=-1)` | liest Inhalt oder `size` Zeichen/Bytes |
| `file.readline(size=-1)` | liest eine Zeile oder Teil davon |
| `file.readlines(hint=-1)` | liest Zeilen als Liste |
| `file.write(text_or_bytes)` | schreibt und gibt Anzahl zurück |
| `file.writelines(lines)` | schreibt Iterable von Strings/Bytes |
| `file.close()` | schließt Datei |
| `file.seek(offset, whence=0)` | Cursor setzen |
| `file.tell()` | Cursorposition |

Nach `close()` sind Lese-/Schreiboperationen ungültig. Ein weiterer `close()`-Aufruf ist erlaubt.

### `with open(...)`

```python
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Nach dem Block ist die Datei geschlossen.

### `errno`

```python
import errno
import sys

try:
    open("missing.txt", "r")
except OSError:
    if sys.exc_info()[1].errno == errno.ENOENT:
        print("missing")
```

### `bytearray`

```python
buffer = bytearray(10)
```

`bytearray` ist mutable und kann beim Lesen/Schreiben binärer Daten als Buffer genutzt werden.

## Mini-Checks

```python
print(list(map(lambda x: x + 10, [1, 2, 3])))
```

??? success "Lösung"
    `[11, 12, 13]`

```python
with open("spam.txt", "r+") as file:
    line = file.read()
file.write(line)
```

??? success "Lösung"
    `ValueError`, weil `file` nach dem `with`-Block geschlossen ist.
