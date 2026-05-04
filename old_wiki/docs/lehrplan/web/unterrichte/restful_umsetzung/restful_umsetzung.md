# Umsetzung einer RESTful API in Flask

[60 min]

## Routen

Das Kernstück jeder Flask-Anwendung sind die Routen, die bestimmen, wie Anfragen an verschiedene URLs gehandhabt werden.

```python
@app.route('/')
def home():
    return "Hallo Welt!"
```

RESTful Design definiert die Existenz der CRUD Operationen. Mit Flask können wir diese Endpoints wie folgt abbilden. Das explizite Angeben der unterstützen Methoden macht den Code auszeichnender und hilft bei der späteren Generierung der Dokumentation.

**GET**: Abrufen von Nutzerdaten. (Basisroute):

```python
@app.route('/users', methods=['GET'])
def get_users():
    # Logik, um Benutzerdaten abzurufen
```

**POST**: Erstellen eines neuen Nutzers (Basisroute).

```python
@app.route('/users', methods=['POST'])
def create_user():
    # Logik, um einen neuen Benutzer zu erstellen
```

**PUT**: Aktualisieren eines bestehenden Nutzers (Variable Route).

```python
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    # Logik, um Benutzerdaten zu aktualisieren
```

**DELETE**: Löschen eines Nutzers (Variable Route).

```python
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Logik, um einen Benutzer zu löschen
```

### Aufgabe: Einfache GET-Route für Benutzerliste 🌶️️

Erstelle eine Route, die eine simulierte Liste von Benutzern zurückgibt.

<details>
<summary>Lösung</summary>

<pre><code>
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
</code></pre>
</details>

### Aufgabe: DELETE-Route zum Löschen eines Benutzers 🌶️️🌶️️

Implementiere eine DELETE-Route, um einen Benutzer zu löschen.

<details>
<summary>Lösung</summary>

<pre><code>
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({"message": "Benutzer gelöscht"}), 200
</code></pre>
</details>

## Datenverarbeitung

Die Datenverarbeitung, z.B. von JSON Daten, sowohl als Payload in der Anfrage als auch in der Antwort ist für die effiziente Nutzung von APIs relevant. Deshalb bietet Flask das `request`-Objekt um Daten aus Anfragen abzurufen.

```python
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    # Verarbeiten von user_data
```

Für das einfach Senden von JSON-Objekten in der Antwort nutzen wir `jsonify`.

```python
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # Angenommene Hilfsfunktion zur Datenbankabfrage
    user = get_user_by_id(id)  
    return jsonify(user)
```

Für das handling von Form-Daten gibt es ein Objektattribute namens `form`. Es beinhaltet alle request-Formular Daten.

```python
@app.route('/submit-form', methods=['POST'])
def handle_data():
    name = request.form['name']
    age = request.form['age']
    # Verarbeiten der Daten
    return jsonify({"message": "Formular erhalten"}), 200
```

### Aufgabe: POST-Route zum Hinzufügen neuer Benutzer 🌶️️🌶️️

Erstelle eine Route, um neue Benutzer hinzuzufügen. Nimm Benutzerdaten aus der Anfrage auf und füge sie der Benutzerliste hinzu.

<details>
<summary>Lösung</summary>

<pre><code>
from flask import Flask, jsonify, request

app = Flask(__name__)
users = []

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.json
    users.append(user_data)
    return jsonify(user_data), 201

if __name__ == '__main__':
    app.run(debug=True)
</code></pre>
</details>

### Aufgabe: PUT-Route zum Aktualisieren von Benutzerdaten 🌶️️🌶️️

Implementiere eine PUT-Route (`/users/<id>`), um die Daten eines bestehenden Benutzers zu aktualisieren.

<details>
<summary>Lösung</summary>

<pre><code>
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    for user in users:
        if user['id'] == user_id:
            user.update(user_data)
            return jsonify(user)
    return jsonify({"error": "Benutzer nicht gefunden"}), 404
</code></pre>
</details>

## Fehlercodes und Ausnahmebehandlung

Bei der Behandlung von Fehlern ist die korrekte Verwendung von HTTP-Fehlercodes entscheidend, um dem Client-Ende nützliches Feedback zu geben. Alle Status Codes sind standardisiert und können z.B. auf der [SelfHTML Seite](https://wiki.selfhtml.org/wiki/HTTP/Statuscodes) eingesehen werden. Es sollte immer der präzise HTTP-Statuscodes gesendet werden um den Zustand der Anfrage zu kommunizieren.

**`404 Nicht gefunden`**

```python
@app.route('/users/<int:id>')
def get_user(id):
    user = get_user_by_id(id)
    if not user:
        return jsonify({"error": "Benutzer nicht gefunden"}), 404 
    return jsonify(user)
```

**`400 Schlechte Anfrage`**

```python
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    if not valid_car_data(data):
        return jsonify({"error": "Ungültige Daten"}), 400
    # Erstellen eines neuen Autos
    return jsonify({"message": "Auto erstellt"}), 201
```

**`401 Unautorisiert`**

```python
@app.route('/secure-area')
def secure_area():
    if not user_is_authenticated():
        return jsonify({"error": "Unautorisiert"}), 401
    return jsonify({"message": "Willkommen im sicheren Bereich"})
```

### Aufgabe: Kombinierte GET- und POST-Anfragen mit Fehlerhandling 🌶️️🌶️️

Kombiniere GET- und POST-Anfragen und implementiere umfassendes Fehlerhandling.

- Sende zuerst eine GET-Anfrage, um Daten abzurufen.
- Verwende die Daten aus der GET-Anfrage, um eine Bedingung für eine POST-Anfrage zu definieren.
- Implementiere Fehlerhandling für beide Anfragen.

<details>
<summary>Lösung</summary>

<pre><code>
@app.route('/fetch-and-create', methods=['GET', 'POST'])
def fetch_and_create():
    try:
        if request.method == 'GET':
            # Simulieren einer externen API-Anfrage
            return jsonify({"data": "Simulierte Daten"})
        elif request.method == 'POST':
            user_data = request.json
            # Simulieren einer Datenverarbeitung
            return jsonify({"message": "Benutzer erstellt"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
</code></pre>
</details>

## Anspruchsvolle Aufgaben

[60 min]

### Authentifizierung für eine sichere Route hinzufügen 🌶️️🌶️️🌶️️🌶️️

Erstelle eine gesicherte Route, die eine Authentifizierung erfordert.

**Schritte**:

1. Definiere eine neue Route `/secure`.
2. Implementiere eine einfache Authentifizierungslogik (z.B. überprüfe einen statischen API-Schlüssel).
3. Erlaube den Zugriff nur, wenn die Authentifizierung erfolgreich ist.

<details>
<summary>Lösung</summary>

<pre><code>
@app.route('/secure')
def secure_route():
    api_key = request.headers.get('API-Key')
    if api_key == "GeheimerSchlüssel":
        return jsonify({"message": "Zugriff gewährt"})
    return jsonify({"error": "Unautorisiert"}), 401
</code></pre>
</details>
