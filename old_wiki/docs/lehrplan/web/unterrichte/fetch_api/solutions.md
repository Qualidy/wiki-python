# Lösungen

## Abrufen und Anzeigen von Header-Informationen
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

## Aktuelle Wetterdaten abrufen
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

## Wetteranfrage basierend auf Benutzereingabe
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

## Komplex-Aufgabe: Wettervorhersage für mehrere Tage abrufen
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