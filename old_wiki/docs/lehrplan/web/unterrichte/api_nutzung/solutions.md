# Lösungen

## 1. CURL
```js
curl "https://api.open-meteo.com/v1/forecast?latitude=52.5200&longitude=13.4050&current_weather=true"
```

## 2. Python Requests
```python
import requests

def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Fehler bei der Anfrage")

get_weather_data(52.5200, 13.4050)
```

## 3. Postman
- Öffne Postman
- Erstelle eine neue GET-Anfrage mit der URL: https://api.open-meteo.com/v1/forecast
- Füge die folgenden Query-Parameter hinzu: latitude=52.5200 und longitude=13.4050
- Sende die Anfrage und betrachte die Antwort.
![Postman Wetter Request](../../images/postman_get_wetter.png)

## 4. API Request an weiteren Wetterservice
```python
# Verwenden Sie CURL oder Python, um die Anfrage zu senden. Beispiel mit CURL:
curl "https://api.brightsky.dev/weather?lat=52.5200&lon=13.4050"

# Oder mit Python:
def get_weather_brightsky(latitude, longitude):
    url = f"https://api.brightsky.dev/weather?lat={latitude}&lon={longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Fehler bei der Anfrage")

get_weather_brightsky(52.5200, 13.4050)
```