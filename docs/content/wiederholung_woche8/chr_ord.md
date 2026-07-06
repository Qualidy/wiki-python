# `chr()` und `ord()`

## Theorie

`ord()` wandelt ein einzelnes Zeichen in seinen Unicode-Codepoint um.

```python
print(ord("A"))
```

`chr()` macht aus einem Integer-Codepoint wieder ein Zeichen.

```python
print(chr(65))
```

Wichtig:

- `ord()` erwartet genau ein Zeichen.
- `chr()` erwartet einen gültigen Integer.
- Groß- und Kleinschreibung haben unterschiedliche Codepoints.

## Aufgaben

### Aufgabe 1: Output

```python
print(ord("A"))
print(ord("a"))
print(chr(ord("A") + 2))
```

??? success "Lösung"
    `65`, `97`, `C`.

### Aufgabe 2: Funktion schreiben

Schreibe `shift_char(char, amount)`.

```python
print(shift_char("A", 2))  # C
```

??? success "Lösung"
    `return chr(ord(char) + amount)`

### Aufgabe 3: Nur Großbuchstaben

Schreibe `only_uppercase(text)`. Aus `"PyTHon 3!"` soll `"PTH"` werden.

??? success "Lösung"
    Prüfe mit `ord("A") <= ord(char) <= ord("Z")`.

### Aufgabe 4: Fehler erkennen

Warum erzeugt dieser Code einen Fehler?

```python
print(ord("AB"))
```

??? success "Lösung"
    `ord()` erwartet genau ein Zeichen, nicht einen String mit zwei Zeichen.

### Aufgabe 5: Caesar light

Schreibe `shift_uppercase(text, amount)`. Es sollen nur Großbuchstaben verschoben werden. Andere Zeichen bleiben gleich. Umlauf von `Z` nach `A` soll funktionieren.

```python
print(shift_uppercase("A-Z!", 1))  # B-A!
```

??? success "Lösung"
    ```python
    def shift_uppercase(text, amount):
        result = ""
        for char in text:
            if "A" <= char <= "Z":
                offset = (ord(char) - ord("A") + amount) % 26
                result += chr(ord("A") + offset)
            else:
                result += char
        return result
    ```

### Aufgabe 6: Codepoint-Liste

Schreibe eine Funktion `codepoints(text)`, die eine Liste der Codepoints aller Zeichen zurückgibt.

```python
print(codepoints("Az!"))  # [65, 122, 33]
```

??? success "Lösung"
    `return [ord(char) for char in text]`
