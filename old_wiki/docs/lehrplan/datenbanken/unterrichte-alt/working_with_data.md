# Arbeiten mit Daten

## Das CRUD Prinzip
In diesem beschreiben wir die grundlegenden Datenbankoperatioen um Daten 
- einzufügen (**C**reate),
- auszulesen (**R**ead),
- zu aktualisieren (**U**pdate) und 
- zu löschen (**D**elete)

-> **CRUD**

## Einfügen von Daten

Nachdem wir im letzten Kapitel gelernt haben, wie man Tabellen in SQLite erstellt, werden wir uns nun darauf
konzentrieren, wie man Daten in diese Tabellen einfügt. Wir werden das `INSERT`-Kommando sowohl über die Konsole als
auch über das SQLite Command Line Interface (CLI) verwenden. Dies wird uns helfen zu verstehen, wie manuell das Einfügen
von Daten erfolgt und wie mühsam es sein kann, größere Datenmengen händisch einzufügen. Zur Vereinfachung dieses
Prozesses werden wir auch die Funktionen von SQLite zur Importierung von Daten aus CSV-Dateien nutzen. Die Überprüfung
der korrekten Dateneinfügung erfolgt durch einfache `SELECT`-Kommandos.

**Manuelles Einfügen über die Konsole/CLI**:
Um Daten manuell in eine Tabelle einzufügen, verwenden wir das `INSERT INTO`-Statement. Angenommen, wir haben eine
Tabelle `personen` mit den Spalten `id`, `name` und `alter`. Ein Beispiel für das Einfügen eines Datensatzes wäre:

```sql
INSERT INTO personen (id, name, alter)
VALUES (1, 'Max Mustermann', 30);
```

### **Aufgabe: Daten manuell einfügen 🌶️️**
[10min]
Wiederholen Sie diesen Vorgang für einige Datensätze, um zu üben, wie Daten manuell eingefügt werden.

**Einfügen mehrerer Datensätze**:

Um den Prozess zu beschleunigen, können Sie mehrere Datensätze gleichzeitig einfügen:

```sql
INSERT INTO personen (id, name, alter)
VALUES (2, 'Maria Musterfrau', 28),
       (3, 'John Doe', 25);
```

### **Aufgabe: Mehrere Datesätze manuell einfügen 🌶️️**
[15min]
Wiederholen sie den Vorgang und fügen sie weitere Datensätze in das Kommando ein.

### **Aufgabe: Überprüfung der Einfügungen 🌶️️**:
[10min]
Um zu überprüfen, ob die Daten korrekt eingefügt wurden, verwenden Sie das `SELECT`-Statement:

```sql
SELECT *
FROM personen;
```

## Importieren von Daten aus einer CSV-Datei (bulk insert)

**Vorbereitung der CSV-Datei**:

Erstellen Sie eine CSV-Datei mit den entsprechenden Daten. Zum Beispiel könnte eine Datei `personen.csv` folgendermaßen
aussehen:

```
id,name,alter
4,Jane Smith,32
5,Alex Johnson,45
```

**Importieren der Daten**:
Verwenden Sie das SQLite-Tool, um die Daten aus der CSV-Datei zu importieren. Öffnen Sie das SQLite CLI und führen
Sie folgende Befehle aus:

```sql
.mode csv
.import pfad/zur/personen.csv personen
```

Stellen Sie sicher, dass der Pfad zur CSV-Datei und der Tabellenname korrekt sind.

**Überprüfung des Imports**:
Verwenden Sie erneut das `SELECT`-Statement, um zu überprüfen, ob die Daten aus der CSV-Datei korrekt importiert
wurden:

```sql
SELECT *
FROM personen;
```

### **Aufgabe: Beispieldaten finden und einfügen 🌶️️🌶️️🌶️️**
[40 min]

1. Suchen sie im Internet nach Datentabellen, die im CSV Format geladen werden können. Hier bieten sich fake Datenbanken
   oder Ortsverzeichnisse mit PLZ an.
2. Erstellen sie die passende Tabelle dazu.
3. Fügen sie die Daten in die Tabelle ein und prüfen sie das Ergebnis.

### INSERT Zusammenfassung

