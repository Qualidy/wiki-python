## SQLite in Python:

- Ich habe ein grundlegendes Verständnis dafür, wie SQLite in Python verwendet wird.
- Ich weiß, wie man SQLite-Verbindungen als Context Manager in einem "`with`"-Statement einsetzt.
- Ich kann eine Verbindung zur SQLite-Datenbank in Python herstellen.
- Ich weiß, wie ich die Verbindung zur SQLite-Datenbank ordnungsgemäß schließe.
- Ich kann einen Cursor in SQLite erstellen und verwenden, um SQL-Anweisungen auszuführen.
- Ich kann Tabellen in SQLite erstellen und Daten mithilfe von SQL-Anweisungen einfügen.
- Ich kann Transaktionen in SQLite steuern, einschließlich Starten, Bestätigen (COMMIT) und Rückgängigmachen (ROLLBACK).
- Ich kann benutzerdefinierte Aggregatfunktionen in SQLite erstellen und verwenden.
- Ich kann SQL-Abfragen in SQLite ausführen.
- Ich kann Ergebnisse von SQL-Abfragen mithilfe von `fetchall` und `fetchone` in SQLite abrufen.
- Ich weiß, wie man die `ROLLBACK`-Anweisung in SQLite-Transaktionen verwendet, um Änderungen rückgängig zu machen.
- Ich kann Fehler in Datenbankoperationen ordnungsgemäß handhaben.

## ORM (Object-Relational Mapping)

- Ich kann das ORM-Konzept verstehen.
- Ich kann SQLAlchemy als ORM-Tool verwenden.

## Engine

- Ich kann eine SQLAlchemy Engine erstellen.
- Ich kann die Engine für verschiedene Datenbanken (SQLite, PostgreSQL, MySQL/MariaDB) konfigurieren.

## Metadata, Table, Column

- Ich kann Metadaten erstellen.
- Ich kann Tabellen und Spalten definieren.
- Ich kann Datentypen wie Integer und String verwenden.

## Table Creation

- Ich kann `metadata.create_all(engine)` verwenden, um Tabellen in der Datenbank zu erstellen.

## Declarative Base

- Ich kann `declarative_base()` verwenden, um deklarative Klassen zu definieren.

## Session Management

- Ich kann eine Session Factory mit `sessionmaker(bind=engine)` erstellen.
- Ich kann Objekte hinzufügen (`session.add(new_user)`).
- Ich kann Änderungen mit `session.commit()` bestätigen.
- Ich kann die Datenbankverbindung mit `session.close()` schließen.

## Querying

- Ich kann Abfragen mit `session.query(MyModel)` durchführen.
- Ich kann `filter` und `filter_by` für WHERE-Bedingungen verwenden.

## ACID

- Ich kann die ACID-Prinzipien (Atomicity, Consistency, Isolation, Durability) erklären.

## SQL Expression Language

- Ich kann die SQLAlchemy SQL Expression Language verwenden.
- Ich kann Roh-SQL-Anweisungen mit `execute` ausführen.

## CRUD Operations

- Ich kann Daten mit `insert` einfügen.
- Ich kann mit `where` Abfragen durchführen.
- Ich kann Daten mit `update` aktualisieren.
- Ich kann Daten mit `delete` löschen.

## Bulk-Operationen

- Ich kann Massenoperationen für effizientes Datenbankmanagement durchführen.

## Eager Loading

- Ich kann `joinedload` verwenden, um Beziehungen effizient zu laden.

## Lazy Loading

- Ich kann Lazy Loading-Strategien verstehen und anwenden.

## Index

- Ich kann Indizes erstellen, um die Abfrageleistung zu verbessern.

## Funktionen (func)

- Ich kann SQL-Funktionen in SQLAlchemy mit `func` verwenden.

## Mixin

- Ich kann das Mixin-Designmuster verstehen und anwenden.

## SQL-Logging

- Ich kann SQL-Logging in SQLAlchemy aktivieren und verwalten.

## Asynchrone Operationen

- Ich kann `asyncio` für asynchrone Programmierung verwenden.
- Ich kann `await` in asynchronen Funktionen verwenden.
