# `bytes` und `bytearray`

## Theorie

Ein Byte ist eine Zahl von `0` bis `255`. `bytes` und `bytearray` sind Folgen solcher Byte-Werte.

Das ist wichtig: Obwohl man sie oft als Text sieht, speichern sie nicht direkt Zeichen wie `"A"` oder `"ä"`, sondern Zahlen. Die Zahl `65` kann zum Beispiel als ASCII/UTF-8-Zeichen `"A"` interpretiert werden.

```python
data = b"ABC"

print(data)      # b'ABC'
print(data[0])   # 65
print(data[1])   # 66
print(data[2])   # 67
```

`b"ABC"` ist ein Bytes-Literal. Es sieht aus wie ein String mit `b` davor, ist aber kein `str`.

```python
text = "ABC"
raw = b"ABC"

print(type(text))  # <class 'str'>
print(type(raw))   # <class 'bytes'>
```

## `bytes` vs. `bytearray`

Der wichtigste Unterschied:

- `bytes` ist unveränderbar.
- `bytearray` ist veränderbar.

Das ist ähnlich wie bei `tuple` und `list`:

| Typ | Vergleichbar mit | Veränderbar? |
|-----|------------------|--------------|
| `bytes` | `tuple` | Nein |
| `bytearray` | `list` | Ja |

```python
data = b"abc"
data[0] = 65
```

Das erzeugt einen Fehler, weil `bytes` nicht verändert werden kann.

```python
data = bytearray(b"abc")
data[0] = 65
print(data)           # bytearray(b'Abc')
print(data.decode())  # Abc
```

Ein `bytearray` ist also dann sinnvoll, wenn man Byte-Daten nachträglich verändern möchte, zum Beispiel beim Einlesen, Bearbeiten oder Schreiben von Binärdaten.

## Werte und Indexing

Jedes einzelne Element ist ein Integer, kein String und kein `bytes`-Objekt.

```python
data = bytearray(b"abc")
print(data[0])
data[0] = ord("A")
print(data)
```

Ausgabe:

```text
97
bytearray(b'Abc')
```

Warum `97`? Weil `ord("a") == 97` ist. `ord()` gibt den Codepoint eines Zeichens zurück. Bei einfachen ASCII-Zeichen entspricht dieser Wert auch dem Byte-Wert.

```python
print(ord("A"))  # 65
print(chr(65))   # A
```

Werte außerhalb von `0` bis `255` sind keine gültigen Bytes.

```python
bytearray([255])  # ok
bytearray([256])  # ValueError
bytearray([-1])   # ValueError
```

## Konstruktion

Es gibt mehrere typische Wege, `bytes` oder `bytearray` zu erzeugen.

### Aus einem Bytes-Literal

```python
a = b"ABC"
b = bytearray(b"ABC")

print(a)  # b'ABC'
print(b)  # bytearray(b'ABC')
```

### Aus Integer-Werten

```python
data = bytearray([65, 66, 67])
print(data)           # bytearray(b'ABC')
print(data.decode())  # ABC
```

Die Liste `[65, 66, 67]` bedeutet nicht `"65 66 67"`, sondern drei Byte-Werte. Diese Byte-Werte können als `A`, `B`, `C` decodiert werden.

### Aus einem String mit Encoding

Ein normaler String kann nicht ohne Encoding direkt in `bytes` umgewandelt werden.

```python
text = "Hallo"
data = text.encode("utf-8")

print(data)          # b'Hallo'
print(type(data))    # <class 'bytes'>
```

Umgekehrt wird aus Byte-Daten mit `.decode(...)` wieder ein String.

```python
data = b"Hallo"
text = data.decode("utf-8")

print(text)        # Hallo
print(type(text))  # <class 'str'>
```

## Encoding und Decoding

`encode()` und `decode()` sind eine häufige Prüfungsfalle.

```python
text = "A"
raw = text.encode("utf-8")

print(raw)      # b'A'
print(raw[0])   # 65
```

Bei Umlauten oder anderen Nicht-ASCII-Zeichen sieht man besonders gut, dass ein Zeichen aus mehreren Bytes bestehen kann.

```python
text = "ä"
raw = text.encode("utf-8")

print(raw)       # b'\xc3\xa4'
print(len(text)) # 1
print(len(raw))  # 2
```

`len(text)` zählt Zeichen. `len(raw)` zählt Bytes.

Wenn man mit der falschen Codierung decodiert oder ungültige Bytefolgen decodieren will, entsteht ein Fehler.

```python
data = bytes([255])
data.decode("utf-8")  # UnicodeDecodeError
```

## Typische Operationen

`.append(x)` hängt genau einen Byte-Wert an. `x` muss ein Integer von `0` bis `255` sein.

```python
data = bytearray(b"abc")
data.append(100)

print(data)           # bytearray(b'abcd')
print(data.decode())  # abcd
```

