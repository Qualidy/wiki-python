# Spaltenorientierte Datenbanken
[20 min]

Spaltenspeicherdatenbanken speichern Daten spaltenweise anstelle von zeilenweise. In herkömmlichen Datenbanken werden Daten als zweidimensionale Tabellen aus Zeilen und Spalten dargestellt. Diese müssen jedoch in einer eindimensionalen Form auf der Festplatte und im Arbeitsspeicher des Computers gespeichert werden. Die spaltenorientierte Datenbank löst diese Herausforderung, indem sie die Daten spaltenweise abspeichert. Spaltenorientierte Systeme bieten Vorteile bei Anwendungen wie Data Warehousing, bei denen Aggregate über große Mengen ähnlicher Elemente gebildet werden. Der effiziente Zugriff auf Festplattendaten steht im Fokus von Vergleichen zwischen zeilenorientierten und spaltenorientierten Systemen. Ein Megabyte sequentiell gespeicherter Daten kann genauso lang dauern wie ein einzelner Direktzugriff.

**_Beispiel:_**

| Personalnr | Nachname | Vorname | Gehalt |
|------------|----------|---------|--------|
| 10001      | Becker   | Thomas  | 55000  |
| 10002      | Wagner   | Sabine  | 48000  |
| 10003      | Schulz   | Andreas | 60000  |

Bei einer Zeilenorientierten Speicherung werden die Daten wie folgt gespeichert:
1001, Becker, Thomas, 55000, 10002, Wagner, Sabine, 48000, 10003, Schulz, Andreas, 60000

Bei einer Spaltenorientierten Speicherung werden die Daten wie folgt gespeichert:
10001, 10002, 10003, Becker, Wagner, Schulz, Thomas, Sabine, Andreas, 55000, 48000, 60000

In der Praxis eignen sich zeilenorientierte Architekturen gut für typische OLTP-Aufgaben (z.B. Buchhaltungssysteme) mit vielen interaktiven Transaktionen, während spaltenorientierte Systeme für OLAP-Aufgaben (z.B. analytische Informationssysteme) mit komplexen Abfragen über alle Datensätze geeignet sind.

Beispiele für bekannte Spaltenspeicherdatenbanken sind Cassandra, HBase und Vertica.

## Exkurs: OLTP und OLAP

### OLTP (Online Transaction Processing)

OLTP steht für "Online Transaction Processing" und beschreibt Systeme, die darauf ausgerichtet sind, Transaktionen in Echtzeit zu verarbeiten. Diese Transaktionen sind typischerweise alltägliche Geschäftsaktivitäten wie das Hinzufügen von Datensätzen, das Aktualisieren von Informationen oder das Durchführen von Abfragen. OLTP-Systeme sind darauf optimiert, schnelle und effiziente Einzeltransaktionen zu unterstützen und bieten eine hohe Datensicherheit.

### OLAP (Online Analytical Processing)

OLAP steht für "Online Analytical Processing" und bezieht sich auf Systeme, die auf die Analyse großer Mengen von Daten ausgerichtet sind. Diese Systeme ermöglichen komplexe Abfragen und Auswertungen, um geschäftliche Entscheidungen zu unterstützen. OLAP-Systeme organisieren Daten in mehrdimensionalen Modellen, um es Benutzern zu ermöglichen, Daten aus verschiedenen Perspektiven zu betrachten. Im Gegensatz zu OLTP-Systemen liegt der Schwerpunkt bei OLAP auf aggregierten und historischen Daten.

## Unterschiede zwischen OLTP und OLAP

| Merkmal          | OLTP                                            | OLAP                                           |
|------------------|-------------------------------------------------|------------------------------------------------|
| Hauptziel        | Verarbeitung von Einzeltransaktionen            | Analyse großer Datenmengen                     |
| Art der Abfragen | Einfache Abfragen auf Einzeldatensätzen         | Komplexe Abfragen und Analyse von Aggregaten   |
| Datenmodell      | Normalisierte Datenmodelle                      | Denormalisierte oder stark strukturierte Daten |
| Antwortzeit      | Niedrige Antwortzeit für einzelne Transaktionen | Akzeptable Antwortzeit für komplexe Abfragen   |
| Datenvolumen     | Geringes bis mittleres Datenvolumen             | Großes Datenvolumen                            |
| Datenaktualität  | Echtzeitaktualität der Daten                    | Aktualität kann etwas verzögert sein           |
| Benutzer         | Alltägliche Benutzer (Clerks, Kunden)           | Entscheidungsträger und Analysten              |
| Beispiele        | Point-of-Sale-System, Buchungssysteme           | Business Intelligence-Systeme, Data Warehouses |