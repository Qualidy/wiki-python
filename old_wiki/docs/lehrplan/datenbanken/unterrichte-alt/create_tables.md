# Tabellen erstellen
[10 min]
## Grundform

Wir erstellen eine Tabelle, die die Anzahl und Eigenschaften der Werkzeuge in unserer Werkstatt aufnehmen soll.

      create table Werkzeuge (
          id int primary key, 
          bezeichnung text,
          gewicht real,
          farbe text 
      );

Man kann darüber streiten, ob die folgende Schreibweise **besser** ist oder nicht.

      create table Werkzeuge (
          id int primary key 
          , bezeichnung text
          , gewicht real
          , farbe text 
      );

Aber die Praxis zeigt, dass es beim Einfügen und Löschen von Spalten immer wieder zu Fehlern bei der Kommasetzung kommt.
Die zweite Form wirkt dem entgegen.

## Ändern der Tabelle

Wir haben erkannt, dass die Werkzeuge in verschiedene Kategorien eingeordnet werden können.

      alter table Werkzeuge
      add column waren_gruppe text;
    
      alter table Werkzeuge
      add column waren_untergruppe text;

Das Gewicht erscheint uns überflüssig.

In SQLite ist das direkte Löschen einer Spalte aus einer Tabelle mit dem `ALTER TABLE`-Befehl nicht möglich. Stattdessen
müssen Sie einen mehrstufigen Prozess durchführen, um eine Spalte zu entfernen. Dieser Prozess beinhaltet das Erstellen
einer neuen Tabelle, die alle gewünschten Spalten der ursprünglichen Tabelle enthält (außer der zu entfernenden Spalte),
das Kopieren der Daten von der alten in die neue Tabelle, das Löschen der alten Tabelle und schließlich das Umbenennen
der neuen Tabelle in den ursprünglichen Tabellennamen.

Hier ist, wie Sie die Spalte `Gewicht` aus Ihrer Tabelle `Werkzeuge` entfernen können:

## Aufgaben:
[30min]
### **1. Erstellen Sie eine neue Tabelle 🌶️**

Erstellen Sie eine neue Tabelle, die identisch mit der ursprünglichen Tabelle `Werkzeuge` ist, aber ohne die 
Spalte `Gewicht`.
```sql
CREATE TABLE Werkzeuge_neu (
    id INT PRIMARY KEY,
    bezeichnung TEXT,
    farbe TEXT,
    Warengruppe TEXT,
    Warenuntergruppe TEXT
);
```

### **2. Kopieren Sie die Daten 🌶️**

Kopieren Sie alle Daten von der alten Tabelle `Werkzeuge` in die neue Tabelle `Werkzeuge_neu`, ohne die Spalte `Gewicht`.
```sql
INSERT INTO Werkzeuge_neu (id, bezeichnung, farbe, Warengruppe, Warenuntergruppe)
SELECT id, bezeichnung, farbe, Warengruppe, Warenuntergruppe FROM Werkzeuge;
```
### 3. **Löschen Sie die alte Tabelle 🌶️️**

Löschen Sie nun die alte Tabelle `Werkzeuge`.
```sql
DROP TABLE Werkzeuge;
```

### 4. **Benennen Sie die neue Tabelle um 🌶️️**:
Benennen Sie die neue Tabelle `Werkzeuge_neu` in `Werkzeuge` um.
```sql
ALTER TABLE Werkzeuge_neu RENAME TO Werkzeuge;
```

## Ergebnisbewertung 
[10min]

Nachdem Sie diese Schritte ausgeführt haben, haben Sie effektiv die Spalte `Gewicht` aus Ihrer Tabelle `Werkzeuge`
entfernt. Stellen Sie sicher, dass Sie vor dem Durchführen dieser Operationen eine Sicherungskopie Ihrer Datenbank
erstellen, um Datenverlust zu vermeiden.

Im Zuge der Normalisierung stellen sie fest, dass die beiden neuen Spalten den falschen Typ haben. Sie sollen als
Fremdschlüssel dienen und keinen Text enthalten.

Da hätte man besser planen müssen!

