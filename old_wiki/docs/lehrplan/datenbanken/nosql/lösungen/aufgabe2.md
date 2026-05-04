# Collection erstellen und User einfügen 🌶

```javascript
// Wechsel zur Datenbank "users" (wenn nicht vorhanden, wird sie automatisch erstellt)
use users

// Füge das Dokument "John Doe" zur Collection hinzu
db.users.insert({
  name: "John Doe"
})

// Zeige alle Dokumente in der "users" Collection an
db.users.find()

// Zeige alle Collections in der aktuellen Datenbank an
show collections
```