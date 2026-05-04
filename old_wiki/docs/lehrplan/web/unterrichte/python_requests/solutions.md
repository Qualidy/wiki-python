# Lösungen

## Abrufen und Anzeigen von Header-Informationen
```python
import requests

def print_response_headers(url):
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

print_response_headers("https://jsonplaceholder.typicode.com/posts")
```

## Abrufen und Anzeigen von Cookie-Informationen
```python
import requests

def print_response_cookies(url):
    response = requests.get(url)
    print("Cookies empfangen:")
    for cookie in response.cookies:
        print(f"{cookie.name}: {cookie.value}")

print_response_cookies("https://jsonplaceholder.typicode.com/posts")
```

## Senden und Verarbeiten einer POST-Anfrage
```python
import requests

def create_post(title, body, user_id):
    data = {'title': title, 'body': body, 'userId': user_id}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    
    if response.status_code == 201:
        print("Erfolgreich erstellt:", response.json())
    else:
        print("Fehler beim Erstellen des Posts")

create_post("Ein neuer Titel", "Dies ist der Body des Posts", 1)
```

## Abrufen und Speichern von Bildinhalten
```python
import requests

def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Bild erfolgreich gespeichert als {filename}")
    else:
        print("Fehler beim Herunterladen des Bildes")

download_image("https://via.placeholder.com/150", "test_image.png")
```

## Komplex-Aufgabe: Kombinierte GET- und POST-Anfragen mit Fehlerhandling
```python
import requests

def combined_get_post_request(get_url, post_url):
    try:
        get_response = requests.get(get_url)
        get_response.raise_for_status()

        # Erste Element aus der GET-Antwort
        post_data = get_response.json()[0] 
        post_response = requests.post(post_url, json=post_data)
        post_response.raise_for_status()

        print("POST-Antwort:", post_response.json())

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP-Fehler aufgetreten: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Fehler bei der Anfrage: {err}")

combined_get_post_request("https://jsonplaceholder.typicode.com/posts", "https://jsonplaceholder.typicode.com/posts")
```




