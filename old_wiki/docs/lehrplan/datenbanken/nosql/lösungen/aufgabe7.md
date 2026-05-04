## Indizes

**1. Index für das "name"-Feld in der Sammlung "Benutzer":**
```javascript
db.benutzer.createIndex({ name: 1 });
```

**2. Zusammengesetzter Index für die Felder "datum" und "produkt" in der Sammlung "Bestellungen":**
```javascript
db.bestellungen.createIndex({ datum: 1, produkt: 1 });
```

**3. Text-Index für das "titel"-Feld in der Sammlung "Bücher":**
```javascript
db.bücher.createIndex({ titel: "text" });
```

**4. Absteigender Index für das "preis"-Feld in der Sammlung "Produkte":**
```javascript
db.produkte.createIndex({ preis: -1 });
```

**5. Geospatial-Index für das "standort"-Feld in der Sammlung "Benutzer":**
```javascript
db.benutzer.createIndex({ standort: "2dsphere" });
```

**6. Hash-Index für das "email"-Feld in der Sammlung "Kunden":**
```javascript
db.kunden.createIndex({ email: "hashed" });
```

**7. Teil-Index für das "produkt"-Feld in der Sammlung "Bestellungen":**
```javascript
db.bestellungen.createIndex({ produkt: 1 }, { partialFilterExpression: { produkt: { $exists: true } } });
```

**8. Einzigartiger Index für das "name"-Feld in der Sammlung "Produkte":**
```javascript
db.produkte.createIndex({ name: 1 }, { unique: true });
```

**9. Index mit Ablaufzeit für das "datum"-Feld in der Sammlung "Bestellungen":**
```javascript
db.bestellungen.createIndex({ datum: 1 }, { expireAfterSeconds: 0 });
```

**10. Sparse-Index für das "alter"-Feld in der Sammlung "Benutzer":**
```javascript
db.benutzer.createIndex({ alter: 1 }, { sparse: true });
```
