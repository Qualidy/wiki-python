# Fetch API in JavaScript

[60 min]

Auch für JavaScript gibt es die Möglichkeit, eigene und externe APIs anzusprechen. Die `fetch`-API ermöglicht es, wie mit `requests` in Python, HTTP-Anfragen zu stellen und Antworten und Fehler zu handeln.

Ein wesentlicher Unterschied zwischen Python und JavaScript ist, dass `requests` in Python **synchron** ist, während die Fetch API in JavaScript **asynchron** arbeitet.

## Asynchrone Anfragen und asynchrone Programmierung

Asynchrone Anfragen sind wichtig, um Daten im Hintergrund zu laden, ohne die Benutzeroberfläche zu blockieren. In JavaScript wird dies oft über `Promises` und das `Async/Await`-Pattern realisiert.

**`Promises`**: Ein Promise ist ein Objekt, das für einen Wert steht, der in der Zukunft verfügbar sein könnte. Es kann sich in einem von drei Zuständen befinden: erfüllt, abgelehnt oder ausstehend.

```javascript
fetch('https://api.example.com/data')
    .then(data => console.log('Geladene Daten:', data))
    .catch(error => console.error('Fehler:', error));
```

**`Async/Await`**: Ist eine moderne Art, asynchronen Code zu schreiben. `async` markiert eine Funktion als asynchron, und `await` wartet auf das Ergebnis eines Promises.

```javascript
async function fetchData() {
    try {
        let response = await fetch('https://api.example.com/data');

        let data = await response.json();
        console.log('Geladene Daten:', data);
    } catch (error) {
        console.error('Fehler:', error);
    }
}

fetchData();
```

```javascript
async function fetchMultipleData() {
    try {
        let [response1, response2] = await Promise.all([
            fetch('https://api.example.com/data1'),
            fetch('https://api.example.com/data2')
        ]);

        let data1 = await response1.json();
        let data2 = await response2.json();

        console.log('Geladene Daten 1:', data1);
        console.log('Geladene Daten 2:', data2);
    } catch (error) {
        console.error('Fehler beim Laden der Daten:', error);
    }
}

fetchMultipleData();
```

## Requests mit der Fetch API

Die Fetch API bietet natürlich, wie Python `requests`, zugang zu allen HTTP-Methoden wie GET, POST, PUT und DELETE.

`GET`

```javascript
fetch('https://api.example.com/data')
  .then(data => console.log('Geladene Daten:', data))
  .catch(error => console.error('Fehler:', error));
```

`POST`

```javascript
fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({name: 'Neuer Eintrag'})
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## Error Handling

Durch die Struktur der `fetch`-API und der Nutzung vom `Promise`-Modell ist die Fehlerbehandlung durch die `.catch`-Funktion bereits gegeben.

```javascript
fetch('https://api.example.com/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('Netzwerkantwort nicht ok');
        }
        return response.json();
    })
    .catch(error => console.error('Fetch-Fehler:', error));
```

## Aufgaben

[60 min]

### Abrufen und Anzeigen von Header-Informationen 🌶️️🌶️️

Verwende JavaScript, um eine GET-Anfrage an die JSON-Placeholder API zu senden und die Header der Antwort anzuzeigen.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Header-Informationen abrufen</title>
</head>
<body>
    <script>
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then(response => {
                console.log('Header-Informationen:', response.headers);
                return response.json();
            })
            .then(data => console.log(data))
            .catch(error => console.error('Ein Fehler ist aufgetreten:', error));
    </script>
</body>
</html>
```

</details>

### Aktuelle Wetterdaten abrufen 🌶️️🌶️️

