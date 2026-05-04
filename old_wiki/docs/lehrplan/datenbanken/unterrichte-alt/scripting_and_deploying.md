# Stapelverarbeitung

In SQLite können SQL-Dateien, die mehrere SQL-Befehle enthalten, als Stapeldatei (Batch) ausgeführt werden. Dies ist
besonders
nützlich, wenn Sie eine Reihe von SQL-Anweisungen automatisiert ausführen möchten, wie z.B. beim Einrichten einer
Datenbank, beim Ausführen von Migrationen oder beim Laden von Daten aus Skripten.

Um SQL-Befehle aus einer Datei in SQLite auszuführen, können Sie das SQLite Command Line Interface (CLI) verwenden. Hier
ist, wie Sie es machen können:

**Erstellen einer SQL-Datei**: Zuerst erstellen Sie eine SQL-Datei (z.B. `meine_befehle.sql`) mit allen gewünschten
SQL-Anweisungen. Diese Anweisungen können `CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE` und andere gültige SQL-Befehle
umfassen. Sie können die Befehle durch Semikolons (`;`) trennen, um anzuzeigen, wo ein Befehl endet und der nächste
beginnt.

**Ausführen der SQL-Datei in SQLite**: Um die SQL-Datei auszuführen, öffnen Sie das SQLite CLI und verwenden
den `.read`-Befehl, gefolgt vom Dateipfad. Zum Beispiel:

```bash
sqlite3 MeineDatenbank.db ".read meine_befehle.sql"
```

Dieser Befehl öffnet die Datenbank `MeineDatenbank.db` (und erstellt sie, falls sie noch nicht existiert) und führt
dann alle SQL-Anweisungen in der Datei `meine_befehle.sql` aus.

**Automatisierung**: Sie können diesen Prozess auch in einem Skript automatisieren, das von der Kommandozeile oder
einem anderen Tool aufgerufen wird, um regelmäßige Datenbankoperationen zu erleichtern.

Beachten Sie, dass beim Ausführen von SQL-Dateien als Batches alle Anweisungen in der Datei ausgeführt werden. Wenn ein
Fehler in einer der Anweisungen auftritt, werden die vorherigen Anweisungen bis zum Fehler dennoch ausgeführt, es sei
denn, die Anweisungen sind in einer Transaktion eingebettet. Es ist daher ratsam, die SQL-Datei sorgfältig zu
überprüfen, bevor Sie sie ausführen, insbesondere wenn Sie mit einer Produktionsdatenbank arbeiten.

## Meta-Programmierung

In SQLite selbst gibt es keine direkte Unterstützung für das Einbinden oder Ausführen von mehreren SQL-Dateien aus einer
übergeordneten SQL-Datei, wie es beispielsweise in einigen anderen SQL-Datenbanksystemen der Fall sein könnte. SQLite
behandelt jede Datei, die mit dem `.read`-Befehl aufgerufen wird, als eigenständige Einheit.

Wenn Sie jedoch mehrere SQL-Dateien in einer Batch-Operation ausführen möchten, können Sie dies außerhalb von SQLite mit
Hilfe eines Shell-Skripts oder eines ähnlichen Mechanismus tun. Hier sind einige Ansätze, wie Sie dies erreichen können:

### Verwendung eines Shell-Skripts

Sie können ein einfaches Shell-Skript (für Unix-basierte Systeme wie Linux oder macOS) oder ein Batch-Skript (für
Windows) erstellen, das mehrere `.read`-Befehle für SQLite enthält, um jede Ihrer SQL-Dateien nacheinander auszuführen.



#### Beispiel für ein Python-Batch-Script:

```python
with open(sql_file_path, 'r') as file:
    sql_script = file.read()
cursor.executescript(sql_script)
```

### Verwendung eines Automatisierungstools

Wenn Sie ein fortgeschritteneres Setup benötigen, können Sie Automatisierungstools wie Makefiles, Python-Skripte (mit
der `sqlite3`-Bibliothek) oder andere Skriptsprachen verwenden, um Ihre SQL-Dateien in der gewünschten Reihenfolge
auszuführen.

### Wichtig zu beachten