Durch das manuelle Einfügen von Daten und den Import aus einer CSV-Datei lernen die Schüler zwei grundlegende Methoden,
um mit Daten in SQLite zu arbeiten. Während das manuelle Einfügen gut für das Verständnis des `INSERT`-Kommandos und für
kleinere Datenmengen geeignet ist, zeigt der Import aus einer CSV-Datei, wie man effizienter mit größeren Datenmengen
umgehen kann. Beide Methoden sind wichtig, um ein umfassendes Verständnis für das Arbeiten mit Datenbanken zu
entwickeln.

## Komplexere Abfragen

Nachdem wir Daten in unsere Datenbank eingefügt haben, ist es an der Zeit, komplexere Abfragen zu üben. Wir werden
verschiedene Sprachelemente von SQL nutzen, darunter `SELECT`-Abfragen
mit `WHERE`, `HAVING`, `ORDER BY`, `GROUP BY`, `LIKE`, `IS (NOT) NULL`, sowie die logischen Operatoren `AND` und `OR`
und den Operatoren `ASC` und `DESC`.
Zunächst erstellen wir eine geeignete Tabelle, und dann üben wir anhand von 15 Beispielen.

### Erstellung einer Beispieltabelle

Lassen Sie uns eine Tabelle `mitarbeiter` erstellen, die wir für unsere Übungen verwenden können:

```sql
CREATE TABLE mitarbeiter
(
    id                INT PRIMARY KEY,
    name              TEXT,
    alter             INT,
    abteilung         TEXT,
    gehalt            REAL,
    eintrittsdatum    DATE,
    hat_fuehrerschein BOOLEAN
);
```

### **Aufgabe: Testdaten 🌶️️🌶️️**
[40min] Fülle die Tabelle mit Testdaten.

### **Aufgabe: Alter nutzen 🌶️️🌶️️**
[30min]  Erweitere die Tabelle mit dem ALTER Befehl und fülle mit Daten

### Liste von Abfragebeispielen

**Einfache Auswahl**:

```sql
SELECT *
FROM mitarbeiter;
```

**Auswahl mit Bedingung**:

```sql
SELECT *
FROM mitarbeiter
WHERE abteilung = 'Vertrieb';
```

**Sortierung der Ergebnisse**:

```sql
SELECT *
FROM mitarbeiter
ORDER BY gehalt DESC;
```

**Auswahl mit mehreren Bedingungen**:

```sql
SELECT *
FROM mitarbeiter
WHERE
alter > 30 AND gehalt > 3000;
```

**Verwendung von OR**:

```sql
SELECT *
FROM mitarbeiter
WHERE abteilung = 'Vertrieb'
   OR abteilung = 'Marketing';
```

**Suche mit LIKE**:

```sql
SELECT *
FROM mitarbeiter
WHERE name LIKE '%Schmidt%';
```

**Überprüfung auf NULL-Werte**:

```sql
SELECT *
FROM mitarbeiter
WHERE eintrittsdatum IS NULL;
```

**Gruppierung von Daten**:

```sql
SELECT abteilung, COUNT(*)
FROM mitarbeiter
GROUP BY abteilung;
```

**Gruppierung mit HAVING**:

```sql
SELECT abteilung, COUNT(*)
FROM mitarbeiter
GROUP BY abteilung
HAVING COUNT(*) > 3;
```

**Auswahl spezifischer Spalten**:

```sql
SELECT name, gehalt
FROM mitarbeiter;
```

**Einschränkung der Ergebnismenge**:

```sql
SELECT *
FROM mitarbeiter
WHERE gehalt > 5000 LIMIT 10;
```

**Kombination von AND und OR**:

```sql
SELECT *
FROM mitarbeiter
WHERE (
alter < 35 OR alter > 50) 
AND abteilung = 'IT';
```

**Überprüfung auf Nicht-NULL-Werte**:

```sql
SELECT *
FROM mitarbeiter
WHERE eintrittsdatum IS NOT NULL;
```

**Sortierung nach mehreren Kriterien**:

```sql
SELECT *
FROM mitarbeiter
ORDER BY abteilung, gehalt DESC; -- alternativ ASC
```

### **Aufgabe: Befehle anwenden 🌶️️🌶️️🌶️️**
[60min] Wende die Befehle auf selbst zugefügte Spalten und Daten an