Um die Datentypen der Spalten `Warengruppe` und `Warenuntergruppe` in Ihrer `Werkzeuge`-Tabelle von `TEXT` auf `INT` zu
ändern und sie als Fremdschlüssel zu definieren, müssen Sie ähnliche Schritte wie beim Entfernen einer Spalte
durchführen. SQLite erlaubt es nicht, den Datentyp einer Spalte direkt zu ändern, wenn sie bereits Daten enthält.
Stattdessen müssen Sie eine neue Tabelle erstellen, die Daten übertragen, die alte Tabelle löschen und die neue Tabelle
umbenennen.

Bevor Sie beginnen, stellen Sie sicher, dass die Tabellen, auf die sich die Fremdschlüssel beziehen, bereits existieren.
Angenommen, Sie haben zwei Tabellen `Warengruppen` und `Warenuntergruppen`, und jede hat eine Spalte `ID` vom Typ `INT`,
die als Primärschlüssel dient.

### **Aufgabe: Lösen sie das Problem nach dem vorgegebenen Schema 🌶️️🌶️️**
[30min]

1. **Erstellen Sie eine neue Tabelle**:

2. **Kopieren Sie die Daten**:
   Kopieren Sie die Daten von der alten Tabelle in die neue. Beachten Sie, dass Sie die Werte für `Warengruppe`
   und `Warenuntergruppe` entsprechend anpassen müssen, damit sie gültige Fremdschlüsselreferenzen darstellen.

3. **Löschen Sie die alte Tabelle**:

4. **Benennen Sie die neue Tabelle um**:

## Fremdschlüssel

Das Hinzufügen von Fremdschlüsselbeziehungen zu einer bestehenden Tabelle in SQLite, nachdem die Tabelle bereits
erstellt wurde, erfordert ähnliche Schritte wie das Ändern des Datentyps einer Spalte. SQLite unterstützt das direkte
Hinzufügen oder Ändern von Fremdschlüsseln in einer bestehenden Tabelle nicht. Sie müssen eine neue Tabelle mit den
gewünschten Fremdschlüsselbeziehungen erstellen, die Daten übertragen, die alte Tabelle löschen und die neue Tabelle
umbenennen.

### **Aufgabe: Wir haben vergessen, die FOREIGN KEYS anzugeben. 🌶️️🌶️️** 
[30min]

1. **Erstellen Sie eine neue Tabelle mit Fremdschlüsseln**:
   Angenommen, Sie haben die Tabellen `Warengruppen` und `Warenuntergruppen` mit den Primärschlüsseln `ID`. Erstellen
   Sie eine neue Tabelle, die die Fremdschlüsselbeziehungen enthält:

2. **Kopieren Sie die Daten**:
   Kopieren Sie die Daten von der alten Tabelle `Werkzeuge` in die neue Tabelle `Werkzeuge_neu`. Stellen Sie sicher,
   dass die Werte in den Spalten `Warengruppe` und `Warenuntergruppe` gültige Fremdschlüsselreferenzen sind.

3. **Löschen Sie die alte Tabelle**:

4. **Benennen Sie die neue Tabelle um**:

## Constraints und Default-Werte
[40min]

Bei der Erstellung von Tabellen in SQLite ist es wichtig, Constraints und Default-Werte zu berücksichtigen, um die
Datenintegrität und Standardverhalten zu gewährleisten. Hier ist eine Ergänzung, die sich auf die Verwendung von
Constraints und Default-Werten in der Tabelle `Werkzeuge` konzentriert:

### Hinzufügen von Constraints

Constraints sind Regeln, die auf die Daten in einer Tabelle angewendet werden, um deren Genauigkeit und Zuverlässigkeit
sicherzustellen. In SQLite können Sie verschiedene Arten von Constraints definieren, wie `UNIQUE`, `NOT NULL`, `CHECK`,
und `FOREIGN KEY`.

Beispiel für die Erweiterung der `Werkzeuge`-Tabelle mit Constraints:

```sql
CREATE TABLE Werkzeuge
(
    id                INT PRIMARY KEY,
    bezeichnung       TEXT NOT NULL,
    gewicht           REAL,
    farbe             TEXT,
    waren_gruppe      TEXT,
    waren_untergruppe TEXT,
    UNIQUE (bezeichnung),
    CHECK (gewicht >= 0)
);
```

In diesem Beispiel wird sichergestellt, dass die `bezeichnung` eindeutig und nicht null ist und das `gewicht` nicht
negativ ist.

