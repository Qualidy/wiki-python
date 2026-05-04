# Was sind Tabellen?

Tabellen sind die Speicher für Daten. Wir wollen uns anschauen, wie wir die folgende Tabelle in einer Datenbank speichern können. Die Spalten einer Datenbanktabelle werden `Spalten`, `Columns` oder `Felder`, `Fields` genannt. Die Zeilen einer Datenbank werden `Zeilen`, `Rows`, `Einträge` oder `Datensätze` genannt.

| Einkäufer | Ware    | Stück |
|-----------|:--------|:------|
| Anton     | Bananen | 4     |
| Anton     | Gurken  | 0     |
| Anton     | Milch   | 0     |
| Betina    | Bananen | 0     |
| Betina    | Gurken  | 2     |
| Betina    | Milch   | 0     |
| Christina | Bananen | 0     |
| Christina | Gurken  | 0     |
| Christina | Milch   | 1     |

### Normal-sprachliche Tabellendefinition

<details>
<summary>
Video 🎦
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vxaY9ug6GpE?si=wDW4etkgjEzHEjS9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Ohne SQL zu kennen, können wir Tabellen in unserer gewohnten Sprache beschreiben. Später werden wir, wie für
Fremdsprachen üblich, in SQL übersetzen.

In unserem Beispiel wäre die normal-sprachliche Beschreibung:

```text
Erstelle die Tabelle Einkaufsliste mit den Spalten "Einkäufer", "Ware" und "Stück".
```

Übersetzt in SQL lautet der Befehl dann:

```sql
CREATE TABLE Einkaufsliste
(
    einkaeufer,
    ware,
    stueck
);
```

Datenbankprogramm aufrufen:

```bash
sqlite3
```

Wir öffnen also in sqlite3 die Datenbank:

```bash
.open test.db
```

Dann erstellen wir eine Tabelle namens `Einkaufsliste`:

```sql
CREATE table Einkaufsliste (einkaeufer, ware, stueck);
```

⚠ Am Ende eines SQL-Befehls muss ein Semikolon `;` gesetzt werden!

⚠ Einrückungen, Leerzeichen, Groß- und Kleinschreibung interessieren Sqlite3 nicht.

Da wir in der Kommandozeile nicht sehen, was passiert, kann man folgendes Kommando nutzen, um die bestehenden Tabellen
aufzulisten:

```bash
.tables
```

Diese Tabelle ist noch leer. Mit dem folgenden Befehl können wir den Inhalt der Tabelle anzeigen:

```sql
SELECT * from Einkaufsliste;
```

Hier kommt aber nichts zurück. Das ist zwar ein gutes Zeichen, da es keine Fehler gab, aber auch langweilig.
Daher fügen wir mit dem folgenden Befehl ein neues Element in die Tabelle ein:

```sql
INSERT INTO Einkaufsliste VALUES ('Anton', 'Bananen', 4);
```

Hiermit haben wir unseren ersten Eintrag hinzugefügt. Diesen sehen wir dann auch, wenn wir wieder alle
Tabelleninhalte abfragen:

```sql
SELECT * FROM Einkaufsliste;
```

Wollen wir den Namen von Anton verändern, können wir dies wie folgt tun:

```sql
UPDATE Einkaufsliste SET name = 'Anton Hintermaier' WHERE name = 'Anton';
```

Die `WHERE` Klausel (so nennt man das auf sql-isch) dient hier als Filterfunktion, um nur die Daten zu finden, um die es
geht.

Wenn wir alle Zeilen Löschen wollen, in denen `Anton` der Einkäufer ist, können wir das wie folgt machen:

```sql
DELETE FROM Einkaufsliste WHERE Einkaeufer LIKE 'Anton';
```

Der `LIKE` - Komparator (nö, keine Klausel, denn hier geht es um Dinge, wie kleiner, größer oder gleich) findet auch
text innerhalb von größeren Zeichenfolgen.

Dieses Kommando löscht alle Einträge in der Tabelle:

```sql
DELETE FROM Einkaufsliste;
```

Um die Tabelle zu löschen, nutzen wir den folgenden Befehl:

```sql
DROP TABLE Einkaufsliste;
```

### Aufgabe: Einkaufszettel schreiben 🌶🌶

Erstelle eine Tabelle in deiner Datenbank, die genau so aussieht wie die am Kapitelanfang.

```bash
| Einkäufer | Ware    | Stück |
|-----------|:--------|:------|
| Anton     | Bananen | 4     |
| Anton     | Gurken  | 0     |
```

<details><summary>Lösung</summary>
In der Kommandozeile oder im Terminal:
<pre><code>
sqlite3
.open test.db

CREATE TABLE Einkaufsliste (einkaeufer, ware, stueck);

INSERT INTO Einkaufsliste VALUES ('Anton', 'Bananen', 4);

INSERT INTO Einkaufsliste VALUES ("Anton", "Gurken", 0),
("Anton", "Milch", 0),
("Betina", "Bananen", 0),
("Betina", "Gurken", 2),
("Betina", "Milch", 0),
("Christina", "Bananen", 0),
("Christina", "Gurken", 0),
("Christina", "Milch", 1);
</code></pre>
</details>

### Aufgaben: Wir sind hier immer noch bei VW 🌶🌶

Angenommen, du hast die folgende Pythonklasse:

```python
class Car:
    def __init__(self, name, doors, speed):
        self.name = name
        self.doors = doors
        self.speed = speed
        self.marke = "VW"

    def change_speed(self, delta):
        self.speed += delta
```

