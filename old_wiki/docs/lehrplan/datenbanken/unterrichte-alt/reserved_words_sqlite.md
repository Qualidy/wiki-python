# Reservierte Ausdrücke in SQLITE

[10min]

Liste von reservierten Wörtern. Diese Wörter haben eine spezielle Bedeutung in SQL und sollten daher
nicht als Namen für Tabellen, Spalten oder andere Datenbankobjekte verwendet werden, es sei denn, sie sind in
Anführungszeichen eingeschlossen.

Hier ist eine vollständige Liste der reservierten Wörter in SQLite:

| Keyword           | Bedeutung                                                                                  |
|:------------------|:-------------------------------------------------------------------------------------------|
| ABORT             | Bricht eine Transaktion ab, ohne Änderungen zu speichern.                                  |
| ACTION            | Spezifiziert die Aktion in Trigger oder Fremdschlüssel-Beziehungen.                        |
| ADD               | Fügt einer bestehenden Tabelle eine neue Spalte hinzu.                                     |
| AFTER             | Definiert einen Trigger, der nach einem Ereignis (z.B. INSERT) ausgeführt wird.            |
| ALL               | Wählt alle Datensätze aus, oft verwendet mit SELECT.                                       |
| ALTER             | Ändert die Struktur einer bestehenden Tabelle (z.B. Umbenennen).                           |
| ANALYZE           | Sammelt statistische Daten über die Datenbank zur Optimierung von Abfragen.                |
| AND               | Kombiniert zwei Bedingungen logisch (beide müssen wahr sein).                              |
| AS                | Erstellt einen Alias für eine Spalte oder Tabelle in Abfragen.                             |
| ASC               | Sortiert die Ergebnisse einer Abfrage in aufsteigender Reihenfolge.                        |
| ATTACH            | Hängt eine externe Datenbank an die aktuelle Sitzung an.                                   |
| AUTOINCREMENT     | Erhöht den Wert eines Primärschlüssels automatisch bei jedem neuen Eintrag.                |
| BEFORE            | Definiert einen Trigger, der vor einem Ereignis (z.B. UPDATE) ausgeführt wird.             |
| BEGIN             | Markiert den Beginn einer Transaktion.                                                     |
| BETWEEN           | Wählt Werte innerhalb eines bestimmten Bereichs aus (inklusive Grenzen).                   |
| BY                | Gibt die Sortier- oder Gruppierungsreihenfolge in Abfragen an.                             |
| CASCADE           | Bei Lösch-/Update-Vorgängen werden Änderungen auf verknüpfte Tabellen übertragen.          |
| CASE              | Ermöglicht bedingte Ausdrücke in SQL-Abfragen.                                             |
| CAST              | Konvertiert einen Wert explizit in einen anderen Datentyp.                                 |
| CHECK             | Definiert eine Bedingung, die für die Werte in einer Spalte gelten muss.                   |
| COLLATE           | Legt eine spezifische Sortierreihenfolge für eine Spalte fest.                             |
| COLUMN            | Bezieht sich auf eine Spalte in einer Tabelle.                                             |
| COMMIT            | Schließt eine Transaktion ab und speichert alle Änderungen.                                |
| CONFLICT          | Gibt an, wie Konflikte bei UNIQUE, NOT NULL oder FOREIGN KEY behandelt werden.             |
| CONSTRAINT        | Definiert eine Einschränkung (z.B. PRIMARY KEY, FOREIGN KEY) für eine Tabelle.             |
| CREATE            | Erstellt ein neues Datenbankobjekt (z.B. Tabelle, Index, View).                            |
| CROSS             | Spezifiziert einen Cross Join, der alle Kombinationen von Zeilen aus zwei Tabellen bildet. |
| CURRENT_DATE      | Gibt das aktuelle Datum zurück.                                                            |
| CURRENT_TIME      | Gibt die aktuelle Uhrzeit zurück.                                                          |
| CURRENT_TIMESTAMP | Gibt das aktuelle Datum und die Uhrzeit zurück.                                            |
| DATABASE          | Bezieht sich auf eine Datenbank in Anweisungen wie ATTACH.                                 |
| DEFAULT           | Gibt einen Standardwert für eine Spalte an.                                                |
| DEFERRABLE        | Legt fest, ob und wann eine Einschränkung überprüft wird (sofort oder verzögert).          |
| DEFERRED          | Verzögert die Überprüfung von Einschränkungen bis zum Ende einer Transaktion.              |
| DELETE            | Löscht Datensätze aus einer Tabelle.                                                       |
| DESC              | Sortiert die Ergebnisse einer Abfrage in absteigender Reihenfolge.                         |
| DETACH            | Löst eine angehängte externe Datenbank von der aktuellen Sitzung.                          |
| DISTINCT          | Wählt nur eindeutige Datensätze aus einer Tabelle aus.                                     |
| DROP              | Löscht ein bestehendes Datenbankobjekt (z.B. eine Tabelle oder einen Index).               |
| EACH              | Wird in Triggern verwendet, um für jeden betroffenen Datensatz auszulösen.                 |
| ELSE              | Teil einer CASE-Anweisung, definiert eine Aktion, wenn keine Bedingung zutrifft.           |
| END               | Markiert das Ende eines Programmblocks (z.B. einer Transaktion).                           |
| ESCAPE            | Gibt ein Escape-Zeichen in LIKE-Abfragen an.                                               |
| EXCEPT            | Kombiniert zwei SELECT-Anweisungen und gibt nur unterschiedliche Datensätze zurück.        |
| EXCLUSIVE         | Startet eine exklusive Transaktion, die anderen Lese- und Schreibzugriffe blockiert.       |
| EXISTS            | Prüft, ob eine Subquery Ergebnisse liefert.                                                |
| EXPLAIN           | Zeigt den Abfrageplan für eine SQL-Anweisung an.                                           |
| FAIL              | Löst einen Fehler aus, wenn ein Konflikt bei einer Einschränkung auftritt.                 |
| FOR               | Definiert eine Zeitspanne für Trigger oder gibt eine Schleife in einer Anweisung an.       |
| FOREIGN           | Definiert einen Fremdschlüssel in einer Tabelle.                                           |
| FROM              | Gibt die Quelltabelle(n) in einer SELECT-Abfrage an.                                       |
| FULL              | Spezifiziert einen Full Outer Join zwischen zwei Tabellen.                                 |
| GLOB              | Führt einen musterbasierenden Vergleich durch (ähnlich wie LIKE, aber mit Glob-Mustern).   |
| GROUP             | Gruppiert Ergebnisse in einer SELECT-Abfrage basierend auf einer oder mehreren Spalten.    |
| HAVING            | Definiert eine Bedingung für Gruppen in einer GROUP BY-Abfrage.                            |
| IF                | Bedingte Anweisung in einigen SQLite-Erweiterungen.                                        |
| IGNORE            | Ignoriert den aktuellen Datensatz bei einem Konflikt (z.B. bei UNIQUE-Einschränkungen).    |
| IMMEDIATE         | Startet eine sofortige Transaktion, die andere Schreibzugriffe blockiert.                  |
| IN                | Prüft, ob ein Wert in einer Liste von Werten oder einer Subquery enthalten ist.            |
| INDEX             | Bezieht sich auf einen Index in einer Tabelle.                                             |
| INDEXED           | Gibt an, welcher Index in einer SELECT-Abfrage verwendet werden soll.                      |
| INITIALLY         | Legt fest, wann eine DEFERRABLE-Einschränkung überprüft wird (sofort oder verzögert).      |
| INNER             | Spezifiziert einen Inner Join zwischen zwei Tabellen.                                      |
| INSERT            | Fügt neue Datensätze in eine Tabelle ein.                                                  |
| INSTEAD           | Wird in INSTEAD OF-Triggern verwendet, um Standardaktionen zu ersetzen.                    |
| INTERSECT         | Kombiniert zwei SELECT-Anweisungen und gibt nur gemeinsame Datensätze zurück.              |
| INTO              | Gibt das Ziel einer INSERT- oder SELECT INTO-Anweisung an.                                 |
| IS                | Vergleicht Werte auf Gleichheit (einschließlich NULL-Werte).                               |
| ISNULL            | Prüft, ob ein Wert NULL ist.                                                               |
| JOIN              | Verknüpft zwei Tabellen basierend auf einer gemeinsamen Spalte.                            |
| KEY               | Wird oft als Synonym für PRIMARY KEY verwendet.                                            |
| LEFT              | Spezifiziert einen Left Outer Join zwischen zwei Tabellen.                                 |
| LIKE              | Führt einen musterbasierenden Vergleich durch (mit % und _ als Platzhalter).               |
| LIMIT             | Begrenzt die Anzahl der zurückgegebenen Datensätze in einer Abfrage.                       |
| MATCH             | Wird in Volltextsuchabfragen verwendet, um nach einem Textmuster zu suchen.                |
| NATURAL           | Führt einen Natural Join basierend auf gemeinsamen Spaltennamen durch.                     |
| NO                | Wird in Verbindung mit ACTION in Fremdschlüssel-Definitionen verwendet.                    |
| NOT               | Negiert eine Bedingung.                                                                    |
| NOTNULL           | Prüft, ob ein Wert nicht NULL ist.                                                         |
| NULL              | Stellt einen NULL-Wert dar.                                                                |
| OF                | Gibt das Ziel eines Triggers an (z.B. UPDATE OF column_name).                              |
| OFFSET            | Gibt den Startpunkt für das Zurückgeben von Datensätzen in einer LIMIT-Abfrage an.         |
| ON                | Definiert Bedingungen für Joins, Trigger oder Einschränkungen.                             |
| OR                | Kombiniert zwei Bedingungen logisch (mindestens eine muss wahr sein).                      |
| ORDER             | Sortiert die Ergebnisse einer SELECT-Abfrage.                                              |
| OUTER             | Wird in Verbindung mit JOIN verwendet, um Outer Joins zu spezifizieren.                    |
| PLAN              | Wird intern für den Abfrageplan verwendet.                                                 |
| PRAGMA            | Führt spezielle Operationen auf der Datenbank aus (z.B. Einstellungen ändern).             |
| PRIMARY           | Definiert den Primärschlüssel einer Tabelle.                                               |
| QUERY             | Wird nicht als reserviertes Wort in SQLite-Dokumentation aufgeführt.                       |
| RAISE             | Löst in einem Trigger eine Ausnahme aus.                                                   |
| RECURSIVE         | Ermöglicht rekursive Abfragen in Common Table Expressions (WITH).                          |
| REFERENCES        | Definiert eine Fremdschlüsselbeziehung zu einer anderen Tabelle.                           |
| REGEXP            | Führt einen regulären Ausdruck-Vergleich durch.                                            |
| REINDEX           | Erstellt einen oder mehrere Indizes neu.                                                   |
| RELEASE           | Gibt einen benannten Savepoint frei.                                                       |
| RENAME            | Benennt eine Tabelle oder Spalte um.                                                       |
| REPLACE           | Ersetzt bestehende Datensätze bei einem Konflikt (z.B. bei UNIQUE-Einschränkungen).        |
| RESTRICT          | Verhindert das Löschen/Ändern von Daten, die von Fremdschlüsseln referenziert werden.      |
| RIGHT             | Spezifiziert einen Right Outer Join zwischen zwei Tabellen.                                |
| ROLLBACK          | Macht Änderungen innerhalb einer Transaktion rückgängig.                                   |
| ROW               | Wird in Window-Funktionen verwendet, um über Zeilen zu operieren.                          |
| SAVEPOINT         | Setzt einen benannten Savepoint in einer Transaktion.                                      |
| SELECT            | Ruft Daten aus einer oder mehreren Tabellen ab.                                            |
| SET               | Weist einer Variablen einen Wert zu oder ändert Einstellungen.                             |
| TABLE             | Bezieht sich auf eine Tabelle in der Datenbank.                                            |
| TEMP              | Erstellt ein temporäres Datenbankobjekt (z.B. eine temporäre Tabelle).                     |
| TEMPORARY         | Synonym für TEMP, erstellt ein temporäres Datenbankobjekt.                                 |
| THEN              | Teil einer CASE-Anweisung, definiert eine Aktion, wenn eine Bedingung zutrifft.            |
| TO                | Wird in Bereichen oder bei der Angabe von Grenzen verwendet.                               |
| TRANSACTION       | Startet eine neue Datenbanktransaktion.                                                    |
| TRIGGER           | Definiert eine Funktion, die auf bestimmte Datenbankaktionen reagiert.                     |
| UNION             | Kombiniert die Ergebnisse zweier SELECT-Abfragen (ohne Duplikate).                         |
| UNIQUE            | Stellt sicher, dass alle Werte in einer Spalte oder Spaltengruppe einzigartig sind.        |
| UPDATE            | Aktualisiert bestehende Datensätze in einer Tabelle.                                       |
| USING             | Spezifiziert die zu verwendenden Spalten in einem JOIN.                                    |
| VACUUM            | Bereinigt die Datenbank, um Speicherplatz freizugeben und die Leistung zu verbessern.      |
| VALUES            | Gibt Werte für eine INSERT-Anweisung an.                                                   |
| VIEW              | Definiert eine virtuelle Tabelle basierend auf einer SELECT-Abfrage.                       |
| VIRTUAL           | Wird für die Definition von virtuellen Tabellen verwendet.                                 |
| WHEN              | Definiert eine Bedingung in Triggern oder CASE-Anweisungen.                                |
| WHERE             | Gibt eine Bedingung für die Auswahl von Datensätzen an.                                    |
| WITH              | Definiert eine Common Table Expression (CTE) für komplexe Abfragen.                        |
| WITHOUT           | Wird in SQLite-Erweiterungen verwendet, z.B. für virtuelle Tabellen.                       |

Diese erweiterten Beschreibungen bieten einen detaillierteren Überblick über die Funktion jedes reservierten Wortes in
SQLite. Beachten Sie, dass einige Wörter in spezifischen Kontexten unterschiedliche Bedeutungen haben können.
