# Exkurs: SQL Scripte erstellen

Das Hauptziel von Scripten ist es, die Effizienz bei wiederkehrenden Datenbankabfragen durch die Automatisierung von SQL-Kommandos zu steigern.

Hierzu erstellen wir zunächst **eine einfache Textdatei mit SQL-Befehlen**, benannt als `myScript.sql`. Diese enthält Anweisungen, die in einer SQLite-Datenbankumgebung ausgeführt werden sollen, beispielsweise zum Öffnen einer Datenbank und zum Auslesen der Skriptdatei.

In unserem Fall enthält die Datei also die Query von zuvor:

```sql
SELECT DISTINCT City
FROM SampleCustomers
ORDER BY City ASC
LIMIT (SELECT count(DISTINCT City) / 2 AS Arbeitsaufwand FROM SampleCustomers);

SELECT DISTINCT City
FROM SampleCustomers
ORDER BY City DESC
LIMIT (SELECT count(DISTINCT City) / 2 AS Arbeitsaufwand FROM SampleCustomers);
```

## Aufgaben

### Aufgabe: Script erstellen und ausführen 🌶️🌶️

Erstelle eine einfache Textdatei mit dem Namen `myScript.sql`.
Setze die beiden Kommandos ein und speichere sie ab.

In der Kommandozeile führst du aus:

```bash
sqlite3

.open test_datenbank.db
.read myScript.sql
.quit
```

Die beiden Listen sollten noch in der Kommandozeile verfügbar sein.

## Script Ausführen

Die Übungen zeigen, wie vielfältig Datenbankabfragen sein können.
Wir werden gleich mit weiteren Beispielen das Wissen darüber vertiefen.

Die Speicherung der Abfragen (nicht der Ergebnisse) in Dateien ermöglicht es, wie auch in anderen Programmiersprachen,
eine Programmierung vorzunehmen. Das Programm kann dann in einem Rutsch immer wieder ausgeführt werden.
Dies gilt natürlich für alle Sprachtypen. So kann man ein Script schreiben, das die vollständige
Struktur der Datenbank beschreibt. Also alle Tabellendefinitionen enthält.
Damit kann man getrennt von dem Datenbankprogramm die Struktur entwickeln und getrennt testen.

Was wir gerade entwickelt haben, war ein Skript zur komplexen Datenbankabfrage.

Doch nun zurück zu den Sprachelementen.

### Einfaches CTE

CTE ist in der Datenbankwelt ein feststehender Begriff.

**C**ommon **T**able **E**xpresion

Auf deutsch könnte man das als `gemeinsamer Tabellenausdruck` übersetzen.

Verwenden wir unser letztes Beispiel, um die Anwendung von CTEs zu verdeutlichen.

```sql
SELECT DISTINCT City
FROM SampleCustomers
ORDER BY City ASC
LIMIT (SELECT count(DISTINCT City) / 2 AS Arbeitsaufwand FROM SampleCustomers);
```

Der Wert, der hier als Parameter für `LIMIT` benötigt wird, wird aus einem anderen SQL Statement berechnet. Dies Technik bezeichnet man als `Unterabfrage`. Wie wir in späteren Beispielen sehen werden, können auch Listen zurückgegeben werden.

#### Definition

`Unterabfrage` ist ein SQL Ausdruck, der Daten für einen anderen SQL Ausdruck bereitstellt.

Einen solchen Unterausdruck kann man herauslösen und in einer CTE darstellen. Hier die Darstellung mit CTE für unser Beispiel:

```sql
WITH numberOfRows AS (SELECT count(DISTINCT City) / 2 as numberOfRowsToShow FROM SampleCustomers)

SELECT DISTINCT City
FROM SampleCustomers
ORDER BY City ASC
LIMIT numberOfRows.numberOfRowsToShow;
```

**Die Zeile `WITH ... SampleCustomers)` ist ein CTE.**

Der `WITH` Befehl erstellt eine temporäre Tabelle, die nur für die Zeit der Ausführung
des gesamten Ausdrucks besteht. Ein darauf folgendes `SELECT` würde `numberOfRows` nicht mehr kennen.

Der Vorteil dieser Art der Programmierung liegt darin, dass das CTE auch komplexer sein kann.
Man verliert aber nicht die Übersicht. Zudem kann man `sprechende` Namen verwenden, um für mehr
Klarheit zu sorgen.

Der Verweis auf die zu verwendende Spalte wird in der Punkt-Notation geschrieben: `[Tabellenname].[Spaltenname]`.
In diesem Fall also die CTE, die eine temporäre Tabelle `numberOfRows` mit der einzigen Spalte `numberOfRowsToShow` erstellt.