- Stellen Sie sicher, dass die Reihenfolge, in der die SQL-Dateien ausgeführt werden, korrekt ist, insbesondere wenn die
  Dateien voneinander abhängige Anweisungen enthalten (wie das Erstellen von Tabellen, bevor Daten eingefügt werden).
- Testen Sie Ihr Skript in einer Entwicklungsumgebung, bevor Sie es in einer Produktionsumgebung ausführen, um
  unerwartete Probleme zu vermeiden.
- Denken Sie daran, Transaktionen zu verwenden, wenn die Ausführung aller Befehle als atomare Operation behandelt werden
  soll.

## Transaktionen

Transaktionen in SQL sind wichtig, um sicherzustellen, dass eine Reihe von SQL-Operationen entweder vollständig oder gar
nicht ausgeführt wird. Dies ist besonders wichtig in Situationen, in denen die Integrität der Datenbank gewahrt werden
muss, wie beispielsweise bei der Aktualisierung mehrerer Tabellen oder Datensätze. In SQLite können Sie Transaktionen
verwenden, um solche Operationen zu gruppieren.

Hier ist ein einfaches Beispiel für die Verwendung von Transaktionen in SQLite:

Angenommen, Sie haben eine Tabelle in Ihrer Datenbank: `konten`. Sie möchten einen Betrag von einem
Konto auf ein anderes überweisen. Dies erfordert zwei Schritte: das Abziehen des Betrags vom einen Konto und das
Hinzufügen des Betrags zum anderen Konto. Beide Schritte sollten als eine einzige Transaktion behandelt werden.

```sql
BEGIN TRANSACTION;

-- Schritt 1: Betrag vom Konto 1 abziehen
UPDATE konten
SET saldo = saldo - 100
WHERE kontonummer = 123;

-- Schritt 2: Betrag zum Konto 2 hinzufügen
UPDATE konten
SET saldo = saldo + 100
WHERE kontonummer = 456;

COMMIT;
```

In diesem Beispiel:

1. `BEGIN TRANSACTION;` startet die Transaktion.
2. Die beiden `UPDATE`-Anweisungen werden ausgeführt, um die Kontostände zu aktualisieren.
3. `COMMIT;` beendet die Transaktion und bestätigt alle Änderungen, die während der Transaktion gemacht wurden.

Wenn während der Transaktion ein Fehler auftritt, können Sie die Transaktion mit `ROLLBACK;` abbrechen, um alle
Änderungen rückgängig zu machen, die seit `BEGIN TRANSACTION;` gemacht wurden. Dies stellt sicher, dass Ihre Datenbank
in einem konsistenten Zustand bleibt.

```sql
BEGIN TRANSACTION;

-- Schritt 1: Betrag vom Konto 1 abziehen
UPDATE konten
SET saldo = saldo - 100
WHERE kontonummer = 123;

-- Angenommen, hier tritt ein Fehler auf
-- ...

-- Transaktion abbrechen, wenn ein Fehler auftritt
ROLLBACK;
```

In diesem Fall wird keine der Änderungen, die nach `BEGIN TRANSACTION;` gemacht wurden, in der Datenbank gespeichert,
und der Zustand der Datenbank bleibt unverändert, als ob die Transaktion nie stattgefunden hätte.

### **Aufgabe: Eine Skripte mit Transaktionen🌶️️🌶️️🌶️️**
[40min] Entwickeln sie eigene Scripte, die mehrere Anweisungen enthalten und in eine Transaktion eingebunden sind. 

### **Aufgabe: Funktionsweise von Commit und Rollback 🌶️️🌶️️🌶️️**
[40min] Untersuchen sie die Funktionalität von COMMIT und ROLLBACK.

### Externe Fehlerbehandlung

SQLite selbst unterstützt keine `TRY...CATCH...FINALLY`-Syntax wie in einigen anderen Programmiersprachen oder
SQL-Datenbanksystemen. Fehlerbehandlung in SQLite wird typischerweise auf der Ebene der Anwendung implementiert, die die
SQLite-Datenbank verwendet.

In Programmiersprachen wie Python, Java oder C#, die SQLite über Bibliotheken integrieren, können
Sie `TRY...CATCH...FINALLY` (oder ähnliche Konstrukte) verwenden, um Transaktionen zu verwalten und auf Fehler zu
reagieren. Hier ist ein Beispiel, wie Sie dies in Python tun könnten:

