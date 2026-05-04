# Dokumentation einer RESTful API in Flask

[45 min]

Eine ausführliche und gut strukturierte Dokumentation ist entscheidend für eine professionelle API. Auch hierfür gibt es nützliche Tools die die Dokumentation deutlich vereinfachen.

## Swagger / OpenAPI

[Swagger](https://swagger.io/) bietet eine grafische Benutzeroberfläche und Werkzeuge zur Erstellung interaktiver API-Dokumentationen. Flask-APIs können mit [Flask-Swagger](https://pypi.org/project/flask-swagger/) integrieren, um automatisch eine Dokumentation zu generieren.

## MkDocs oder Sphinx:

Für eine eher traditionelle Dokumentation können Werkzeuge wie [MkDocs](https://www.mkdocs.org/) verwendet werden, die z.B. Markdown nutzen, um Seiten und Navigation zu erstellen.

## Beispielstruktur einer API-Dokumentation

```python
# Meine RESTful API

## Übersicht
- Endpoints
- Fehlercodes

## Endpoints

### GET /users
- Beschreibung: Abrufen einer Liste aller Benutzer.
- Parameter: Keine.

- Beispielanfrage: GET /users

- Beispielantwort (JSON):
  {
    "users": [
      {"id": 1, "name": "John Doe"},
      {"id": 2, "name": "Jane Doe"}
    ]
  }

### POST /users
Beschreibung: Erstellen eines neuen Benutzers.
Parameter: name (String), email (String).

Beispielanfrage (JSON): POST /users
{
  "name": "Max Mustermann",
  "email": "max@example.com"
}

Beispielantwort (JSON):
{
  "message": "Benutzer erstellt",
  "userId": 3
}

### Fehlercodes
400 Bad Request: Ungültige Anfragedaten.
404 Not Found: Ressource nicht gefunden.
500 Internal Server Error: Allgemeiner Serverfehler.
```

## Aufgaben

[30 min]

### Erstellen einer Swagger-Dokumentation. 🌶️️🌶️️

Integriere Swagger in Ihre Flask-API, um eine interaktive Dokumentation zu erstellen.

#### Schritte

- Installiere `flask-swagger` im Flask-Projekt.
- Erstelle YAML-Dokumentationsblöcke für die bestehenden Endpoints.
- Konfiguriere Flask-Swagger, um diese Dokumentationsblöcke zu sammeln und eine interaktive API-Dokumentation bereitzustellen.

<details>
<summary>Lösung</summary>

<pre><code>
pip install flask-swagger
</code></pre>

<pre><code>
from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def users():
    """
    get:
        description: Abrufen einer Liste aller Benutzer.
        responses:
            200:
                description: Eine Liste von Benutzern.
                schema:
                    type: object
                    properties:
                        users:
                            type: array
                            items:
                                $ref: '#/definitions/User'
    definitions:
        User:
            type: object
            properties:
                id:
                    type: integer
                name:
                    type: string
    """
    # Implementierung der Logik
    return jsonify(users=[{"id": 1, "name": "John Doe"}])

@app.route("/apidocs")
def apidocs():
    return jsonify(swagger(app))

if __name__ == "__main__":
    app.run(debug=True)
</code></pre>
</details>