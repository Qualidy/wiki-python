# Dateien lesen und schreiben

Dateiaufgaben prüfen oft nicht grosse Projekte, sondern kleine Details:

- Modus beim Oeffnen
- Unterschied zwischen `read()`, `readline()` und `readlines()`
- Cursorposition
- Schreiben mit `write()`
- automatische Schliessung mit `with`

Offizielle Referenz: [`open()` in der Python-Dokumentation](https://docs.python.org/3.11/library/functions.html#open)

## Datei oeffnen

```python
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

Besser:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

`with` schliesst die Datei automatisch.

## Wichtige Modi

| Modus | Bedeutung |
|-------|-----------|
| `"r"` | lesen, Datei muss existieren |
| `"w"` | schreiben, ueberschreibt vorhandene Datei |
| `"a"` | anhaengen |
| `"x"` | neu erstellen, Fehler wenn Datei existiert |
| `"b"` | binaer, z.B. `"rb"` |
| `"t"` | Textmodus, Standard |

## Lesen

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
```

```python
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
```

Wichtig:

- `read()` liest ab aktueller Cursorposition bis zum Ende.
- `readline()` liest eine Zeile.
- `readlines()` liefert eine Liste von Zeilen.
- Zeilen enthalten oft noch `\n`.

## Cursorposition mit `seek()` und `tell()`

Dateien besitzen eine aktuelle Cursorposition. Leseoperationen starten an
dieser Position und verschieben sie weiter.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.read(3))
    print(file.tell())
    file.seek(0)
    print(file.read(3))
```

Wichtige Begriffe:

| Ausdruck | Bedeutung |
|----------|-----------|
| `file.tell()` | gibt die aktuelle Position zurueck |
| `file.seek(0)` | setzt die Position an den Anfang |
| `file.seek(n)` | setzt die Position auf `n` |

!!! warning "PCAP-Falle"
    Nach `read()` steht der Cursor oft am Ende. Mit `seek(0)` kann man wieder
    an den Anfang springen. In Textdateien sollte man fuer PCAP-Aufgaben
    meistens nur einfache Positionen wie `0` sicher verwenden.

## An bestimmter Position schreiben

Mit Modi wie `"r+"` kann eine Datei gelesen und geschrieben werden. Mit
`seek()` kann der Cursor an eine bestimmte Position gesetzt werden.

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("abcdef")

with open("data.txt", "r+", encoding="utf-8") as file:
    file.seek(2)
    file.write("XY")
```

Danach steht in der Datei:

```text
abXYef
```

Wichtig: `write()` fuegt hier nicht ein, sondern ueberschreibt vorhandene
Zeichen ab der aktuellen Cursorposition.

!!! warning "PCAP-Falle"
    In-place-Schreiben ist bei Textdateien nur dann einfach, wenn gleich viele
    Zeichen ersetzt werden. Soll Text eingefuegt werden, muss man meistens den
    Inhalt lesen, im Speicher veraendern und die Datei neu schreiben.

## Schreiben

```python
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Hallo\n")
    file.write("Python\n")
```

`write()` gibt die Anzahl geschriebener Zeichen zurueck.

```python
with open("result.txt", "w", encoding="utf-8") as file:
    count = file.write("abc")
    print(count)
```

Ausgabe:

```text
3
```

## Iteration ueber Dateien

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Das ist fuer grosse Dateien oft besser als alles auf einmal mit `read()` zu
laden.

## Typische Fallen

| Falle | Erklaerung |
|-------|------------|
| zweimal `read()` | zweites `read()` liefert oft `""`, weil der Cursor am Ende ist |
| `seek(0)` vergessen | nach einem vollstaendigen `read()` muss der Cursor zurueckgesetzt werden, wenn erneut von vorne gelesen werden soll |
| `write()` nach `seek()` | ueberschreibt ab Cursorposition, fuegt aber nicht automatisch ein |
| `"w"` statt `"a"` | Datei wird ueberschrieben |
| fehlendes `close()` | mit `with` vermeiden |
| `\n` vergessen | mehrere `write()`-Aufrufe schreiben sonst in dieselbe Zeile |
| falscher Pfad | Datei wird relativ zum Arbeitsverzeichnis gesucht |

## `errno` bei Dateioperationen

