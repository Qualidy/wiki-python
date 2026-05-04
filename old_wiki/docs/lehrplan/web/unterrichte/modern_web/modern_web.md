# Modern Web Applications

[60 min]

Moderne Webanwendungen sind um ein vielfaches komplexer als die einfachen Websites und JS-Skripte die wir bisher entworfen haben. Der Deep Dive in diese Themen würde den Rahmen hier komplett sprengen. Es ist trotzdem wichtig, die folgenden Themen zur Einordnung kurz gehört zu haben.

## Web APIs

Web-APIs bieten Schnittstellen zwischen JavaScript und Browserfunktionen bzw. Hardware, die weit über das Anzeigen von Webseiten hinausgehen.

### Geolocation API

Ermöglicht den Zugriff auf geografische Standortdaten und bietet Websites oder Apps die Möglichkeit, Karten oder lokale Geschäftssuche einzubinden.

```javascript
navigator.geolocation.getCurrentPosition(function(position) {
    console.log("Breitengrad: " + position.coords.latitude);
    console.log("Längengrad: " + position.coords.longitude);
});
```

### Canvas API

Ermöglicht das Zeichnen von 2D- und 3D-Grafiken um z.B. Spiele, Grafikeditoren oder interaktive Bildungsanwendungen zu erstellen.

```javascript
let canvas = document.getElementById('meinCanvas');
let ctx = canvas.getContext('2d');
ctx.fillStyle = 'green';
ctx.fillRect(10, 10, 100, 100);
```

### Web Storage API

Speichert Daten im Browser des Benutzers und ermöglicht z.B. das Speichern von Benutzerpräferenzen oder Warenkorbinhalten.

```javascript
localStorage.setItem('username', 'MaxMustermann');
console.log(localStorage.getItem('username'));
```

### WebRTC (Web Real-Time Communication)

Ermöglicht Audio- und Video-Kommunikation in Echtzeit für Tools wie Video-Chat und Online-Konferenz-Tools.

```javascript
// Hinweis: WebRTC benötigt ein komplexeres Setup für Peer-Verbindungen.
let pc = new RTCPeerConnection();
// ...weitere Konfiguration für Video-Chat...
```

### Service Workers

Ermöglicht Funktionen im Hintergrund, wie das Zwischenspeichern von Webseiten für das Offline-Browsing, was speziell interessant für Progressive Web Apps (PWAs) ist, die schnelles Laden und Offline-Funktionalität bieten.

```javascript
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').then(function(registration) {
        console.log('Service Worker registriert:', registration);
    });
}
```

### Web Audio API

Ermöglicht das Abspielen und Manipulieren von Audioinhalten für z.B. Musik-Apps und Spiele mit Audioeffekten.

```javascript
let audioContext = new AudioContext();
let oscillator = audioContext.createOscillator();
oscillator.connect(audioContext.destination);
oscillator.start();
```

## Moderne JavaScript-Frameworks und -Bibliotheken

Die wohl relevanteste Entwicklung im Bereich der Webentwicklung sind Frameworks wie Angular, React und Vue. Sie sind sehr populär und werden meist zur Erstellung von komplexeren und interaktiven Benutzeroberflächen genutzt.

### React

