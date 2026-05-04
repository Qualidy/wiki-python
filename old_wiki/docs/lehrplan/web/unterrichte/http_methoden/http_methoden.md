# HTTP Elemente Deep Dive

[60 min]

Auch wenn wir im späteren Verlauf der Woche Postman nochmals nutzen werden, fokussierne wir uns auf die Nutzung der Python Requests Library. Wir werden uns die verschiedenen Methoden, Header, Parameter und Payloads ansehen, die für die Kommunikation mit Webdiensten und APIs verwendet werden.

## HTTP Methoden

Im vorherigen Kapitel haben wir bereits kurz die Methoden für HTTP Request kennengelernt.
Wichtig zu verstehen ist, dass diese eine zentrale Rolle bei der Verwendung mit Python Requests einnehmen.

Hier ein detaillierter Blick auf die wichtigsten HTTP-Methoden im Kontext der Python Requests.

### GET

Die GET-Methode wird verwendet, um Daten von einem Server abzurufen. Es ist die am häufigsten verwendete HTTP-Methode und wird für Anfragen eingesetzt, die keine Änderung des Serverzustands bewirken.

```python
response = requests.get('https://api.example.com/data')
```

Parameter für die Abfrage können über das `params` Attribut übergeben werden.

```python
params = {
  'key': 'value'
}

response = requests.get('https://api.example.com/data', params=params)
```

### POST

POST wird verwendet, um neue Daten an den Server zu senden. Es ist typischerweise die Methode der Wahl, wenn es darum geht, neue Ressourcen zu erstellen, wie z.B. einen neuen Eintrag in einer Datenbank. Daten ([Payloads](#payloads)) werden über das `data` Argument übergeben.

```python
response = requests.post('https://api.example.com/data', data={'key': 'value'})
```

### PUT

PUT wird eingesetzt, um bestehende Daten auf dem Server zu aktualisieren oder zu ersetzen. Wenn die spezifizierte Ressource nicht existiert, kann sie neu erstellt werden.

```python
response = requests.put('https://api.example.com/data/1', data={'key': 'new_value'})
```

### DELETE

Wie der Name schon sagt, wird die DELETE-Methode verwendet, um Ressourcen vom Server zu entfernen.

```python
response = requests.delete('https://api.example.com/data/1')
```

## Payloads

Bei HTTP-Requests, insbesondere bei POST und PUT, spielt der "Data Payload" (auch Request Body) eine zentrale Rolle. Data Payloads transportieren die erforderlichen Informationen, um eine Aktion auf dem Server auszuführen, wie z.B. das Hinzufügen eines neuen Benutzers oder das Aktualisieren eines Produkts.

Payloads sind flexibel im Format und können sowohl Text, JSON, XML, Dateiuploads als auch andere Datenformate enthalten. Wichtig hierbei ist vor allem der [Content-Type Header](#headers) um den Typ des Payloads zu definieren (z.B. application/json für JSON-Daten).

## Headers

HTTP-Headers sind essentiell in HTTP-Anfragen und -Antworten. Es sind simple Key-Value-Paare, die wichtige Informationen über die Anfrage oder Antwort liefern. Headers können eine Vielzahl von Daten, wie Metadaten, Authentifizierungsinformationen und Informationen über Codierung, Sprache und Authentifizierung enthalten.

### Content-Type

Beschreibt den Medientyp (MIME-Typ) des Inhalts im Body der HTTP-Anfrage oder -Antwort.

`Content-Type: application/json` - für JSON-Daten.

`Content-Type: text/plain` - für Klartext.

`Content-Type: multipart/form-data` - für Formulardaten mit Datei-Uploads.

`Content-Type: application/x-www-form-urlencoded` - für  Formulardaten in URL-kodierter Form.

#### Beispiel

```python
data = {'key': 'value'}
headers = {'Content-Type': 'application/json'}
response = requests.post('https://api.example.com/data', json=data, headers=headers)
```

### Authorization

Übermittelt Authentifizierungsinformationen zum Server.

`Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==` - für Basic Auth (Base64-kodierte Benutzername:Passwort-Kombination).

`Authorization: Bearer YOUR_TOKEN` - für Authentifizierungsstandards wie OAuth 2.0 

#### Beispiel

```python
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get('https://api.example.com/protected', headers=headers)
```

### Cookie

Überträgt Cookies vom Client zum Server.
Beispiel:

`Cookie: session_id=abc123` - für Infos zur Session

`Cookie: id=a3fWa; isLoggedIn=true` - für mehrere Cookies.

#### Beispiel

```python
cookies = {'session_id': '123456'}
response = requests.get('https://api.example.com/data', cookies=cookies)
```

## Komplexere Aufgaben

### Aufgabe 1: Währungsumrechner

Erstelle ein Python-Skript, das den Umrechnungskurs zwischen zwei Währungen abruft und diesen verwendet, um einen Betrag von der einen in die andere Währung umzurechnen.
Nutze die https://www.exchangerate-api.com/, eine kostenlose API für Währungsumrechnungen. Hole dir einen kostenlosen API-Key.

Das Skript sollte den Benutzer auffordern, zwei Währungscodes (z. B. USD, EUR) 
und den umzurechnenden Betrag einzugeben. Sende eine GET-Anfrage an die ExchangeRate-API, um die aktuellen Wechselkurse zwischen den gewählten Währungen zu erhalten.

Verwende den erhaltenen Wechselkurs, um den Betrag in die Zielwährung umzurechnen. Gib das Ergebnis der Umrechnung auf dem Bildschirm aus.

Füge Fehlerbehandlungen hinzu, um auf mögliche Probleme wie ungültige Währungscodes oder Netzwerkfehler angemessen zu reagieren.

### Aufgabe 2: Büchersuche mit der Open Library API

Entwickle ein Python-Skript, das die Open Library API verwendet, um Informationen zu Büchern basierend auf einem vom Benutzer einegebenen Titel oder Autor abzurufen.
Besuche die Open Library API (https://openlibrary.org/developers/api) Dokumentation, um mehr über die verfügbaren Endpunkte zu erfahren.

Das Skript sollte den Benutzer auffordern, einen Suchbegriff (z.B. Titel oder Autor) einzugeben. Nutze [bullet](https://github.com/bchao1/bullet) um die CLI noch visueller und interaktiver zu machen.

Sende eine GET-Anfrage an die Open Library API, um Informationen zu Büchern zu erhalten, die dem Suchbegriff entsprechen. Parse die Antwort der API und zeige relevante Informationen über die gefundenen Bücher an, wie Titel, Autor, Veröffentlichungsjahr und eine kurze Beschreibung.

Füge Funktionen hinzu, um nach verschiedenen Kriterien zu filtern oder sortieren, wie Veröffentlichungsjahr oder Popularität.
