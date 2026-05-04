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

### Aufgabe: Alternativen zu read🌶

Ändere das obige Beispiel ab, sodass statt `read` die Methode `readline` und `readlines`
verwendet werden. Was liefern diese Methoden und wie kann man sie nutzen? Was passiert, wenn man `readline`
mehrfach hintereinander ausführt?

<details><summary>Lösung</summary>
<code>read</code>gibt einen String mit der gesamten Datei zurück.<br>
<code>readline</code> gibt die erste Zeile der Datei zurück. Beim zweiten Aufruf wird die zweite Zeile gelesen usw.
Wenn es keine Zeile mehr zu lesen gibt, werden leere Zeilen zurückgegeben.<br>
<code>readlines</code> gibt eine Liste mit den Zeilen der Datei zurück.</details>

### Aufgabe: Fehler fangen🌶🌶

Welcher Fehler wird geworfen, wenn es die Datei nicht existiert?
Schreibe Code, in denen du den Fehler bewusst auslöst und auffängst. Lass dir in
eine Nachricht auf der Konsole ausgeben und lese den Namen der Datei aus der Exception aus.

<details><summary>🍀 Tipp</summary>
<pre><code>except ... as e:</code></pre></details>

<details><summary>Lösung</summary>
<pre><code>try:
    datei = open("not_existing", "r")
    inhalt = datei.read()
    print(inhalt)
    datei.close()
except FileNotFoundError as e:
    print(f"Datei existiert nicht: {e.filename}")
</code></pre></details>

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

### Aufgabe: Zeilenweise lesen🌶🌶

Erstelle ein Programm, dass eine Datei ausließt und die erste Zeile
der Datei ausgibt. Dann wartet das Programm auf eine Nutzereingabe (z.B.
das Drücken von `enter`) und gibt dann die nächste Zeile aus.
Dies wird so lange wiederholt, bis die ganze Datei gelesen wurde.
Das Programm endet dann.

<details><summary>🍀Tipps</summary>
Nutze wiederholt <code>read_line</code></details>

<details><summary>Lösung</summary>
<pre><code>path = "beispiel.txt"
with open(path) as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
        input()
</code></pre></details>

### Aufgabe: Zeichen zählen 🌶️️

Erstelle eine Funktion, die die Anzahl der Zeichen in einer Textdatei zählt und zurückgibt.
Berücksichtige dabei auch Leerzeichen und Sonderzeichen.

<details><summary>🍀Tipps</summary>
Wie erhält man die Anzahl der Zeichen in einem String?</details>

<details><summary>Lösung</summary>
<pre><code>def count_characters_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return len(content)


print("Anzahl der Zeichen in der Datei:", count_characters_in_file("beispiel.txt"))
</code></pre></details>

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

### Aufgabe: Binäres Lesen🌶

Lese [beispiel.txt](beispiel.txt) und [mein_passwort.png](mein_passwort.png) mit `r`, `rt` und `rb`. Was ist möglich?

<details><summary>Lösung</summary>
Die <code>beispiel.txt</code> lässt sich in allen Fällen lesen. <code>"rt"</code> liefert
den exakten Text zurück, <code>r</code> erzeugt nach jeder Zeile einen Absatz und 
<code>"rb"</code> führt Zeilenumbrüche etc. nicht aus.<br>
Die <code>mein_passwort.png</code> lässt sich nur im Modus <code>"rb"</code> ohne Fehler anzeigen,
jedoch ist die Ausgabe nicht für Menschen verständlich.
</details>

## In Dateien schreiben

Mit dem folgenden Code wird in eine Datei geschrieben

```python
with open("save_file", "w") as datei:
    datei.write("Hallo")
```

Beachte, dass die Datei automatisch erstellt wird, wenn sie nicht existiert. Das ist doch nett 😉

### Aufgabe: Inhalte schreiben 🌶

Schreibe ein Programm, dass den Nutzer um eine Eingabe bittet.
Diese Eingabe wird ein eine Datei gespeichert.
Das Programm fragt den Nutzer so lange nach einer Eingabe,
bis der Nutzer `quit` eingibt. Dann schließt das Programm.

