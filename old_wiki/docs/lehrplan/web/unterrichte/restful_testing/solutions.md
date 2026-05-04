# Lösungen

## Testen der GET-Route für Benutzerliste
```python
import requests

def test_get_users_list():
    response = requests.get('http://localhost:5000/users')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

test_get_users_list()
```

## Testen der POST-Route für das Hinzufügen eines neuen Benutzers
```python
import requests

def test_add_new_user():
    new_user = {"name": "John Doe", "email": "john@example.com"}
    response = requests.post('http://localhost:5000/users', json=new_user)
    assert response.status_code == 201
    assert "id" in response.json()

test_add_new_user()
```

## Testen der DELETE-Route für das Löschen eines Benutzers
```python
import requests

def test_delete_user():
    # Annahme: Hier wird ein Benutzer hinzugefügt und seine ID für den Test verwendet
    new_user = {"name": "Test User", "email": "testuser@example.com"}
    post_response = requests.post('http://localhost:5000/users', json=new_user)
    user_id = post_response.json()['id']

    # Benutzer löschen
    delete_response = requests.delete(f'http://localhost:5000/users/{user_id}')
    assert delete_response.status_code in [200, 204]
```