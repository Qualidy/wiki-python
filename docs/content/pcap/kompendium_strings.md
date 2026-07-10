# PCAP-Kompendium: Strings

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| String | immutable Sequenz von Unicode-Zeichen |
| Code point | numerischer Wert eines Zeichens |
| ASCII | alter 7-Bit-Zeichensatz |
| Unicode | Standard für Zeichen und Codepoints |
| UTF-8 | Kodierung für Unicode-Codepoints |
| Escape sequence | Schreibweise mit Backslash, z. B. `\n` |
| Immutability | String kann nicht in-place geändert werden |

## Literale und Escape-Sequenzen

```python
"spam"
'spam'
"""multi
line"""
```

Wichtige Escape-Sequenzen:

| Sequenz | Bedeutung |
| --- | --- |
| `\n` | newline |
| `\t` | tab |
| `\\` | Backslash |
| `\"` | doppeltes Quote |
| `\'` | einfaches Quote |

Falle:

```python
print("\")
```

Ein einzelner Backslash vor dem schließenden Quote ist ein Syntaxfehler.

## `ord()` und `chr()`

```python
ord(c)
chr(i)
```

| Funktion | Parameter | Ergebnis |
| --- | --- | --- |
| `ord(c)` | String der Länge `1` | Unicode-Codepoint als `int` |
| `chr(i)` | Integer-Codepoint | Zeichen als String |

```python
ord("A")  # 65
chr(65)   # "A"
```

Fallen:

```python
ord("AB")  # TypeError
chr("A")   # TypeError
```

## Indexing und Slicing

```python
s = "Spam,Ham,Eggs"

s[0]      # "S"
s[-1]     # "s"
s[5:8]    # "Ham"
s[-8:-5]  # "Ham"
s[::-1]   # rückwärts
```

Slice-Form:

```python
sequence[start:stop:step]
```

`stop` ist exklusiv.

## Operatoren

| Operator | Bedeutung |
| --- | --- |
| `+` | Konkatenation |
| `*` | Wiederholung |
| `in` | Teilstring enthalten |
| `not in` | Teilstring nicht enthalten |
| Vergleichsoperatoren | lexikografischer Vergleich |

```python
"ham" * 3        # "hamhamham"
"a" in "spam"    # True
```

REPL-Falle:

```python
>>> spam, ham = 1, "ham"
>>> spam *= 3
>>> ham *= 3
>>> spam, ham
(3, 'hamhamham')
```

## Immutability

```python
s = "spam"
s[0] = "S"  # TypeError
```

Korrekt:

```python
s = "S" + s[1:]
```

## Wichtige Methoden

| Methode | Parameter | Ergebnis / Besonderheit |
| --- | --- | --- |
| `s.find(sub[, start[, end]])` | Suchstring, optional Bereich | erster Index oder `-1` |
| `s.rfind(sub[, start[, end]])` | Suchstring, optional Bereich | letzter Index oder `-1` |
| `s.index(sub[, start[, end]])` | Suchstring, optional Bereich | erster Index oder `ValueError` |
| `s.split(sep=None, maxsplit=-1)` | Trenner, maximale Splits | Liste |
| `sep.join(iterable)` | Iterable aus Strings | String |
| `s.strip([chars])` | zu entfernende Zeichen | neuer String |
| `s.upper()` / `s.lower()` | keine | neuer String |
| `s.startswith(prefix)` | String oder Tupel | `bool` |
| `s.endswith(suffix)` | String oder Tupel | `bool` |
| `s.isalpha()` | keine | nur Buchstaben und nicht leer |
| `s.isdigit()` | keine | nur Ziffern und nicht leer |
| `s.isalnum()` | keine | Buchstaben/Ziffern und nicht leer |
| `s.isspace()` | keine | nur Whitespace und nicht leer |

## Sortieren

```python
sorted(iterable, key=None, reverse=False)
list.sort(key=None, reverse=False)
```

Unterschied:

- `sorted(...)` gibt eine neue Liste zurück.
- `list.sort(...)` sortiert in-place und gibt `None` zurück.

## Mini-Checks

```python
print("\\\\")
```

??? success "Lösung"
    Zwei Backslashes.

```python
s = "Hello"
s[0] = "h"
```

??? success "Lösung"
    `TypeError`, Strings sind immutable.
