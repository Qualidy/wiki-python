# Eingebaute Funktionen

SQLite bietet eine Vielzahl von eingebauten Funktionen, die für verschiedene Operationen verwendet werden können, von
mathematischen Berechnungen bis hin zur Textmanipulation. Diese Funktionen sind direkt in SQLite integriert und können
in Ihren SQL-Abfragen verwendet werden.

### Beispiele für eingebaute Funktionen

**Mathematische Funktionen**:

- `ABS(x)`: Gibt den absoluten Wert von `x` zurück.

```sql
SELECT ABS(-15);
```

- `ROUND(x, y)`: Rundet `x` auf `y` Dezimalstellen.

```sql
SELECT ROUND(gehalt, 2)
FROM mitarbeiter;
```

**Textfunktionen**:

- `LENGTH(x)`: Gibt die Länge des Strings `x` zurück.

```sql
SELECT name, LENGTH(name) AS Namenslänge
FROM mitarbeiter;
```

- `UPPER(x)`, `LOWER(x)`: Konvertiert den String `x` in Groß- bzw. Kleinbuchstaben.

```sql
SELECT UPPER(name)
FROM mitarbeiter;
```

**Datum- und Zeitfunktionen**:

- `DATE()`, `TIME()`, `DATETIME()`: Gibt das aktuelle Datum, die aktuelle Uhrzeit bzw. beides zurück.

```sql
SELECT DATE('now');
```

**Sonstige Funktionen**:

- `RANDOM()`: Gibt eine Zufallszahl zurück.

```sql
SELECT RANDOM();
```

# Aggregatefunktionen in SQLite

Aggregatefunktionen in SQLite werden verwendet, um eine Berechnung auf einer Gruppe von Werten durchzuführen und ein
einzelnes Ergebnis zurückzugeben. Sie sind besonders nützlich in Kombination mit der `GROUP BY`-Klausel.

#### Beispiele für Aggregatefunktionen

**COUNT()**:

- Zählt die Anzahl der Zeilen in einer Tabelle.

```sql
SELECT COUNT(*)
FROM mitarbeiter;
```

**SUM()**:

- Summiert die Werte einer bestimmten Spalte.

```sql
SELECT SUM(gehalt)
FROM mitarbeiter;
```

**AVG()**:

- Berechnet den Durchschnittswert einer Spalte.

```sql
SELECT AVG(gehalt)
FROM mitarbeiter;
```

**MAX() und MIN()**:

- Findet den höchsten bzw. niedrigsten Wert in einer Spalte.

```sql
SELECT MAX(gehalt), MIN(gehalt)
FROM mitarbeiter;
```

**GROUP_CONCAT()**:

- Kombiniert Werte aus einer Spalte zu einem durch Kommas getrennten String.

```sql
SELECT GROUP_CONCAT(name)
FROM mitarbeiter
WHERE abteilung = 'IT';
```

## Zusammenfassung

Die Verwendung von eingebauten Funktionen und Aggregatefunktionen in SQLite ermöglicht es, komplexe Berechnungen und
Datenmanipulationen effizient durchzuführen. Diese Funktionen erweitern die Möglichkeiten der Datenabfrage und -analyse
erheblich und sind ein wesentlicher Bestandteil der SQL-Kenntnisse. Durch das Üben mit diesen Funktionen können die
Schüler lernen, wie man Daten in einer Datenbank effektiv verarbeitet und analysiert.

## Liste der eingebauten Funktionen

