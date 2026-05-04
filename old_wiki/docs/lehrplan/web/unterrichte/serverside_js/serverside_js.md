# JavaScript außerhalb des Browsers

[45 min]

Seit 2009 gibt es zusätzlich zur `Client`-seitigen Entwicklung auch die Möglichkeit `Server`-seitig mit Javascript zu entwickeln. [Node.js](https://nodejs.org) nutzt die V8 JavaScript Engine von Google Chrome und Kernkonzepte wie eine Asynchrone, ereignisgesteuerte Architektur, um eine skalierbare Netzwerkanwendungen anzubieten.

## Serverseitige Programmierung mit Node.js und Express

Vergleichbar mit Flask in Python, ermöglicht die Kombination von Node.js und [Express](https://expressjs.com/) das Erstellen von serverseitigen Anwendungen, die HTTP-Anfragen bearbeiten können.

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hallo Welt!');
});

app.listen(3000, () => {
    console.log('Server läuft auf Port 3000');
});
```

## Modularität und Strukturierung

Module in Node.js, wie Express, ermöglichen das Teilen des Codes in kleinere, wiederverwendbare Einheiten. Diese Module (oder auch Libraries) können von jedem erstellt und über den Node Package Manager ([npm](https://www.npmjs.com/)) zur Verfügung gestellt werden.

```javascript
// export in einer Datei
export function meineFunktion() { /*...*/ }

// import in einer anderen Datei
import { meineFunktion } from './meineModulDatei';
```

## Node Package Manager (NPM)

NPM ist ein zentrales Repository für Node.js-Pakete welche das Hinzufügen, Aktualisieren und Verwalten von Bibliotheken und Tools deutlich vereinfacht.

```javascript
// meinModul.js
exports.meineFunktion = function() {
    console.log("Hallo Welt!");
};
```

```javascript
// app.js
const meinModul = require('./meinModul');
meinModul.meineFunktion(); // "Hallo Welt!"
```