Bonus: Öffne die Datei am Ende der Programmausführung. 🌶🌶

<details>
<summary>Lösung</summary>

<pre><code>
from os import system

path = "meintext.txt"
with open(path, "wt") as file:
    while True:
    user_input = input()

    if user_input == "quit":
        break
    
    file.write(user_input + "\n")

system("open -a TextEdit " + path) # MacOS
system("notepad.exe " + path) # Windows
</code></pre>
</details>

### Aufgabe: Anhängen 🌶

Was passiert, wenn du den Code mehrfach ausführst?
Wie muss das obige Beispiel geändert werden, damit bei jeder erneuten Ausführung ein neuer Absatz mit "Hallo"
hinzugefügt wird?

<details><summary>🍀Tipp</summary>
Schaue in die Modus-Tabelle.</details>

<details><summary>Lösung</summary>
<pre><code>with open("save_file", "a") as datei:
    datei.write("Hallo\n")
</code></pre>
</details>

## Mehrere Dateien öffnen

Wir können natürlich auch den Inhalt der einen Datei in die andere Schreiben und
ggf. auf dem Weg manipulieren. Hier werden alle `"e"` durch `"*"` ersetzt:

```python
with open("beispiel.txt", "rt") as org, open("censored_text.txt", "wt") as censored:
    text = org.read()
    censored.write(text.replace("e", "*"))
```

### Aufgabe: Umkehrung einer Datei 🌶️️🌶️️

Schreibe eine Funktion `reverse_file_content(file_path, save_file_path)`,
die den Inhalt einer Textdatei ausliest, sie umkehrt und in eine andere Datei speichert.
Das heißt, die erste Zeile wird zur letzten, die zweite zur vorletzten, usw.

<details><summary>🍀Tipp</summary>
Zum Umkehren von Listen lässt sich <code>reversed</code> nutzen.</details>

<details><summary>Lösung</summary>
<pre><code>def reverse_file_content(file_path, save_file):
    with open(file_path, 'r') as file_in, open(save_file, 'w') as file_out:
        lines = file_in.readlines()
        file_out.writelines(reversed(lines))

reverse_file_content("beispiel.txt", "beispiel_reversed.txt")
</code></pre></details>

### Aufgabe: ZENSUR!!!🌶🌶🌶

Schreibe eine Klasse `Censorer` mit einer statischen Methode
`create_censored_file(org_file_path, censored_file_path, censored_words, symbol)`,
die die Angegeben String mit einem Symbol ersetzt. Dieses Symbol soll standardmäßig <code>*</code>.

Wenn alles richtig gemacht wurde, dann wird der folgende Unittest
funktionieren:

```python
import unittest
import os
from tempfile import NamedTemporaryFile


class TestCensorer(unittest.TestCase):
    def test_create_censored_file(self):
        original_text = "Dies ist ein Test, um zu überprüfen, ob bestimmte Wörter zensiert werden."
        censored_words = ["Test", "Wörter"]
        expected_censored_text = "Dies ist ein ****, um zu überprüfen, ob bestimmte ****** zensiert werden."

        # Erstelle temporäre Dateien
        with NamedTemporaryFile(mode='w', delete=False) as org_file, NamedTemporaryFile(mode='w', delete=False) as censored_file:
            org_file.write(original_text)
            org_file_path = org_file.name
            censored_file_path = censored_file.name

        # Zensiere die Datei
        Censorer.create_censored_file(org_file_path, censored_file_path, censored_words)

        # Überprüfe, ob die zensierte Datei existiert
        self.assertTrue(os.path.exists(censored_file_path))

        # Überprüfe den Inhalt der zensierten Datei
        with open(censored_file_path, 'r') as censored_file:
            actual_censored_text = censored_file.read()

        self.assertEqual(actual_censored_text, expected_censored_text)

        # Bereinige die temporären Dateien
        os.remove(org_file_path)
        os.remove(censored_file_path)

# Starte den Test
unittest.main(argv=[''], exit=False)
```

<details><summary>🍀Tipp</summary>
Eine statische Methode wird mit <code>@staticmethod</code> dekoriert.
</details>

