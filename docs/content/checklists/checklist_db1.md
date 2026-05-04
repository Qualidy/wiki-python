# Lernziele SQL Datenbanken

# Einführung in SQL

- Ich weiß, dass Daten in Tabellen in Datenbanken gespeichert werden können.
- Ich weiß, das SQL eine Sprache ist, mit der man Datenbanken bedienen kann.

# Arbeitsumgebung einrichten

- Ich kann über SQLite3 auf eine Datenbank zugreifen, erstellen und Befehle eingeben.
- Ich kann SQLite3 sowohl über meine IDE als auch über die Konsole bedienen.

# Tabellen

- Ich weiß, wie ich Tabellen anlege, mit Inhalten fülle, sie manipuliere oder lösche.
- Ich kann Tabellen löschen.
- Ich kann eine Datenbankdatei mit SQLite öffnen.
- Ich weiß, dass es reservierte Worte gibt, die nicht für die Namensgebung verwendet werden sollten.

# Arbeiten mit Daten

- Ich kenne die CRUD Operationen, die auf Datenbanken angewendet werden können
- Ich kann entsprechende Befehle verfassen
- Ich kann in diesen Befehlen eingebaute Funktionen oder Aggregatefunktionen einsetzen
- Ich kann Daten durch den Einsatz von
    - WHERE filtern,
    - mittels ORDER BY und ASC/DESC aufsteigend oder absteigend sortieren,
    - mittels GROUP BY gruppieren

# Aliase

- Ich weiß, was Aliase sind und wie man sie einsetzt
- Ich kann in einem Skript Aliase erkennen

# Relationale Datenbanken

- Ich verstehe die Struktur relationaler Datenbanken, einschließlich der Rollen von Tabellen, Spalten und Zeilen.
- Ich kann die Bedeutung und den Zweck von Primär- und Fremdschlüsseln erklären.
- Ich erkenne die Wichtigkeit relationaler Datenbanken für die Organisation und Verwaltung von Daten.

# Einführung in SQL

- Ich kann einfache SQL-Befehle wie `SELECT`, `INSERT`, `UPDATE`, und `DELETE` ausführen.
- Ich verstehe die Bedeutung von SQL als Werkzeug zur Interaktion mit relationalen Datenbanken.
- Ich bin fähig, grundlegende Abfragen zu formulieren, um spezifische Datenanforderungen zu erfüllen.

# Erstellung und Design von Datenbanktabellen

- Ich weiß, wie man Tabellen erstellt und strukturiert, um Datenlagerung zu ermöglichen.
- Ich kann geeignete Datentypen für Tabellenspalten basierend auf den Datenanforderungen auswählen.
- Ich verstehe, wie die Wahl der Datentypen die Integrität und die Leistung der Datenbank beeinflusst.

# Datenmanipulation und -abfrage

- Ich bin in der Lage, Daten effektiv in Datenbanktabellen einzufügen, zu aktualisieren und zu löschen.
- Ich kann Daten mit Bedingungen filtern und sortieren, um relevante Informationen abzurufen.
- Ich verstehe, wie man Abfragen entwickelt, um spezifische Datenbedürfnisse zu erfüllen.

# Einsatz von Aggregatfunktionen

- Ich kann Aggregatfunktionen wie `COUNT`, `SUM`, `AVG`, `MAX`, und `MIN` anwenden, um Datenanalysen durchzuführen.
- Ich verstehe, wie man diese Funktionen nutzt, um zusammengefasste Informationen aus großen Datensätzen zu extrahieren.
- Ich erkenne den Wert von Aggregatfunktionen bei der Unterstützung von Entscheidungsfindungsprozessen.

# Verständnis und Anwendung von JOINs

- Ich kann unterschiedliche JOIN-Typen erklären und anwenden, um Daten aus mehreren Tabellen zu verknüpfen.
- Ich weiß, wie man INNER JOIN und LEFT JOIN verwendet, um relevante Datenbeziehungen darzustellen.
- Ich erkenne die Bedeutung von JOINs für die Erstellung umfassender Datensätze aus relationalen Datenbanken.

