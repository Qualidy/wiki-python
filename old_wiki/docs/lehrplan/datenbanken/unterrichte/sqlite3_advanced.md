# Parametrisierung von SQL-Abfragen
[20min]

Die Parametrisierung von SQL-Abfragen ist eine Möglichkeit, SQL-Abfragen zu erstellen, die Platzhalter für Daten enthalten, die zur Laufzeit eingesetzt werden. Dies ist eine gute Möglichkeit, um SQL-Injection-Angriffe zu verhindern. Die Parametrisierung von SQL-Abfragen wird durch die Verwendung von Platzhaltern erreicht, die in der SQL-Anweisung verwendet werden. Diese Platzhalter werden dann durch die Werte ersetzt, die zur Laufzeit eingesetzt werden. Die Platzhalter werden durch ein Fragezeichen dargestellt. Die Werte, die zur Laufzeit eingesetzt werden, werden als Tupel übergeben.

``` py
# Daten einfügen
cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Max', 25))
```

## Exkurs: SQL-Injection
[15min]

![SQL Injection Joke](https://imgs.xkcd.com/comics/exploits_of_a_mom_2x.png)

SQL-Injection ist eine Art von Angriff, bei dem ein Angreifer SQL-Code in eine Webformular-Eingabe oder in die URL einer Webseite einfügt, um die Datenbank zu manipulieren und Informationen preiszugeben, die der Entwickler nicht beabsichtigt hat. SQL-Injection ist eine der häufigsten Webangriffstechniken.

SQL-Injektionen treten auf, wenn Benutzereingaben oder andere nicht vertrauenswürdige Daten direkt in SQL-Anweisungen eingefügt werden, ohne ordnungsgemäße Validierung oder Bereinigung. Über die Parametrisierung von SQL-Abfragen können SQL-Injektionen verhindert werden. Die Parametrisierung von SQL-Abfragen bietet drei Hauptvorteile:

1. **Trennung von Daten und Anweisung:**
  Platzhalter ermöglichen es, die SQL-Anweisung und die Daten, die in die Anweisung eingefügt werden sollen, zu trennen. Dadurch wird verhindert, dass Benutzereingaben direkt in die Anweisung eingebettet werden.

1. **Automatische Typkonvertierung:**
  Die Parameterisierung ermöglicht eine automatische Typkonvertierung. Wenn beispielsweise ein Platzhalter für einen INTEGER-Wert verwendet wird und der Benutzer einen String einschickt, wird der Treiber automatisch versuchen, den String in einen INTEGER umzuwandeln, was zu sichereren Abfragen führt.

1. **Bereinigung von Sonderzeichen:**
  Die meisten Datenbanktreiber führen interne Bereinigungen durch, um sicherzustellen, dass die eingefügten Daten sicher sind. Dies kann das Entfernen oder Maskieren von potenziell schädlichen Zeichen beinhalten.

Beispiel ohne Platzhalter (anfällig für SQL-Injektion):

```python
# ACHTUNG: Nicht empfohlen, da anfällig für SQL-Injektionen
user_input = "John Doe'; DROP TABLE users --"
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
```

Beispiel mit Platzhaltern (verhindert SQL-Injektionen):

```python
# Verwendung von Platzhaltern
user_input = "John Doe'; DROP TABLE users --"
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
```

In diesem Beispiel würde der Versuch, eine SQL-Injektion durchzuführen, scheitern, da der Wert von `user_input` sicher durch den Platzhalter eingefügt wird, und der Treiber kümmert sich um die richtige Behandlung der Daten. Platzhalter sind daher eine bewährte Praxis, um die Sicherheit von Datenbankabfragen zu verbessern.

### Aufgabe: Keine SQL-Injection möglich 🌶
Erstelle eine SQLite-Datenbank namens 'Hunde.db' mit einer Tabelle namens 'Hunde', die die Eigenschaften jedes Hundes wie Rasse, Name und Farbe speichert. Füge dann mindestens drei Beispieldatensätze von verschiedenen Hunden in die Tabelle ein, bei denen SQL-Injektion verhindert wird. Gib die Tabelle in der Konsole aus.


<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('Hunde.db')
cursor = conn.cursor()

# Neue Tabelle für Hunde erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS hunde (
                    id INTEGER PRIMARY KEY,
                    rasse TEXT NOT NULL,
                    name TEXT NOT NULL,
                    farbe TEXT NOT NULL
                )''')

# Einzelnen Eintrag einfügen
cursor.execute('''INSERT INTO hunde (rasse, name, farbe) VALUES (?, ?, ?)''', ('Siberian Husky', 'Luna', 'Grau-Weiß'))

# Mehrere Einträge einfügen
hunde_daten = [
    ('Labrador Retriever', 'Buddy', 'Golden'),
    ('Deutscher Schäferhund', 'Rex', 'Schwarz-Braun'),
    ('Beagle', 'Bailey', 'Weiß-Braun'),
    ('Dackel', 'Fritz', 'Gestromt'),
]

cursor.executemany('''INSERT INTO hunde (rasse, name, farbe) VALUES (?, ?, ?)''', hunde_daten)

# Alle Einträge aus der Tabelle 'hunde' abrufen
cursor.execute('''SELECT * FROM hunde''')
hunde = cursor.fetchall()

# Einträge anzeigen
for hund in hunde:
    print("ID:", hund[0])
    print("Rasse:", hund[1])
    print("Name:", hund[2])
    print("Farbe:", hund[3])
    print()  # Leerzeile für bessere Lesbarkeit

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
</code></pre></details>

## Methoden in der Übersicht
[20min]

Die folgende Tabelle zeigt eine Übersicht über die wichtigsten Methoden, die in der `sqlite3`-Bibliothek verwendet werden können. Weitere Funktionen und Details zu dem Modul  `sqlite3` können der [Dokumentation](https://docs.python.org/3/library/sqlite3.html) entnommen werden.

| Name                     | Beschreibung                                  | Beispiel                                                                                                                                                                                                  |
| ------------------------ | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sqlite3.connect()`      | Verbindung zur SQLite-Datenbank herstellen    | `connection = sqlite3.connect("example.db")`                                                                                                                                                              |
| `connection.cursor()`    | Cursor erstellen                              | `cursor = connection.cursor()`                                                                                                                                                                            |
| `cursor.execute()`       | SQL-Anweisung ausführen                       | `cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")`                                                                                                     |
| `connection.commit()`    | Transaktion bestätigen                        | `connection.commit()`                                                                                                                                                                                     |
| `connection.close()`     | Verbindung schließen                          | `connection.close()`                                                                                                                                                                                      |
| `cursor.fetchall()`      | Alle Datensätze abrufen                       | `rows = cursor.fetchall()`                                                                                                                                                                                |
| `cursor.fetchone()`      | Einen Datensatz abrufen                       | `row = cursor.fetchone()`                                                                                                                                                                                 |
| `cursor.executemany()`   | Mehrere SQL-Anweisungen ausführen             | `data = [("John", 25), ("Jane", 30)]`<br>`cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)`                                                                                        |
| `cursor.executescript()` | Skript mit SQL-Anweisungen ausführen          | `script = """CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL);`<br>`INSERT INTO products (name, price) VALUES ('Widget', 19.99);"""`<br>`cursor.executescript(script)` |
| `cursor.rowcount`        | Anzahl der betroffenen Zeilen abrufen         | `print("Anzahl der betroffenen Zeilen:", cursor.rowcount)`                                                                                                                                                |
| `cursor.description`     | Spalteninformationen zu den abgerufenen Daten | `columns = [column[0] for column in cursor.description]`<br>`print("Spalten:", columns)`                                                                                                                  |
| `cursor.rollback()`      | Transaktion rückgängig machen                 | `cursor.rollback()`                                                                                                                                                                                       |

## Rollback

Die `rollback()`-Methode kann verwendet werden, um fehlerhafte oder ungewollte Transaktionen rückgängig zu machen. Daher wird sie oft in Verbindung mit der `try`-`except`-Anweisung verwendet, um sicherzustellen, dass die Transaktionen nur dann bestätigt werden, wenn keine Fehler auftreten.

``` py
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("example.db")

# Cursor erstellen
cursor = connection.cursor()

try:
    # Beginn einer Transaktion
    cursor.execute("BEGIN")

    # Durchführung von Änderungen (z. B. INSERT, UPDATE, DELETE)
    cursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")

    # Überprüfung auf Bedingungen
    condition_not_met = True

    if condition_not_met:
        # Rückgängig machen aller Änderungen bei Bedingungsfehler
        cursor.execute("ROLLBACK")
        print("Transaktion rückgängig gemacht.")
    else:
        # Bestätigung der Transaktion
        cursor.execute("COMMIT")
        print("Transaktion bestätigt.")

except Exception as e:
    print("Fehler:", str(e))
    # Falls ein Fehler auftritt, Transaktion rückgängig machen
    cursor.execute("ROLLBACK")
    print("Transaktion rückgängig gemacht aufgrund eines Fehlers.")

finally:
    # Verbindung schließen
    connection.close()
```

### Aufgabe: Rollback 🌶

Erweitere den oben erstellten Code zur Erstellung einer Hunde Datenbank um eine Rollback Funktion.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

def rollback(connection):
    connection.rollback()
    print("Rollback durchgeführt und Verbindung geschlossen.")

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('Hunde.db')
cursor = conn.cursor()

try:
    # Neue Tabelle für Hunde erstellen
    cursor.execute('''CREATE TABLE IF NOT EXISTS hunde (
                        id INTEGER PRIMARY KEY,
                        rasse TEXT NOT NULL,
                        name TEXT NOT NULL,
                        farbe TEXT NOT NULL
                    )''')

    # Einzelnen Eintrag einfügen
    cursor.execute('''INSERT INTO hunde (rasse, name, farbe) VALUES (?, ?, ?)''', ('Siberian Husky', 'Luna', 'Grau-Weiß'))

    # Daten einfügen
    hunde_daten = [
        ('Labrador Retriever', 'Buddy', 'Golden'),
        ('Deutscher Schäferhund', 'Rex', 'Schwarz-Braun'),
        ('Beagle', 'Bailey', 'Weiß-Braun'),
        ('Dackel', 'Fritz', 'Gestromt'),
    ]
    cursor.executemany('''INSERT INTO hunde (rasse, name, farbe) VALUES (?, ?, ?)''', hunde_daten)

    # Alle Einträge aus der Tabelle 'hunde' abrufen
    cursor.execute('''SELECT * FROM hunde''')
    hunde = cursor.fetchall()

    # Einträge anzeigen
    for hund in hunde:
        print("ID:", hund[0])
        print("Rasse:", hund[1])
        print("Name:", hund[2])
        print("Farbe:", hund[3])
        print()  # Leerzeile für bessere Lesbarkeit

    # Änderungen speichern
    conn.commit()
    print("Änderungen gespeichert.")

except Exception as e:
    print("Fehler aufgetreten:", e)
    rollback(conn)

finally:
    conn.close()
</code></pre>
</details>

### Aufgabe: Erweitere den Code 🌶🌶

Füge zum folgenden Code eine Funktion hinzu mit der ein neuer Benutzer zur Tabelle benutzer hinzugefügt werden kann. Beachte, dass keine SQL-Injektion möglich sein soll. Außerdem sollen Rollback Funktionen hinzugefügt werden, um mögliche Fehler abzufangen

``` py
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('benutzerdatenbank.db')
cursor = conn.cursor()

# Tabelle für Benutzerdaten erstellen (falls sie nicht vorhanden ist)
cursor.execute('''CREATE TABLE IF NOT EXISTS benutzer (
                    benutzername TEXT,
                    passwort TEXT
                )''')

# Funktion zur Überprüfung der Anmeldedaten
def anmeldung(benutzername, passwort):
    # SQL-Befehl zum Überprüfen der Anmeldedaten
    cursor.execute("SELECT * FROM benutzer WHERE benutzername = ? AND passwort = ?", (benutzername, passwort))
    
    # Ergebnis abrufen
    result = cursor.fetchall()
    
    # Überprüfen, ob ein Ergebnis gefunden wurde
    if len(result) > 0:
        print("Anmeldung erfolgreich!")
    else:
        print("Falscher Benutzername oder falsches Passwort.")

# Beispielaufruf der Anmeldungsfunktion
anmeldung("admin", "geheim")

# Transaktion beenden und Verbindung zur Datenbank schließen
conn.commit()
conn.close()
```

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('benutzerdatenbank.db')
cursor = conn.cursor()

# Tabelle für Benutzerdaten erstellen (falls sie nicht vorhanden ist)
cursor.execute('''CREATE TABLE IF NOT EXISTS benutzer (
                    benutzername TEXT,
                    passwort TEXT
                )''')

# Funktion zur Überprüfung der Anmeldedaten
def anmeldung(benutzername, passwort):
    try:
        # SQL-Befehl zum Überprüfen der Anmeldedaten mit parametrisierter Abfrage
        cursor.execute("SELECT * FROM benutzer WHERE benutzername = ? AND passwort = ?", (benutzername, passwort))

        # Ergebnis abrufen
        result = cursor.fetchall()

        # Überprüfen, ob ein Ergebnis gefunden wurde
        if len(result) > 0:
            print("Anmeldung erfolgreich!")
        else:
            print("Falscher Benutzername oder falsches Passwort.")
    except sqlite3.Error as e:
        print("Fehler bei der Anmeldung:", e)
        conn.rollback()  # Rollback bei Fehler

# Funktion zum Hinzufügen eines neuen Benutzers
def benutzer_hinzufuegen(benutzername, passwort):
    try:
        # SQL-Befehl zum Hinzufügen eines neuen Benutzers mit parametrisierter Abfrage
        cursor.execute("INSERT INTO benutzer (benutzername, passwort) VALUES (?, ?)", (benutzername, passwort))
        conn.commit()  # Transaktion bestätigen
        print("Benutzer erfolgreich hinzugefügt!")
    except sqlite3.Error as e:
        print("Fehler beim Hinzufügen des Benutzers:", e)
        conn.rollback()  # Rollback bei Fehler

# Beispielaufruf der Anmeldungsfunktion
anmeldung("admin", "123456") # Ausgabe: Falscher Benutzername oder falsches Passwort.

# Beispielaufruf zum Hinzufügen eines neuen Benutzers
benutzer_hinzufuegen("admin", "123456")
benutzer_hinzufuegen("neuer_benutzer", "987654")

# Beispielaufruf der Anmeldungsfunktion
anmeldung("admin", "123456")

# Verbindung zur Datenbank schließen
conn.close()
</code></pre></details>

## Eigene Aggregatfunktionen

Neben den bisher genannten Methoden gibt es eine Reihe weiterer Methoden, die in der `sqlite3`-Bibliothek verwendet werden können, jedoch nicht in diesem Kurs behandelt werden. Beispielsweise können über die Methode `create_aggregate()` eigene Aggregationsfunktionen erstellt werden, welche dann in SQL-Abfragen verwendet werden können.

``` py
import sqlite3

# Benutzerdefinierte Aggregatfunktion
class MyAggregate:
    def __init__(self):
        self.total = 0

    def step(self, value):
        self.total += value

    def finalize(self):
        return self.total

# Daten nur in Memory speichern statt in einer DB auf dem Gerät
connection = sqlite3.connect(":memory:")

# Aggregatfunktion erstellen
connection.create_aggregate("my_sum", 1, MyAggregate)

# Cursor erstellen
cursor = connection.cursor()

# Tabelle erstellen und Daten einfügen
cursor.execute("CREATE TABLE numbers (value INTEGER)")
cursor.executemany("INSERT INTO numbers VALUES (?)", [(1,), (2,), (3,)])

# Benutzerdefinierte Aggregatfunktion verwenden
result = cursor.execute("SELECT my_sum(value) FROM numbers").fetchone()[0]

# Ausgabe des Ergebnisses
print("Ergebnis der benutzerdefinierten Aggregatfunktion:", result)

# Verbindung schließen
connection.close()
```

### Aufgabe: Eigene Aggregatfunktion zum Erstellen des Durchschnitts 🌶🌶

Erstelle Code nach Vorlage der eben besprochenen Aggregatfunktion, um eine eigene Aggregatfunktion zu erstellen, die den Durchschnitt von Einträgen berechnet.
<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

class MyAverageAggregate:
    def __init__(self):
        self.total = 0
        self.count = 0

    def step(self, value):
        self.total += value
        self.count += 1

    def finalize(self):
        if self.count == 0:
            return None
        else:
            return self.total / self.count

connection = sqlite3.connect(":memory:")

connection.create_aggregate("my_avg", 1, MyAverageAggregate)

cursor = connection.cursor()

cursor.execute("CREATE TABLE numbers (value INTEGER)")
cursor.executemany("INSERT INTO numbers VALUES (?)", [(1,), (2,), (3,)])

result = cursor.execute("SELECT my_avg(value) FROM numbers").fetchone()[0]

print("Result of the custom average aggregate function:", result)

connection.close()
</code></pre></details>

## Context-Manager

[10min]

Die `sqlite3`-Bibliothek unterstützt die Verwendung von Context-Managern. Ein Context Manager in Python ist ein Objekt, welches das "`with`"-Statement unterstützt. Der Hauptzweck besteht darin, sicherzustellen, dass bestimmte Ressourcen ordnungsgemäß verwaltet und freigegeben werden, unabhängig davon, ob ein Fehler auftritt oder nicht.

Wir kennen Context-Manager bereits vom Lesen und Schreiben von Dateien.

```python
with open("example.txt", "r") as file:
    # Datei lesen
```

In `sqlite3` wird der Context Manager häufig mit der `connect`-Funktion verwendet. Durch den Context Manager kann die Verbindung zur Datenbank automatisch geschlossen werden, wenn der Kontext verlassen wird. Die Verwendung ist optional, da die Verbindung auch manuell geschlossen werden kann.

```python
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen und als Context Manager verwenden
with sqlite3.connect("example.db") as connection:
    # Cursor erstellen
    cursor = connection.cursor()

    # Beispiel: Tabelle erstellen
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

    # Beispiel: Daten einfügen
    cursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")

    # Beispiel: Abfrage ausführen
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print(rows)  # Ausgabe der abgerufenen Daten

# Verbindung wird automatisch geschlossen, wenn der "with"-Block verlassen wird
```

In diesem Beispiel wird `sqlite3.connect` als Context Manager verwendet. Die Verbindung zur Datenbank wird am Anfang des "`with`"-Blocks hergestellt und am Ende des Blocks automatisch geschlossen, unabhängig davon, ob ein Fehler auftritt oder nicht. Dies sorgt für eine robuste und fehlersichere Verwendung von SQLite-Verbindungen.

### Aufgabe: Context-Manager 🌶

Füge der Hunde Datenbank einen Context-Manager hinzu.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

def rollback(connection):
    connection.rollback()
    print("Rollback durchgeführt und Verbindung geschlossen.")

# Verbindung zur SQLite-Datenbank herstellen und als Context Manager verwenden
with sqlite3.connect('hunde.db') as conn:
    cursor = conn.cursor()

    try:
        # Neue Tabelle für Hunde erstellen
        cursor.execute('''CREATE TABLE IF NOT EXISTS hunde (
                            id INTEGER PRIMARY KEY,
                            rasse TEXT NOT NULL,
                            name TEXT NOT NULL,
                            farbe TEXT NOT NULL
                        )''')

        # Eintrag einfügen
        cursor.execute('''INSERT INTO hunde (rasse, name, farbe) VALUES (?, ?, ?)''', ('Siberian Husky', 'Luna', 'Grau-Weiß'))

        # Daten einfügen
        hunde_daten = [
            ('Labrador Retriever', 'Buddy', 'Golden'),
            ('Deutscher Schäferhund', 'Rex', 'Schwarz-Braun'),
            ('Beagle', 'Bailey', 'Weiß-Braun'),
            ('Dackel', 'Fritz', 'Gestromt'),
        ]
        cursor.executemany('''INSERT INTO hunde (rasse, name, farbe) VALUES (?, ?, ?)''', hunde_daten)

        # Alle Einträge aus der Tabelle 'hunde' abrufen
        cursor.execute('''SELECT * FROM hunde''')
        hunde = cursor.fetchall()

        # Einträge anzeigen
        for hund in hunde:
            print("ID:", hund[0])
            print("Rasse:", hund[1])
            print("Name:", hund[2])
            print("Farbe:", hund[3])
            print()  # Leerzeile für bessere Lesbarkeit

        # Änderungen speichern
        conn.commit()
        print("Änderungen gespeichert.")

    except Exception as e:
        print("Fehler aufgetreten:", e)
        rollback(conn)
</code></pre>
</details>

### **Projektaufgabe: Online-Shop Datenbank modellieren und verwenden 🌶️️🌶️️🌶️️**

[80min]

Angenommen, du bist damit beauftragt, eine SQLite-Datenbank für einen Online-Shop zu erstellen und zu verwalten. Die Datenbank soll Informationen über Produkte, Kunden und Bestellungen speichern. Hier sind mehrere Aufgaben, um die Funktionalität der Datenbank zu überprüfen:

1.**Datenbank erstellen 🌶️️:**  
Erstelle eine SQLite-Datenbank mit dem Namen "OnlineShop.db". Lege die notwendigen Tabellen für Produkte, Kunden und Bestellungen an. Achte darauf, Beziehungen zwischen den Tabellen herzustellen.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Produkte (
                ProduktID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Preis REAL NOT NULL,
                Lagerbestand INTEGER NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Kunden (
                KundenID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS Bestellungen (
                BestellungsID INTEGER PRIMARY KEY,
                KundenID INTEGER,
                ProduktID INTEGER,
                Menge INTEGER NOT NULL,
                Bestelldatum DATE NOT NULL,
                FOREIGN KEY (KundenID) REFERENCES Kunden(KundenID),
                FOREIGN KEY (ProduktID) REFERENCES Produkte(ProduktID)
            )''')

