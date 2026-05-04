## Schlüssel (eng. Key)

Primär- und Fremdschlüssel sind die Grundpfeiler relationaler Datenbanken, die Ordnung und Struktur in die Speicherung und Abfrage von Daten bringen.

Ein **Primärschlüssel (Primary Key)** garantiert die Einzigartigkeit jeder Zeile in einer Tabelle, was die schnelle Identifikation von Daten ermöglicht.

**Fremdschlüssel (Foreign Key)** hingegen verknüpfen Tabellen miteinander und erleichtern das Verständnis von Beziehungen zwischen verschiedenen Datensätzen.

Indem wir diese "Schlüssel"-konzepte beherrschen, können wir effizienter mit Datenbanken arbeiten.

### Definition

**Primärschlüssel**: Ein Primärschlüssel ist ein Feld oder eine Gruppe von Feldern, die einen Datensatz in einer Tabelle einzigartig identifizieren. Jede Tabelle sollte einen Primärschlüssel haben und jeder Wert im Primärschlüsselfeld muss **einzigartig** sein.

**Fremdschlüssel**:
Ein Fremdschlüssel ist ein Feld oder eine Gruppe von Feldern in einer Tabelle, die auf den Primärschlüssel einer anderen Tabelle verweisen, um relationale Beziehungen zu definieren.

#### ⚠️ Wichtig
Standardmäßig verwendet SQLite keine foreign keys. Dies muss durch den folgenden Befehl erst eingestellt werden.

```sql
PRAGMA foreign_keys = on;
```

Das liegt daran, dass man Sqlite oft in Verbindung mit anderen Programmiersprachen verwendet und **eher selten Geschäftslogik in die Datenbank einbaut**. Es bleibt dem Programmierer überlassen, welchem Konzept er folgt.
Zum allgemeinen Verständnis ist es aber wichtig, diese Konzepte zu verstehen, da sie später, wenn auch in anderer Form, angewendet werden.

### Umsetzung in SQLite

Hier nun die DDL unserer bekannten Tabellen mit Index, Schlüssel und Verweisen in SQL:

```sql
  CREATE TABLE Berufe
  (
      BerufeIndex INTEGER PRIMARY KEY AUTOINCREMENT,
      Beruf TEXT
  );

CREATE INDEX idx_Berufe ON Berufe (Beruf);
```

Hier definieren wir eine Tabelle `Berufe` mit dem primären Index auf die Spalte "Index". Dabei wird automatisch ein Index
erstellt. In diesem Fall basiert der Index auf ganzen Zahlen.
Diese Zahlen werden automatisch generiert (Identity) beginnend bei 0 und einem Inkrement von 1.

```sql
CREATE TABLE Orte
  (
      OrteIndex INTEGER PRIMARY KEY AUTOINCREMENT,
      Stadt TEXT
  )

CREATE INDEX idx_Stadt ON Orte (Stadt);
```

Das Ganze im gleichen Stil für `Orte`.

Nun die Sicht aus der Zieltabelle `Personen`:

```sql
CREATE TABLE Personen (
      PersonenIndex integer PRIMARY KEY AUTOINCREMENT,
      Name TEXT,
      Strasse TEXT,
      Ort INT,
      Email TEXT,
      Beruf INT,
      CONSTRAINT fk_Orte FOREIGN KEY (Ort) REFERENCES Orte (Index),
      CONSTRAINT fk_Berufe FOREIGN KEY (Beruf) REFERENCES Berufe (Index)
  );
  
CREATE INDEX idx_Ort ON Personen (Ort);
CREATE INDEX idx_Name ON Personen (Name);
CREATE INDEX idx_Beruf ON Personen (Beruf);
```

Es fällt auf, das hier kein Primärer Index erstellt wurde

#### Aufgabe: Erläutere Vor- und Nachteile dieser Tatsache 🌶️🌶️

<details>
<summary>
Lösung:
</summary>
<p>Es gibt eigentlich nur einen Vorteil:</p> 
<ul>
<li>die Tabelle braucht weniger Speicher, weil sie eine Spalte weniger hat.</li>
</ul>
<br>
<p>Ansonsten gibt es nur Nachteile:</p>
<ul>
<li>man kann nur schwer auf diese Tabelle verweisen und sich auf einen eindeutigen Datensatz beziehen. Man würde dafür einen zusammengesetzten Index benötigen, der aber ebenfalls nicht definiert ist.</li>
<li>Die erstellten Indizes vereinfachen die Suche auf den einzelnen Spalten, aber einen eindeutigen Datensatz findet man so nicht.</li>
<li>Suchen sind daher zwar möglich, aber sehr aufwendig und daher langsam.</li>
</ul>

<strong><u>Allgemein gilt:</u></strong> Jede Tabelle bekommt einen primären automatischen Index.
</details>

### Constraints - Bedingungen

"Constraint" ist die SQL Bezeichnung für Bedingung.
Hier werden zwei Bedingungen definiert:

- `fk_Orte`: Die Spalte "Ort" aus der eigenen Tabelle referenziert die Spalte "Index" aus der Tabelle "Orte".
- `fk_Berufe`: Die Spalte "Beruf" aus der eigenen Tabelle referenziert die Spalte "Index" aus der Tabelle "Berufe".

Anm:
- `fk` steht dabei für **foreign key** ( Fremdschlüssel)
- `idx` steht dabei für **Index**


#### Aufgabe: Mit Daten füllen 🌶️

Befülle die oben angelegten Tabellen mit jeweils 3 Beispieleinträgen. Was musst du dabei beachten?

<details>
<summary>Lösung</summary>

<pre><code>

-- Beispieldaten für die Tabelle `Berufe`
INSERT INTO Berufe (Beruf) VALUES ('Softwareentwickler');
INSERT INTO Berufe (Beruf) VALUES ('Projektmanager');
INSERT INTO Berufe (Beruf) VALUES ('Grafikdesigner');

-- Beispieldaten für die Tabelle `Orte`
INSERT INTO Orte (Stadt) VALUES ('Berlin');
INSERT INTO Orte (Stadt) VALUES ('München');
INSERT INTO Orte (Stadt) VALUES ('Hamburg');

-- Beispieldaten für die Tabelle `Personen`
INSERT INTO Personen (Name, Strasse, Ort, Email, Beruf) VALUES ('Max Mustermann', 'Musterstraße 1', 1, 'max@example.com', 1);
INSERT INTO Personen (Name, Strasse, Ort, Email, Beruf) VALUES ('Maria Musterfrau', 'Musterweg 2', 2, 'maria@example.com', 2);
INSERT INTO Personen (Name, Strasse, Ort, Email, Beruf) VALUES ('John Doe', 'Example Lane 3', 3, 'john@example.com', 3);

</code></pre>

- Beachte, dass die Fremdschlüssel `Ort` und `Beruf` müssen auf existierende Einträge in den Tabellen `Orte` und `Berufe` verweisen.

- Da `AUTOINCREMENT` verwendet wird, beginnen die IDs bei 1.

</details>