`.extend(...)` hängt mehrere Byte-Werte an. Das kann ein Bytes-Literal, ein anderes `bytearray` oder eine Liste von Integern sein.

```python
data = bytearray(b"abc")
data.extend(b"de")
data.extend([102, 103])

print(data.decode())  # abcdefg
```

Wichtig: `.append(b"x")` ist falsch, weil `.append()` einen Integer erwartet.

```python
data = bytearray(b"abc")

data.append(ord("d"))  # ok
data.extend(b"ef")     # ok
data.append(b"g")      # TypeError
```

## Slicing

Indexing liefert einen Integer. Slicing liefert wieder ein Objekt desselben Typs.

```python
data = b"abcdef"

print(data[1])    # 98
print(data[1:4])  # b'bcd'
```

```python
data = bytearray(b"abcdef")

print(data[1])    # 98
print(data[1:4])  # bytearray(b'bcd')
```

Bei `bytearray` sind auch Slice-Zuweisungen möglich.

```python
data = bytearray(b"abcdef")
data[1:4] = b"XYZ"
print(data.decode())  # aXYZef
```

Die Länge muss dabei nicht gleich bleiben.

```python
data = bytearray(b"abcdef")
data[1:4] = b"X"

print(data.decode())  # aXef
```

## Prüfungsfallen

- `bytes` und `bytearray` sind keine Strings.
- `b"abc"[0]` ergibt `97`, nicht `b"a"` und nicht `"a"`.
- `bytearray(b"abc")[0] = "A"` ist falsch, weil ein Integer erwartet wird.
- `bytearray(b"abc")[0] = ord("A")` ist richtig.
- `bytearray([65, 66, 67])` ergibt Byte-Werte, keine Liste der Zeichen `"65"`, `"66"`, `"67"`.
- `.decode()` macht aus Bytes einen String.
- `.encode()` macht aus einem String Bytes.
- `append()` nimmt einen einzelnen Integer.
- `extend()` nimmt mehrere Byte-Werte.
- Ein Byte darf nur zwischen `0` und `255` liegen.

## Aufgaben

### Aufgabe 1: Output

```python
data = bytearray([65, 66, 67])
data[1] = 90
print(data)
print(data[0])
```

??? success "Lösung"
    `bytearray(b'AZC')` und danach `65`.

### Aufgabe 2: Reparieren

Der Code soll `Hello!` ausgeben.

```python
data = bytearray(b"hello")

# erstes Zeichen zu H machen
# Ausrufezeichen anhängen

print(data.decode())
```

??? success "Lösung"
    `data[0] = ord("H")` und `data.append(ord("!"))`.

### Aufgabe 3: Fehler erklären

Warum ist das ungültig?

```python
data = bytearray([300])
```

??? success "Lösung"
    Ein Byte darf nur Werte von `0` bis `255` haben.

### Aufgabe 4: Slice-Zuweisung

Was wird ausgegeben?

```python
data = bytearray(b"python")
data[1:4] = b"XYZ"
print(data.decode())
```

??? success "Lösung"
    `pXYZon`

### Aufgabe 5: Prüfsumme berechnen

Schreibe `checksum(data)`. Die Funktion bekommt ein `bytes`- oder `bytearray`-Objekt und gibt die Summe aller Byte-Werte modulo `256` zurück.

```python
print(checksum(bytearray([255, 1, 2])))  # 2
```

??? success "Lösung"
    ```python
    def checksum(data):
        return sum(data) % 256
    ```

### Aufgabe 6: In-place normalisieren

Schreibe `to_upper_ascii(data)`. Die Funktion bekommt ein `bytearray` und soll alle ASCII-Kleinbuchstaben in Großbuchstaben ändern. Andere Zeichen bleiben unverändert.

```python
data = bytearray(b"aB3z!")
to_upper_ascii(data)
print(data.decode())  # AB3Z!
```

??? success "Lösung"
    ```python
    def to_upper_ascii(data):
        for index, value in enumerate(data):
            if ord("a") <= value <= ord("z"):
                data[index] = value - 32
    ```

### Aufgabe 7: `bytes` vs. `bytearray`

Warum funktioniert die erste Zuweisung nicht, die zweite aber schon?

```python
a = b"abc"
a[0] = 65

b = bytearray(b"abc")
b[0] = 65
```

??? success "Lösung"
    `bytes` ist unveränderbar. `bytearray` ist veränderbar.

### Aufgabe 8: Decoder-Falle

Was ist der Unterschied zwischen diesen beiden Zeilen?

```python
print(bytearray([65, 66, 67]))
print(bytearray([65, 66, 67]).decode())
```

??? success "Lösung"
    Die erste Zeile zeigt die Bytearray-Repräsentation `bytearray(b'ABC')`. Die zweite Zeile decodiert die Bytes zu einem String: `ABC`.