<details><summary>Lösung</summary>
<pre><code>class Censorer:
    @staticmethod
    def create_censored_file(org_file_path, censored_file_path, censored_words, symbol="*"):
        with open(org_file_path, "rt") as org, open(censored_file_path, "wt") as censored:
            text = org.read()
            for word_to_censor in censored_words:
                replacement = symbol * len(word_to_censor)
                text = text.replace(word_to_censor, replacement)
            censored.write(text)</code></pre>
</details>

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

### Aufgabe: CSV als Speicherformat nutzen🌶🌶🌶

Erweitere die folgende Klasse um zwei Methoden:

* `create_persons_from_csv(cls, file_path)` ist eine Klassenmethode, die aus einer csv-Datei Personen ausließt und
  erstellt.
* `def save_to_csv(self, file_path, mode='a')` speichert die `Person`-Instanz in einer CSV.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name and self.age == other.age
```

CSV-Datei:

```text
Swantje,32
Maja,12
Niko,31
Sven,38

```

<details><summary>Lösung</summary>
<pre><code>from csv import reader, writer


class Person:
def __init__(self, name, age):
self.name = name
self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age}"

    @classmethod
    def create_persons_from_csv(cls, file_path):
        result = list()
        with open(file_path) as csv_file:
            for zeile in reader(csv_file):
                name, age = zeile
                result.append(cls(name, age))

        return result

    def save_to_csv(self, file_path, mode="a"):
        with open(file_path, mode, newline="") as csv_file:
            writer(csv_file).writerow([self.name, self.age])

csv_file_path = "persons.csv"
persons = Person.create_persons_from_csv(csv_file_path)

for person in persons:
print(person)

Person("Gustav", 32).save_to_csv(csv_file_path)
</code></pre></details>

### Aufgabe: CSV-Datei filtern 🌶️️🌶️️🌶️️

Erweitere die Funktion `create_persons_from_csv` um einen Parameter
`csv_filter`, mit dem man einen Teil der Elemente aus der CSV herausgefiltert wird.
Achte darauf, dass die Funktion auch noch funktioniert, wenn kein `csv_filter` gesetzt ist.

```python
def no_underaged(name, age):
    return age >= 18


persons = Person.create_persons_from_csv("persons.csv", no_underaged)

for person in persons:
    print(person)
# Swantje,32
# Niko,31
# Sven,38
```

<details><summary>🍀Tipps</summary>
Erinnere dich, wie man Funktionen als Parameter übergeben hat
und diese dann ausgeführt hat.</details>

<details><summary>Lösung</summary>
<pre><code>    @classmethod
    def create_persons_from_csv(cls, file_path, csv_filter=None):
        result = list()
        with open(file_path) as csv_file:
            for zeile in reader(csv_file):
                name, age = zeile
                if not csv_filter or csv_filter(name, age):
                    result.append(cls(name, age))

        return result

</code></pre></details>

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

### Aufgabe: Erstelle und analysiere eine Dateiliste mit pathlib 🌶️🌶️🌶️

Erstelle mit der pathlib-Bibliothek eine Liste aller Dateien in einem spezifischen Verzeichnis und analysiere diese. Iteriere durch die Verzeichnisse und sammle Informationen über die gefundenen Dateien.

| Ihr müsst in diesem Fall nach den richtigen Funktionen selber Googeln!

Importiere und erstelle ein `Path`-Objekt, das auf ein Verzeichnis deiner Wahl verweist. Dies kann z.B. ein Ordner sein, in dem du einige deiner Projekte oder Dokumente gespeichert hast.

Für jede gefundene Datei, sammle folgende Informationen:

* Dateiname
* Dateigröße in Kilobytes (KB)
* Dateierweiterung (z.B. `.txt`, `.py`, etc.)

Gib die gesammelten Informationen für jede Datei formatiert in der Konsole aus.

```txt
Dateiname: report.txt, Größe: 120KB, Erweiterung: .txt
Dateiname: image.jpeg, Größe: 1024KB, Erweiterung: .jpeg
Dateiname: script.py, Größe: 4KB, Erweiterung: .py
```

<details><summary>Lösung</summary>

<pre><code>
from pathlib import Path

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