### Zusammenfassung

Diese Abfragen decken eine breite Palette von SQL-Funktionen ab und bieten eine solide Grundlage für das Verständnis und
die Anwendung komplexerer SQL-Abfragen. Durch das Üben dieser Beispiele werden die Schüler in der Lage sein, effektiv
mit Daten in SQLite zu arbeiten und die vielfältigen Möglichkeiten von SQL-Abfragen zu erkunden.

## Löschen und Ändern von Daten

Nachdem wir uns mit dem Einfügen und Abfragen von Daten vertraut gemacht haben, ist es wichtig, zu lernen, wie man Daten
aktualisiert und löscht. In diesem Abschnitt konzentrieren wir uns auf die `UPDATE`- und `DELETE`-Befehle in SQLite.
Diese Befehle ermöglichen es uns, vorhandene Daten zu modifizieren oder zu entfernen, was besonders nützlich ist, wenn
Daten korrigiert oder nicht mehr benötigte Informationen entfernt werden müssen.

### Verwendung des UPDATE-Befehls

Der `UPDATE`-Befehl wird verwendet, um vorhandene Daten in einer Tabelle zu ändern. Hier sind einige Beispiele:

**Aktualisieren eines einzelnen Datensatzes**:
```sql
UPDATE mitarbeiter SET gehalt = 3500 WHERE id = 1;
```

**Aktualisieren mehrerer Datensätze**:
```sql
UPDATE mitarbeiter SET abteilung = 'Marketing' WHERE alter > 40;
```

**Kombination von Bedingungen**:
```sql
UPDATE mitarbeiter SET gehalt = gehalt + 500 WHERE abteilung = 'IT' AND gehalt < 4000;
```

**Aktualisieren unter Verwendung von OR**:
```sql
UPDATE mitarbeiter SET hat_fuehrerschein = TRUE WHERE name = 'Max Mustermann' OR name = 'Maria Musterfrau';
```

**Setzen von NULL-Werten**:

**Entfernen eines Wertes (Setzen auf NULL)**:
```sql
UPDATE mitarbeiter SET gehalt = NULL WHERE id = 3;
```

**Aktualisieren mit mathematischen Operationen**:
```sql
UPDATE mitarbeiter SET alter = alter + 1 WHERE name LIKE '%Schmidt%';
```

**Aktualisieren mit Bedingungen und Sortierung**:
```sql
UPDATE mitarbeiter SET gehalt = gehalt * 1.1 WHERE abteilung = 'Vertrieb' ORDER BY eintrittsdatum LIMIT 5;
```

### Verwendung des DELETE-Befehls

Der `DELETE`-Befehl wird verwendet, um Datensätze aus einer Tabelle zu entfernen. Hier sind einige Beispiele:

**Löschen eines spezifischen Datensatzes**:
```sql
DELETE FROM mitarbeiter WHERE id = 4;
```

**Löschen mehrerer Datensätze**:
```sql
DELETE FROM mitarbeiter WHERE abteilung = 'Marketing';
```

**Löschen mit Bedingungen**:
```sql
DELETE FROM mitarbeiter WHERE gehalt < 3000 AND alter > 50;
```

**Löschen unter Verwendung von OR**:
```sql
DELETE FROM mitarbeiter WHERE name = 'Max Mustermann' OR name = 'Maria Musterfrau';
```

**Löschen von Datensätzen mit NULL-Werten**:
```sql
DELETE FROM mitarbeiter WHERE eintrittsdatum IS NULL;
```

**Löschen aller Datensätze**:
```sql
DELETE FROM mitarbeiter;
```

### Zusammenfassung

Die `UPDATE`- und `DELETE`-Befehle sind wesentliche Werkzeuge in SQLite, um Daten zu pflegen und zu verwalten. Durch das
Üben dieser Beispiele lernen die Schüler, wie man Daten effektiv aktualisiert und löscht, was für die Aufrechterhaltung
der Datenintegrität und -aktualität unerlässlich ist. Es ist wichtig, diese Befehle mit Vorsicht zu verwenden,
insbesondere den `DELETE`-Befehl, da er Daten dauerhaft entfernt.
