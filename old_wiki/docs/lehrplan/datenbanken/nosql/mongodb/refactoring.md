# Exkurs: Refactoring von Datenbanken (MongoDB)
[20 min]

In der Praxis können sich Anforderungen an die Datenbank im Laufe der Zeit ändern, sodass sich Optimierungspotenziale ergeben. In diesem Fall kann es sinnvoll sein, die Datenbankstruktur zu überarbeiten, um die Effizienz, Leistung und Wartbarkeit der Datenbank zu verbessern. Dieser Prozess wird als Datenbank-Refactoring bezeichnet.

***Beispiel***

Wir haben eine MongoDB-Datenbank, die Informationen über Bücher speichert. Zu diesen Informationen gehört unter anderem der Autor. Die Ausgangslage wird durch folgenden Beispieleintrag beschrieben:

```json
// Vorheriges Datenmodell
{
  "_id": ObjectId("..."),
  "title": "Die Verwandlung",
  "genre": "Fiction",
  "year": 1915,
  "author": {
    "name": "Franz Kafka",
    "birth_year": 1883,
    "nationality": "Austrian"
  }
}
```

Um die Struktur zu optimieren, wurde beschlossen, Autoreninformationen in einem separaten Dokument zu speichern und darauf in den Büchern zu verweisen.

**Neues Datenmodell:**

```json
// Bücher-Dokument
{
  "_id": ObjectId("..."),
  "title": "Die Verwandlung",
  "genre": "Fiction",
  "year": 1915,
  "author_id": ObjectId("...")
}

// Autoren-Dokument
{
  "_id": ObjectId("..."),
  "name": "Franz Kafka",
  "birth_year": 1883,
  "nationality": "Austrian"
}
```

Das Refactoring des Datenmodells bringt mehrere Vorteile mit sich. Durch die Auslagerung der Autoreninformationen in ein separates Dokument wird die Datenbank normalisiert, was die Wartbarkeit und Konsistenz verbessert. Zusätzlich wird die Flexibilität gesteigert, da neue Informationen über Autoren einfach hinzugefügt werden können, ohne das Bücherdokument zu ändern. Die Beziehung zwischen Büchern und Autoren ist nun klar durch die Verwendung von `author_id` definiert. Dadurch können Abfragen nach Autoreninformationen effizienter durchgeführt werden, was zu einer insgesamt verbesserten Leistung der Datenbank führt.


Wir werden uns im Folgenden einige Ansätze ansehen, wie Datenbank-Refactoring bei Dokumentendatenbanken beidurchgeführt werden kann.

## Index-Optimierung:
[20 min]

Die Index-Optimierung ist ein wichtiger Aspekt, um die Effizienz einer MongoDB-Datenbank zu steigern. Bestehende Indizes sollten sorgfältig überprüft und bei Bedarf optimiert werden, um die Abfrageleistung zu verbessern. Bei häufigen Abfragen ist es beispielsweise empfehlenswert, gezielte Indizes hinzuzufügen, um die Datenabfrage zu beschleunigen. Gleichzeitig ist sollten nicht benötigte Indizes zu identifizieren und zu entfernen, um die Schreibgeschwindigkeit zu erhöhen und den Overhead bei Aktualisierungen zu minimieren.

***Beispiel***: Angenommen in einer Sammlung von Kundendaten werden häufig Abfragen nach dem Kundenalter durchgeführt. In diesem Fall könnte ein Index auf dem Feld "Geburtsdatum" hinzugefügt werden, um die Abfrageleistung zu steigern. Ausgangslage ist folgendes Datenmodell:

```json
// Vorheriges Kunden-Dokument
{
  "_id": ObjectId("..."),
  "name": "Max Mustermann",
  "birthdate": ISODate("1990-05-15"),
  "email": "max@example.com",
  // Andere Felder...
}
```

Hier gibt es möglicherweise keine gezielten Indizes auf dem Geburtsdatum-Feld. Diesen fügen wir nun hinzu.

```json
// Aktualisiertes Kunden-Dokument nach Refactoring
{
  "_id": ObjectId("..."),
  "name": "Max Mustermann",
  "birthdate": ISODate("1990-05-15"),
  "email": "max@example.com",
  // Andere Felder...
}
```

Neben den Datenänderungen haben wir einen Index erstellt:

```javascript
// Hinzufügen eines Index auf dem Geburtsdatum-Feld für verbesserte Abfrageleistung
db.customers.createIndex({ "birthdate": 1 });
```


## Datenmodell-Optimierung:
[20 min]

Bei der Überprüfung des Datenmodells auf effiziente Strukturen ist es ratsam, die Datenbankstruktur regelmäßig auf optimal bzgl. der Anforderungen an die Anwendung zu überprüfen. Dies könnte bedeuten, redundante Informationen zu eliminieren, unnötige Felder zu identifizieren oder die Normalisierung von Daten zu überdenken.