Verwende die Fetch API, um aktuelle Wetterdaten von der [Open-Meteo API](https://open-meteo.com/) abzurufen und in der Konsole anzuzeigen.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Wetteranfrage</title>
</head>
<body>
    <input type="text" id="latitude" placeholder="Breitengrad">
    <input type="text" id="longitude" placeholder="Längengrad">
    <button id="abfrageButton">Wetter abfragen</button>
    <div id="wetterErgebnis"></div>

    <script>
        document.getElementById('abfrageButton').addEventListener('click', function() {
            let latitude = document.getElementById('latitude').value;
            let longitude = document.getElementById('longitude').value;
            
            fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('wetterErgebnis').innerText = JSON.stringify(data, null, 2);
                })
                .catch(error => console.error('Fehler:', error));
        });
    </script>
</body>
</html>
```

</details>

### Wetteranfrage basierend auf Benutzereingabe 🌶️️🌶️️🌶️️

Erstelle eine interaktive Benutzeroberfläche, bei der Benutzer einen Standort eingeben können und das Wetter für diesen Ort angezeigt wird.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>7-Tage Wettervorhersage</title>
</head>
<body>
    <input type="text" id="location" placeholder="Ort">
    <button id="forecastButton">Vorhersage anzeigen</button>
    <div id="forecastResult"></div>

    <script>
        document.getElementById('forecastButton').addEventListener('click', function() {
            let location = document.getElementById('location').value;
            // Hier müsste eine Funktion implementiert werden, die die Koordinaten für den eingegebenen Ort abruft.
            let latitude = '52.52'; // Beispiel Koordinaten für Berlin
            let longitude = '13.405';
            
            fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto`)
                .then(response => response.json())
                .then(data => {
                    let forecastHtml = data.daily.time.map((time, index) => {
                        return `<div>
                                    <h4>${time}</h4>
                                    <p>Max Temp: ${data.daily.temperature_2m_max[index]}°C</p>
                                    <p>Min Temp: ${data.daily.temperature_2m_min[index]}°C</p>
                                    <p>Wettercode: ${data.daily.weathercode[index]}</p>
                                </div>`;
                    }).join('');
                    document.getElementById('forecastResult').innerHTML = forecastHtml;
                })
                .catch(error => console.error('Fehler:', error));
        });
    </script>
</body>
</html>
```

</details>

## Anspruchsvolle Aufgaben

[45 min]

### Wettervorhersage für mehrere Tage abrufen 🌶️️🌶️️🌶️️🌶️️

Entwickle eine Anwendung, die eine 7-Tage-Wettervorhersage für einen eingegebenen Standort liefert.

- Sende eine GET-Anfrage an die Open-Meteo API, um die 7-Tage-Wettervorhersage für den angegebenen Standort zu erhalten.
- Zeige die Wettervorhersage (z.B. Temperatur, Wetterbedingungen) für jeden Tag auf der Webseite an.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>7-Tage Wettervorhersage</title>
</head>
<body>
    <input type="text" id="location" placeholder="Ort">
    <button id="forecastButton">Vorhersage anzeigen</button>
    <div id="forecastResult"></div>

    <script>
        document.getElementById('forecastButton').addEventListener('click', function() {
            let location = document.getElementById('location').value;
            // Hier müsste eine Funktion implementiert werden, die die Koordinaten für den eingegebenen Ort abruft.
            let latitude = '52.52'; // Beispiel Koordinaten für Berlin
            let longitude = '13.405';
            
            fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto`)
                .then(response => response.json())
                .then(data => {
                    let forecastHtml = data.daily.time.map((time, index) => {
                        return `<div>
                                    <h4>${time}</h4>
                                    <p>Max Temp: ${data.daily.temperature_2m_max[index]}°C</p>
                                    <p>Min Temp: ${data.daily.temperature_2m_min[index]}°C</p>
                                    <p>Wettercode: ${data.daily.weathercode[index]}</p>
                                </div>`;
                    }).join('');
                    document.getElementById('forecastResult').innerHTML = forecastHtml;
                })
                .catch(error => console.error('Fehler:', error));
        });
    </script>
</body>
</html>
```

</details>