Bevor wir an dieser Stelle weiter machen können, müssen wir andere Funktionen kennenlernen.

Erinnern wir uns an unsere letzten Aufgaben.

**Wie viele Menschen sind in jeder Stadt gemeldet?**

Eine Tabelle mit diesen Informationen ermöglicht uns einen Aufkleber für die Fähnchen zu machen.

Das Problem und Lösungsansätze:
Die Aufgabe stellt uns vor das Problem, dass wir für jede Stadt die Anzahl der Personen zählen müssen.
Wir haben in anderen Übungen gelernt, dass Filter `DISTINCT` uns die eindeutige Liste der Orte liefert.
Klassisch würden wir jetzt in einer Schleife die Tabelle wieder und wieder nach jeder Stadt filtern (`WHERE City = x`).
Dann könnte man für jedes Ergebnis mit `COUNT` die Anzahl herausfinden.

Anders gesagt: Wir haben eine Liste der eindeutigen Orte. Dort fügen wir eine Spalte `Einwohner` hinzu.
Jetzt gehen wir Schritt
für Schritt durch diese Liste und führen `SELECT count(*) FROM sampleCustomers WHERE City = ?;` aus, wobei das
Fragezeichen für die aktuelle Stadt steht. Das Ergebnis schreiben wir mit `UPDATE cityPopulation SET Einwohner = ?`.
Sind wir am Ende angekommen, so geben wir die Liste aus.

Natürlich können wir kombinieren:
```sql
CREATE TABLE cityPopulation
(
    stadt,
    einwohner
);

INSERT INTO cityPopulation (stadt)
SELECT DISTINCT city
FROM sampleCustomers
ORDER BY city ASC;

UPDATE cityPopulation
SET einwohner = (select count(*) FROM sampleCustomers WHERE sampleCustomers.city = cityPopulation.stadt);

SELECT *
FROM cityPopulation;
```

**Anmerkung:**
Man erkennt, dass keine Schleife konstruiert wird, wie in anderen Sprachen üblich.
In SQL zu denken fordert, in Tabellen zu denken. Die Schleife wird hier implizit aus `UPDATE` und `SELECT`gebildet.

⚠️ Den obigen Befehlt auszuführen kann relativ lange dauern. Nicht wundern.

## Aufgabe: Gruppieren 🌶️🌶️

Erstelle ine Query dafür, wie viele Menschen in jeder Stadt gemeldet sind.

<details><summary>🍀 Tipps</summary>
Mach dich schlau über den Befehl 'GROUP BY'.
</details>

<details><summary>Lösung</summary>
<pre><code>SELECT city AS Stadt, count(City) AS Einwohner FROM SampleCustomers GROUP BY City;
</code></pre>
</details>

In diesem Beispiel wollen wir einerseits die Stadt und andererseits die Anzahl der Einwohne wissen.

Dazu definieren wir die beiden Spalten `city` und `count(city)`. Beiden Spalten geben wir einen Alias, damit
das Ergebnis verständlich und auf deutsch ist.

Das `GROUP BY` sorgt dafür, dass `count` sich auf die jeweilige Gruppe bezieht. Es verwirklicht in etwa unsere erste
Idee, alle Einwohner einer Stadt zu zählen und dann das Ergebnis als Liste anzuzeigen. Im Gegensatz zu unserer Lösung ist
das Ergebnis nicht persistent. Es steht nämlich nicht in einer Tabelle (`cityPopulation`).

# Komplex Aufgaben

## Aufgabe: Ja, aber ... 🌶️🌶️🌶️

... ich wollte doch nur die Städte mit mehr als 35 Einwohnern.

<details><summary>🍀 Tipps</summary>
Mach dich schlau über den Befehl 'HAVING'.
</details>

<details><summary>Lösung</summary>
<pre><code>select city as Stadt, count(City) as Einwohner 
from SampleCustomers 
GROUP BY City
HAVING count(city) > 35;
</code></pre>

Alternative Lösungen wären auch:

mit Unterabfrage:
<pre><code>
SELECT Stadt, Einwohner
FROM (
    SELECT city AS Stadt, COUNT(*) AS Einwohner
    FROM SampleCustomers
    GROUP BY city
) AS subquery
WHERE Einwohner > 35;
</code></pre>