Bei Dateioperationen kann Python eine `OSError` oder eine Unterklasse davon
werfen, zum Beispiel `FileNotFoundError` oder `PermissionError`.

Viele dieser Fehlerobjekte besitzen ein Attribut `errno`. Darin steht eine
plattformnahe Fehlernummer. Das Modul `errno` stellt sprechende Konstanten fuer
diese Fehlernummern bereit.

```python
import errno

try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
except OSError as error:
    if error.errno == errno.ENOENT:
        print("Die Datei existiert nicht.")
    elif error.errno == errno.EACCES:
        print("Keine Berechtigung.")
    else:
        print("Anderer Datei-Fehler:", error)
```

Wichtige Werte:

| Konstante | Bedeutung |
|-----------|-----------|
| `errno.ENOENT` | Datei oder Verzeichnis existiert nicht |
| `errno.EACCES` | Zugriff verweigert |
| `errno.EEXIST` | Datei existiert bereits |
| `errno.ENOTDIR` | Ein Pfadteil ist kein Verzeichnis |

!!! warning "PCAP-Falle"
    `errno` ist nicht dasselbe wie der Exception-Typ. Der Exception-Typ sagt,
    welche Art von Fehler aufgetreten ist. `error.errno` enthaelt die konkrete
    Betriebssystem-Fehlernummer.

## `bytearray` als Buffer

Ein `bytearray` ist eine veraenderbare Folge von Bytes. Jedes Element ist ein
Integer zwischen `0` und `255`.

```python
buffer = bytearray([65, 66, 67])
print(buffer)       # bytearray(b'ABC')
print(buffer[0])    # 65

buffer[1] = 90
print(buffer)       # bytearray(b'AZC')
```

Fuer binaere Dateien ist `bytearray` praktisch, weil Bytes vor dem Schreiben
noch veraendert werden koennen.

```python
data = bytearray([0, 64, 128, 255])

with open("values.bin", "wb") as file:
    file.write(data)
```

Wichtig:

- `bytes` ist unveraenderlich.
- `bytearray` ist veraenderlich.
- Ein einzelnes Element aus `bytes` oder `bytearray` ist ein `int`, kein `str`.
- Beim binaeren Schreiben wird der Modus `"wb"` verwendet.
- Beim binaeren Lesen wird der Modus `"rb"` verwendet.

### Binaer lesen und in `bytearray` umwandeln

`file.read()` liefert im Binaermodus ein `bytes`-Objekt. Wenn die gelesenen
Daten danach veraendert werden sollen, kann man daraus einen `bytearray` bauen.

```python
with open("values.bin", "rb") as file:
    data = file.read()

buffer = bytearray(data)
buffer[0] = 255
```

Man kann den `bytearray` danach wieder binaer schreiben:

```python
with open("changed_values.bin", "wb") as file:
    file.write(buffer)
```

!!! warning "PCAP-Falle"
    `file.read()` im Binaermodus liefert `bytes`, nicht `bytearray`. Erst
    `bytearray(file.read())` macht daraus einen veraenderbaren Buffer.

## Bilddaten als Bytes

Digitale Bilder bestehen aus Pixelwerten. Fuer ein RGB-Bild hat jedes Pixel
drei Werte:

- Rot
- Gruen
- Blau

Jeder Wert liegt zwischen `0` und `255`.

Ein schwarzer Pixel:

```python
[0, 0, 0]
```

Ein weisser Pixel:

```python
[255, 255, 255]
```

Ein roter Pixel:

```python
[255, 0, 0]
```

Fuer PCAP ist nicht wichtig, eine komplette Bildbibliothek zu kennen. Fuer eine
praktische Aufgabe ist ein externes Modul aber sinnvoll: Die Datei- und
CSV-Schritte bleiben sichtbar, waehrend die Bildspeicherung von `Pillow`
uebernommen wird.

Installation:

```bash
pip install Pillow
```

Relevant ist das Prinzip:

1. Textdaten oder Zahlen lesen.
2. Daraus Bytes bauen.
3. Pixelwerte an ein externes Modul uebergeben.
4. Das Bild speichern.

Das folgende Hilfsprogramm schreibt aus einem RGB-Buffer ein PNG mit `Pillow`.