conn.commit()
conn.close()
</code></pre>
</details>

<br />

2.**Daten einfügen 🌶️️🌶️️:**  
Füge einige Beispieldaten für Produkte, Kunden und Bestellungen in die entsprechenden Tabellen ein.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3
from datetime import date

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

c.execute('''INSERT INTO Produkte (Name, Preis, Lagerbestand) VALUES
                ('Smartphone', 600, 50),
                ('Laptop', 1000, 30),
                ('Tablet', 400, 20)''')

c.execute('''INSERT INTO Kunden (Name, Email) VALUES
                ('Max Mustermann', 'max@example.com'),
                ('Maria Musterfrau', 'maria@example.com')''')

c.execute('''INSERT INTO Bestellungen (KundenID, ProduktID, Menge, Bestelldatum)
                VALUES (1, 1, 2, "2024-03-19"),
                       (1, 2, 1, ?),
                       (2, 3, 3, ?)''', (date.today(), date.today()))

# Aktualisierung des Lagerbestands basierend auf den eingefügten Bestellungen
c.execute('''UPDATE Produkte
                SET Lagerbestand = Lagerbestand - (
                    SELECT Menge
                    FROM Bestellungen
                    WHERE Bestellungen.ProduktID = Produkte.ProduktID
                )
                WHERE ProduktID IN (
                    SELECT ProduktID
                    FROM Bestellungen
                )''')