mit CTE:
<pre><code>
WITH CityCounts AS (
    SELECT city AS Stadt, COUNT(*) AS Einwohner
    FROM SampleCustomers
    GROUP BY city
)
SELECT Stadt, Einwohner
FROM CityCounts
WHERE Einwohner > 35;
</code></pre>

mit Bezug auf bestehende Tabellen:
<pre><code>
SELECT Stadt, Einwohner
FROM cityPopulation
WHERE Einwohner > 35;
</code></pre>

Alle Lösungen erzeugen das gleiche Ergebnis. Jedoch ist die Benutzung von `HAVING` kürzer formuliert und das 
Datenbankprogramm kann möglicherweise besser optimieren. Nur die Lösung mit einer vorgefertigten Tabelle ist 
kürzer. Die vorgefertigte Tabelle wird in den anderen Lösungen als temporäre Tabelle oder Unterabfrage ebenfalls
erstellt.

Grundsätzlich sollte man die vorgefertigten Sprachelemente nutzen. Sie sind für den beabsichtigten Zweck hin optimiert und erprobt.

</details>

## Aufgabe: Statistik 🌶️🌶️🌶️

Für Aufträge in denen statistische Daten gebraucht werden, gibt es `Aggregate-Funktionen`.
Eine davon ist `Count`, die wir schon kennengelernt haben. Andere sind `AVG`, `MIN` und `MAX`.
Entwickle Abfragen, die diese Funktionen einsetzen.

<details><summary>Lösung</summary>
<pre><code>
SELECT Stadt AS Kleinste_Stadt, MIN(Einwohner) FROM cityPopulation;

SELECT Stadt AS Kleinste_Stadt, MAX(Einwohner) FROM cityPopulation;

SELECT AVG(Einwohner) Durchschnittliche_Einwohnerzahl FROM cityPopulation;
</code></pre>

Da wir die kleinste und die größte aller Städte herausfinden wollen, nutzen wir das bereits bestehende Ergebnis in der 
Tabelle `cityPopulation`. Natürlich könnten wir diese Tabelle durch eine Unterabfrage oder ein CTE 'on-the-fly' erstellen.
Hier zeigt sich ein Vorteil von Vorberechnungen. 

Bei der Funktion `AVG` fällt natürlich der Stadtname weg. Das Ergebnis ist ja ein Mittelwert ohne Bezug zu einer 
bestimmten Stadt.

</details>

## Aufgabe: Fallunterscheidung in Spalten 🌶️🌶️🌶️🌶️

Es gibt strategische Überlegungen unterschiedliche Werbekampagnen alters angepasst zu entwickeln.
Die Geburtstage der Menschen sind in unsere Tabelle enthalten. 
Wir wollen jetzt eine Einteilung in drei Altersgruppen vornehmen.

1. jünger als 30 Jahre werden in der Spalte als 'jung',
2. zwischen 30 und 60 Jahre werden in der Spalte als 'mittel' und 
3. über 60 Jahre alte Menschen werden in der Spalte als 'senior' markiert.

Lies im Internet über die `CASE` Anweisung nach.

<details><summary>Lösung</summary>
<pre><code>
SELECT
    GivenName || ' ' || FamilyName AS Name,
    BirthDate,
    CASE
        WHEN ((strftime('%Y', 'now') - strftime('%Y', BirthDate)) < 30) THEN 'Jung'
        WHEN ((strftime('%Y', 'now') - strftime('%Y', BirthDate)) >= 30 AND
              (strftime('%Y', 'now') - strftime('%Y', BirthDate)) < 60) THEN 'Mittel'
        ELSE 'Senior'
    END AS Altersgruppe
FROM
    SampleCustomers;
</code></pre>

In dieser Codesequenz wird die Funktion `strftime` verwendet. Dies ist eine Sqlite eigene Funktion zur 
Bearbeitung von Datum-Zeit-Werten. Schlage dazu in der Dokumentation nach, welche Möglichkeiten die Funktion bietet.
Hier wird vom Datum nur das Jahr '%Y' berücksichtigt, um die Unterscheidung vorzunehmen. Der Parameter 'now' bewirkt 
die Verwendung des aktuellen Datum-Zeit-Wertes.
Die Funktion ist in dieser Form nicht besonders genau.
Diese Lösung bietet eine gute Grundlage, um für weitere Arbeiten zu dienen.
Daher wollen wir diese Daten speichern.

</details>

## Aufgabe: genaues Alter 🌶️🌶️🌶️🌶️

Entwickle eine Lösung, die das exakte Alter des Menschen berechnet.