Wenn es sinnvoll ist und die Anforderungen der Anwendung dies zulassen, kann das Kombinieren von Dokumenten in MongoDB eine effektive Strategie sein. Durch die Zusammenführung von Informationen in einem Dokument können mehrere Abfragen reduziert werden, was zu einer verbesserten Abfrageleistung führt.

Umgekehrt, wenn Dokumente zu groß sind und Anwendungen häufig nur einen Teil der Daten benötigen, könnte es vorteilhaft sein, große Dokumente zu unterteilen. Dies ermöglicht eine selektivere Abfrage und verbessert die Leseeffizienz, da nur die benötigten Teile des Dokuments geladen werden.

**Beispiel:**

Angenommen, wir haben ein Datenmodell für Bücher mit umfassenden Informationen:

```json
// Vorheriges Buch-Dokument
{
  "_id": ObjectId("..."),
  "title": "Die Verwandlung",
  "genre": "Fiction",
  "year": 1915,
  "author": {
    "name": "Franz Kafka",
    "birth_year": 1883,
    "nationality": "Austrian"
  },
  "publisher": {
    "name": "XYZ Verlag",
    "location": "Berlin"
  },
  // Andere Felder...
}
```


Hier könnten Informationen über den Autor und den Verlag in separaten Dokumenten kombiniert werden, wenn dies zu einer effizienteren Datenabfrage führt.

```json
// Aktualisiertes Buch-Dokument nach Refactoring
{
  "_id": ObjectId("..."),
  "title": "Die Verwandlung",
  "genre": "Fiction",
  "year": 1915,
  "author_id": ObjectId("..."),
  "publisher_id": ObjectId("..."),
  // Andere Felder...
}
```

**Autoren-Dokument:**

```json
// Autoren-Dokument
{
  "_id": ObjectId("..."),
  "name": "Franz Kafka",
  "birth_year": 1883,
  "nationality": "Austrian"
}
```

**Verlags-Dokument:**

```json
// Verlags-Dokument
{
  "_id": ObjectId("..."),
  "name": "XYZ Verlag",
  "location": "Berlin"
}
```

Durch dieses Refactoring könnten Abfragen nach Büchern effizienter gestaltet werden, insbesondere wenn nur Informationen über den Autor oder den Verlag benötigt werden. Es ist wichtig, solche Entscheidungen basierend auf den tatsächlichen Anwendungsanforderungen und Nutzungsverhalten zu treffen. Eine Umsetzung mit Pymongo könnte wie folgt aussehen:

```python
from pymongo import MongoClient

# Verbindung zur MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["deineDatenbank"]

# Bücherkollektion erstellen
books_collection = db["books"]

# Autorenkollektion erstellen
authors_collection = db["authors"]

# Verlagskollektion erstellen
publishers_collection = db["publishers"]

# Iteriere über alle Bücher
for book in books_collection.find():
    # Extrahiere Informationen über den Autor und den Verlag
    author_info = book.get("author", {})
    publisher_info = book.get("publisher", {})

    # Suche oder füge den Autor zur Autorenkollektion hinzu
    author = authors_collection.find_one({"name": author_info.get("name")})
    if not author:
        author_id = authors_collection.insert_one(author_info).inserted_id
    else:
        author_id = author["_id"]

    # Suche oder füge den Verlag zur Verlagskollektion hinzu
    publisher = publishers_collection.find_one({"name": publisher_info.get("name")})
    if not publisher:
        publisher_id = publishers_collection.insert_one(publisher_info).inserted_id
    else:
        publisher_id = publisher["_id"]

    # Aktualisiere das Buchdokument, um auf den Autor und den Verlag zu verweisen
    books_collection.update_one(
        {"_id": book["_id"]},
        {"$set": {"author_id": author_id, "publisher_id": publisher_id}}
    )

# Entferne die veralteten Felder "author" und "publisher" aus den Büchern
books_collection.update_many({}, {"$unset": {"author": "", "publisher": ""}})
```

## Embedded vs. Referenzierte Daten:
[20 min]

Die Entscheidung zwischen dem Einbetten (embedding) von Daten und dem Verknüpfen (referencing) durch Referenzensteht in direkter Verbindung mit der Datenmodell-Optimierung.

Wenn es Sinn macht, bestimmte Daten direkt in ein Dokument einzubetten, kann dies die Abfrageleistung verbessern, da alle benötigten Informationen in einem einzigen Dokument vorhanden sind. Dies kann insbesondere bei Abfragen, die häufig auf diese Daten zugreifen, effizienter sein.

**Beispiel:**

Angenommen, wir haben ein Datenmodell für Blogposts und Kommentare:

