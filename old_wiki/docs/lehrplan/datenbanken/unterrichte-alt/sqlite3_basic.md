# Python und SQL

[15min]

Python bietet uns die Möglichkeit, über ein Modul auf eine SQLite-Datenbanken zuzugreifen. Dieses Modul heißt `sqlite3` und ist in der Standardbibliothek von Python enthalten. Wir müssen es also nicht extra installieren. `sqlite3` stellt damit eine eingebettete Datenbank-Engine dar, die direkt in Anwendungen integriert werden kann, ohne dass ein separater Datenbankserver erforderlich ist. Die Interaktionen mit der Datenbank erfolgen über SQL-Abfragen, die in Python-Strings (Docstrings) geschrieben werden.

## Verbindung zur Datenbank

[15min]

Eine Verbindung zur SQLite-Datenbank kann über die `connect()`-Methode erstellt werden.

``` py
import sqlite3
# Verbindung zur Datenbank herstellen (erstellt eine neue Datenbank namens "example.db" falls nicht vorhanden)
connection = sqlite3.connect("example.db")
```

Wenn die Datenbank nicht vorhanden ist, wird sie erstellt. Die `connect()`-Methode gibt ein Verbindungsobjekt zurück, das für die Durchführung von Datenbankoperationen verwendet wird. Dieses Verbindungsobjekt wird dann für die Erstellung eines Cursor-Objekts verwendet, um SQL-Anweisungen auszuführen.

Es ist wichtig zu beachten, dass diese Verbindung offen bleibt, bis wir sie ausdrücklich schließen. Das Schließen der Verbindung wird oft am Ende Ihrer Datenbankoperationen durchgeführt. **Das Schließen der Verbindung ist wichtig, um sicherzustellen, dass alle Änderungen, die während der Datenbankoperationen vorgenommen wurden, korrekt gespeichert werden, und um Ressourcen freizugeben**. Wenn du die Verbindung nicht schließt, können unerwartete Probleme auftreten, insbesondere wenn du die Anwendung beenden oder weitere Datenbankoperationen durchführen möchtest. Das Schließen der Datenbankverbindung erfolgt über die `close()`-Methode.

``` py
# Verbindung schließen
connection.close()
```

## Das Curser-Objekt

[10min]

Der Cursor in der SQLite-Bibliothek (und in vielen anderen Datenbank-Bibliotheken) **fungiert als Arbeitsbereich oder Zeiger**, der es ermöglicht, SQL-Anweisungen auf der Datenbank auszuführen und mit den Ergebnissen zu interagieren. Der Cursor wird aus der Verbindungsinstanz erstellt und stellt die Schnittstelle bereit, um SQL-Anweisungen auf der Datenbank auszuführen. Das Cursor-Objekt wird über die Methode `cursor()` des Verbindungsobjekts erstellt.

``` py
# Cursor-Objekt erstellen
cursor = connection.cursor()
```

## Datenbankoperationen

[15min]

Über das cursor Objekt können wir nun Datenbankoperationen ausführen. Dazu gehören das Erstellen von Tabellen, das Einfügen von Daten, das Abrufen von Daten und das Löschen von Daten. Wichtig ist, dass die Operationen nach dem Ausführen mit der `commit()`-Methode bestätigt werden müssen. Die Operationen selbst werden durch die `execute()`-Methode ausgeführt.

``` py
# Transaktion bestätigen
connection.commit()
```

Die folgenden Beispiele zeigen, wie die verschiedenen Operationen ausgeführt werden können.

### CREATE TABLE

``` py
# Tabelle erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
```

### **Aufgabe 1: Datenbank erstellen 🌶️️**

Erstelle eine SQLite-Datenbank mit dem Namen "School.db". Füge eine Tabelle "Students" hinzu, die die Spalten "StudentID" (INTEGER), "Name" (TEXT) und "Grade" (INTEGER) enthält.

<details>
<summary>Lösung</summary>

<pre><code>
# myschool.py
import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('School.db')

# Cursor-Objekt erstellen, um Abfragen auszuführen
cur = conn.cursor()

# Tabelle "Students" erstellen, wenn sie nicht existiert
cur.execute('''CREATE TABLE IF NOT EXISTS Students (
                StudentID INTEGER PRIMARY KEY,
                Name TEXT,
                Grade INTEGER
            )''')

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
</code></pre></details>