```python
from PIL import Image


def save_png(path, width, height, rgb_buffer):
    image = Image.new("RGB", (width, height))
    pixels = [
        tuple(rgb_buffer[index:index + 3])
        for index in range(0, len(rgb_buffer), 3)
    ]
    image.putdata(pixels)
    image.save(path)
```

## Aufgaben

### Aufgabe 1: Cursorposition erklären

Warum liefert ein zweites `file.read()` direkt danach oft einen leeren String?

??? success "Lösung"
    Nach dem ersten `read()` steht der Dateicursor am Ende. Ein weiteres `read()` liest ab dort weiter und findet nichts mehr.

### Aufgabe 2: Datei-Modi wählen

Wähle den passenden Modus:

1. Datei neu schreiben und alten Inhalt löschen
2. Logdatei erweitern
3. Datei lesen, die existieren muss
4. Binärdatei lesen

??? success "Lösung"
    1. `"w"`, 2. `"a"`, 3. `"r"`, 4. `"rb"`.

### Aufgabe 3: Rückgabewert von `write`

Was gibt dieser Code aus?

```python
with open("result.txt", "w", encoding="utf-8") as file:
    print(file.write("Python"))
```

??? success "Lösung"
    `6`, weil `write()` die Anzahl geschriebener Zeichen zurückgibt.

### Aufgabe 4: Zeilen zählen

Schreibe eine Funktion `count_lines(path)`, die die Anzahl der Zeilen einer Textdatei zurückgibt.

??? success "Lösung"
    ```python
    def count_lines(path):
        with open(path, "r", encoding="utf-8") as file:
            return sum(1 for line in file)
    ```

### Aufgabe 5: Datei kopieren

Schreibe `copy_text(source, target)`. Die Funktion soll den Inhalt einer Textdatei lesen und in eine andere Datei schreiben.

??? success "Lösung"
    ```python
    def copy_text(source, target):
        with open(source, "r", encoding="utf-8") as src:
            content = src.read()
        with open(target, "w", encoding="utf-8") as dst:
            dst.write(content)
    ```

### Aufgabe 6: `readline()` vs. `readlines()`

Erkläre den Unterschied zwischen `readline()` und `readlines()`.

??? success "Lösung"
    `readline()` liest eine einzelne Zeile. `readlines()` liest alle verbleibenden Zeilen und gibt eine Liste zurück.

### Aufgabe 7: `errno` gezielt auswerten

Schreibe eine Funktion `read_text_or_message(path)`.

Die Funktion soll:

1. Eine Textdatei lesen und den Inhalt zurueckgeben.
2. Bei einer nicht vorhandenen Datei den Text `"Datei nicht gefunden"` zurueckgeben.
3. Bei fehlender Berechtigung den Text `"Keine Berechtigung"` zurueckgeben.
4. Andere `OSError`-Fehler erneut werfen.

Nutze `errno.ENOENT` und `errno.EACCES`.

??? success "Lösung"
    ```python
    import errno


    def read_text_or_message(path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except OSError as error:
            if error.errno == errno.ENOENT:
                return "Datei nicht gefunden"
            if error.errno == errno.EACCES:
                return "Keine Berechtigung"
            raise
    ```

### Aufgabe 8: `bytearray`-Buffer veraendern und binaer schreiben

Erstelle einen `bytearray` mit den Werten `0` bis `255`. Invertiere danach alle
Werte, sodass aus `0` der Wert `255` wird, aus `1` der Wert `254` usw.
Schreibe das Ergebnis binaer in die Datei `inverted.bin`.

??? success "Lösung"
    ```python
    buffer = bytearray(range(256))

    for index, value in enumerate(buffer):
        buffer[index] = 255 - value

    with open("inverted.bin", "wb") as file:
        file.write(buffer)
    ```

### Aufgabe 9: CSV mit Pixelwerten erzeugen

Erzeuge eine CSV-Datei `gradient.csv` fuer ein Bild mit `16` Pixeln Breite und
`16` Pixeln Hoehe.

Jede Zeile der CSV soll so aussehen:

```text
x,y,r,g,b
```

Die Datei soll eine Kopfzeile enthalten. Danach soll fuer jeden Pixel eine Zeile
folgen. Nutze eine List Comprehension, um die Zeilen fuer einen
Helligkeitsverlauf zu erzeugen:

