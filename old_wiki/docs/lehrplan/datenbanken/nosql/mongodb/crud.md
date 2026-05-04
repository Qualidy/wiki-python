# CRUD Operationen

In dem letzten Abschnitt haben wir uns angesehen, wie wir über einen Docker Container eine MongoDB Datenbank starten können und wie wir uns mit dieser Datenbank verbinden können. In diesem Abschnitt werden wir uns nun mit den CRUD Operationen beschäftigen. Die CRUD Operationen kennen wir bereits aus den vergangenen Einheiten zu Datenbanken. MongoDB verwendet standardmäßig JavaScript Objekte, um Daten zu speichern. Wir werden zur Vereinfachung jedoch direkt mit dem offiziell unterstützten python Wrapper `pymongo` arbeiten.

Die Crud Operationen können ohne Python beispielsweise in der MongoDB Shell oder in dem Editor des VSCode Plugins MongoDB for VS Code ausgeführt werden.

Verwenden wir Python und `pymongo`, müssen wir zuerst die Bibliothek installieren:

```bash
pip install pymongo
```

Im Anschluss können wir uns mit einer bestehenden Datenbank verbinden und CRUD Operationen durchführen.

```python
import pymongo

# Verbindung zur Datenbank herstellen
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["meineDatenbank"]
collection = database["meineCollection"]

```

## Create
[5 min]

Um Daten in MongoDB zu erstellen, können wir die `insert_one()` Methode verwenden. Diese Methode erwartet ein Dictionary als Parameter. Das Dictionary enthält die Daten, die wir in die Datenbank einfügen möchten. Die Methode gibt ein `InsertOneResult` Objekt zurück, das die ID des eingefügten Dokuments enthält.

```bash
# Einfügen eines Dokuments in eine Collection
collection.insert_one({
  "name": 'Beispiel',
  "alter": 25,
  "ort": 'Irgendwo'
})
```

## Read
[5 min]

Um Daten aus MongoDB zu lesen, können wir die `find()` Methode verwenden. Diese Methode gibt ein `Cursor` Objekt zurück, das alle Dokumente in der Collection enthält.

**Hinweis**: Um die Daten aus dem Cursor zu lesen, können wir in Javascript die `forEach()` Methode verwenden. Diese Methode erwartet eine Funktion als Parameter, die für jedes Dokument in der Collection ausgeführt wird. Die Funktion erhält das aktuelle Dokument als Parameter

```bash
# Anzeigen aller Dokumente in der Collection
collection.find()

# Anzeigen con Dokumenten mit einer bestimmten Eigenschaft
collection.find({ "name": 'Beispiel' })

# Anzeigen aller Dokumente in der Collection mit forEach
results = collection.find()
for result in results:
  print(result)

```

## Update
[5 min]

Um Daten in MongoDB zu aktualisieren, können wir die `update_one()` Methode verwenden. Diese Methode erwartet zwei Parameter: ein Objekt, das das zu aktualisierende Dokument enthält, und ein Objekt, das die Aktualisierungen enthält. Die Methode gibt ein `UpdateResult` Objekt zurück, das die Anzahl der aktualisierten Dokumente enthält.

```bash
# Aktualisieren eines Dokuments in einer Collection
collection.update_one(
  { "name": 'Beispiel' },
  {"$set": { "name": 'Neuer Name' } }
)
```

## Delete
[5 min]

Um Daten in MongoDB zu löschen, können wir die `delete_one()` Methode verwenden. Diese Methode erwartet ein Objekt, das das zu löschende Dokument enthält. Die Methode gibt ein `DeleteResult` Objekt zurück, das die Anzahl der gelöschten Dokumente enthält.

```bash
# Löschen eines Dokuments in einer Collection
collection.delete_one({ "name": 'Beispiel' })

# Löschen aller Dokumente in einer Collection
collection.delete_many({})
```

## Weitere Methoden
[20 min]

