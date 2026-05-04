# Lösungen

## Testen der GET-Route für Benutzerliste
```bash
pip install flask-swagger
```

```python
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
```