- `r`, `g` und `b` sollen gleich sein.
- Links soll der Wert dunkel sein.
- Rechts soll der Wert hell sein.

Dieser Schritt soll nur die CSV-Datei erzeugen, noch kein Bild.

??? success "Lösung"
    ```python
    width = 16
    height = 16

    rows = [
        f"{x},{y},{x * 255 // (width - 1)},{x * 255 // (width - 1)},{x * 255 // (width - 1)}\n"
        for y in range(height)
        for x in range(width)
    ]

    with open("gradient.csv", "w", encoding="utf-8") as file:
        file.write("x,y,r,g,b\n")
        file.writelines(rows)
    ```

### Aufgabe 10: CSV-Pixelwerte in einen `bytearray` lesen

Lies `gradient.csv` ein und baue daraus einen `bytearray` mit RGB-Werten.

Die Aufgabe soll nur den Buffer erzeugen und pruefen:

- Der Buffer soll `width * height * 3` Werte enthalten.
- Fuer jeden CSV-Eintrag werden `r`, `g` und `b` an den Buffer angehaengt.
- Die Kopfzeile soll uebersprungen werden.

??? success "Lösung"
    ```python
    width = 16
    height = 16
    pixels = bytearray()

    with open("gradient.csv", "r", encoding="utf-8") as file:
        next(file)  # Kopfzeile ueberspringen

        for line in file:
            x, y, r, g, b = line.strip().split(",")
            pixels.extend([int(r), int(g), int(b)])

    print(len(pixels))
    print(width * height * 3)
    ```

### Aufgabe 11: PNG aus einem `bytearray` mit Pillow schreiben

Nutze den `pixels`-Buffer aus Aufgabe 10 und das externe Modul `Pillow`.
Schreibe daraus die Datei `gradient.png`.

Dieser Schritt soll nur aus bereits vorhandenen RGB-Bytes ein PNG schreiben.
Falls Pillow noch nicht installiert ist:

```bash
pip install Pillow
```

??? success "Lösung"
    ```python
    from PIL import Image


    def save_png(path, width, height, rgb_buffer):
        image = Image.new("RGB", (width, height))
        pixels_as_tuples = [
            tuple(rgb_buffer[index:index + 3])
            for index in range(0, len(rgb_buffer), 3)
        ]
        image.putdata(pixels_as_tuples)
        image.save(path)


    width = 16
    height = 16
    pixels = bytearray()

    with open("gradient.csv", "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            x, y, r, g, b = line.strip().split(",")
            pixels.extend([int(r), int(g), int(b)])

    save_png("gradient.png", width, height, pixels)
    ```

### Aufgabe 12: Pixel vor dem Schreiben manipulieren

Erzeuge aus dem Buffer aus Aufgabe 10 einen zweiten Buffer `inverted_pixels`.
Invertiere jeden Farbwert:

```python
255 - value
```

Schreibe danach mit `save_png` die Datei `gradient_inverted.png`.

Dieser Schritt manipuliert nicht die fertige PNG-Datei, sondern die Pixelwerte
vor dem Schreiben. Der Fokus liegt auf dem `bytearray`.

??? success "Lösung"
    ```python
    inverted_pixels = bytearray(255 - value for value in pixels)
    save_png("gradient_inverted.png", width, height, inverted_pixels)
    ```

### Aufgabe 13: Farbverlauf statt Helligkeitsverlauf

Erzeuge eine neue CSV-Datei `color_gradient.csv`.

Nutze wieder eine List Comprehension. Diesmal sollen die Farben so entstehen:

- `r` haengt von `x` ab.
- `g` haengt von `y` ab.
- `b` bleibt konstant `128`.

Danach soll wieder ein eigener Schritt die CSV lesen und mit Pillow ein PNG
`color_gradient.png` schreiben.

??? success "Lösung"
    ```python
    width = 32
    height = 32

    rows = [
        f"{x},{y},{x * 255 // (width - 1)},{y * 255 // (height - 1)},128\n"
        for y in range(height)
        for x in range(width)
    ]

    with open("color_gradient.csv", "w", encoding="utf-8") as file:
        file.write("x,y,r,g,b\n")
        file.writelines(rows)

    pixels = bytearray()

    with open("color_gradient.csv", "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            x, y, r, g, b = line.strip().split(",")
            pixels.extend([int(r), int(g), int(b)])

    save_png("color_gradient.png", width, height, pixels)
    ```