Entwickelt von Facebook, ist [React](https://react.dev/) eine der führenden Bibliotheken für die Erstellung von Benutzeroberflächen. Sie ermöglicht es Entwicklern, komplexe Benutzeroberflächen aus kleinen, wiederverwendbaren Komponenten zu erstellen. Eines der Hauptmerkmale von React ist JSX, eine Syntaxerweiterung, die es erlaubt, HTML-Code in JavaScript zu schreiben. Dies macht den Code übersichtlicher und leichter zu verstehen. Reacts effizientes Update- und Rendering-System ermöglicht es, dass nur die Komponenten, die sich ändern, neu gerendert werden.

```javascript
// React-Komponente mit JSX
class Begrüßung extends React.Component {
  render() {
    return <h1>Hallo, {this.props.name}!</h1>;
  }
}

// Verwendung der Komponente
<Begrüßung name="Max" />
```

### Vue

[Vue.js](https://vuejs.org/), oft als progressives Framework bezeichnet, zeichnet sich durch seine einfache und flexible Struktur aus. Es erleichtert das Erstellen interaktiver UIs durch ein reaktives und datengetriebenes Modell. Änderungen an Daten führen automatisch zu Updates in der Benutzeroberfläche. Vue ist bekannt für seine Leichtigkeit und schnelle Einarbeitung, was es zu einer beliebten Wahl für viele Entwickler macht.

```js
// Vue-Instanz
new Vue({
  el: '#app',
  data: {
    message: 'Hallo Vue!'
  }
});

// HTML-Template
<div id="app">
  {{ message }}
</div>
```

## Anspruchsvolle Aufgaben

[90 min]

### Standortbasierte Wetteranzeige mit Geolocation API 🌶️️🌶️️🌶️️🌶️️

Erstelle eine Webanwendung, die die Geolocation API verwendet, um den aktuellen Standort des Benutzers zu ermitteln und darauf basierend Wetterinformationen von einer externen API (z.B. Open-Meteo) anzeigt.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Wetteranzeige</title>
</head>
<body>
    <h1>Wetterinformationen für Ihren Standort</h1>
    <div id="wetterInfo">Lade Wetterdaten...</div>

    <script src="script.js"></script>
</body>
</html>
```

```js
function fetchWeather(latitude, longitude) {
    const apiUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m`;
    
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const wetterInfo = data.hourly.temperature_2m[0] + ' °C';
            document.getElementById('wetterInfo').textContent = 'Aktuelle Temperatur: ' + wetterInfo;
        })
        .catch(error => {
            console.error('Fehler beim Abrufen der Wetterdaten:', error);
            document.getElementById('wetterInfo').textContent = 'Wetterdaten konnten nicht geladen werden.';
        });
}

function handleGeolocationError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            updateWetterInfo('Zugriff auf Standort wurde verweigert.');
            break;
        case error.POSITION_UNAVAILABLE:
            updateWetterInfo('Standortinformationen sind nicht verfügbar.');
            break;
        case error.TIMEOUT:
            updateWetterInfo('Anfragezeit für Standort abgelaufen.');
            break;
        default:
            updateWetterInfo('Ein unbekannter Fehler ist aufgetreten.');
            break;
    }
}

function updateWetterInfo(message) {
    document.getElementById('wetterInfo').textContent = message;
}

if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(position => {
        fetchWeather(position.coords.latitude, position.coords.longitude);
    }, handleGeolocationError);
} else {
    updateWetterInfo('Geolocation wird von Ihrem Browser nicht unterstützt.');
}
```

</details>

### Interaktiver Zeichenbereich mit Canvas API 🌶️️🌶️️🌶️️🌶️️

Erstelle eine Webanwendung, die die Canvas API nutzt, um einen interaktiven Zeichenbereich zu implementieren. Benutzer sollen in der Lage sein, mit der Maus auf dem Canvas zu zeichnen.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Canvas Zeichenbereich</title>
</head>
<body>
    <canvas id="zeichencanvas" width="500" height="500" style="border:1px solid #000;"></canvas>
    <button onclick="clearCanvas()">Canvas löschen</button>

    <script>
        let canvas = document.getElementById('zeichencanvas');
        let ctx = canvas.getContext('2d');
        let drawing = false;

        function startDrawing(e) {
            drawing = true;
            draw(e);
        }

        function endDrawing() {
            drawing = false;
            ctx.beginPath();
        }

        function draw(e) {
            if (!drawing) return;

            ctx.lineWidth = 3; // Dicke des Zeichenstifts
            ctx.lineCap = 'round'; // Form der Linie

            ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        }

        function clearCanvas() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }

        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mouseup', endDrawing);
        canvas.addEventListener('mousemove', draw);
    </script>
</body>
</html>
```

</details>
