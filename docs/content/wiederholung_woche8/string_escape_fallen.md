# Strings, Escape-Sequenzen und Repr-Fallen

PCAP-Fragen zu Strings sind oft keine schweren Algorithmen, sondern genaue Syntax- und Ausgabe-Fragen.

## Backslash

Der Backslash `\` leitet Escape-Sequenzen ein.

```python
print("\\")
```

gibt einen einzelnen Backslash aus.

```python
print("\\\\")
```

gibt zwei Backslashes aus.

Ein einzelner Backslash am Ende eines Strings ist ein Syntaxfehler:

```python
print("\")
```

## Quotes

Diese Varianten sind gültig:

```python
print('John said: "Hi"')
print("John said: \"Hi\"")
```

In der REPL werden Strings mit Quotes dargestellt:

```python
>>> "ham" * 3
'hamhamham'
```

Bei `print()` sieht man die Quotes nicht:

```python
print("ham" * 3)
```

Ausgabe:

```text
hamhamham
```

## `ord()` und `chr()`

Kurz wiederholt:

```python
ord("A")   # 65
chr(65)    # "A"
```

Fallen:

```python
ord("AB")  # TypeError
chr("A")   # TypeError
```

`ord()` erwartet einen String der Länge `1`. `chr()` erwartet einen Integer-Codepoint.

## String ist immutable

Strings können nicht an einer Position geändert werden.

```python
s = "spam"
s[0] = "S"  # TypeError
```

Man erzeugt stattdessen einen neuen String:

```python
s = "S" + s[1:]
```

## Aufgaben

### Aufgabe 1: Backslashes

Was wird ausgegeben?

```python
print("\\\\")
```

??? success "Lösung"
    Zwei Backslashes: `\\`

### Aufgabe 2: Syntaxfehler erkennen

Warum ist das ein Syntaxfehler?

```python
print("C:\Users\")
```

??? success "Lösung"
    Der letzte Backslash escaped das schließende Quote. Außerdem können Backslashes in Pfaden Escape-Sequenzen erzeugen.

### Aufgabe 3: REPL-Ausgabe

Was zeigt die REPL?

```python
>>> spam, ham = 1, "ham"
>>> spam *= 3
>>> ham *= 3
>>> spam, ham
```

??? success "Lösung"
    ```python
    (3, 'hamhamham')
    ```

### Aufgabe 4: `chr`

Was passiert?

```python
print(chr("A"))
```

??? success "Lösung"
    `TypeError`, weil `chr()` einen Integer erwartet.

### Aufgabe 5: String ändern

Warum funktioniert das nicht?

```python
s = "Hello"
s[0] = "h"
```

??? success "Lösung"
    Strings sind immutable. Einzelne Zeichen können nicht direkt ersetzt werden.

### Aufgabe 6: Quotes richtig setzen

Schreibe eine gültige Zeile, die Folgendes ausgibt:

```text
John said: "I'm fine!"
```

??? success "Lösung"
    ```python
    print('John said: "I\\'m fine!"')
    ```

    oder:

    ```python
    print("John said: \"I'm fine!\"")
    ```