### Aufgabe 14: `seek()` und `tell()` nachvollziehen

Erstelle eine Datei `letters.txt` mit dem Inhalt:

```text
abcdef
```

Lies danach zuerst drei Zeichen, gib die Cursorposition mit `tell()` aus, springe
mit `seek(0)` zurueck an den Anfang und lies wieder drei Zeichen.

Erklaere, warum zweimal `"abc"` gelesen wird.

??? success "Lösung"
    ```python
    with open("letters.txt", "w", encoding="utf-8") as file:
        file.write("abcdef")

    with open("letters.txt", "r", encoding="utf-8") as file:
        first = file.read(3)
        position = file.tell()
        file.seek(0)
        second = file.read(3)

    print(first)
    print(position)
    print(second)
    ```

    Nach `file.read(3)` steht der Cursor hinter den ersten drei Zeichen.
    `file.tell()` zeigt diese Position. `file.seek(0)` setzt den Cursor wieder
    an den Anfang, deshalb liest das zweite `read(3)` erneut `"abc"`.

### Aufgabe 15: Binaerdatei in einen `bytearray` lesen

Erstelle zuerst eine Datei `raw_values.bin` mit den Bytes `10`, `20`, `30` und
`40`.

Lies die Datei danach im Binaermodus ein, wandle den Inhalt in einen
`bytearray` um und veraendere den zweiten Wert auf `200`.

Schreibe den veraenderten Buffer in `raw_values_changed.bin`.

??? success "Lösung"
    ```python
    original = bytearray([10, 20, 30, 40])

    with open("raw_values.bin", "wb") as file:
        file.write(original)

    with open("raw_values.bin", "rb") as file:
        data = file.read()

    buffer = bytearray(data)
    buffer[1] = 200

    with open("raw_values_changed.bin", "wb") as file:
        file.write(buffer)
    ```

    `file.read()` liefert im Binaermodus ein `bytes`-Objekt. Weil `bytes`
    unveraenderlich ist, wird mit `bytearray(data)` ein veraenderbarer Buffer
    erzeugt.

### Aufgabe 16: In-place schreiben mit `seek()`

Erstelle eine Datei `word.txt` mit dem Inhalt:

```text
Python
```

Oeffne die Datei danach mit `"r+"`, setze den Cursor auf Position `2` und
schreibe `"XX"`.

1. Was steht danach in der Datei?
2. Warum wird nichts eingefuegt?

??? success "Lösung"
    ```python
    with open("word.txt", "w", encoding="utf-8") as file:
        file.write("Python")

    with open("word.txt", "r+", encoding="utf-8") as file:
        file.seek(2)
        file.write("XX")

    with open("word.txt", "r", encoding="utf-8") as file:
        print(file.read())
    ```

    Ausgabe:

    ```text
    PyXXon
    ```

    `seek(2)` setzt den Cursor vor das dritte Zeichen. `write("XX")`
    ueberschreibt danach die vorhandenen Zeichen `t` und `h`. Es wird kein
    Platz eingefuegt.

### Aufgabe 17: Text einfuegen durch Neu-Schreiben

Erstelle wieder eine Datei `word.txt` mit dem Inhalt:

```text
Python
```

Fuege im Speicher nach `Py` den Text `"--"` ein, sodass die Datei danach
folgenden Inhalt hat:

```text
Py--thon
```

Nutze dafuer nicht `r+`, sondern:

1. Datei komplett lesen
2. String im Speicher zusammensetzen
3. Datei mit `"w"` neu schreiben

??? success "Lösung"
    ```python
    with open("word.txt", "w", encoding="utf-8") as file:
        file.write("Python")

    with open("word.txt", "r", encoding="utf-8") as file:
        content = file.read()

    changed = content[:2] + "--" + content[2:]

    with open("word.txt", "w", encoding="utf-8") as file:
        file.write(changed)
    ```

    In-place-Schreiben ueberschreibt vorhandene Zeichen. Fuer echtes Einfuegen
    ist Lesen, Veraendern und Neu-Schreiben oft die einfachere und sichere
    Strategie.
