# Indexes 
[15 min]

In MongoDB sind Indizes spezielle Datenstrukturen, die die Abfrageleistung verbessern, indem sie den Zugriff auf Daten beschleunigen. Indizes sind eine Möglichkeit, die Geschwindigkeit von Abfragen zu erhöhen, insbesondere wenn Sie nach bestimmten Werten suchen, sortieren oder Join-Operationen durchführen. MongoDB verwendet B-Baum-Indizes, um den schnellen Zugriff auf Daten zu ermöglichen. Diese Struktur erlaubt es, Werte effizient zu suchen und zu sortieren. Indizes können auf einzelnen Feldern oder auf mehreren Feldern erstellt werden. Zusammengesetze Indizes sind insbesondere dann nützlich, wenn Sie nach mehreren Feldern suchen oder sortieren möchten. In MongoDB werden Indizes automatisch auf dem `_id` Feld erstellt. Sie können jedoch auch manuell erstellt werden.

![B-Baum](../../images/b-baum.png)

### Exkurs: B-Baum
Der B-Baum (Balanced Tree) ist eine Datenstruktur, die in vielen Datenbanksystemen, darunter auch MongoDB, für die Implementierung von Indizes verwendet wird. Seine Konstruktion ermöglicht das schnelle Suchen, Einfügen und Löschen von Daten in großen Mengen, und dabei bleibt er stets ausbalanciert.

Bei einem B-Baum-Index wird dieser auf Basis einer oder mehrerer Tabellenspalten erstellt. Die Struktur des Baumes beginnt mit der Wurzel und erstreckt sich über verschiedene Ebenen von Knoten. Jeder Knoten enthält mehrere Schlüsselwerte und dazugehörige Zeiger auf Kindknoten. Die Blätter des Baumes enthalten schließlich die eigentlichen Datenwerte und Zeiger auf die Datensätze in der Tabelle.

Die Schlüsselwerte im B-Baum sind sortiert, was bedeutet, dass sie in jedem Knoten in aufsteigender Reihenfolge angeordnet sind. Diese sortierte Struktur ermöglicht eine effiziente Suche nach Schlüsselwerten.

Bei der Suche in einem B-Baum startet man in der Wurzel und vergleicht den Suchwert mit den Schlüsselwerten im aktuellen Knoten. Basierend auf diesem Vergleich wird entschieden, welcher Zweig des Baums weiter untersucht werden soll. Dieser Prozess wiederholt sich rekursiv, bis der gesuchte Wert gefunden oder festgestellt wird, dass er nicht im Baum vorhanden ist.

Beim Einfügen eines neuen Werts wird zunächst die Position gefunden, an der der Wert eingefügt werden soll. Der B-Baum wird dann so angepasst, dass er weiterhin ausbalanciert bleibt. Das kann das Aufteilen von Knoten oder das Einfügen neuer Ebenen beinhalten, um die Balance zu gewährleisten. Auch beim Löschen eines Werts wird die Position des zu löschenden Werts gefunden, und der B-Baum wird entsprechend angepasst, um die Balance beizubehalten.

Die logarithmische Höhe des B-Baums sorgt dafür, dass die Suchzeiten effizient bleiben, selbst wenn die Anzahl der Datensätze zunimmt. Dies stellt einen klaren Vorteil im Vergleich zu unsortierten Listen oder Arrays dar.

## Index erstellen
[5 min]

Um einen Index in MongoDB zu erstellen, können wir die `createIndex()` Methode verwenden. Diese Methode erwartet ein Objekt als Parameter, das die Felder enthält, auf denen der Index erstellt werden soll. Das Objekt enthält die Feldnamen als Schlüssel und die Sortierreihenfolge als Wert. Die Sortierreihenfolge kann entweder `1` für aufsteigend oder `-1` für absteigend sein. Die Methode gibt ein `CreateIndexesResult` Objekt zurück, das die Namen der erstellten Indizes enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Erstellen eines Indexes auf einem Feld
db.meineCollection.createIndex({ name: 1 })
```

## Index löschen
[5 min]

Um einen Index in MongoDB zu löschen, können wir die `dropIndex()` Methode verwenden. Diese Methode erwartet ein Objekt als Parameter, das die Felder enthält, auf denen der Index erstellt wurde. Das Objekt enthält die Feldnamen als Schlüssel und die Sortierreihenfolge als Wert. Die Sortierreihenfolge kann entweder `1` für aufsteigend oder `-1` für absteigend sein. Die Methode gibt ein `DropIndexesResult` Objekt zurück, das die Namen der gelöschten Indizes enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Löschen eines Indexes auf einem Feld
db.meineCollection.dropIndex({ name: 1 })
```