### INSERT

``` py
# Daten einfügen
cursor.execute('''INSERT INTO users (name, age) VALUES ('Max', 25)''')
```

### **Aufgabe 2: Daten einfügen 🌶️️**

Füge drei Datensätze in die "Students"-Tabelle ein.
<!--Verwende Platzhalter für StudentID, Name und Grade.-->


<details>
<summary>Lösung</summary>

<pre><code>
# myschool.py
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('School.db')
cur = conn.cursor()

# Datensätze einfügen
cur.execute("INSERT INTO Students (StudentID, Name, Grade) VALUES (1, 'Alice', 1)")
cur.execute("INSERT INTO Students (StudentID, Name, Grade) VALUES (2, 'Bob', 4)")
cur.execute("INSERT INTO Students (StudentID, Name, Grade) VALUES (3, 'Charlie', 2)")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
</code></pre></details>

Was passiert, wenn der Code mehrmals hintereinander durchgeführt wird?

<details>
<summary>Lösung</summary>

Die folgende Fehlermeldung erscheint:

<pre><code>
cur.execute("INSERT INTO Students (StudentID, Name, Grade) VALUES (1, 'Alice', 12)")
IntegrityError: UNIQUE constraint failed: Students.StudentID
</code></pre>

Das Problem: Der Primary Key muss eindeutig sein! Bei wiederholter Durchführung des Codes werden allerdings nochmal die Einträge zur Datenbank hinzugefügt, mit denselben Primary Keys, die immernoch dieselben Werte besitzen. Damit sind sie nicht mehr eindeutig.

</details>

### SELECT

``` py
# Daten abfragen
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

### **Aufgabe 3: Daten abfragen 🌶️️**

Schreibe eine SQL-Abfrage, um alle Datensätze aus der "Students"-Tabelle abzurufen.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('School.db')
cur = conn.cursor()

# Daten aus der Tabelle abfragen
cur.execute("SELECT * FROM Students")

# Alle Datensätze ausgeben
rows = cur.fetchall()
for row in rows:
    print(row)

# Verbindung schließen
conn.close()
</code></pre>
</details>

### **Aufgabe 4: Bedingte Abfrage 🌶️️🌶️️**

Schreibe eine Abfrage, um alle Schüler mit einer Note besser als 3 abzurufen.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('School.db')
cur = conn.cursor()

# Daten abrufen
cur.execute("SELECT * FROM Students WHERE Grade > 3")

# Ergebnisse ausgeben
rows = cur.fetchall()
for row in rows:
    print(row)

# Verbindung schließen
conn.close()
</code></pre>
</details>

### UPDATE

``` py
# Daten aktualisieren
cursor.execute('''UPDATE users SET age = 26 WHERE id = 1''')
```

### **Aufgabe 5: Daten aktualisieren 🌶️️**

Aktualisiere den Namen des Schülers mit der StudentID 1 auf "Emily Johnson".

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('School.db')
cur = conn.cursor()

# Namen aktualisieren
cur.execute("UPDATE Students SET Name = 'Emily Johnson' WHERE StudentID = 1")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
</code></pre></details>

### DELETE

``` py
# Daten löschen
cursor.execute('''DELETE FROM users WHERE id = 1''')
```

### **Aufgabe 6: Daten löschen 🌶️️**

Lösche den Schüler mit der StudentID 2 aus der Tabelle.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('School.db')
cur = conn.cursor()

# Schüler mit StudentID 2 löschen
cur.execute("DELETE FROM Students WHERE StudentID = 2")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
</code></pre></details>

### AGGREGATFUNKTIONEN

``` py
# Aggregatfunktion Durchschnitt
cursor.execute('''SELECT AVG(age) FROM users''')
# Aggregatfunktion Zählen
cursor.execute('''SELECT COUNT(age) FROM users''')
# Aggregatfunktion Maximum
cursor.execute('''SELECT MAX(age) FROM users''')
# Aggregatfunktion Minimum
cursor.execute('''SELECT MIN(age) FROM users''')
```

### **Aufgabe 7: Aggregatfunktionen 🌶️️🌶️️**

Schreibe eine Abfrage, um den Durchschnitt der Noten aller Schüler zu berechnen.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('School.db')
cur = conn.cursor()

# Durchschnitt der Noten abfragen
cur.execute("SELECT AVG(Grade) FROM Students")

# Ergebnis abrufen
average_grade = cur.fetchone()[0]
print("Durchschnittsnote aller Schüler:", average_grade)

# Verbindung schließen
conn.close()
</code></pre></details>

### JOIN

``` py
cur.execute('''SELECT users.Name, game.gameName
               FROM Students
               JOIN Courses ON users.id = game.gameId''')