### Hinzufügen von Default-Werten

Default-Werte werden verwendet, um einem Feld automatisch einen Wert zuzuweisen, wenn beim Einfügen eines Datensatzes
kein Wert für dieses Feld angegeben wird. Dies kann hilfreich sein, um Standardwerte für bestimmte Felder festzulegen.

Beispiel für die Erweiterung der `Werkzeuge`-Tabelle mit Default-Werten:

```sql
CREATE TABLE Werkzeuge
(
    id                INT PRIMARY KEY,
    bezeichnung       TEXT NOT NULL,
    gewicht           REAL DEFAULT 0,
    farbe             TEXT DEFAULT 'Unbekannt',
    waren_gruppe      TEXT,
    waren_untergruppe TEXT
);
```

Hier wird, falls kein `gewicht` angegeben wird, automatisch der Wert `0` gesetzt, und für `farbe` wird 'Unbekannt' als
Standardwert verwendet, falls kein Wert angegeben wird.

### Zusammenfassung

Durch das Hinzufügen von Constraints und Default-Werten in der `Werkzeuge`-Tabelle können Sie die Datenintegrität
verbessern und sicherstellen, dass die Datenbank konsistente und sinnvolle Informationen enthält. Diese Praktiken sind
entscheidend für die Erstellung robuster und zuverlässiger Datenbankstrukturen in SQLite.

## Modifikation von Constraints und Default-Werten mit ALTER

In SQLite ist die Modifikation von Constraints und Default-Werten nach der Erstellung einer Tabelle begrenzt.
Der `ALTER TABLE`-Befehl in SQLite unterstützt nicht direkt das Hinzufügen, Entfernen oder Ändern von Constraints oder
Default-Werten in bestehenden Tabellen. Dies stellt eine Einschränkung dar, die bei der Datenbankplanung und -wartung
berücksichtigt werden muss. Hier sind einige wichtige Punkte:

### 1. **Ändern von Default-Werten**: 

SQLite erlaubt nicht das direkte Ändern von Default-Werten mit dem `ALTER TABLE`
-Befehl. Um einen Default-Wert zu ändern, müssen Sie eine neue Tabelle mit der geänderten Definition erstellen, die
Daten übertragen, die alte Tabelle löschen und die neue Tabelle umbenennen.

### 2. **Hinzufügen oder Entfernen von Constraints**: 

Ähnlich wie bei Default-Werten unterstützt SQLite nicht das direkte
Hinzufügen oder Entfernen von Constraints (wie `UNIQUE`, `NOT NULL`, `CHECK`, `FOREIGN KEY`) in einer bestehenden
Tabelle. Um Constraints hinzuzufügen oder zu entfernen, müssen Sie den gleichen Prozess wie beim Ändern von
Default-Werten befolgen: Erstellen einer neuen Tabelle, Übertragen der Daten, Löschen der alten Tabelle und
Umbenennen der neuen Tabelle.

### 3. **Praktische Überlegungen**: 

Diese Einschränkungen bedeuten, dass sorgfältige Planung erforderlich ist, bevor eine
Tabelle erstellt wird. Es ist wichtig, alle erforderlichen Constraints und Default-Werte im Voraus zu
berücksichtigen. Änderungen nachträglich können zeitaufwendig sein und erfordern eine sorgfältige Datenmigration.

### 4. **Datenmigration**: 
Bei der Datenmigration ist es entscheidend, die Datenintegrität zu wahren. Es empfiehlt sich,
eine vollständige Sicherung der Datenbank vorzunehmen, bevor Änderungen durchgeführt werden. Außerdem sollten die
Daten nach der Migration überprüft werden, um sicherzustellen, dass keine Daten verloren gegangen sind oder verändert
wurden.

### 5. **Zusammenfassung:**
Zusammenfassend lässt sich sagen, dass während SQLite eine flexible und leichte Datenbanklösung bietet, die
Einschränkungen im Zusammenhang mit dem `ALTER TABLE`-Befehl eine Herausforderung darstellen können. Eine
vorausschauende Planung und sorgfältige Datenmigration sind entscheidend, um die Struktur und Integrität der Datenbank
im Laufe der Zeit zu erhalten und zu verwalten.