### Aufgabe: Index erstellen🌶
[15 min]

Erstelle einen Index auf dem Feld `name` in der Collection `meineCollection`. Überprüfe, ob der Index erstellt wurde. Lösche den Index wieder.

[Link zur Lösung](../lösungen/aufgabe5.md)

## Indexe anzeigen
[5 min]

Um die Indizes einer Collection in MongoDB anzuzeigen, können wir die `getIndexes()` Methode verwenden. Diese Methode gibt ein Array von Objekten zurück, die die Indizes der Collection enthalten.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Anzeigen der Indizes einer Collection
db.meineCollection.getIndexes()
```

## Indexeigenschaften
[5 min]

Um die Eigenschaften eines Indexes in MongoDB anzuzeigen, können wir die `stats()` Methode verwenden. Diese Methode gibt ein Objekt zurück, das die Eigenschaften des Indexes enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Anzeigen der Eigenschaften eines Indexes
db.meineCollection.stats()
```

### Aufgabe: Eigenschaften des Index🌶
[10 min]

Erstelle einen Index auf dem Feld `name` in der Collection `meineCollection`. Überprüfe, ob der Index erstellt wurde. Gib die Eigenschaften des Indexes aus. Welche Eigenschaften werden dir angezeigt und was bedeuten sie?

[Link zur Lösung](../lösungen/aufgabe6.md)

## Zusammengesetzte Indexe

Um einen zusammengesetzten Index in MongoDB zu erstellen, können wir die `createIndex()` Methode verwenden. Diese Methode erwartet ein Objekt als Parameter, das die Felder enthält, auf denen der Index erstellt werden soll. Das Objekt enthält die Feldnamen als Schlüssel und die Sortierreihenfolge als Wert. Die Sortierreihenfolge kann entweder `1` für aufsteigend oder `-1` für absteigend sein. Die Methode gibt ein `CreateIndexesResult` Objekt zurück, das die Namen der erstellten Indizes enthält.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Erstellen eines zusammengesetzten Indexes auf mehreren Feldern
db.meineCollection.createIndex({ name: 1, age: -1 })
```

## Aufgaben: Indizes
[90 min]

1. **Index für das "name"-Feld in der Sammlung "Benutzer":** 🌶
     - Erstelle einen einfachen Index für das Feld "name" in der Sammlung "Benutzer".

2. **Zusammengesetzter Index für die Felder "datum" und "produkt" in der Sammlung "Bestellungen":** 🌶
       - Erstelle einen zusammengesetzten Index für die Felder "datum" und "produkt" in der Sammlung "Bestellungen".

3. **Text-Index für das "titel"-Feld in der Sammlung "Bücher":** 🌶
      - Erstelle einen Text-Index für das Feld "titel" in der Sammlung "Bücher".

4. **Absteigender Index für das "preis"-Feld in der Sammlung "Produkte":** 🌶
     - Erstelle einen absteigenden Index für das Feld "preis" in der Sammlung "Produkte".

5. **Geospatial-Index für das "standort"-Feld in der Sammlung "Benutzer":** 🌶🌶
     - Erstelle einen Geospatial-Index für das Feld "standort" in der Sammlung "Benutzer".

6. **Hash-Index für das "email"-Feld in der Sammlung "Kunden":** 🌶🌶
     - Erstelle einen Hash-Index für das Feld "email" in der Sammlung "Kunden".

7. **Teil-Index für das "produkt"-Feld in der Sammlung "Bestellungen":** 🌶🌶
     - Erstelle einen Teil-Index für das Feld "produkt" in der Sammlung "Bestellungen", der nur Dokumente mit einer bestimmten Bedingung enthält.

8. **Einzigartiger Index für das "name"-Feld in der Sammlung "Produkte":** 🌶🌶
     - Erstelle einen einzigartigen Index für das Feld "name" in der Sammlung "Produkte".

9. **Index mit Ablaufzeit für das "datum"-Feld in der Sammlung "Bestellungen":** 🌶🌶
    - Erstelle einen Index mit Ablaufzeit für das Feld "datum" in der Sammlung "Bestellungen".

10. **Sparse-Index für das "alter"-Feld in der Sammlung "Benutzer":** 🌶🌶
     - Erstelle einen sparsen Index für das Feld "alter" in der Sammlung "Benutzer", um nur Dokumente mit diesem Feld zu indizieren.

[Link zur Lösung](../lösungen/aufgabe7.md)