```python
import sqlite3

try:
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('meine_datenbank.db')
    cursor = conn.cursor()

    # Beginn der Transaktion
    cursor.execute('BEGIN TRANSACTION;')

    # Schritt 1: Betrag vom Konto 1 abziehen
    cursor.execute('UPDATE konten SET saldo = saldo - 100 WHERE kontonummer = 123;')

    # Schritt 2: Betrag zum Konto 2 hinzufügen
    cursor.execute('UPDATE konten SET saldo = saldo + 100 WHERE kontonummer = 456;')

    # Transaktion bestätigen
    conn.commit()

except sqlite3.Error as e:
    # Fehlerbehandlung
    print(f"Ein Fehler ist aufgetreten: {e}")
    conn.rollback()

finally:
    # Schließen der Datenbankverbindung
    conn.close()
```

In diesem Python-Beispiel:

- Der `try`-Block enthält den Code, der ausgeführt werden soll (einschließlich der Transaktion).
- Der `except`-Block fängt mögliche Fehler während der Transaktion ab. Im Fehlerfall wird `rollback` aufgerufen, um die
  Transaktion rückgängig zu machen.
- Der `finally`-Block wird am Ende ausgeführt, unabhängig davon, ob ein Fehler aufgetreten ist oder nicht, und schließt
  die Datenbankverbindung.

Die genaue Implementierung kann je nach der verwendeten Programmiersprache und den spezifischen Anforderungen Ihrer
Anwendung variieren.

# Verteilung von Datenbanken

Das Verteilen (Deployment) einer Datenbank ist ein kritischer Schritt in der Entwicklung und Wartung von datenbasierten
Anwendungen. Es beinhaltet die Bereitstellung der Datenbank in einer Produktionsumgebung, die für Endbenutzer oder
Client-Anwendungen zugänglich ist. Dieser Prozess kann die Einrichtung des Datenbankservers, die Konfiguration von
Netzwerkeinstellungen, die Sicherstellung der Datensicherheit und die Optimierung der Leistung umfassen. Bei größeren
Systemen kann das Deployment auch die Replikation von Daten über mehrere Server oder Standorte und die Einrichtung von
Failover- und Recovery-Systemen beinhalten. Wichtig ist dabei, dass die Datenintegrität, Sicherheit und Verfügbarkeit
gewährleistet sind, um einen reibungslosen Betrieb zu ermöglichen.

### Deployment von SQLite-Datenbanken

Im Gegensatz zu serverbasierten Datenbanksystemen wie MySQL oder PostgreSQL ist das Deployment einer SQLite-Datenbank
wesentlich einfacher, da SQLite eine serverlose Architektur besitzt. Eine SQLite-Datenbank wird in einer einzigen Datei
gespeichert, was die Verteilung und den Betrieb vereinfacht. Das Deployment einer SQLite-Datenbank umfasst in der Regel
folgende Schritte:

1. **Integration in die Anwendung**: Die SQLite-Datenbankdatei wird direkt in die Anwendung integriert oder neben ihr
   platziert. Da SQLite als eingebettete Datenbank fungiert, wird sie mit der Anwendung zusammen verteilt.

2. **Konfiguration**: Die Konfiguration von SQLite ist minimal und beinhaltet in der Regel das Festlegen des Dateipfads
   zur Datenbank und eventuell das Anpassen einiger Verbindungsparameter.

3. **Datensicherheit**: Obwohl SQLite keine umfangreichen Netzwerkkonfigurationen benötigt, sollte die Sicherheit der
   Datenbankdatei beachtet werden. Dies beinhaltet den Schutz der Datei vor unbefugtem Zugriff und die Implementierung
   von Backup-Strategien.

4. **Leistungsoptimierung**: Für Anwendungen mit hoher Last oder speziellen Leistungsanforderungen können Optimierungen
   wie das Tuning von SQLite-Pragmas oder die Anpassung von Transaktionen erforderlich sein.

Das Deployment von SQLite ist aufgrund seiner Einfachheit und Portabilität besonders beliebt für Desktop-Anwendungen,
mobile Anwendungen und kleinere Webprojekte. Es bietet eine unkomplizierte Lösung für Anwendungen, die eine
zuverlässige, leichtgewichtige und einfach zu verwaltende Datenbank benötigen.
