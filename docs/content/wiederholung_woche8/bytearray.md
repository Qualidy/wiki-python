# `bytearray`

## Theorie

Ein `bytearray` ist eine veränderbare Folge von Bytes. Jedes Element ist ein Integer zwischen `0` und `255`.

```python
data = bytearray(b"abc")
print(data[0])
data[0] = ord("A")
print(data)
```

Wichtig:

- `bytes` ist unveränderbar.
- `bytearray` ist veränderbar.
- Einzelne Elemente sind Integer, keine Strings.
- Werte außerhalb von `0` bis `255` erzeugen einen Fehler.
- `bytearray(b"text")` startet mit Bytes aus einem Bytes-Literal.
- `bytearray([65, 66])` startet mit Integer-Werten.
- `.decode()` wandelt Bytes in einen String um, wenn die Bytes zur gewählten Codierung passen.
- `.append(x)` erwartet einen einzelnen Integer von `0` bis `255`.
- `.extend(...)` kann mehrere Bytes anhängen, zum Beispiel aus `b"abc"` oder aus einer Liste von Integern.

## Typische Operationen

```python
data = bytearray(b"abc")
data.append(100)
data.extend(b"ef")
print(data.decode())  # abcdef
```

Slicing liefert wieder ein `bytearray`.

```python
data = bytearray(b"abcdef")
part = data[1:4]
print(part)
```

Auch Slice-Zuweisungen sind möglich.

```python
data = bytearray(b"abcdef")
data[1:4] = b"XYZ"
print(data.decode())  # aXYZef
```

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
