## Projekt: Integration von SQLAlchemy in einem Flask-Projekt 🌶️️🌶️️🌶️️🌶️️
[120 min]

Entwickel ein einfaches Flask-Webprojekt mit SQLAlchemy, das ein Auto-Datenmodell verwendet. Sie werden CRUD-Operationen implementieren und die Funktionalität über HTTP-Endpoints bereitstellen.

### Aufgabenstellung

1. **Einrichten eines Flask-Projekts mit SQLAlchemy**:
    - Erstelle ein neues Flask-Projekt.
    - Konfiguriere SQLAlchemy mit einer lokalen SQLite-Datenbank.

2.  **Datenmodell `Auto` erstellen**:
   - Definiere ein Modell `Auto` mit den Feldern `id` (Integer, Primärschlüssel) und `marke` (String).

3. **CRUD-Operationen implementieren**:
    - Implementiere Flask-Routen, um Autos hinzuzufügen (`/add-auto`), alle Autos anzuzeigen (`/autos`) und ein bestimmtes Auto zu löschen (`/delete-auto/<id>`).

4. **Testen der Routes mit `curl`**:
    - Führe Test-HTTP-Requests mit `curl` aus, um die Funktionalität Ihrer Routen zu überprüfen.

### Lösung zur Übungsaufgabe


```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Stellen Sie sicher, dass das Verzeichnis für die Datenbank existiert
database_dir = os.path.join(os.path.abspath(os.curdir), 'db')
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

# Absolute Pfadangabe zur Datenbankdatei
database_path = os.path.join(database_dir, 'autos.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
db = SQLAlchemy(app)

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marke = db.Column(db.String)

@app.route('/add-auto', methods=['POST'])
def add_auto():
    if not request.json or 'marke' not in request.json:
        return jsonify({"message": "Bad Request"}), 400
    marke = request.json['marke']
    new_auto = Auto(marke=marke)
    db.session.add(new_auto)
    db.session.commit()
    return jsonify({"message": "Auto added"}), 201

@app.route('/autos', methods=['GET'])
def get_autos():
    autos = Auto.query.all()
    return jsonify([{"id": auto.id, "marke": auto.marke} for auto in autos]), 200

@app.route('/delete-auto/<int:id>', methods=['DELETE'])
def delete_auto(id):
    auto = Auto.query.get(id)
    if auto:
        db.session.delete(auto)
        db.session.commit()
        return jsonify({"message": "Auto deleted"}), 200
    return jsonify({"message": "Auto not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()  # Ändern Sie den Port hier bei Bedarf

```

     * Serving Flask app '__main__'
     * Debug mode: off


    [31m[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.[0m
     * Running on http://127.0.0.1:5000
    [33mPress CTRL+C to quit[0m
    127.0.0.1 - - [11/Dec/2023 16:26:19] "GET /autos HTTP/1.1" 200 -
    /var/folders/n9/5zsytn3s4hj75c26k015w8080000gp/T/ipykernel_6658/3503689519.py:38: LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
      auto = Auto.query.get(id)
    127.0.0.1 - - [11/Dec/2023 16:26:25] "DELETE /delete-auto/1 HTTP/1.1" 200 -
    127.0.0.1 - - [11/Dec/2023 16:26:29] "[35m[1mPOST /add-auto HTTP/1.1[0m" 201 -
    127.0.0.1 - - [11/Dec/2023 16:26:34] "[35m[1mPOST /add-auto HTTP/1.1[0m" 201 -
    127.0.0.1 - - [11/Dec/2023 16:26:38] "GET /autos HTTP/1.1" 200 -


### Testen der Routes mit `curl`

```bash
# Ein Auto hinzufügen
curl -X POST -H "Content-Type: application/json" -d '{"marke": "BMW"}' http://localhost:5000/add-auto

# Alle Autos anzeigen
curl http://localhost:5000/autos

# Ein Auto löschen
curl -X DELETE http://localhost:5000/delete-auto/1
```
