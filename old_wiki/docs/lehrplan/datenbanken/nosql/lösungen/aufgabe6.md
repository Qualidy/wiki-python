# Eigenschaften des Index

```javascript
// Erstelle einen Index auf dem Feld "name" in der Collection "meineCollection"
db.meineCollection.createIndex({ name: 1 })

// Zeige alle Indizes für die Collection "meineCollection"
db.meineCollection.getIndexes()

// Zeige die Eigenschaften des Indexes für die Collection "meineCollection"
var indexInfo = db.meineCollection.getIndexes().filter(index => index.name === "name_1")[0];
printjson(indexInfo);
```

- **`name`**: Der Name des Indexes. Im Beispiel ist es "name_1".
- **`key`**: Das Feld, nach dem der Index erstellt wurde, und die Sortierreihenfolge (1 für aufsteigend, -1 für absteigend).
- **`ns`**: Der Namespace, der die Datenbank und die Collection angibt.
- **`v`**: Die Version des Indexformats.
- **`background`**: Gibt an, ob der Index im Hintergrund erstellt wurde (true) oder blockierend (false).
- **`unique`**: Gibt an, ob der Index eindeutige Werte erzwingt (true/false).
- **`sparse`**: Gibt an, ob der Index nur für Dokumente erstellt wird, die das entsprechende Feld haben (true/false).
- **`expireAfterSeconds`**: Wenn der Index für TTL (Time-to-Live) verwendet wird, gibt diese Eigenschaft an, nach wie vielen Sekunden Dokumente ablaufen sollen.
