# Testing einer RESTful API in Flask

[60 min]

Abhängig von der Art der Tests (Unit, Integration oder End-To-End) gibt es verschiedene Möglichkeiten diese zu implementieren. Das Testen mit Python Requests und Postman bietet eine sich ergänzende Kombination, die Funktionalität und Zuverlässigkeit einer Flask-API sicherzustellen. 

Während Python Requests ideal für das Schreiben automatisierter Testskripte (Unit Tests) ist, bietet Postman eine leistungsstarke Plattform für manuelles Testing, Automatisierung und Dokumentation (vor allem Integrationstests). Durch die Kombination beider Methoden kann ein robustes Testframework für APIs aufgebaut werden.

## Testing mit Python Requests

Die Python Requests Library haben wir bereits kennen gelernt. Sie ist eine einfache, aber leistungsstarke HTTP-Bibliothek, die für das Senden aller Arten von HTTP-Anfragen verwendet werden kann und somit perfekt geeignet um unsere API zu testen.

**Grundlegendes Testing**: In diesem Beispiel wird eine GET-Anfrage an die /users-Route gesendet. Es wird überprüft, ob der Statuscode 200 ist und ob die Antwort JSON-Daten enthält.
Erweiterte Testbeispiele

```python
import requests

def test_get_users():
    response = requests.get('http://localhost:5000/users')
    assert response.status_code == 200
    assert response.json() is not None
```

**Fehlerbehandlung testen**: Dieser Test überprüft, ob die API korrekt auf nicht gefundene Ressourcen mit einem 404-Fehler reagiert.

```python
def test_get_user_not_found():
    response = requests.get('http://localhost:5000/users/999')
    assert response.status_code == 404
```

### Aufgabe: Testen der GET-Route für Benutzerliste 🌶️️

Schreibe einen Python-Test, der die GET-Route für die Benutzerliste testet.

<details>
<summary>Lösung</summary>

<pre><code>
import requests

def test_get_users_list():
    response = requests.get('http://localhost:5000/users')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

test_get_users_list()
</code></pre>
</details>

### Aufgabe: Testen der POST-Route für das Hinzufügen eines neuen Benutzers 🌶️️🌶️️

Schreibe einen Python-Test, um das Hinzufügen eines neuen Benutzers zu testen.

<details>
<summary>Lösung</summary>

<pre><code>
import requests

def test_add_new_user():
    new_user = {"name": "John Doe", "email": "john@example.com"}
    response = requests.post('http://localhost:5000/users', json=new_user)
    assert response.status_code == 201
    assert "id" in response.json()

test_add_new_user()
</code></pre>
</details>

### Aufgabe: Testen der DELETE-Route für das Löschen eines Benutzers 🌶️️🌶️️

Schreibe einen Python-Test, um das Löschen eines Benutzers zu testen.

<details>
<summary>Lösung</summary>

<pre><code>
import requests

def test_delete_user():
    # Annahme: Hier wird ein Benutzer hinzugefügt und seine ID für den Test verwendet
    new_user = {"name": "Test User", "email": "testuser@example.com"}
    post_response = requests.post('http://localhost:5000/users', json=new_user)
    user_id = post_response.json()['id']

    # Benutzer löschen
    delete_response = requests.delete(f'http://localhost:5000/users/{user_id}')
    assert delete_response.status_code in [200, 204]
</code></pre>
</details>

## Testing mit Postman

Postman ist ein beliebtes Werkzeug für das Testen von APIs und das Werkzeug der Wahl für das kommende Tagesprojekt. Es bietet eine benutzerfreundliche Oberfläche und leistungsstarke Funktionen zum Erstellen, Testen und Dokumentieren von APIs.

#### Erstellen eines neuen Requests

![Postman Neue GET Query](../../images/postman_get_example.png)

#### Erstellen einer Postman Collections

![Postman Neue Collection](../../images/postman_new_collection_query.png)

#### Erstellen eines Tests für einen GET-Endpoint

Füge im nächsten Schritt den Status-Code Test im "Tests"-Tab hinzu.

```javascript
pm.test("Statuscode ist 200", function () {
    pm.response.to.have.status(200);

    var jsonData = pm.response.json();
    pm.expect(jsonData).to.not.be.empty;
});
```

![Postman Test Sektion](../../images/postman_test_section.png)

Über einen Rechtsklick auf die Collection können dann alle Requests inklusive tests in der angegebenen Reihenfolge getestet werden.

![Postman Test Sektion](../../images/postman_run_collection.png)

### Automatisierung und wiederholbares Testing
Postman ermöglicht es, alle Anfragen innerhalb einer Collection automatisch auszuführen. Das ist nützlich, um Regressionstests durchzuführen.

![Postman Collection Test Run](../../images/postman_collection_run.png)

Zusätzlich bietet Postman die Möglichkeit, Collections über die [Postman API](https://www.postman.com/postman/workspace/postman-public-workspace/documentation/12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a) oder [Newman](https://www.npmjs.com/package/newman) (eine Command-Line-Version von Postman) in CI/CD-Pipelines zu integrieren. Das ermöglicht das automatische Testen von APIs bei jedem Build oder Deployment.

### Aufgabe: Testen der GET-Route für Benutzerliste mit Postman 🌶️️

Erstelle einen Postman-Test, der die GET-Route für die Benutzerliste testet.

<details>
<summary>Lösung</summary>

<pre><code>
pm.test("Statuscode ist 200", function () {
    pm.response.to.have.status(200);
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});
</code></pre>
</details>

### Aufgabe: Testen der POST-Route für das Hinzufügen eines neuen Benutzers mit Postman 🌶️️🌶️️

Erstelle einen Postman-Test, um das Hinzufügen eines neuen Benutzers zu testen.

<details>
<summary>Lösung</summary>

<pre><code>
pm.test("Statuscode ist 201", function () {
    pm.response.to.have.status(201);
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
});
</code></pre>
</details>

### Aufgabe: Testen der DELETE-Route für das Löschen eines Benutzers mit Postman 🌶️️🌶️️

Erstelle einen Postman-Test, um das Löschen eines Benutzers zu testen.

<details>
<summary>Lösung</summary>

<pre><code>
pm.test("Statuscode ist 200 oder 204", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 204]);
});
</code></pre>
</details>