# Datenbanktransaktionen

- Ich habe ein grundlegendes Verständnis von der Rolle und Wichtigkeit von Datenbanktransaktionen.
- Ich kann erklären, wie Transaktionen die Datenintegrität und -konsistenz gewährleisten.
- Ich verstehe die Konzepte der Transaktionssteuerung, einschließlich Commit und Rollback.

# Datenbank Views

- Ich weiß, wie man Views erstellt, um komplexere Abfragen effizient zu verwalten und zu vereinfachen.
- Ich kann die Vorteile der Verwendung von Views für die Datenabstraktion und Sicherheit erklären.
- Ich verstehe, wie Views die Wiederverwendung von SQL-Abfragen fördern und die Komplexität reduzieren.

# Index, Indizes (eng. index, indexes)

- Ich verstehe die Notwendigkeit von Indizes in relationalen Datenbanken zur Beschleunigung des Datenzugriffs.
- Ich kann einfache und zusammengesetzte Indizes in SQLite erstellen, um die Abfrageleistung zu verbessern.
- Ich weiß, wie Indizes die Datenbankabfragen beeinflussen und kann `EXPLAIN QUERY PLAN` verwenden, um die Abfrageausführung zu analysieren.
- Ich verstehe den grundlegenden Aufbau und die Funktionsweise von B-Bäumen als Grundlage für die Implementierung von Indizes in relationalen Datenbanksystemen.

# Schlüssel (eng. Key)

- Ich verstehe die Rolle von Primär- und Fremdschlüsseln in relationalen Datenbanken zur Sicherstellung der Datenintegrität und zum Aufbau von Beziehungen zwischen Tabellen.
- Ich kann in SQL Tabellen mit Primär- und Fremdschlüsseln erstellen, um komplexe Datenstrukturen und Beziehungen effektiv zu modellieren.
- Ich erkenne, wie Primär- und Fremdschlüssel die Datenkonsistenz innerhalb der Datenbank durch referentielle Integrität gewährleisten.
- Ich bin in der Lage, die Beziehungen zwischen Daten in verschiedenen Tabellen durch den Einsatz von Fremdschlüsseln zu verstehen und zu navigieren.

# Normalisierung von Daten

- Ich weiß, warum Daten für die Verwendung in relationalen Datenbanken normalisiert werden müssen
- Ich kenne Ausnahmen zu dieser Regel
- Ich kann Daten in Tabellen ordnen, sodass diese der 1.NF, 2.NF oder 3.NF entsprechen
- Ich weiß, dass die inneren Zusammenhänge dieser Daten durch referentielle Integrität abgesichert wird

# Batch, Script, Deploy

- Ich kann SQLite Kommandos in einer Datei zusammenfassen.
- Ich weiß, dass das Ausführen aufeinander folgender Kommandos batch genannt wird, die Datei script
- Ich kann erklären, was Transaktionen sind
- Ich kann ein batch oder ein script mit Transaktionen gegen Fehler absichern
- Ich weiß, dass komplexe Fälle mit anderen Sprachen (z.B. python) verarbeitet werden müssen.
- Ich weiß, wie ich, im Falle von SQLite, eine Datenbank verteilen kann.

# Unterabfragen und Common Table Expressions

- Ich kann eine Abfrage als Unterabfrage in SELECT, INSERT oder UPDATE Kommandos erstellen.
- Ich verstehe die allgemeine Form der Common Table Expression und deren Bedeutung
- Ich kann einfache Unterabfragen in CTE umschreiben

# UML-Diagramme

- Ich verstehe, was UML-Diagramme sind,
- was sie in Bezug auf Datenbanken ausdrücken und
- welche Bedeutung die Zeichen in diesen Diagrammen haben (Bezug Mermaid / Markdown)
- Ich kann die normalsprachlichen Formulierungen eines Datenbankproblems in UML-Diagramme umsetzen
- Ich kann die UML_Diagramme in die Tabellenstruktur einer Datenbank überführen