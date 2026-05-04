# Lösungsskizze Migration

**Teil 1: Datenbankerstellung und Testumgebung**

```python
from pymongo import MongoClient

# Datenbankerstellung mit PyMongo
def create_database():
    client = MongoClient('localhost', 27017)
    db = client['example_database']
    collection = db['users']

    test_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22}
    ]

    collection.insert_many(test_data)
    client.close()

create_database()
```

Für den Docker-Container können wir eine `docker-compose.test.yml`-Datei erstellen:


```yaml
version: '3'
services:
mongodb:
   image: mongo
   container_name: mongodb-test
   ports:
      - "27017:27017"
   environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
   volumes:
      - ./data:/data/db
```

Dann führen wir den Container mit dem Befehl `docker-compose -f docker-compose.test.yml up` aus.

**Teil 2: Datenbankmigration und Produktionsumgebung**

```python
from pymongo import MongoClient

# Datenbankmigrationsskript
def perform_migration():
    client = MongoClient('localhost', 27017)
    db = client['example_database']
    collection = db['users']

    # Beispiel-Migration: Ändere den Datentyp des "age"-Feldes von int zu str
    documents_to_update = collection.find({"age": {"$type": "int"}})

    for document in documents_to_update:
        new_age = str(document["age"])
        collection.update_one({"_id": document["_id"]}, {"$set": {"age": new_age}})

    client.close()

perform_migration()
```

Für den Docker-Container können wir eine `docker-compose.prod.yml`-Datei erstellen:


```yaml
version: '3'
services:
mongodb:
   image: mongo
   container_name: mongodb-prod
   ports:
      - "27017:27017"
   environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
   volumes:
      - ./data:/data/db
```

Dann führen wir den Container mit dem Befehl `docker-compose -f docker-compose.prod.yml up` aus.

**Rollback-Plan:**

Wir könnten vor Ausrollen des Migrations-Skripts ein Backup der Datenbank erstellen. Wenn das Skript fehlschlägt, können wir die Datenbank wiederherstellen und den Container neu starten.

```bash
mongodump --db your_database_name --out /path/to/backup/folder
```

Das Wiederherstellen des Backups bei fehlgeschlagener Migration kann mit dem folgenden Befehl erfolgen:

```bash
mongodump --db your_database_name --out /path/to/backup/folder
```

**Kommunikation und Dokumentation:**

Für das Logging können wir beispielweise das Logging von MongoDB verwenden. Mehr dazu finden wir in dem vorherigen Abschnitt zu Sicherheitsmechanismen für MongoDB.

```yaml
# Konfigurationsdatei (mongod.conf)
auditLog:
  destination: file
  path: /var/log/mongodb/audit.log
```

