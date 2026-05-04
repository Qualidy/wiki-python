# Verschachtelte Abfragen

## Unterabfragen in SQLite

Unterabfragen, auch Subqueries genannt, sind SQL-Abfragen, die innerhalb einer anderen SQL-Abfrage verwendet werden. Sie
ermöglichen es, komplexe Abfragen zu erstellen, indem man die Ergebnisse einer Abfrage als Eingabe für eine andere
verwendet. Unterabfragen können in verschiedenen Teilen einer SQL-Abfrage eingesetzt werden, wie in der `SELECT`, `FROM`
oder `WHERE`-Klausel.

### Beispiele für Unterabfragen

**Unterabfrage in der WHERE-Klausel**:
```sql
SELECT * FROM mitarbeiter 
WHERE gehalt > (SELECT AVG(gehalt) FROM mitarbeiter);
```
Diese Abfrage wählt alle Mitarbeiter aus, deren Gehalt über dem Durchschnittsgehalt liegt.

**Unterabfrage in der FROM-Klausel**:
```sql
SELECT AVG(gehalt) 
FROM (SELECT * FROM mitarbeiter WHERE abteilung = 'IT');
```
Hier wird das durchschnittliche Gehalt der Mitarbeiter in der IT-Abteilung berechnet.

**Unterabfrage in der SELECT-Klausel**:
```sql
SELECT name, 
       (SELECT COUNT(*) FROM mitarbeiter WHERE abteilung = m.abteilung) AS Abteilungsgröße 
FROM mitarbeiter m;
```
Diese Abfrage zeigt den Namen jedes Mitarbeiters zusammen mit der Anzahl der Mitarbeiter in ihrer Abteilung.

## Vertiefung: Common Table Expressions (CTEs) in SQLite

CTEs bieten eine alternative Methode zur Strukturierung von Abfragen, die Unterabfragen ersetzen oder ergänzen können.
Eine CTE ist im Wesentlichen eine temporäre Ergebnismenge, die innerhalb einer SQL-Abfrage definiert und wie eine
Tabelle verwendet wird. CTEs werden oft für die bessere Lesbarkeit und Organisation von komplexen Abfragen verwendet.

### Beispiele für CTEs

**Einfache CTE**:
```sql
WITH Durchschnittsgehalt AS (
    SELECT AVG(gehalt) AS avg_gehalt FROM mitarbeiter
)
SELECT * FROM mitarbeiter 
WHERE gehalt > (SELECT avg_gehalt FROM Durchschnittsgehalt);
```
Diese CTE berechnet das Durchschnittsgehalt und verwendet es in der Hauptabfrage.

**Mehrere CTEs in einem WITH-Statement**:
```sql
WITH IT_Mitarbeiter AS (
    SELECT * FROM mitarbeiter WHERE abteilung = 'IT'
),
Marketing_Mitarbeiter AS (
    SELECT * FROM mitarbeiter WHERE abteilung = 'Marketing'
)
SELECT * FROM IT_Mitarbeiter
UNION ALL
SELECT * FROM Marketing_Mitarbeiter;
```
Hier werden zwei CTEs definiert, eine für IT-Mitarbeiter und eine für Marketing-Mitarbeiter, und dann
zusammengeführt.

### CTEs als Ersatz für Unterabfragen

CTEs können oft anstelle von Unterabfragen verwendet werden, um die Lesbarkeit und Struktur der SQL-Abfragen zu
verbessern. Insbesondere bei komplexen Abfragen, bei denen dieselbe Unterabfrage mehrfach verwendet wird, können CTEs
die Abfrage effizienter und verständlicher machen.

### Zusammenfassung

Sowohl Unterabfragen als auch CTEs sind mächtige Werkzeuge in SQL, die es ermöglichen, komplexe Abfragen auf eine
strukturierte und effiziente Weise zu erstellen. Während Unterabfragen direkt in die Hauptabfrage eingebettet werden,
bieten CTEs eine klarere Trennung und Strukturierung, insbesondere bei der Verwendung mehrerer temporärer Tabellen.
Durch das Üben dieser Beispiele können die Schüler lernen, wie man beide Techniken effektiv einsetzt.
