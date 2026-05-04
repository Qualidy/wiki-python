# Python Requests Library

[60 min]

Kernobjekt der Requests Library ist das `response` Objekt. Vor allem der Status Code kann bei der Implementierung des finalen Projektes helfen.

## Status Code (`response.status_code`)

Gibt den HTTP-Statuscode der Antwort zurück. Zum Beispiel steht `200` für Erfolg, `404` für nicht gefunden und `500` für einen Serverfehler.

```python
if response.status_code == 200:
    print("Erfolgreiche Anfrage!")
```

## Content (`response.content`)

Der rohe Antwortinhalt in Bytes is vor allem nützlich, wenn man mit binären Daten wie Bildern oder PDFs arbeitet.

```python
content = response.content
```

## Text (`response.text`)

Der Antwortinhalt als Unicode-String. Geeignet für Textantworten wie HTML oder JSON.

```python
html_content = response.text
```

## JSON (`response.json()`)

Eine Methode, die den Inhalt der Antwort als JSON interpretiert und in ein Python-Objekt (in der Regel ein Dictionary) umwandelt. Funktioniert nur, wenn der Antwortinhalt gültiges JSON ist.

```python
data = response.json()
```

## Headers (`response.headers`):

Ein Case-Insensitive Dictionary, das alle Antwort-Header enthält.

```python
content_type = response.headers['Content-Type']
```

## Cookies (`response.cookies`):

Ein Requests `CookieJar`-Objekt, das alle Cookies enthält, die in der Antwort gesetzt wurden.

```python
cookies = response.cookies
```

## Error Handling

Die Handhabung von HTTP-Error-Statuscodes in Python, insbesondere bei der Verwendung der Requests Library, ist ein wesentlicher Bestandteil der robusten Netzwerkprogrammierung. 

Fehlercodes wie `404` und `500` signalisieren Probleme, die entweder **clientseitig** (`4xx`) oder **serverseitig** (`5xx`) sind. Eine angemessene Behandlung dieser Fehler stellt sicher, dass Ihr Programm auf solche Probleme richtig reagiert.

Ein Beispiel für das Fehlerhandling kann wie folgt aussehen.

```python
import requests

url = "https://api.example.com/data"

try:
    response = requests.get(url)
    response.raise_for_status()  # Überprüft den Statuscode der Antwort
    
    # Weiterer Code zur Verarbeitung der Antwort, wenn kein Fehler auftritt
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as err:
    # Behandlung von HTTP-Fehlern, die von raise_for_status() geworfen werden
    print(f"HTTP-Fehler aufgetreten: {err}")
except requests.exceptions.RequestException as e:
    # Behandlung aller anderen Requests-bezogenen Fehler
    print(f"Fehler bei der Anfrage: {e}")
```

## Aufgaben

[90 min]

### Aufgabe: Abrufen und Anzeigen von Header-Informationen 🌶️️

Sende Sie eine GET-Anfrage an die [JSON-Placeholder API](https://jsonplaceholder.typicode.com/) und zeige die Header der Antwort an.

<details>
<summary>Lösung</summary>
<pre><code>

import requests

def print_response_headers(url):
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

print_response_headers("https://jsonplaceholder.typicode.com/posts")

</code></pre>
</details>

### Aufgabe: Abrufen und Anzeigen von Cookie-Informationen 🌶️️

Sende eine GET-Anfrage an die [JSON-Placeholder API](https://jsonplaceholder.typicode.com/) und gib die empfangenen Cookies aus.

<details>
<summary>Lösung</summary>
<pre><code>

import requests

def print_response_cookies(url):
    response = requests.get(url)
    print("Cookies empfangen:")
    for cookie in response.cookies:
        print(f"{cookie.name}: {cookie.value}")

print_response_cookies("https://jsonplaceholder.typicode.com/posts")

</code></pre>
</details>

### Aufgabe: Senden und Verarbeiten einer POST-Anfrage 🌶️️🌶️️

Sende eine POST-Anfrage an die [JSON-Placeholder API](https://jsonplaceholder.typicode.com/) und verarbeiten Sie die Antwort.

<details>
<summary>Lösung</summary>
<pre><code>

import requests

def create_post(title, body, user_id):
    data = {'title': title, 'body': body, 'userId': user_id}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    
    if response.status_code == 201:
        print("Erfolgreich erstellt:", response.json())
    else:
        print("Fehler beim Erstellen des Posts")

create_post("Ein neuer Titel", "Dies ist der Body des Posts", 1)

</code></pre>
</details>

### Aufgabe: Abrufen und Speichern von Bildinhalten 🌶️️🌶️️🌶️️

Lade [dieses Bild](https://via.placeholder.com/150) über GET-Anfrage herunter und speichere es lokal.

<details>
<summary>Lösung</summary>
<pre><code>

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

</code></pre>
</details>

## Anspruchsvolle Aufgaben

[45 min]

### Aufgabe: Kombinierte GET- und POST-Anfragen mit Fehlerhandling 🌶️️🌶️️🌶️️

Kombinieren Sie GET- und POST-Anfragen und implementieren Sie umfassendes Fehlerhandling.

- Sende zuerst eine GET-Anfrage, um Daten abzurufen.
- Verwende die Daten aus der GET-Anfrage, um eine Bedingung für eine POST-Anfrage zu definieren.
- Implementiere Fehlerhandling für beide Anfragen.

<details>
<summary>Lösung</summary>
<pre><code>

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

</code></pre>
</details>