```json
// Vorheriges Blogpost-Dokument
{
  "_id": ObjectId("..."),
  "title": "Ein interessanter Blogpost",
  "content": "Inhalt des Blogposts",
  "comments": [
    {
      "author": "Benutzer1",
      "text": "Ein Kommentar."
    },
    {
      "author": "Benutzer2",
      "text": "Ein weiterer Kommentar."
    }
  ]
}
```

Hier sind Kommentare eingebettet, was die Abfrageleistung verbessert, wenn alle Informationen zu einem Blogpost benötigt werden.

Wenn hingegen Aktualisierungen oder Änderungen an den eingebetteten Daten häufig vorkommen und unabhängig von anderen Dokumenten sein können, ist es möglicherweise besser, auf Referenzen zu setzen. Dies kann zu einem verringerten Schreibaufwand führen, da Änderungen nur an einem einzigen Ort vorgenommen werden müssen.

```json
// Aktualisiertes Blogpost-Dokument nach Refactoring
{
  "_id": ObjectId("..."),
  "title": "Ein interessanter Blogpost",
  "content": "Inhalt des Blogposts",
  "comments": [
    ObjectId("comment1_id"),
    ObjectId("comment2_id")
  ]
}
```

```json
// Kommentar 1
{
  "_id": ObjectId("comment1_id"),
  "author": "Benutzer1",
  "text": "Ein Kommentar."
}

// Kommentar 2
{
  "_id": ObjectId("comment2_id"),
  "author": "Benutzer2",
  "text": "Ein weiterer Kommentar."
}
```

In diesem Beispiel wurden die Kommentare als separate Dokumente referenziert. Diese Herangehensweise kann den Schreibaufwand verringern, insbesondere wenn Kommentare häufig aktualisiert oder gelöscht werden. Die Umsetzung könnte wie folgt aussehen:

```python
from pymongo import MongoClient

# Verbindung zur MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["deineDatenbank"]

# Blogposts-Kollektion erstellen
blogposts_collection = db["blogposts"]

# Kommentare-Kollektion erstellen
comments_collection = db["comments"]

# Iteriere über alle Blogposts
for blogpost in blogposts_collection.find():
    # Extrahiere Kommentare aus dem Blogpost
    comments_info = blogpost.get("comments", [])

    # Erstelle separate Kommentare und erhalte die Kommentar-IDs
    comment_ids = []
    for comment_info in comments_info:
        comment_id = comments_collection.insert_one(comment_info).inserted_id
        comment_ids.append(comment_id)

    # Aktualisiere das Blogpost-Dokument mit den Kommentar-IDs
    blogposts_collection.update_one(
        {"_id": blogpost["_id"]},
        {"$set": {"comments": comment_ids}}
    )

# Entferne das veraltete eingebettete Kommentarfeld aus den Blogposts
blogposts_collection.update_many({}, {"$unset": {"comments": ""}})
```



## Datentypen und Validierung:
[20 min]

Bei der Gestaltung eines MongoDB-Datenmodells ist die Verwendung der richtigen Datentypen für Felder wichtig, um den Speicherplatz zu optimieren und eine effiziente Datenverarbeitung sicherzustellen.

**Beispiel:**

Angenommen, wir haben ein Datenmodell für Benutzerprofile:

```json
// Vorheriges Benutzer-Dokument
{
  "_id": ObjectId("..."),
  "username": "user123",
  "age": "25",  // Falscher Datentyp (String statt Zahl)
  "email": "user@example.com",
  // Andere Felder...
}
```

Hier wird das Alter als Zeichenkette (String) statt als Zahl (Number) gespeichert. Das Ändern des Datentyps auf Number würde den Speicherplatz optimieren und eine korrekte Datenrepräsentation ermöglichen.


```json
// Aktualisiertes Benutzer-Dokument nach Refactoring
{
  "_id": ObjectId("..."),
  "username": "user123",
  "age": 25,  // Korrekter Datentyp (Number)
  "email": "user@example.com",
  // Andere Felder...
}
```

Die Verwendung von MongoDB 4.0 oder höher bietet zusätzlich erweiterte Validierungsoptionen, die dazu beitragen können, die Datenintegrität zu verbessern. Dadurch können Regeln für die Datenvalidierung direkt in der Datenbank festgelegt werden.


```javascript
// Validierung für das Benutzer-Dokument
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["username", "age", "email"],
      properties: {
        username: {
          bsonType: "string",
          description: "Username must be a string."
        },
        age: {
          bsonType: "int",
          minimum: 0,
          description: "Age must be a non-negative integer."
        },
        email: {
          bsonType: "string",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
          description: "Email must be a valid email address."
        }
        // Andere Felder...
      }
    }
  }
});
```

In diesem Beispiel wird eine Validierung für das Benutzer-Dokument erstellt, um sicherzustellen, dass die erforderlichen Felder vorhanden sind und die Datentypen den Erwartungen entsprechen. Die Validierungsoptionen können entsprechend den spezifischen Anforderungen der Anwendung angepasst werden.

