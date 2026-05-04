# Tabellen abfragen im Detail

Im folgenden schauen wir uns das Thema SQL Queries genauer an, insbesondere das Abfragen von einzelnen Tabellen.

Wir beginnen mit einer Einführung in die verschiedenen SQL-Typklassen, darunter die [Data Definition Language (DDL)](#data-definition-language-ddl), die [Data Manipulation Language (DML)](#data-manipulation-language-dml) und die [Data Query Language (DQL)](#data-query-language-dql). Jede dieser Klassen spielt eine entscheidende Rolle in der Strukturierung, Manipulation und Abfrage von Daten in relationalen Datenbanken wie SQLite, die in diesem Skript verwendet wird.

## Typklassen

### Data Definition Language (DDL)

Die DDL ermöglicht es uns, die Struktur unserer Datenbank durch das Erstellen und Löschen von Tabellen zu definieren und zu ändern.

| SQL Anweisung  | Kurze Erklärung                                                   | SQL Snippet                        |
|----------------|-------------------------------------------------------------------|------------------------------------|
| `CREATE TABLE` | Erstellt eine neue Tabelle und definiert die Spalten und Datentypen. | `CREATE TABLE Mitarbeiter (ID INTEGER, Vorname TEXT, Nachname TEXT, Abteilung TEXT, Email TEXT, Gehalt INTEGER, Geburtsdatum TEXT);` |
| `DROP TABLE`   | Löscht eine Tabelle und alle ihre Daten dauerhaft.                | `DROP TABLE Mitarbeiter;`          |                 |

### Data Manipulation Language (DML)

Mit DML-Befehlen können wir Daten innerhalb unserer Tabellen hinzufügen, aktualisieren oder löschen. 

| SQL Anweisung | Kurze Erklärung                                                               | SQL Snippet                                                                                           |
|---------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `INSERT INTO` | Fügt neue Zeilen in eine Tabelle ein.                                         | `INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (1, 'Max', 'Mustermann', 'IT', 'max@example.com', 5000, '1980-01-01');`                                    |
| `UPDATE`      | Aktualisiert bestehende Daten in einer Tabelle auf der Basis einer Bedingung. | `UPDATE Mitarbeiter SET Nachname = 'Musterfrau' WHERE ID = 1;`                                     |
| `DELETE FROM` | Löscht Zeilen aus einer Tabelle auf Basis einer Bedingung.                    | `DELETE FROM Mitarbeiter WHERE ID = 1;`                                                              |                 |

### Data Query Language (DQL)

DQL konzentriert sich hauptsächlich auf das Abrufen (Query) von Daten aus den Tabellen.

| SQL Anweisung | Kurze Erklärung                                                                                                                       | SQL Snippet                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `SELECT`      | Ruft Daten aus einer angegebenen Tabelle ab.                                                                                          | `SELECT Vorname FROM Mitarbeiter;`                                                                       |
| `COUNT()`     | Gibt die Anzahl der Zeilen zurück, die ein bestimmtes Kriterium erfüllen.                                                             | `SELECT COUNT(*) FROM Mitarbeiter;`                                                                   |
| `MAX()`       | Gibt den maximalen Wert einer Spalte im Ergebnissatz zurück.                                                                          | `SELECT MAX(Gehalt) FROM Mitarbeiter;`                                                                |
| `MIN()`       | Gibt den minimalen Wert einer Spalte im Ergebnissatz zurück.                                                                          | `SELECT MIN(Gehalt) FROM Mitarbeiter;`                                                                |
| `AVG()`       | Gibt den Durchschnittswert einer numerischen Spalte zurück.                                                                           | `SELECT AVG(Gehalt) FROM Mitarbeiter;`                                                                |
| `SUM()`       | Gibt die Gesamtsumme einer numerischen Spalte zurück.                                                                                 | `SELECT SUM(Gehalt) FROM Mitarbeiter;`                                                                |
| `CASE`        | Ermöglicht bedingte Logik innerhalb von SQL-Abfragen und ermöglicht unterschiedliche Ausgaben, abhängig von spezifischen Bedingungen. | `SELECT Name, CASE WHEN Gehalt > 5000 THEN 'Hoch' ELSE 'Niedrig' END AS Gehaltsklasse FROM Mitarbeiter;` |

### Zusätzliche Klauseln und Funktionen

Sie beinhalten verschiedene Operationen, die in den DML- und DQL-Befehlen genutzt werden können, um die Ausführung von
Befehlen zu kontrollieren und zu verfeinern.

| SQL Anweisung                        | Kurze Erklärung                                                                                                         | SQL Snippet                                                                                               |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `WHERE`                              | Filtert Datensätze auf der Basis von angegebenen Bedingungen.                                                           | `SELECT * FROM Mitarbeiter WHERE Abteilung = 'IT';`                                                       |
| `AND`, `OR`, `NOT`                   | Logische Operatoren, die innerhalb von `WHERE`-Klausel verwendet werden, um Bedingungen zu verknüpfen oder zu negieren. | `SELECT * FROM Mitarbeiter WHERE Gehalt > 3000 AND Abteilung = 'IT';`                                      |
| `BETWEEN`                            | Filtert Datensätze, bei denen die Werte einer Spalte zwischen zwei Werten liegen.                                       | `SELECT * FROM Mitarbeiter WHERE Geburtsdatum BETWEEN '1990-01-01' AND '2000-12-31';`                     |
| `ALL`, `ANY`, `IN`, `EXISTS`         | Spezialoperatoren für komplexe Bedingungen.                                                                             | `SELECT * FROM Mitarbeiter WHERE Abteilung IN ('IT', 'HR');`                                              |
| `TOP` (oder `LIMIT` in einigen DBMS) | Begrenzt die Anzahl der in einem Query-Ergebnis zurückgegebenen Zeilen.                                                 | `SELECT * FROM Mitarbeiter LIMIT 5;`  (Hinweis: `TOP` wird in SQL Server verwendet, `LIMIT` in SQLite/MySQL) |
| `NULL`                               | Gibt an, dass ein Feld einen Nullwert enthalten kann.                                                                   | `SELECT * FROM Mitarbeiter WHERE Email IS NULL;`                                                          |
| Aliase                               | Erlaubt es, eine Tabelle oder Spalte während eines Abfragelaufs umzubenennen.                                           | `SELECT Name AS Mitarbeitername FROM Mitarbeiter;`                                                        |
| Kommentare                           | Erlauben das Einfügen von Kommentaren im SQL-Code.                                                                      | `-- Dies ist ein Kommentar`                                                                               |
| NULL Funktionen                      | Funktionen zum Umgang mit NULL-Werten (z.B. `COALESCE`, `IFNULL`).                                                      | `SELECT COALESCE(Email, 'keine Email') FROM Mitarbeiter;`                                                 |
| Operatoren                           | Arithmetische, vergleichende und logische Operatoren, die in Bedingungen und Berechnungen verwendet werden.             | `SELECT * FROM Mitarbeiter WHERE Gehalt * 12 > 50000;`                                                    |
| Platzhalter                          | Werden mit dem `LIKE`-Operator verwendet, um nach einem bestimmten Muster in einer Spalte zu suchen.                    | `SELECT * FROM Mitarbeiter WHERE Name LIKE 'Ma%';`                                                        |              |


## Aufgaben

Wir werden wie in den Beispielen oben mit einer Tabelle **Mitarbeiter** arbeiten. 

<details><summary>Tabelle Queries</summary>
<pre><code>
CREATE TABLE Mitarbeiter (
    ID INTEGER ,
    Vorname TEXT,
    Nachname TEXT,
    Abteilung TEXT,
    Email TEXT,
    Gehalt INTEGER,
    Geburtsdatum TEXT
);

INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (1, 'Max', 'Mustermann', 'IT', 'max.mustermann@example.com', 5000, '1985-01-01');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (2, 'Anna', 'Schmidt', 'HR', 'anna.schmidt@example.com', 4500, '1987-02-15');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (3, 'Peter', 'Pan', 'Marketing', 'peter.pan@example.com', 4700, '1980-08-24');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (4, 'Maria', 'Maier', 'Vertrieb', 'maria.maier@example.com', 5500, '1990-05-30');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (5, 'Lukas', 'Graf', 'IT', 'lukas.graf@example.com', 5300, '1983-12-10');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (6, 'Julia', 'Stein', 'HR', 'julia.stein@example.com', 4600, '1992-03-07');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (7, 'Tobias', 'Klein', 'Marketing', 'tobias.klein@example.com', 4800, '1988-07-19');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (8, 'Sara', 'Lange', 'Vertrieb', 'sara.lange@example.com', 5100, '1986-11-05');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (9, 'Tom', 'Neumann', 'IT', 'tom.neumann@example.com', 4900, '1991-09-14');
INSERT INTO Mitarbeiter (ID, Vorname, Nachname, Abteilung, Email, Gehalt, Geburtsdatum) VALUES (10, 'Sophie', 'Bauer', 'HR', 'sophie.bauer@example.com', 4300, '1989-04-22');

DROP TABLE IF EXISTS Mitarbeiter;
</code></pre>
</details>

### Aufgabe 1: Einfache SELECT Abfrage 🌶️

Führe eine `SELECT`-Anweisung aus, um die `Vornamen` aller Mitarbeiter aus der Tabelle `Mitarbeiter` zu erhalten.

<details><summary>🍀 Tipps</summary>Verwende SELECT.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT Vorname FROM Mitarbeiter;</code></pre>
</details>

### Aufgabe 2: Verwendung von WHERE zur Filterung 🌶️🌶️

Selektiere alle Mitarbeiter der `Abteilung` "IT".

<details><summary>🍀 Tipps</summary>Verwende WHERE zusammen mit der Bedingung für die Abteilung.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT * FROM Mitarbeiter WHERE Abteilung = 'IT';</code></pre>
</details>

### Aufgabe 3: Anwendung von COUNT() 🌶️

Zähle, wie viele Mitarbeiter insgesamt in der Datenbank aufgeführt sind.

<details><summary>🍀 Tipps</summary>Verwende COUNT() in deiner SELECT-Abfrage.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT COUNT(*) FROM Mitarbeiter;</code></pre>
</details>

### Aufgabe 4: MAX() Funktion 🌶️🌶️

Finde das höchste Gehalt, das innerhalb der Mitarbeiter gezahlt wird.

<details><summary>🍀 Tipps</summary>Verwende MAX() für die Spalte Gehalt.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT MAX(Gehalt) FROM Mitarbeiter;</code></pre>
</details>

### Aufgabe 5: Verwendung von LIKE für Mustersuchen 🌶️🌶️

Finde alle Mitarbeiter, deren Namen mit 'Ma' beginnen.

<details><summary>🍀 Tipps</summary>Verwende LIKE zusammen mit dem Platzhalter '%'. 'Ma%' findet alle Einträge, die mit 'Ma' beginnen.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT * FROM Mitarbeiter WHERE Vorname LIKE 'Ma%';</code></pre>
</details>

### Aufgabe 6: Filtern nach Geburtsdatum 🌶️🌶️

Selektiere alle Mitarbeiter, die nach dem 1. Januar 1985 geboren wurden.

<details><summary>🍀 Tipps</summary>Verwende `WHERE` zusammen mit der Bedingung für das Geburtsdatum und `>`.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT * FROM Mitarbeiter WHERE Geburtsdatum > '1985-01-01';</code></pre>
</details>

### Aufgabe 7: Ermitteln des jüngsten Mitarbeiters 🌶️🌶️

Finde den jüngsten Mitarbeiter in der Datenbank.

<details><summary>🍀 Tipps</summary>Verwende `MAX()` für die Spalte Geburtsdatum.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT MAX(Geburtsdatum) FROM Mitarbeiter;</code></pre>
</details>

### Aufgabe 8: Auswahl von Mitarbeitern nach Gehalt 🌶️🌶️

Finde alle Mitarbeiter, deren Gehalt über 4500, aber unter 5000 liegt.

<details><summary>🍀 Tipps</summary>Verwende `WHERE` zusammen mit `AND` für die Gehaltsbedingungen.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT * FROM Mitarbeiter WHERE Gehalt > 4500 AND Gehalt < 5000;</code></pre>
</details>

### Aufgabe 9: Verwendung von IN für Mehrfachauswahl 🌶️🌶️

Finde alle Mitarbeiter in den Abteilungen "IT" und "HR".

<details><summary>🍀 Tipps</summary>Verwende `IN` für eine Liste von Abteilungen.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT * FROM Mitarbeiter WHERE Abteilung IN ('IT', 'HR');</code></pre>
</details>

### Aufgabe 10: Ausschluss von NULL-Werten 🌶️🌶️

Wähle alle Mitarbeiter aus, die eine Email-Adresse haben.

<details><summary>🍀 Tipps</summary>Verwende `IS NOT NULL` für die Bedingung.</details>

<details><summary>Lösung</summary>
<pre><code>SELECT * FROM Mitarbeiter WHERE Email IS NOT NULL;</code></pre>
</details>