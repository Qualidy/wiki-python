# Lösungen

## Standortbasierte Wetteranzeige mit Geolocation API
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

## Interaktiver Zeichenbereich mit Canvas API 
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