Die korrekte Verwendung von Datentypen und Validierung in MongoDB trägt dazu bei, Datenintegrität zu gewährleisten und gleichzeitig den Speicherplatz effizient zu nutzen.

## Aggretation Framework:
[10 min]

Das Aggregation Framework haben wir bereits in den vergangenen Abschnittenkennengelernt. Es ermöglicht die Verarbeitung von Daten in der Datenbank, ohne dass die Daten an die Anwendung übertragen werden müssen. Dies kann die Leistung verbessern, insbesondere wenn große Datenmengen verarbeitet werden müssen. Allgemein sind bei Datenbanksprachen die eingebauten Aggregationsfunktionen effizienter als die Verarbeitung von Daten in der Anwendung und sollten daher bevorzugt werden.

## Datenbereinigung:
[10 min]

Die Datenbereinigung ist ein wichtiger Aspekt, um die Effizienz und Leistung von MongoDB-Datenbanken zu verbessern. Durch die Entfernung von nicht mehr benötigten Daten, Indizes oder Sammlungen kann der Speicherplatz optimiert werden. Dies kann insbesondere dann sinnvoll sein, wenn die Datenbankkapazität erreicht ist und die Datenbank nicht mehr effizient arbeitet. Zu der Datenbankbereinigung gehört auch das Archivieren nicht mehr benötigter (historischer) Daten, um die Datenbankgröße zu reduzieren. In diesem Zusammenhang ist auch eine Überprüfung der Backup-Strategie sinnvoll, um die Datensicherheit zu gewährleisten.

## Sharding
[15 min]

Sharding ist eine Technik zur Skalierung von Datenbanken, die es ermöglicht, große Datenmengen über mehrere Server zu verteilen. Diese Methode wird besonders in Umgebungen mit umfangreichen Datenmengen eingesetzt, um die Leistung und Kapazität der Datenbankinfrastruktur zu verbessern.

Im Kontext von MongoDB bezieht sich Sharding auf die horizontale Partitionierung von Daten, bei der der Datenbestand in kleinere Teile, sogenannte Shards, aufgeteilt wird. Jeder Shard ist eine eigenständige Datenbankinstanz, die auf einem separaten Server oder Cluster ausgeführt wird. Durch diese Verteilung können Anwendungen Daten effizient über mehrere Server hinweg verteilen und abfragen.

Ein MongoDB-Shard-Cluster besteht normalerweise aus drei Hauptkomponenten:

1. **Shard(s):** Jeder Shard enthält einen Teil der Datenmenge und ist für die Verwaltung und Speicherung dieser Daten verantwortlich.

2. **Config Server(s):** Diese Server speichern Metadaten über die Verteilung der Daten auf den Shards, wie zum Beispiel Informationen darüber, welche Daten auf welchen Shard verteilt sind.

3. **Query Router (mongos):** Der Query Router ist die Schnittstelle zwischen der Anwendungslogik und dem Sharded Cluster. Er empfängt Abfragen von Anwendungen und leitet sie an die entsprechenden Shards weiter.

Die Entscheidung, welche Daten auf welchem Shard gespeichert werden, kann auf unterschiedlichen Kriterien basieren, wie beispielsweise einem Sharding-Key. Der Sharding-Key ist ein Feld in den Dokumenten, nach dem die Daten auf die Shards verteilt werden. Dieser Key sollte sorgfältig ausgewählt werden, um eine gleichmäßige Verteilung der Daten zu gewährleisten.

Die Verwendung von Sharding in MongoDB ermöglicht eine horizontale Skalierung, was bedeutet, dass die Datenbankkapazität durch das Hinzufügen weiterer Server und Shards erhöht werden kann. Dies ist insbesondere dann vorteilhaft, wenn die Datenmengen so groß sind, dass ein einzelner Server nicht mehr ausreicht, um die Leistungsanforderungen zu erfüllen.


## Weitere Refactoring Möglichkeiten:
[10 min]

Neben den angesprochenen Strategien zur Optimierung von Datenbanken gibt es weitere Möglichkeiten, die Effizienz, Leistung und Sicherheit von MongoDB-Datenbanken zu verbessern. Diese umfassen unter anderem die folgenden Aspekte und Empfehlungen, welche im Rahmen dieses Kurses nicht genauer betrachtet werden:


1. **Sicherheit:** Überprüfe die Sicherheitskonfiguration, Benutzerzugriffe und Rollen.

2. **Dokumentation:** Aktualisiere die Dokumentation deiner MongoDB-Datenbankstruktur für das Entwicklerteam.

3.  **Backup-Strategie:** Überprüfe und optimiere deine Backup-Strategie, um die Datensicherheit zu gewährleisten.