```

### **Aufgabe 8: Join-Operation 🌶️️🌶️️**

Erstelle eine zweite Tabelle "Courses" mit den Spalten "CourseID" (INTEGER) und "CourseName" (TEXT). Füge 5 eigene Datensätze mit INSERTS ein.

Update die Tabelle Students und füge eine weitere Spalte "CourseID" ein, die jeweils eine der Spalten über eine Primary-Foreign-Key Beziehung referenziert.

Schreibe eine SQL-Abfrage, die die Schülerdaten mit den Kursdaten verbindet.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('School.db')

# Cursor-Objekt erstellen, um Abfragen auszuführen
cur = conn.cursor()

# Tabelle "Students" erstellen, wenn sie nicht existiert
cur.execute('''CREATE TABLE IF NOT EXISTS Students (
                StudentID INTEGER PRIMARY KEY,
                Name TEXT,
                Grade INTEGER
            )''')

# Tabelle "Courses" erstellen, wenn sie nicht existiert
cur.execute('''CREATE TABLE IF NOT EXISTS Courses (
                CourseID INTEGER PRIMARY KEY,
                CourseName TEXT
            )''')

# Datensätze in "Courses" einzeln einfügen
cur.execute("INSERT INTO Courses (CourseID, CourseName) VALUES (1, 'Mathe')")
cur.execute("INSERT INTO Courses (CourseID, CourseName) VALUES (2, 'Politik')")
cur.execute("INSERT INTO Courses (CourseID, CourseName) VALUES (3, 'Geschichte')")
cur.execute("INSERT INTO Courses (CourseID, CourseName) VALUES (4, 'Biologie')")
cur.execute("INSERT INTO Courses (CourseID, CourseName) VALUES (5, 'Kunst')")

# Spalte "CourseID" zu "Students" hinzufügen
cur.execute("ALTER TABLE Students ADD COLUMN CourseID INTEGER")

# Datensätze in "Students" einzeln einfügen
cur.execute("INSERT INTO Students (StudentID, Name, Grade, CourseID) VALUES (1, 'Alice', 1, 1)")
cur.execute("INSERT INTO Students (StudentID, Name, Grade, CourseID) VALUES (2, 'Bob', 4, 2)")
cur.execute("INSERT INTO Students (StudentID, Name, Grade, CourseID) VALUES (3, 'Charlie', 2, 3)")

# Änderungen speichern
conn.commit()

# SQL-Abfrage mit JOIN, um Schülerdaten mit Kursdaten zu verbinden
cur.execute('''SELECT Students.Name, Students.Grade, Courses.CourseName
               FROM Students
               JOIN Courses ON Students.CourseID = Courses.CourseID''')

# Ergebnisse abrufen und ausgeben
results = cur.fetchall()
for row in results:
    print(row)

# Verbindung schließen
conn.close()
</code></pre>
</details>

### INDEX

``` py
cur.execute('''CREATE INDEX IF NOT EXISTS idx_name ON users (name)''')
```

### **Aufgabe 9: Indizes erstellen 🌶️️🌶️️**

Erstelle einen Index auf der Spalte "Name" der "Students"-Tabelle, um Abfragen nach Schülernamen zu optimieren.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird sie erstellt)
conn = sqlite3.connect('School.db')

# Cursor-Objekt erstellen, um Abfragen auszuführen
cur = conn.cursor()

# Index auf der Spalte "Name" erstellen
cur.execute('''CREATE INDEX IF NOT EXISTS idx_name ON Students (Name)''')

# Änderungen speichern
conn.commit()

# Verbindung schließen
conn.close()
</code></pre>
</details>
