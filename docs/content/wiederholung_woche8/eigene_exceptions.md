# Eigene Exceptions

## Theorie

Die Grundlagen sind bereits gut abgedeckt:

- [Exceptions](../wiederholung/exceptions.md)
- [Exceptions im Skript](../exceptions/index.md)

Eine eigene Exception erbt meistens direkt von `Exception`.

```python
class InvalidScoreError(Exception):
    pass
```

Sie macht Sinn, wenn ein Fehler fachlich eine eigene Bedeutung hat und gezielt abgefangen werden soll.

## Aufgaben

### Aufgabe 1: Score prüfen

Schreibe eine Exception `InvalidScoreError`. Eine Funktion `add_score(score)` soll:

- nur Werte von `0` bis `100` akzeptieren
- bei ungültigen Werten `InvalidScoreError` werfen
- bei gültigen Werten `"ok"` zurückgeben

??? success "Lösung"
    ```python
    class InvalidScoreError(Exception):
        pass

    def add_score(score):
        if score < 0 or score > 100:
            raise InvalidScoreError("score must be between 0 and 100")
        return "ok"
    ```

### Aufgabe 2: Gezielt abfangen

Schreibe einen `try`/`except`-Block, der `InvalidScoreError` anders behandelt als andere Exceptions.

??? success "Lösung"
    ```python
    try:
        add_score(120)
    except InvalidScoreError as error:
        print("Ungültiger Score:", error)
    except Exception as error:
        print("Anderer Fehler:", error)
    ```

### Aufgabe 3: Exception mit Nachricht

Schreibe `InvalidAgeError`. Die Funktion `register(age)` soll bei Alter unter `18` eine Nachricht enthalten: `"age must be at least 18"`.

??? success "Lösung"
    ```python
    class InvalidAgeError(Exception):
        pass

    def register(age):
        if age < 18:
            raise InvalidAgeError("age must be at least 18")
        return "registered"
    ```

### Aufgabe 4: Reihenfolge der `except`-Blöcke

Warum ist diese Reihenfolge schlecht?

```python
try:
    add_score(200)
except Exception:
    print("general")
except InvalidScoreError:
    print("score")
```

??? success "Lösung"
    `InvalidScoreError` erbt von `Exception`. Der allgemeine Block fängt den Fehler zuerst ab; der spezifische Block wird nicht erreicht.

### Aufgabe 5: Eigene Exception nutzen

Schreibe `parse_positive_int(text)`. Die Funktion soll:

- einen String in `int` umwandeln
- bei ungültigem Format `ValueError` durchlassen
- bei Zahlen kleiner oder gleich `0` eine eigene `NotPositiveError` werfen

??? success "Lösung"
    ```python
    class NotPositiveError(Exception):
        pass

    def parse_positive_int(text):
        number = int(text)
        if number <= 0:
            raise NotPositiveError("number must be positive")
        return number
    ```

### Aufgabe 6: `raise` ohne Argument

Was macht `raise` ohne Argument in einem `except`-Block?

??? success "Lösung"
    Es wirft die gerade behandelte Exception erneut.