Wie müsste eine Datenbanktabelle aussehen, in der die Daten der Instanzen dieser Klasse gespeichert werden?
Wie würde ein entsprechender Befehl zum Anlegen der Datenbank aussehen?
Dies ist z.B. nützlich, wenn du das Programm herunterfährst und möchtest,
dass Daten in der Datenbank gespeichert werden.

<details><summary>Lösung</summary>
<pre><code>CREATE TABLE Car
(
    name,
    doors,
    speed,
    marke
);
</code></pre>
</details>

### Aufgabe: Datenbank laden🌶🌶

[Lade diese Datei herunter 🔽](../../material/test_datenbank.db). Es handelt sich um eine Datenbank. Binde diese ein,
finde heraus, welche Tabellen existieren und schau dir den Inhalt an.

<details>
<summary>🍀 Tipps</summary>

Datenbank `test_datenbank.db`. Ortschaften und SampleCustomers. Achte darauf, dass du im richtigen Verzeichnis bist.

</details>

<details>
<summary>Lösung</summary>

In der Kommandozeile oder im Terminal:

<pre><code>
cd //zu dem Verzeichnis wechseln, in dem die Datenbankdatei liegt.  

sqlite3

.open test_datenbank.db

.tables

SELECT * FROM Ortschaften;
</code></pre>

</details>

### Aufgabe: Datenbank Inhalt ändern🌶️🌶️

Ändere einen Eintrag in der Datenbank.

<details>
<summary>🍀 Tipps</summary>

Erst lesen, dann ändern. Nutze zuerst SELECT und dann UPDATE.

</details>

<details>
<summary>Lösung</summary>

Um eine Änderung vornehmen zu können, sollte man wissen, was man ändern will.
Daher schränken wir unsere Auswahl ein und verändern dann einen zugehörigen Wert.

Wählen Sie über die Postleitzahl einen Ort.

<pre><code>
SELECT plz, ort FROM ortschaften WHERE plz = 24768;
</code></pre>

Ergebnis

<table>
<tr>
<th>PLZ</th>
<th>Ort</th>
</tr>
<tr>
<td>24768</td>
<td>Rendsburg</td>
</tr>
<tr>
<td>24768</td>
<td>Schülp</td>
</tr>
</table>

<pre><code>
UPDATE Ortschaften SET ort = 'Da willst du nicht wohnen' WHERE plz = 24768;
</code></pre>

Kontrolle:

<pre><code>
SELECT plz, ort FROM ortschaften WHERE plz = 24768;
</code></pre>

<table>
<tr>
<th>PLZ</th>
<th>Ort</th>
</tr>
<tr>
<td>24768</td>
<td>Da willst du nicht wohnen</td>
</tr>
<tr>
<td>24768</td>
<td>Da willst du nicht wohnen</td>
</tr>
</table>

</details>

### Aufgabe: Ordnung muss sein 🌶️

Zu [welcher Klasse](../einführung/einführung.md#die-klassen-der-sql-sprachelemente) 
gehören die bisher genannten Befehle?

<details><summary>Lösung</summary>
<table style="width: 100%">
    <tr>
        <th>Begriff</th>
        <th>Klasse</th>
    </tr>
    <tr>
        <td>CREATE TABLE</td>
        <td>DDL</td>
    </tr>
    <tr>
        <td>SELECT</td>
        <td>DQL</td>
    </tr><tr>
        <td>INSERT</td>
        <td>DML</td>
    </tr>
    <tr>
        <td>UPDATE</td>
        <td>DML</td>
    </tr><tr>
        <td>DELETE</td>
        <td>DML</td>
    </tr>
    <tr>
        <td>LIKE</td>
        <td>DQL</td>
    </tr><tr>
        <td>DROP TABLE</td>
        <td>DDL</td>
    </tr>
    <tr>
        <td>WHERE</td>
        <td>DQL</td>
    </tr>
</table>
</details>

## Datentypen

Wie wir gesehen haben, verarbeitet Sqlite3 die Spalten ohne die Angabe von Datentypen.
Dieses Verhalten nennt man **schwache Typisierung**.

**SQLite benutzt ein dynamisches Typsystem.** Wenn eine Tabelle erstellt wird, wird der Typ aus den Daten "erraten". SQLite3
konvertiert die Typen automatisch. Diese Flexibilität ist eines der herausragenden Merkmale von SQLite.

SQLite3 verwendet als Datentypen nur:

- `NULL`: Der Wert ist `NULL` (für uns Pythonnasen `None`).
- `INTEGER`: Der Wert ist ein Integer.
- `REAL`: Der Wert ist ein Float im 8-byte IEEE floating point number format.
- `TEXT`: Der Wert ist ein String mit einem Datenbank-Encoding (UTF-8, UTF-16BE or UTF-16LE).
- `BLOB`: Der Wert ist ein **B**inary **L**arge **OB**ject, der genau so gespeichert wird, wie er eingegeben wurde.

Unsere Tabellendefinition ändert sich mit diesem Wissen wie folgt:

```sql
  CREATE TABLE Einkaufsliste
  (
      einkaeufer TEXT,
      ware       INTEGER,
      stueck     INTEGER
  )
```

Wenn du mehr darüber erfahren möchtest, kannst du das in der
[Dokumentation von Sqlite3](https://www.sqlite.org/datatype3.html) tun.
