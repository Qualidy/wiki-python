# Dateioperationen

## Dateien manuell öffnen und schließen

[Lade die Datei `beispiel.txt` herunter🔽](beispiel.txt) und lese sie mit folgendem Code aus:

```python
datei = open("beispiel.txt")
inhalt = datei.read()
print(inhalt)
datei.close()
```

`open` öffnet die Datei, `read` liest sie aus und `close` schließt sie wieder.

Beim Arbeiten mit Dateien ohne `with open` musst du darauf achten,
die Datei manuell zu öffnen und zu schließen. Das kann zu Problemen führen, wenn ein Fehler auftritt,
bevor die Datei geschlossen wird. Daher wird dieser Weg nicht empfohlen, sondern man sollte immer
mit `with` arbeiten.

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/01_alternativen_zu_read.yaml") }}
{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/02_fehler_fangen.yaml") }}
## Dateien mit `with open` nutzen

Um sicherzustellen, dass Dateien immer geschlossen werden (auch bei Fehlern),
sollten Dateien mit `with open` geöffnet und gelesen werden:

```python
with open("beispiel.txt") as datei:
    inhalt = datei.read()

print(inhalt)
```

Die `with open`-Anweisung ist eine sicherere Methode, um mit Dateien umzugehen.
Sie stellt sicher, dass die Datei ordnungsgemäß geschlossen wird, selbst wenn ein Fehler auftritt.

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/03_zeilenweise_lesen.yaml") }}
{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/04_zeichen_zahlen.yaml") }}
## Zugriffsmodi

Es gibt verschiedene Zugriffsmodi auf Dateien, die mit dem zweiten Parameter von `open` ausgewählt werden.

[Link zur Dokumentation von open](https://docs.python.org/3/library/functions.html#open)

| Modus | Beschreibung                    |
|-------|---------------------------------|
| `"r"` | Lesen (default)                 |
| `"w"` | Schreiben                       |
| `"x"` | Exklusives Schreiben            |
| `"a"` | Anhängen                        |
| `"b"` | Binärmodus                      |
| `"t"` | Textmodus (default)             |
| `"+"` | Aktualisieren (Lesen/Schreiben) |

Es können auch mehrere dieser Modi auf ein mal gewählt werden, indem man diese in einem String zusammenstellt.
Z.B. erlaubt `"rw"` das Lesen und Schreiben der Datei.

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/05_binares_lesen.yaml") }}
## In Dateien schreiben

Mit dem folgenden Code wird in eine Datei geschrieben

```python
with open("save_file", "w") as datei:
    datei.write("Hallo")
```

Beachte, dass die Datei automatisch erstellt wird, wenn sie nicht existiert. Das ist doch nett 😉

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/06_inhalte_schreiben.yaml") }}
{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/07_anhangen.yaml") }}
## Mehrere Dateien öffnen

Wir können natürlich auch den Inhalt der einen Datei in die andere Schreiben und
ggf. auf dem Weg manipulieren. Hier werden alle `"e"` durch `"*"` ersetzt:

```python
with open("beispiel.txt", "rt") as org, open("censored_text.txt", "wt") as censored:
    text = org.read()
    censored.write(text.replace("e", "*"))
```

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/08_umkehrung_einer_datei.yaml") }}
{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/09_zensur.yaml") }}
## CSV-Dateien

CSV-Dateien dienen dazu tabulare Daten zu speichern.
In diesen werden Zeilen einer Tabelle gespeichert. Meist sind
Zeilen mit einem Absatz getrennt und Einträge in einer Zeile mit einem `,`.

Fülle eine Exceltabelle mit Inhalt und speichere dann die
Datei als `.csv`. Öffne die Datei dann mit einem Texteditor,
um die Struktur einer CSV zu sehen.

Das `csv`-Modul ermöglicht das Lesen von CSV-Dateien.
Mit der `csv.reader`-Funktion kannst du die Zeilen der CSV-Datei durchgehen.
Der folgende Code zeigt, wie man die CSV-Datei
[persons.csv🔽](persons.csv) öffnen und lesen kann:

```python
import csv

with open("persons.csv", "r") as csv_datei:
    csv_reader = csv.reader(csv_datei)
    for zeile in csv_reader:
        print(zeile)
```

Wenn du Daten in eine CSV-Datei schreiben möchtest,
kannst du auch die `csv`-Bibliothek ebenfalls verwenden.
Hier ist ein Beispiel:

```python
import csv

# Daten, die in die CSV-Datei geschrieben werden sollen
daten = [
    ["Name", "Alter", "Stadt"],
    ["Max", 25, "Berlin"],
    ["Anna", 30, "München"],
    ["Tom", 22, "Hamburg"]
]

# Öffne die CSV-Datei im Schreib-Modus
with open("ausgabe.csv", "w", newline="") as csv_datei:
    # Erstelle einen CSV-Writer
    csv_writer = csv.writer(csv_datei)

    # Schreibe die Daten in die CSV-Datei
    for zeile in daten:
        csv_writer.writerow(zeile)

```

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/10_csv_als_speicherformat_nutzen.yaml") }}
{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/11_csv_datei_filtern.yaml") }}
## Exkurs: Dateipfade

Lade diesen [gezippten Order](beispiel_verzeichnis.zip) herunter,
um die folgenden Beispiele durchführen zu können.

Um sicher mit Pfaden umzugehen, sollte mit einer Library wie `pathlib`
gearbeitet werden. Lade dazu das folgede Verzeichnis herunter:

Hier siehst du zunächst verschiedene Möglichkeiten, um Pfade zusammen
zustellen:

```python
from pathlib import Path

# Erstellen eines Pfadobjekts
pfad = Path("my_file_1.txt")

pfad_current = Path()  # Ordner vom gestarteten .py file.

pfad_my_file_3 = pfad_current / "some_directory" / "my_file_3.txt"
# Mit / zu arbeiten erlaubt Plattformunabhängiges zusammensetzen von Pfaden.
```

Wir können prüfen, ob eine Datei existiert:

```python
if pfad.exists():
    print("Der angegebene Pfad existiert.")
```

Und wir können diese dann Öffnen mit `open(pfad)` oder `pfad.open()`

```python
if pfad.is_file():
    with pfad.open() as datei:
        inhalt = datei.read()
    print("Der Inhalt der Datei lautet:")
    print(inhalt)
```

Auch das Anzeigen eines Verzeichnisses ist möglich:

```python
verzeichnis = Path("some_directory")

print("Dateien im Verzeichnis:")
for element in verzeichnis.iterdir():
    if element.is_file():
        print(element.name)
```

{{ task(file="tasks/python_grundlagen/dateioperationen/dateioperationen/12_erstelle_und_analysiere_eine_dateiliste_mit_pathlib.yaml") }}
# Erstelle ein Path-Objekt, das auf das gewünschte Verzeichnis verweist
verzeichnis_pfad = Path("dein/verzeichnis/pfad")  # Ändere "dein/verzeichnis/pfad" zu deinem Zielverzeichnis

# Liste zur Speicherung der Dateiinformationen
datei_infos = []

# Iteriere durch das Verzeichnis
for element in verzeichnis_pfad.iterdir():
    if element.is_file():  # Prüfe, ob das Element eine Datei ist
        info = {
            "Dateiname": element.name,
            "Größe": element.stat().st_size / 1024,  # Größe in Kilobytes (KB)
            "Erweiterung": element.suffix
        }
        datei_infos.append(info)

# Drucke die gesammelten Informationen für jede Datei aus
for datei_info in datei_infos:
    print(f"Dateiname: {datei_info['Dateiname']}, Größe: {datei_info['Größe']:.2f}KB, Erweiterung: {datei_info['Erweiterung']}")
</code></pre>
</details>
