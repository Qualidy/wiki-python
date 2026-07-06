# Dateien lesen und schreiben

Dateiaufgaben prüfen oft nicht grosse Projekte, sondern kleine Details:

- Modus beim Oeffnen
- Unterschied zwischen `read()`, `readline()` und `readlines()`
- Cursorposition
- Schreiben mit `write()`
- automatische Schliessung mit `with`

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
| `"w"` statt `"a"` | Datei wird ueberschrieben |
| fehlendes `close()` | mit `with` vermeiden |
| `\n` vergessen | mehrere `write()`-Aufrufe schreiben sonst in dieselbe Zeile |
| falscher Pfad | Datei wird relativ zum Arbeitsverzeichnis gesucht |

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