<details><summary>Lösung</summary>
<pre><code>
SELECT 
    GivenName || ' ' || FamilyName AS FullName, 
    BirthDate, 
    (
        strftime('%Y', 'now') - strftime('%Y', BirthDate)
    ) - (
        strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate)
    ) AS ExactAge
FROM 
    SampleCustomers;
</code></pre>

Erläutere die Funktionsweise deines Statements. Erkläre die Lösung.
Modifiziere die Lösung so, dass die `CASE` Anweisung wieder zum Einsatz kommt.

Sqlite kennt keine frei definierbaren Funktionen, wie man das aus anderen Sprachen kennt. Daher ist die vollständige Lösung etwas umständlich.

</details>

<details><summary>Lösung</summary>
<pre><code>
SELECT
    GivenName || ' ' || FamilyName AS Name,
    BirthDate,
    CASE
        WHEN (
            (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate)) 
        ) < 30) THEN 'Jung'
        WHEN (
            (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate))
        ) >= 30 
        AND (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate))
        ) < 60) THEN 'Mittel'
        ELSE 'Senior'
    END AS Altersgruppe
FROM
    SampleCustomers;
</code></pre>
</details>

## Aufgabe: Wiederholung 🌶️🌶️🌶️

Erstelle eine Tabelle, die das Ergebnis der Altersgruppierung aufnehmen kann und füge die Daten ein.
Ziehe dazu die vorherigen Lösungen zurate.

<details><summary>ungefähre Lösung</summary>
<pre><code>
CRAETE TABLE Altersgruppen (
    Name,
    BirthDate,
    Altersgruppe
);

INSERT INTO Altersgruppen (Name, BirthDate, Altersgruppe) 
SELECT
    GivenName || ' ' || FamilyName AS Name,
    BirthDate,
    CASE
        WHEN ((strftime('%Y', 'now') - strftime('%Y', BirthDate)) < 30) THEN 'Jung'
        WHEN ((strftime('%Y', 'now') - strftime('%Y', BirthDate)) >= 30 AND
              (strftime('%Y', 'now') - strftime('%Y', BirthDate)) < 60) THEN 'Mittel'
        ELSE 'Senior'
    END AS Altersgruppe
FROM
    SampleCustomers;
</code></pre>

</details><details><summary>exakte Lösung</summary>
<pre><code>
CRAETE TABLE Altersgruppen (
    Name,
    BirthDate,
    Altersgruppe
);

INSERT INTO Altersgruppen (Name, BirthDate, Altersgruppe) 
SELECT
    GivenName || ' ' || FamilyName AS Name,
    BirthDate,
    CASE
        WHEN (
            (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate)) 
        ) < 30) THEN 'Jung'
        WHEN (
            (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate))
        ) >= 30 
        AND (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate))
        ) < 60) THEN 'Mittel'
        ELSE 'Senior'
    END AS Altersgruppe
FROM
    SampleCustomers;
</code></pre>
</details>

## Aufgabe: Werbe E-Mail schicken 🌶️🌶️🌶️🌶️

Die Werbekampagnen sollen per email durchgeführt werden.
Verändere das Skript so, dass die E-Mail Adressen in der Tabelle 'Altersgruppen' gelistet sind.

<details><summary>exakte Lösung</summary>
<pre><code>
DROP TABLE Altersgruppen;

CRAETE TABLE Altersgruppen (
    Name,
    BirthDate,
    Altersgruppe,
    Email
);

INSERT INTO Altersgruppen (Name, BirthDate, Altersgruppe) 
SELECT
    GivenName || ' ' || FamilyName AS Name,
    BirthDate,
    CASE
        WHEN (
            (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate)) 
        ) < 30) THEN 'Jung'
        WHEN (
            (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate))
        ) >= 30 
        AND (strftime('%Y', 'now') - strftime('%Y', BirthDate)) - 
            (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate))
        ) < 60) THEN 'Mittel'
        ELSE 'Senior'
    END AS Altersgruppe,
    EMail
FROM
    SampleCustomers;
</code></pre>

Nun können die E-Mail verschickt werden.

Schreibe die Statements zur Auswahl der EMail und des Namens nach Altersgruppe sortiert nach Name.

</details>

<details>
<summary>Lösung:
</summary>
<pre><code>
select Name, Email from Altersgruppen where Altersgruppe = 'Jung' order by Name;
select Name, Email from Altersgruppen where Altersgruppe = 'Mittel' order by Name;
select Name, Email from Altersgruppen where Altersgruppe = 'Senior' order by Name;
</code></pre>
</details>