conn.commit()
conn.close()
</code></pre>
</details>
<br />

3.**Kundendaten abfragen 🌶️️:**  
Schreibe eine Abfrage, um alle Kundendaten abzurufen, einschließlich ihrer Bestellungen.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

c.execute('''SELECT Kunden.Name, Kunden.Email, Produkte.Name AS Produkt, Bestellungen.Menge, Bestellungen.Bestelldatum
                FROM Kunden
                JOIN Bestellungen ON Kunden.KundenID = Bestellungen.KundenID
                JOIN Produkte ON Bestellungen.ProduktID = Produkte.ProduktID''')
print(c.fetchall())

conn.close()
</code></pre>
</details>

<br />

4.**Produkte mit Bestellinformationen 🌶️️🌶️️:**  
Erstelle eine Abfrage, um alle Produkte anzuzeigen, die bestellt wurden, und füge Informationen über die Anzahl der verkauften Einheiten hinzu.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

c.execute('''SELECT Produkte.*, SUM(Bestellungen.Menge) AS VerkaufteEinheiten
                FROM Produkte
                LEFT JOIN Bestellungen ON Produkte.ProduktID = Bestellungen.ProduktID
                GROUP BY Produkte.ProduktID''')
print(c.fetchall())

conn.close()

</code></pre>
</details>

