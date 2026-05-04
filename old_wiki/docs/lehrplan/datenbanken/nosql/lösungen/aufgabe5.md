# Index erstellen

```bash
// Erstelle einen Index auf dem Feld "name" in der Collection "meineCollection"
db.meineCollection.createIndex({ name: 1 })

// Zeige alle Indizes für die Collection "meineCollection"
db.meineCollection.getIndexes()

// Lösche den Index auf dem Feld "name" in der Collection "meineCollection"
db.meineCollection.dropIndex({ name: 1 })
```