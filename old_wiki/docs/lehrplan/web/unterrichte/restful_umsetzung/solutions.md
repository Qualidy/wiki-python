# Lösungen

## Einfache GET-Route für Benutzerliste

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
```

## POST-Route zum Hinzufügen neuer Benutzer

```python
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
```

## PUT-Route zum Aktualisieren von Benutzerdaten

```python
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    for user in users:
        if user['id'] == user_id:
            user.update(user_data)
            return jsonify(user)
    return jsonify({"error": "Benutzer nicht gefunden"}), 404
```

## DELETE-Route zum Löschen eines Benutzers

```python
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({"message": "Benutzer gelöscht"}), 200
```

## Komplex-Aufgabe: Kombinierte GET- und POST-Anfragen mit Fehlerhandling

```python
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
```

## Komplex-Aufgabe: Authentifizierung für eine sichere Route hinzufügen

```python
@app.route('/secure')
def secure_route():
    api_key = request.headers.get('API-Key')
    if api_key == "GeheimerSchlüssel":
        return jsonify({"message": "Zugriff gewährt"})
    return jsonify({"error": "Unautorisiert"}), 401
```