<br />

5.**Bestellhistorie eines Kunden 🌶️️🌶️️:**  
Schreibe eine Abfrage, um die Bestellhistorie eines bestimmten Kunden anzuzeigen, einschließlich der Produkte, die in jeder Bestellung enthalten sind.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

kunden_id = 1  # Beispielkunden-ID

c.execute('''SELECT Kunden.Name, Produkte.Name AS Produkt, Bestellungen.Menge, Bestellungen.Bestelldatum
                FROM Kunden
                JOIN Bestellungen ON Kunden.KundenID = Bestellungen.KundenID
                JOIN Produkte ON Bestellungen.ProduktID = Produkte.ProduktID
                WHERE Kunden.KundenID = ?''', (kunden_id,))
print(c.fetchall())

conn.close()
</code></pre>
</details>

<br />

6.**Gesamtumsatz berechnen 🌶️️🌶️️🌶️️:**
Schreibe eine SQL-Abfrage, um den Gesamtumsatz des Online-Shops zu berechnen. Berücksichtige dabei alle abgeschlossenen Bestellungen.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

c.execute('''SELECT SUM(Produkte.Preis * Bestellungen.Menge) AS Gesamtumsatz
                FROM Produkte
                JOIN Bestellungen ON Produkte.ProduktID = Bestellungen.ProduktID''')
