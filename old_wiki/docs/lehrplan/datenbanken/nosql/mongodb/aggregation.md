# Exkurs: Weitere Funktionen

### aggregate()
[20 min]

Die `aggregate()` Methode führt eine Aggregation auf der Collection aus. Diese Methode erwartet ein Array von Objekten als Parameter, die die Aggregationsschritte enthalten. Das Vorgehen über mehrere Schritte in der Agrregation wird auch als als Pipeline bezeichnet.

```python
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
db = client.meineDatenbank

# Aggregation der Dokumente in der Collection
pipeline = [
  { "$match": { "name": "Beispiel" } },
  { "$group": { "_id": "$name", "count": { "$sum": 1 } } }
]

result = db.meineCollection.aggregate(pipeline)
for doc in result:
  print(doc)
```

Die 1 bei der $sum -Operation wird verwendet, um die Anzahl der Dokumente in jeder Gruppe zu zählen. Genauer bedeutet die 1, dass für jeden gefundennen Treffer 1 addiert wird.

***Beispiel***

Angenommen, wir haben eine Collection `meineCollection` mit Dokumenten, die Benutzerinformationen enthalten:

```json
{ "_id": 1, "name": "Beispiel", "age": 25 }
{ "_id": 2, "name": "Beispiel", "age": 30 }
{ "_id": 3, "name": "Anderes Beispiel", "age": 25 }
```

#### Aggregationsstufen in MongoDB-Shell-Code

```bash
[
  // Stufe 1: Filtere Dokumente mit dem Namen 'Beispiel'
  { "$match": { "name": 'Beispiel' } },

  // Stufe 2: Gruppiere nach dem Namen und zähle die Dokumente pro Gruppe
  { "$group": { "_id": '$name', "count": { "$sum": 1 } } }
]
```

Die Aggregationsstufen entsprechen den Schritten:

1. **$match**: Filtert die Dokumente, bei denen der Name gleich 'Beispiel' ist.
2. **$group**: Gruppiert die verbleibenden Dokumente nach dem Namen und zählt die Anzahl der Dokumente in jeder Gruppe.

#### Ausführung der `aggregate()`-Methode in der MongoDB-Shell

```python
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
db = client.meineDatenbank
# Aggregation der Dokumente in der Collection
pipeline = [
  { "$match": { "name": "Beispiel" } },
  { "$group": { "_id": "$name", "count": { "$sum": 1 } } }
]
result = db.meineCollection.aggregate(pipeline)
for doc in result:
  print(doc)
```

Das Ergebnis der Aggregation wäre:

```json
{ "_id": "Beispiel", "count": 2 }
```

In diesem Beispiel haben wir eine einfache Aggregation durchgeführt, um die Anzahl der Dokumente mit dem Namen 'Beispiel' zu zählen.

Es sind auch Pipelines mit mehr Schritten möglich:

```python
db.meineCollection.aggregate([
  { "$match": { "status": "aktiv" } },
  { "$group": { "_id": "$department", "total": { "$sum": "$salary" } } },
  { "$sort": { "total": -1 } },
  { "$limit": 5 }
])
```

In diesem Beispiel wird nach dem Status 'aktiv' gefiltert, die Dokumente nach Abteilung gruppierti und die Gesamtsumme der Gehälter berechnet. Zusätzlich wird absteigend nach der nach der Gesamtsumme sortiert und die ersten 5 Ergebnisse zurückgegeben.


### Weiterführende Aggregationsfunktionen in Javascript

Nicht alle Funktionen für Monogo Queries sind in `pymongo` verfügbar. In der MongoDB-Shell können Sie auch auf die folgenden Funktionen zurückgreifen:

### mapReduce()
[20 min]

Die `mapReduce()` Methode führt eine Map-Reduce-Operation auf der Collection aus. Diese Methode erwartet zwei Funktionen als Parameter: eine Map-Funktion und eine Reduce-Funktion.

```bash
# Verwendung einer Datenbank (falls nicht vorhanden, wird sie erstellt)
use meineDatenbank

# Map-Reduce-Operation auf der Collection
db.meineCollection.mapReduce(
  function() { emit(this.name, 1) },
  function(key, values) { return Array.sum(values) },
  { out: 'map_reduce_example' }
)
```

In der Map-Funktion wird ein Dictionary nurch die Funktion `emit()` erstellt und mit Schlüssel-Wert-Paaren gefüllt. Dieses wird an die Reduce-Funktion übergeben, welche die Werte des Dictionaries summiert und das Ergebnis zurückgibt. Die Rückgabe erfolgt in Form eines neuer neue Collection `map_reduce_example`.

***Beispiel***

Angenommen, wir haben eine Collection `meineCollection` mit Dokumenten, die Benutzerinformationen enthalten:

```json
{ "_id": 1, "name": "Alice", "age": 25 }
{ "_id": 2, "name": "Bob", "age": 30 }
{ "_id": 3, "name": "Charlie", "age": 25 }
{ "_id": 4, "name": "Alice", "age": 28 }
```

Die Map-Funktion wird auf jedes Dokument in der Collection angewendet und erzeugt Schlüssel-Wert-Paare (Emit). Im Beispiel zählen wir die Anzahl der Dokumente pro `name`:

```javascript
function mapFunction() {
  emit(this.name, 1);
}
```

Das Ergebnis der Map-Funktion für unsere Collection wäre:

```json
{ "_id": "Alice", "value": 1 }
{ "_id": "Bob", "value": 1 }
{ "_id": "Charlie", "value": 1 }
{ "_id": "Alice", "value": 1 }
```

Die Reduce-Funktion wird auf die emiteten Werte angewendet und kombiniert sie. Im Beispiel addieren wir die Werte, um die Gesamtanzahl pro Name zu erhalten:```bash
function reduceFunction(key, values) {
  return Array.sum(values);
}
```

#### Ausführung der `mapReduce()`-Methode

Die `mapReduce()`-Methode führt die Map- und Reduce-Funktionen aus und speichert das Ergebnis in einer neuen Collection `map_reduce_example`:

```bash
db.meineCollection.mapReduce(
  function() { emit(this.name, 1) },
  function(key, values) { return Array.sum(values) },
  { out: 'map_reduce_example' }
)
```

Das Ergebnis in der `map_reduce_example`-Collection wäre:

```json
{ "_id": "Alice", "value": 2 }
{ "_id": "Bob", "value": 1 }
{ "_id": "Charlie", "value": 1 }
```

In diesem Beispiel haben wir eine einfache Zählung der Vorkommen jedes Namens in der `meineCollection` durchgeführt.


## Aufgaben: Aggregationen
[90 min]

Für die folgenden Aufgaben kannst du dieses Skript als Vorlage für die Datenbankverbindung verwenden:

```python
from pymongo import MongoClient

# Verbindung zur MongoDB herstellen
client = MongoClient('mongodb://localhost:27017/')

# Datenbank erstellen oder auswählen
db = client['shopDB']

# Collections erstellen oder auswählen
users_collection = db['users']
products_collection = db['products']
orders_collection = db['orders']
carts_collection = db['carts']
books_collection = db['books']

users_data = [
    {"_id": 1, "name": "Alice", "age": 30, "city": "Berlin"},
    {"_id": 2, "name": "Bob", "age": 25, "city": "Berlin"},
    {"_id": 3, "name": "Charlie", "age": 35, "city": "Hamburg"}
]

products_data = [
    {"_id": 1, "name": "Product A", "price": 100},
    {"_id": 2, "name": "Product B", "price": 150},
    {"_id": 3, "name": "Product C", "price": 200}
]

orders_data = [
    {
        "_id": 1,
        "userId": 1,
        "date": "2024-06-15",
        "products": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 1}
        ]
    },
    {
        "_id": 2,
        "userId": 2,
        "date": "2024-06-16",
        "products": [
            {"productId": 1, "quantity": 1},
            {"productId": 3, "quantity": 1}
        ]
    },
    {
        "_id": 3,
        "userId": 1,
        "date": "2024-06-17",
        "products": [
            {"productId": 2, "quantity": 2}
        ]
    }
]

carts_data = [
    {
        "_id": 1,
        "userId": 1,
        "products": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 1}
        ]
    },
    {
        "_id": 2,
        "userId": 2,
        "products": [
            {"productId": 1, "quantity": 1},
            {"productId": 3, "quantity": 1}
        ]
    },
    {
        "_id": 3,
        "userId": 1,
        "products": [
            {"productId": 2, "quantity": 2}
        ]
    }
]

books_data = [
    {"_id": 1, "title": "Book A", "author": "Author 1"},
    {"_id": 2, "title": "Book B", "author": "Author 1"},
    {"_id": 3, "title": "Book C", "author": "Author 2"}
]

users_collection.insert_many(users_data)
products_collection.insert_many(products_data)
orders_collection.insert_many(orders_data)
carts_collection.insert_many(carts_data)
books_collection.insert_many(books_data)

print("Daten wurden erfolgreich eingefügt.")
```

1. **Berechne den Gesamtpreis aller Bestellungen, gruppert nach Produkt:** 🌶🌶🌶

2. **Bereche das Durchschnittsalter der Benutzer je Stadt:** 🌶🌶🌶

3. **Berechne die Anzahl der Bestellungen je Tag:** 🌶🌶🌶
  
4. **Berechne den Gesamtpreis der Produkte in jedem Warenkorb:** 🌶🌶🌶

5. **Zähle Anzahl der Bestellungen je Kunde:** 🌶🌶🌶

6. **Berechne die durchschnittliche Anzahl der Produkte in einem Warenkorb:** 🌶🌶🌶

7. **Berechne den durchschnittlichen Gesamtpreis aller Artikel im Warenkorb:** 🌶🌶🌶

8. **Gruppiere die Bestellungen nach Produkt und zähle, wie oft jedes Produkt gekauft wurde** 🌶🌶🌶

9.  **Berechne den Gesamtwert aller Bestellungen unter Berücksichtigung der Produktmenge und des Einzelpreises** 🌶🌶🌶

10. **Zähle die Anzahl der Benutzer pro Stadt** 🌶🌶

11. **Gruppiere die Bücher nach Autoren und erstelle eine Liste der Büchertitel für jeden Autor** 🌶🌶



[Link zur Lösung](../lösungen/aufgabe4.md)