| Gruppe       | Funktion            | Bedeutung                                                                | Beispiel                                   |
|--------------|---------------------|--------------------------------------------------------------------------|--------------------------------------------|
| String       | `LENGTH`            | Gibt die Länge eines Strings zurück.                                     | `LENGTH('Hello')` -> 5                     |
| String       | `UPPER`             | Konvertiert einen String in Großbuchstaben.                              | `UPPER('Hello')` -> 'HELLO'                |
| String       | `LOWER`             | Konvertiert einen String in Kleinbuchstaben.                             | `LOWER('Hello')` -> 'hello'                |
| String       | `SUBSTR`            | Extrahiert einen Teilstring.                                             | `SUBSTR('Hello', 2, 3)` -> 'ell'           |
| String       | `TRIM`              | Entfernt Leerzeichen am Anfang und Ende eines Strings.                   | `TRIM('  Hello  ')` -> 'Hello'             |
| String       | `LTRIM`             | Entfernt Leerzeichen am Anfang eines Strings.                            | `LTRIM('  Hello')` -> 'Hello'              |
| String       | `RTRIM`             | Entfernt Leerzeichen am Ende eines Strings.                              | `RTRIM('Hello  ')` -> 'Hello'              |
| String       | `REPLACE`           | Ersetzt Teilstrings.                                                     | `REPLACE('Hello', 'He', 'Ha')` -> 'Hallo'  |
| String       | `QUOTE`             | Gibt einen String sicher für SQL-Abfragen zurück.                        | `QUOTE('It''s SQLite')` -> 'It''s SQLite'  |
| Numerisch    | `ABS`               | Gibt den absoluten Wert zurück.                                          | `ABS(-5)` -> 5                             |
| Numerisch    | `ROUND`             | Rundet eine Zahl.                                                        | `ROUND(5.75)` -> 6                         |
| Numerisch    | `RANDOM`            | Generiert eine Zufallszahl.                                              | `RANDOM()` -> Zufallszahl                  |
| Datum/Zeit   | `DATE`              | Gibt das aktuelle Datum zurück.                                          | `DATE('now')` -> 'YYYY-MM-DD'              |
| Datum/Zeit   | `TIME`              | Gibt die aktuelle Uhrzeit zurück.                                        | `TIME('now')` -> 'HH:MM:SS'                |
| Datum/Zeit   | `STRFTIME`          | Formatiert Datum/Zeit nach einem Muster.                                 | `STRFTIME('%Y-%m-%d', 'now')`              |
| Datum/Zeit   | `JULIANDAY`         | Gibt das Julianische Datum zurück.                                       | `JULIANDAY('now')` -> Julianisches Datum   |
| Datum/Zeit   | `DATETIME`          | Gibt Datum und Uhrzeit zurück.                                           | `DATETIME('now')` -> 'YYYY-MM-DD HH:MM:SS' |
| Aggregat     | `COUNT`             | Zählt die Anzahl der Datensätze.                                         | `COUNT(*)` -> Anzahl der Datensätze        |
| Aggregat     | `MAX`               | Findet den maximalen Wert.                                               | `MAX(age)` -> älteste Person               |
| Aggregat     | `MIN`               | Findet den minimalen Wert.                                               | `MIN(age)` -> jüngste Person               |
| Aggregat     | `AVG`               | Berechnet den Durchschnittswert.                                         | `AVG(price)` -> Durchschnittspreis         |
| Aggregat     | `SUM`               | Summiert Werte.                                                          | `SUM(amount)` -> Gesamtsumme               |
| Aggregat     | `GROUP_CONCAT`      | Verkettet Strings einer Gruppe.                                          | `GROUP_CONCAT(name, ', ')`                 |
| Aggregat     | `TOTAL`             | Summiert Werte, gibt immer einen Wert zurück.                            | `TOTAL(column)` -> Gesamtsumme             |
| Mathematisch | `HEX`               | Konvertiert einen BLOB in einen Hexadezimal-String.                      | `HEX('SQLite')` -> Hexadezimal-String      |
| Mathematisch | `ZEROBLOB`          | Erzeugt einen BLOB der angegebenen Länge mit Nullen.                     | `ZEROBLOB(10)` -> BLOB mit Nullen          |
| Mathematisch | `TYPEOF`            | Gibt den Datentyp eines Ausdrucks zurück.                                | `TYPEOF('Hello')` -> 'text'                |
| Mathematisch | `CHANGES`           | Gibt die Anzahl der durch die letzte Anweisung geänderten Zeilen zurück. | `CHANGES()` -> Anzahl geänderter Zeilen    |
| Mathematisch | `INSTR`             | Gibt die Position eines Teilstrings in einem String zurück.              | `INSTR('Hello', 'e')` -> 2                 |
| Mathematisch | `SQRT`              | Berechnet die Quadratwurzel einer Zahl.                                  | `SQRT(9)` -> 3                             |
| Mathematisch | `MOD`               | Berechnet den Rest einer Division.                                       | `MOD(10, 3)` -> 1                          |
| Mathematisch | `GLOB`              | Gibt TRUE zurück, wenn ein String einem GLOB-Muster entspricht.          | `GLOB('F*', 'Foo')` -> 1                   |
| Mathematisch | `LIKE`              | Gibt TRUE zurück, wenn ein String einem LIKE-Muster entspricht.          | `LIKE('F%', 'Foo')` -> 1                   |
| Sonstige     | `COALESCE`          | Gibt den ersten nicht-NULL-Wert zurück.                                  | `COALESCE(NULL, NULL, 'Hello')` -> 'Hello' |
| Sonstige     | `NULLIF`            | Gibt NULL zurück, wenn zwei Werte gleich sind, sonst den ersten Wert.    | `NULLIF(5, 5)` -> NULL                     |
| Sonstige     | `LAST_INSERT_ROWID` | Gibt die ROWID des zuletzt eingefügten Datensatzes zurück.               | `LAST_INSERT_ROWID()` -> Letzte ROWID      |
| Sonstige     | `RANDOMBLOB`        | Erzeugt einen zufälligen BLOB einer bestimmten Länge.                    | `RANDOMBLOB(10)` -> Zufälliger BLOB        |

## Ausblick

In SQLite können auch eigene Funktionen programmiert werden. Dieses Kapitel ist Bestandteil eines weiterführenden
Kurses.