print(c.fetchone()[0])

conn.close()
</code></pre>
</details>

<br />

7.**Aktualisiere Produktpreise 🌶️️:**  
Aktualisiere die Preise aller Produkte um 10%. Stelle sicher, dass dies nur für zukünftige Bestellungen gilt und nicht die Preise bereits abgeschlossener Bestellungen beeinflusst.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

# Preise von Produkten erhöhen, die noch nicht bestellt wurden
c.execute('''UPDATE Produkte
                SET Preis = Preis * 1.1
                WHERE ProduktID NOT IN (
                    SELECT DISTINCT ProduktID
                    FROM Bestellungen
                )''')

conn.commit()
conn.close()
</code></pre>
</details>

<br />

8.**Neuen Kunden hinzufügen 🌶️️🌶️️:**  
Füge einen neuen Kunden zur Datenbank hinzu und platziere eine Testbestellung für einige Produkte.

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3
from datetime import date

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

# Füge neuen Kunden hinzu
c.execute('''INSERT INTO Kunden (Name, Email) VALUES (?, ?)''', ('Matthias Muster', 'matze@example.com'))
new_customer_id = c.lastrowid  # ID des neuen Kunden erhalten

# Platzieren einer Testbestellung für einige Produkte
c.execute('''INSERT INTO Bestellungen (KundenID, ProduktID, Menge, Bestelldatum)
                VALUES (?, ?, ?, ?),
                       (?, ?, ?, ?)''', (new_customer_id, 1, 2, date.today(),
                                        new_customer_id, 2, 1, date.today()))

conn.commit()
conn.close()
</code></pre>
</details>

<br />

9.**Lagerbestand überprüfen 🌶️️🌶️️:**  
Schreibe eine Abfrage, um den aktuellen Lagerbestand jedes Produkts anzuzeigen und markiere diejenigen, die unter einem bestimmten Schwellenwert liegen (z.B., weniger als 10 Einheiten).

<details>
<summary>Lösung</summary>

<pre><code>
import sqlite3

conn = sqlite3.connect('OnlineShop.db')
c = conn.cursor()

# Abfrage, um den aktuellen Lagerbestand jedes Produkts anzuzeigen
c.execute('''SELECT Name, Lagerbestand,
                CASE
                    WHEN Lagerbestand < 10 THEN 'Niedrig'
                    ELSE 'Ausreichend'
                END AS Lagerstatus
                FROM Produkte''')

print(c.fetchall())

conn.close()
</code></pre>
</details>
