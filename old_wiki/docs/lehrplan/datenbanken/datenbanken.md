# SQL in Datenbanken

eine Einführung in die strukturierte Abfragesprache SQL

### Was ist SQL

SQL, kurz für "Structured Query Language", ist eine spezielle Programmiersprache, die für die Verwaltung und
Manipulation von Daten in relationalen Datenbanken verwendet wird. Relationale Datenbanken sind eine Art von Datenbank,
die Daten in Tabellenform speichert, ähnlich wie in einem Excel-Arbeitsblatt. Jede Tabelle in einer relationalen
Datenbank kann eine Vielzahl von Daten enthalten, die in Zeilen und Spalten organisiert sind.

### Grundkonzepte von SQL:

1. **Datenbanken und Tabellen:**

    - Eine Datenbank ist eine Sammlung von Daten, die organisiert und leicht zugänglich sind.
    - Innerhalb einer Datenbank sind Daten in Tabellen gespeichert. Jede Tabelle repräsentiert eine Art von Daten (z.B.
      Kunden, Produkte) und besteht aus Zeilen und Spalten.

2. **SQL-Anweisungen:**
    - SQL verwendet spezielle [Anweisungen oder Befehle](unterrichte-alt/sql_types.md), um mit Datenbanken zu interagieren.
    - Diese Anweisungen und Befehle ermöglichen es Ihnen
      - Datenstrukturen aufzubauen sowie 
      - Daten zu erstellen, abzurufen, zu aktualisieren und zu löschen.

### Wichtige SQL-Anweisungen:

   1. **SELECT:**
     - Wird verwendet, um Daten aus einer Tabelle abzurufen.
     - Beispiel: `SELECT name FROM kunden` holt die Namen aller Kunden aus der Tabelle `kunden`.

   2. **INSERT:**
     - Fügt neue Daten in eine Tabelle ein.
     - Beispiel: `INSERT INTO kunden (name, email) VALUES ('John Doe', 'john@example.com')` fügt einen 
       neuen Kunden in die Tabelle `kunden` ein.

   3. **UPDATE:**
     - Ändert bestehende Daten in einer Tabelle.
     - Beispiel: `UPDATE kunden SET email = 'newemail@example.com' WHERE name = 'John Doe'` aktualisiert die
       E-Mail-Adresse eines Kunden.

   4. **DELETE:**
     - Entfernt Daten aus einer Tabelle.
     - Beispiel: `DELETE FROM kunden WHERE name = 'John Doe'` löscht einen Kunden aus der Tabelle `kunden`.

### Warum ist SQL wichtig?

  - **Universell:** SQL wird von fast allen relationalen Datenbanksystemen unterstützt, was es zu einer universellen Sprache für Datenbankmanagement macht.
  - **Mächtig:** Mit SQL können Sie komplexe Abfragen und Analysen durchführen, um genau die Daten zu erhalten, die Sie
    benötigen.
  - **Effizient:** SQL ermöglicht es Ihnen, schnell und effizient mit großen Mengen von Daten zu arbeiten.

### Fazit:

Für jeden, der in die Welt der Datenbanken und der Datenverwaltung einsteigt, ist SQL ein unverzichtbares Werkzeug. Es
ist die Grundlage für das Verständnis, wie moderne Anwendungen Daten speichern, abrufen und verarbeiten. Mit SQL können
Sie die Kraft relationaler Datenbanken nutzen, um komplexe Datenanforderungen effizient zu bewältigen.

# Bestandteile des Kurses

### [Einführung](datenbanken.md)

### [Arten von SQL Anweisungen](unterrichte-alt/sql_types.md)

### [UML für Datenbanken](unterrichte-alt/uml_diagramme.md)

### [Normalisierung von Daten](unterrichte-alt/normalization.md)

### [Indizes und Referentielle Integrität](unterrichte-alt/indices_and_referential_integrity.md)

### [Arbeitsumgebung](unterrichte-alt/how_we_will_work.md)

### [Reservierte Ausdrücke in SQLite](unterrichte-alt/reserved_words_sqlite.md)

### [Datentypen in SQLite](unterrichte-alt/daten_typen_sqlite.md)

### [Erstellen von Tabellen](unterrichte-alt/create_tables.md)

### [Arbeiten mit Daten](unterrichte-alt/working_with_data.md)

### [Verwenden von Aliasen](unterrichte-alt/aliases.md)

### [Eingebaute Funktionen](unterrichte-alt/build_in_functions.md)

### [Verschachtelte Abfragen](unterrichte-alt/subselect_and_cte.md)

### [Batch, Script, Deploy](unterrichte-alt/scripting_and_deploying.md)

### [Gruppenarbeit - Projekte](unterrichte-alt/projects.md)

### [Fragen an die Datenbank](unterrichte-alt/joins_and_views.md)

### [Schlußbemerkungen](unterrichte-alt/finally.md)