Neben den hier vorgestellten Methoden gibt es noch viele weitere Methoden, die wir verwenden können. Eine vollständige Liste der Methoden findest du in der [MongoDB Dokumentation](https://docs.mongodb.com/manual/reference/method/). Hier werden wir lediglich einige der weiteren Methoden gemeinsam ansehen.

### find_one()

Die `find_one()` Methode gibt das erste Dokument in der Collection zurück. Diese Methode erwartet ein Objekt als Parameter, das die Eigenschaften des gesuchten Dokuments enthält.

```bash
# Anzeigen des ersten Dokuments in der Collection
collection.find_one()
```

### count_documents()

Die `count_documents()` Methode gibt die Anzahl der Dokumente in der Collection zurück. Diese Methode erwartet ein Objekt als Parameter, das die Eigenschaften der gesuchten Dokumente enthält.

```bash
# Anzeigen der Anzahl der Dokumente in der Collection
collectionn.count_documents({})
```

### sort()

Die `sort()` Methode sortiert die Dokumente in der Collection. Diese Methode erwartet ein Objekt als Parameter, das die Eigenschaften enthält, nach denen die Dokumente sortiert werden sollen.

```bash
# Sortieren der Dokumente in der Collection
collection.find().sort({ "name": 1 })
```

### limit()

Die `limit()` Methode begrenzt die Anzahl der zurückgegebenen Dokumente. Diese Methode erwartet eine Zahl als Parameter, die die Anzahl der zurückgegebenen Dokumente angibt.

```bash
# Begrenzen der Anzahl der zurückgegebenen Dokumente
collection.find().limit(5)
```

### skip()

Die `skip()` Methode überspringt eine bestimmte Anzahl von Dokumenten. Diese Methode erwartet eine Zahl als Parameter, die die Anzahl der zu überspringenden Dokumente angibt.

```bash
# Überspringen der ersten 5 Dokumente
collection.find().skip(5)
```

Dies sind einfache Funktionen, welche wir in Ähnlicher Weise bereits aus den SQL Datenbanken kennen. In den folgenden Abschnitten werden wir uns mit etwas komplexeren Funktionen beschäftigen, die MongoDB uns bietet.

## Aufgaben
[90 min]

Für die folgenden Aufgaben kannst du folgenden Code kopieren, umd ie entsprechenden Sammlungen zu erstellen:

```bash

# Beispiel für die Erstellung von Sammlungen in der MongoDB-Shell
database.create_collection("benutzer")
database.create_collection("produkte")
database.create_collection("kunden")
database.create_collection("warenkorb")
database.create_collection("bestellungen")
database.create_collection("bücher")

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Benutzer"
benutzer = database["benutzer"]
benutzer.insert_many([
    {"name": "Max Mustermann", "alter": 30, "stadt": "Berlin"},
    {"name": "Anna Schmidt", "alter": 25, "stadt": "München"}
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Produkte"
produkte = database["produkte"]
produkte.insert_many([
    {"name": "Smartphone", "preis": 500, "marke": "XYZ"},
    {"name": "Laptop", "preis": 1000, "marke": "ABC"},
    {"name": "Mousepad", "preis": 300, "marke": "XYZ"},
    {"name": "Playstation", "preis": 2000, "marke": "ABC"},
    {"name": "Printer", "preis": 1200, "marke": "XYZ"},
    {"name": "Keyboard", "preis": 400, "marke": "ABC"}
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Kunden"
kunden = database["kunden"]
kunden.insert_many([
    {"name": "John Doe", "email": "john.doe@example.com", "adresse": "Hauptstraße 123"},
    {"name": "Jane Doe", "email": "jane.doe@example.com", "adresse": "Nebenstraße 456"}
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Warenkorb"
warenkorb = database["warenkorb"]
warenkorb.insert_many([
    {"produkt": "Smartphone", "preis": 500, "menge": 2},
    {"produkt": "Laptop", "preis": 1000, "menge": 1},
    {"produkt": "Mousepad", "preis": 300, "menge": 3},
    {"produkt": "Playstation, "preis": 2000, "menge": 4}
    {"produkt": "Printer", "preis": 1200, "menge": 5},
    {"produkt": "Keyboard", "preis": 400, "menge": 6}
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Bestellungen"
bestellungen = database["bestellungen"]
bestellungen.insert_many([
    {"datum": datetime.datetime(2022, 12, 1), "produkt": "Smartphone", "menge": 2},
    {"datum": datetime.datetime(2022, 11, 15), "produkt": "Laptop", "menge": 1}
    {"datum": datetime.datetime(2023, 12, 1), "produkt": "Smartphone", "menge": 3},
    {"datum": datetime.datetime(2024, 01, 01), "produkt": "Laptop", "menge": 4}
    {"datum": datetime.datetime(2023, 12, 1), "produkt": "Smartphone", "menge": 12},
    {"datum": datetime.datetime(2021, 11, 15), "produkt": "Laptop", "menge": 1}
])

# Beispiel für das Einfügen von Dokumenten in die Sammlung "Bücher"
bücher = database["bücher"]
bücher.insert_many([
    {"titel": "The Great Gatsby", "autor": "F. Scott Fitzgerald"},
    {"titel": "To Kill a Mockingbird", "autor": "Harper Lee"}
])
```

1. **Lesen (Read):** 🌶
    - Lies alle Dokumente in der Sammlung "Benutzer" und gib sie aus.

2. **Suchen (Read):** 🌶
    - Finde alle Dokumente in der Sammlung "Produkte" mit einem Preis über 50.

3. **Einfügen (Create):** 🌶
    - Füge ein neues Dokument zur Sammlung "Kunden" hinzu. Das Dokument soll Informationen wie "Name", "E-Mail" und "Adresse" enthalten.

4. **Aktualisieren (Update):** 🌶
    - Aktualisiere den Preis aller Produkte in der Sammlung "Warenkorb" um 10%.

5. **Löschen (Delete):** 🌶
    - Lösche alle Dokumente in der Sammlung "Bestellungen", die älter als 30 Tage sind.

6. **Filtern und Auswählen (Read):** 🌶🌶
    - Finde alle Dokumente in der Sammlung "Bücher", die den Autor "John Doe" haben, und gib nur die Buchtitel aus.

7. **Skip und Limit für Produkte:** 🌶🌶
    - Überspringe die ersten 2 Produkte und gib die nächsten 3 Produkte aus.

8. **Sortiere Bestellungen nach Datum absteigend:**
    - Sortiere die Bestellungen nach dem Datum in absteigender Reihenfolge.

9. **Count der Kunden in Berlin:** 🌶🌶
    - Zähle die Anzahl der Benutzer, die in Berlin leben.

10. **Erstes Buch im Alphabet:** 🌶🌶
    - Finde das erste Buch im Alphabetisch sortierten Titel.

11. **Suche nach einem bestimmten Produkt:** 🌶🌶
    - Finde ein Produkt in der Sammlung "Produkte" nach einem bestimmten Kriterium.

12. **Anzahl der Bestellungen für jedes Produkt:** 🌶🌶
    - Zähle die Anzahl der Bestellungen für jedes Produkt.


[Link zur Lösung](../lösungen/aufgabe3.md)