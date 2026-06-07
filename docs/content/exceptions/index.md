


# **Modul: Python Exceptions – Vertiefung, benutzerdefinierte Exceptions und Exception Handling**

---

## **1. Einführung in Exceptions in Python**
Exceptions (Ausnahmen) sind **Fehler oder unerwartete Ereignisse**, die während der Ausführung eines Programms auftreten. Python bietet ein **mächtiges System zur Fehlerbehandlung**, das es ermöglicht, auf solche Ereignisse **gesteuert zu reagieren** und das Programm **robust und fehlerresistent** zu gestalten.

### **1.1 Warum Exception Handling?**
- **Vermeidet Abstürze**: Programme können auf Fehler reagieren, ohne abrupt zu beenden.
- **Bessere Benutzererfahrung**: Klare Fehlermeldungen statt kryptischer Stack Traces.
- **Debugging**: Gezielte Fehlerbehandlung erleichtert die Fehlersuche.
- **Ressourcenmanagement**: Sicherstellen, dass Ressourcen (z. B. Dateien, Datenbankverbindungen) **korrekt freigegeben** werden, selbst bei Fehlern.



## **2. Grundlagen von Exceptions in Python**



### **2.1 Built-in Exceptions**
Python bietet eine **Hierarchie von eingebauten Exceptions**, die in der Klasse `BaseException` verwurzelt sind. Die wichtigsten Kategorien sind:

| **Exception-Klasse** | **Beschreibung** | **Beispiel** |
|----------------------|------------------|--------------|
| `BaseException` | Basisklasse für alle Exceptions. | – |
| `Exception` | Basisklasse für alle **nicht-systemkritischen** Exceptions. | – |
| `ArithmeticError` | Fehler bei arithmetischen Operationen. | `ZeroDivisionError`, `OverflowError` |
| `LookupError` | Fehler bei Zugriff auf nicht existierende Indizes/Keys. | `IndexError`, `KeyError` |
| `OSError` | Fehler im Zusammenhang mit dem Betriebssystem. | `FileNotFoundError`, `PermissionError` |
| `ValueError` | Falscher Wert für eine Operation. | `int("abc")` |
| `TypeError` | Falscher Datentyp für eine Operation. | `"5" + 3` |
| `AttributeError` | Zugriff auf nicht existierendes Attribut. | `obj.non_existent_attr` |
| `RuntimeError` | Allgemeiner Laufzeitfehler. | – |
| `StopIteration` | Wird von `next()` ausgelöst, wenn keine Elemente mehr vorhanden sind. | – |
| `ImportError` | Fehler beim Importieren eines Moduls. | `import non_existent_module` |
| `KeyboardInterrupt` | Wird ausgelöst, wenn der Benutzer `Strg+C` drückt. | – |

**Beispiel: Häufige Built-in Exceptions**
```python
# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Fehler: {e}")  # Fehler: division by zero

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"Fehler: {e}")  # Fehler: list index out of range

# KeyError
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"Fehler: {e}")  # Fehler: 'c'

# ValueError
try:
    num = int("abc")
except ValueError as e:
    print(f"Fehler: {e}")  # Fehler: invalid literal for int() with base 10: 'abc'

# TypeError
try:
    result = "5" + 3
except TypeError as e:
    print(f"Fehler: {e}")  # Fehler: can only concatenate str (not "int") to str

# FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Fehler: {e}")  # Fehler: [Errno 2] No such file or directory: 'non_existent_file.txt'
```

---

### **2.2 `try`-`except`-Block: Grundlagen**
Der **`try`-`except`-Block** ist der **Standardmechanismus** zur Fehlerbehandlung in Python.

**Syntax:**
```python
try:
    # Code, der eine Exception auslösen könnte
    riskanter_code()
except [ExceptionType] as [variable]:
    # Code, der ausgeführt wird, wenn die Exception auftritt
    fehlerbehandlung()
```

**Beispiel: Einfaches Exception Handling**
```python
try:
    num = int(input("Geben Sie eine Zahl ein: "))
    result = 10 / num
    print(f"Ergebnis: {result}")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt!")
except ValueError:
    print("Fehler: Das ist keine gültige Zahl!")
```

---
### **2.3 `else` und `finally`**
- **`else`**: Wird ausgeführt, wenn **keine Exception** auftritt.
- **`finally`**: Wird **immer** ausgeführt, unabhängig davon, ob eine Exception aufgetreten ist oder nicht (z. B. für Cleanup-Aktionen).

**Beispiel:**
```python
try:
    num = int(input("Geben Sie eine Zahl ein: "))
    result = 10 / num
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
except ValueError:
    print("Fehler: Ungültige Eingabe!")
else:
    print(f"Ergebnis: {result}")  # Wird nur ausgeführt, wenn keine Exception auftritt
finally:
    print("Danke für die Nutzung!")  # Wird immer ausgeführt
```

---
### **2.4 Mehrere Exceptions in einem Block**
Sie können **mehrere Exceptions** in einem einzigen `except`-Block abfangen oder **mehrere `except`-Blöcke** verwenden.

**Beispiel 1: Mehrere Exceptions in einem Block**
```python
try:
    num = int(input("Geben Sie eine Zahl ein: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"Fehler: {e}")
```

**Beispiel 2: Mehrere `except`-Blöcke**
```python
try:
    num = int(input("Geben Sie eine Zahl ein: "))
    result = 10 / num
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
except ValueError:
    print("Fehler: Ungültige Eingabe!")
```

---
### **2.5 `raise`: Exceptions manuell auslösen**
Mit `raise` können Sie **manuell eine Exception auslösen**.

**Beispiel:**
```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt!")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Fehler: {e}")  # Fehler: Division durch Null ist nicht erlaubt!
```

---
### **2.6 `assert`: Bedingungen prüfen**
`assert` wird verwendet, um **Bedingungen zu prüfen** und eine `AssertionError`-Exception auszulösen, wenn die Bedingung `False` ist.

**Beispiel:**
```python
def calculate_discount(price, discount):
    assert 0 <= discount <= 100, "Rabatt muss zwischen 0 und 100 liegen!"
    return price * (1 - discount / 100)

try:
    final_price = calculate_discount(100, 150)  # Rabatt > 100
except AssertionError as e:
    print(f"Fehler: {e}")  # Fehler: Rabatt muss zwischen 0 und 100 liegen!
```

---
---
## **3. Vertiefung: Exception Handling**

---

### **3.1 Exception-Hierarchie und Vererbung**
Alle Exceptions in Python **erben von `BaseException`**. Die meisten nutzbaren Exceptions erben von `Exception`.

**Beispiel: Eigene Exception-Klasse erstellen (mehr dazu in Abschnitt 4)**
```python
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Ein benutzerdefinierter Fehler!")
except MyCustomError as e:
    print(f"Fehler: {e}")  # Fehler: Ein benutzerdefinierter Fehler!
```


### **3.2 `try`-`except`-`else`-`finally` kombiniert**
**Beispiel:**
```python
try:
    file = open("datei.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Fehler: Datei nicht gefunden!")
except PermissionError:
    print("Fehler: Keine Berechtigung zum Lesen der Datei!")
else:
    print(f"Dateiinhalt: {content}")  # Wird nur ausgeführt, wenn keine Exception auftritt
finally:
    if 'file' in locals() and not file.closed:
        file.close()  # Datei wird immer geschlossen
    print("Dateioperation abgeschlossen.")
```


### **3.3 Exception-Objekte und Attribute**
Exception-Objekte haben **nützliche Attribute**, z. B.:
- **`args`**: Enthält die Fehlermeldung als Tuple.
- **`__str__()`**: Gibt die Fehlermeldung als String zurück.

**Beispiel:**
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Fehlertyp: {type(e).__name__}")  # Fehlertyp: ZeroDivisionError
    print(f"Fehlermeldung: {e.args[0]}")     # Fehlermeldung: division by zero
    print(f"String-Darstellung: {str(e)}")   # String-Darstellung: division by zero
```

---
### **3.4 Exception-Chaining mit `from`**
Mit `raise ... from ...` können Sie **Exception-Chains** erstellen, um den **Zusammenhang zwischen Exceptions** zu dokumentieren.

**Beispiel:**
```python
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        raise ValueError(f"Datei {filename} nicht gefunden!") from e

try:
    content = read_file("non_existent.txt")
except ValueError as e:
    print(f"Fehler: {e}")  # Fehler: Datei non_existent.txt nicht gefunden!
    print(f"Ursprünglicher Fehler: {e.__cause__}")  # Ursprünglicher Fehler: [Errno 2] No such file or directory: 'non_existent.txt'
```

---
### **3.5 `suppress` aus dem `contextlib`-Modul**
Mit `suppress` können Sie **bestimmte Exceptions unterdrücken** (ähnlich wie `try-except pass`, aber eleganter).

**Beispiel:**
```python
from contextlib import suppress

# Unterdrückt FileNotFoundError
with suppress(FileNotFoundError):
    with open("non_existent.txt", "r") as f:
        content = f.read()

print("Programm läuft weiter, auch wenn die Datei nicht existiert.")
```


### **3.6 `try`-`except` in Schleifen**
**Beispiel: Mehrere Dateien lesen, Fehler ignorieren**
```python
files = ["datei1.txt", "datei2.txt", "non_existent.txt", "datei3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"Inhalt von {file}: {f.read()}")
    except FileNotFoundError:
        print(f"Warnung: {file} nicht gefunden. Überspringe...")
    except PermissionError:
        print(f"Warnung: Keine Berechtigung für {file}. Überspringe...")
```



## **4. Benutzerdefinierte Exceptions**

---
### **4.1 Warum benutzerdefinierte Exceptions?**
- **Bessere Lesbarkeit**: Klare Fehlermeldungen, die **spezifisch für Ihre Anwendung** sind.
- **Fehlerkategorisierung**: Unterschiedliche Fehlerarten können **unterschiedlich behandelt** werden.
- **Wiederverwendbarkeit**: Exceptions können in **mehreren Modulen** verwendet werden.


### **4.2 Einfache benutzerdefinierte Exception erstellen**
Eine benutzerdefinierte Exception ist eine **Klasse, die von `Exception` oder einer anderen Exception-Klasse erbt**.

**Beispiel:**
```python
class InvalidAgeError(Exception):
    """Wird ausgelöst, wenn ein ungültiges Alter angegeben wird."""
    pass

def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Alter muss zwischen 0 und 120 liegen!")
    print(f"Alter {age} ist gültig.")

try:
    check_age(-5)
except InvalidAgeError as e:
    print(f"Fehler: {e}")  # Fehler: Alter muss zwischen 0 und 120 liegen!
```


### **4.3 Benutzerdefinierte Exception mit zusätzlichen Attributen**
Sie können **benutzerdefinierte Attribute** zu Ihrer Exception hinzufügen.

**Beispiel:**
```python
class InvalidEmailError(Exception):
    """Wird ausgelöst, wenn eine ungültige E-Mail-Adresse angegeben wird."""
    def __init__(self, email, message="Ungültige E-Mail-Adresse!"):
        self.email = email
        self.message = message
        super().__init__(self.message)

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError(email, "E-Mail muss ein '@'-Zeichen enthalten!")
    print(f"E-Mail {email} ist gültig.")

try:
    validate_email("user.example.com")
except InvalidEmailError as e:
    print(f"Fehler für {e.email}: {e.message}")  # Fehler für user.example.com: E-Mail muss ein '@'-Zeichen enthalten!
```


### **4.4 Benutzerdefinierte Exception mit Standardwerten**
**Beispiel:**
```python
class InsufficientFundsError(Exception):
    """Wird ausgelöst, wenn nicht genug Geld auf dem Konto ist."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Nicht genug Geld! Kontostand: {balance}, Betrag: {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Fehler: {e}")  # Fehler: Nicht genug Geld! Kontostand: 100, Betrag: 150
```


### **4.5 Hierarchie benutzerdefinierter Exceptions**
Sie können **mehrere benutzerdefinierte Exceptions** erstellen, die von einer **Basisklasse** erben.

**Beispiel:**
```python
class ValidationError(Exception):
    """Basisklasse für Validierungsfehler."""
    pass

class InvalidAgeError(ValidationError):
    """Wird ausgelöst, wenn ein ungültiges Alter angegeben wird."""
    pass

class InvalidEmailError(ValidationError):
    """Wird ausgelöst, wenn eine ungültige E-Mail-Adresse angegeben wird."""
    pass

def validate_user(age, email):
    if age < 0 or age > 120:
        raise InvalidAgeError("Alter muss zwischen 0 und 120 liegen!")
    if "@" not in email:
        raise InvalidEmailError("E-Mail muss ein '@'-Zeichen enthalten!")

try:
    validate_user(-5, "user@example.com")
except ValidationError as e:
    print(f"Validierungsfehler: {e}")  # Validierungsfehler: Alter muss zwischen 0 und 120 liegen!
```


### **4.6 Benutzerdefinierte Exceptions mit Methoden**
Sie können **Methoden** zu Ihren Exceptions hinzufügen, um **zusätzliche Funktionalität** bereitzustellen.

**Beispiel:**
```python
class NetworkError(Exception):
    """Wird ausgelöst, wenn ein Netzwerkfehler auftritt."""
    def __init__(self, url, status_code):
        self.url = url
        self.status_code = status_code
        super().__init__(f"Netzwerkfehler: {url} (Status: {status_code})")

    def log_error(self):
        """Loggt den Fehler in eine Datei."""
        with open("network_errors.log", "a") as f:
            f.write(f"{self.url} - {self.status_code}\n")

def fetch_url(url):
    # Simulierter Netzwerkfehler
    if url == "https://example.com/error":
        raise NetworkError(url, 404)

try:
    fetch_url("https://example.com/error")
except NetworkError as e:
    print(f"Fehler: {e}")  # Fehler: Netzwerkfehler: https://example.com/error (Status: 404)
    e.log_error()  # Loggt den Fehler in network_errors.log
```


## **5. Fortgeschrittenes Exception Handling**


### **5.1 Exception Handling in Funktionen**
**Beispiel: Funktion mit Exception Handling**
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')  # Rückgabe von Unendlich bei Division durch Null
    except TypeError:
        return None  # Rückgabe von None bei falschem Datentyp

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # inf
print(safe_divide("10", 2)) # None
```


### **5.2 Exception Handling in Klassen**
**Beispiel: Klasse mit Exception Handling**
```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Nicht genug Geld! Kontostand: {self.balance}, Betrag: {amount}")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Einzahlungsbetrag muss positiv sein!")
        self.balance += amount
        return self.balance

account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(f"Fehler: {e}")  # Fehler: Nicht genug Geld! Kontostand: 100, Betrag: 150
```







## **6. Best Practices für Exception Handling**

---
### **6.1 Wann sollte man Exceptions verwenden?**
| **Szenario** | **Exception verwenden?** | **Alternative** |
|--------------|--------------------------|----------------|
| **Unerwartete Fehler** (z. B. Datei nicht gefunden) | ✅ Ja | – |
| **Erwartete Bedingungen** (z. B. Benutzereingabe validieren) | ❌ Nein | `if`-Bedingungen |
| **Logische Fehler** (z. B. falsche Eingabe) | ❌ Nein | `if`-Bedingungen + Rückgabewerte |
| **Ressourcenfreigabe** (z. B. Dateien schließen) | ✅ Ja (mit `finally` oder `with`) | – |


### **6.2 Wann sollte man `try`-`except` vermeiden?**
- **Für Flusskontrolle**: Exceptions sollten **nicht für normale Programmabläufe** verwendet werden.
  ❌ **Schlecht:**
  ```python
  try:
      if x > 0:
          raise ValueError("x ist positiv")
  except ValueError:
      print("x ist nicht positiv")
  ```
  ✅ **Besser:**
  ```python
  if x <= 0:
      print("x ist nicht positiv")
  ```

- **Für erwartete Bedingungen**: Verwenden Sie **`if`-Bedingungen** statt Exceptions.
  ❌ **Schlecht:**
  ```python
  try:
      result = my_dict["key"]
  except KeyError:
      result = None
  ```
  ✅ **Besser:**
  ```python
  result = my_dict.get("key")
  ```


### **6.3 Wie sollte man Exceptions dokumentieren?**
- **Dokumentieren Sie Exceptions** in der **Dokumentation Ihrer Funktionen/Klassen**.
- Verwenden Sie **Docstrings**, um mögliche Exceptions zu beschreiben.

**Beispiel:**
```python
def divide(a, b):
    """
    Teilt a durch b.

    Args:
        a (int/float): Dividend.
        b (int/float): Divisor.

    Returns:
        float: Ergebnis der Division.

    Raises:
        ZeroDivisionError: Wenn b 0 ist.
        TypeError: Wenn a oder b nicht numerisch sind.
    """
    if b == 0:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt!")
    return a / b
```


### **6.4 Wie sollte man Exceptions loggen?**
Verwenden Sie das **`logging`-Modul**, um Exceptions zu **protokollieren**.

**Beispiel:**
```python
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Division durch Null: {e}", exc_info=True)
        raise
    except TypeError as e:
        logging.error(f"Falscher Datentyp: {e}", exc_info=True)
        raise

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Ein Fehler ist aufgetreten. Siehe Log-Datei für Details.")
```


### **6.5 Wie sollte man benutzerdefinierte Exceptions benennen?**
- **Namen sollten klar und beschreibend** sein.
- **Enden Sie den Namen mit `Error`** (z. B. `InvalidInputError`, `NetworkTimeoutError`).
- **Verwenden Sie eine Hierarchie**, wenn es sinnvoll ist (z. B. `ValidationError` als Basisklasse für `InvalidAgeError`, `InvalidEmailError`).


## **7. Übungsaufgaben**

---
### **Frage 1**
Was ist der Unterschied zwischen `try-except` und `try-finally`?

??? success "Antwort"
    - **`try-except`**: Fängt und behandelt **Exceptions**.
    - **`try-finally`**: Führt den `finally`-Block **immer aus**, unabhängig davon, ob eine Exception aufgetreten ist oder nicht (z. B. für Cleanup-Aktionen).

---
### **Frage 2**
Wie können Sie eine **`ValueError`-Exception** manuell auslösen, wenn eine Eingabe nicht gültig ist?

??? success "Antwort"
    ```python
    if not valid_input:
        raise ValueError("Ungültige Eingabe!")
    ```

---
### **Frage 3**
Erstellen Sie eine **benutzerdefinierte Exception `NegativeNumberError`**, die ausgelöst wird, wenn eine negative Zahl übergeben wird.

??? success "Antwort"
    ```python
    class NegativeNumberError(Exception):
        pass

    def check_positive(number):
        if number < 0:
            raise NegativeNumberError("Zahl muss positiv sein!")
        return number

    try:
        check_positive(-5)
    except NegativeNumberError as e:
        print(f"Fehler: {e}")  # Fehler: Zahl muss positiv sein!
    ```

---
### **Frage 4**
Wie können Sie **mehrere Exceptions in einem einzigen `except`-Block** abfangen?

??? success "Antwort"
    ```python
    try:
        # Code, der Exceptions auslösen könnte
        pass
    except (ValueError, TypeError) as e:
        print(f"Fehler: {e}")
    ```

---
### **Frage 5**
Was ist der Unterschied zwischen `raise` und `raise ... from ...`?

??? success "Antwort"
    - **`raise`**: Löst eine **neue Exception** aus.
    - **`raise ... from ...`**: Löst eine **neue Exception** aus und **verknüpft sie mit der ursprünglichen Exception** (für Exception-Chaining).

---
### **Frage 6**
Erstellen Sie eine **benutzerdefinierte Exception `InsufficientPermissionsError`**, die den **Benutzernamen** und die **erforderlichen Berechtigungen** als Attribute speichert.

??? success "Antwort"
    ```python
    class InsufficientPermissionsError(Exception):
        def __init__(self, username, required_permissions):
            self.username = username
            self.required_permissions = required_permissions
            super().__init__(f"Benutzer {username} hat nicht die erforderlichen Berechtigungen: {required_permissions}")

    def check_permissions(username, permissions):
        required = ["read", "write"]
        if not all(p in permissions for p in required):
            raise InsufficientPermissionsError(username, required)

    try:
        check_permissions("alice", ["read"])
    except InsufficientPermissionsError as e:
        print(f"Fehler: {e}")  # Fehler: Benutzer alice hat nicht die erforderlichen Berechtigungen: ['read', 'write']
    ```

---
### **Frage 7**
Wie können Sie **Exception-Chaining** verwenden, um eine `ValueError` aus einer `FileNotFoundError` abzuleiten?

??? success "Antwort"
    ```python
    try:
        with open("non_existent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        raise ValueError("Datei nicht gefunden!") from e
    ```

---
### **Frage 8**
Erstellen Sie eine Funktion `safe_sqrt`, die die **Wurzel einer Zahl** berechnet und eine **`ValueError`-Exception** auslöst, wenn die Zahl negativ ist.

??? success "Antwort"
    ```python
    import math

    def safe_sqrt(number):
        if number < 0:
            raise ValueError("Zahl muss nicht-negativ sein!")
        return math.sqrt(number)

    try:
        print(safe_sqrt(16))  # 4.0
        print(safe_sqrt(-4))  # Löst ValueError aus
    except ValueError as e:
        print(f"Fehler: {e}")  # Fehler: Zahl muss nicht-negativ sein!
    ```

---
### **Frage 9**
Wie können Sie **`assert`** verwenden, um sicherzustellen, dass eine Liste nicht leer ist?

??? success "Antwort"
    ```python
    my_list = []

    try:
        assert len(my_list) > 0, "Liste darf nicht leer sein!"
    except AssertionError as e:
        print(f"Fehler: {e}")  # Fehler: Liste darf nicht leer sein!
    ```

---
### **Frage 10**
Erstellen Sie eine **benutzerdefinierte Exception-Hierarchie** mit einer Basisklasse `ValidationError` und zwei Unterklassen `InvalidEmailError` und `InvalidAgeError`.

??? success "Antwort"
    ```python
    class ValidationError(Exception):
        pass

    class InvalidEmailError(ValidationError):
        def __init__(self, email):
            self.email = email
            super().__init__(f"Ungültige E-Mail: {email}")

    class InvalidAgeError(ValidationError):
        def __init__(self, age):
            self.age = age
            super().__init__(f"Ungültiges Alter: {age}")

    def validate_user(email, age):
        if "@" not in email:
            raise InvalidEmailError(email)
        if age < 0 or age > 120:
            raise InvalidAgeError(age)

    try:
        validate_user("user.example.com", -5)
    except ValidationError as e:
        print(f"Validierungsfehler: {e}")  # Validierungsfehler: Ungültige E-Mail: user.example.com
    ```

---
---
## **8. Praktische Beispiele**

---
### **Beispiel 1: Benutzerdefinierte Exception für eine Bankanwendung**
**Szenario:** Eine Bankanwendung soll **`InsufficientFundsError`** auslösen, wenn ein Konto nicht genug Geld hat.

**Lösung:**
```python
class InsufficientFundsError(Exception):
    """Wird ausgelöst, wenn nicht genug Geld auf dem Konto ist."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Nicht genug Geld! Kontostand: {balance}, Betrag: {amount}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Einzahlungsbetrag muss positiv sein!")
        self.balance += amount
        return self.balance

# Beispielnutzung
account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Fehler: {e}")  # Fehler: Nicht genug Geld! Kontostand: 100, Betrag: 150
```

---
### **Beispiel 2: Exception Handling in einer Dateiverwaltungs-Klasse**
**Szenario:** Eine Klasse `FileManager` soll Dateien lesen und schreiben, mit **Exception Handling** für häufige Fehler.

**Lösung:**
```python
class FileNotFoundError(Exception):
    """Wird ausgelöst, wenn eine Datei nicht gefunden wird."""
    pass

class PermissionDeniedError(Exception):
    """Wird ausgelöst, wenn keine Berechtigung für eine Dateioperation besteht."""
    pass

class FileManager:
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Datei {filename} nicht gefunden!")
        except PermissionError:
            raise PermissionDeniedError(f"Keine Berechtigung zum Lesen von {filename}!")

    @staticmethod
    def write_file(filename, content):
        try:
            with open(filename, "w") as f:
                f.write(content)
        except PermissionError:
            raise PermissionDeniedError(f"Keine Berechtigung zum Schreiben in {filename}!")

# Beispielnutzung
try:
    content = FileManager.read_file("non_existent.txt")
except FileNotFoundError as e:
    print(f"Fehler: {e}")  # Fehler: Datei non_existent.txt nicht gefunden!

try:
    FileManager.write_file("/root/protected.txt", "Hallo!")
except PermissionDeniedError as e:
    print(f"Fehler: {e}")  # Fehler: Keine Berechtigung zum Schreiben in /root/protected.txt!
```

---
### **Beispiel 3: Exception Handling in einer API-Anfrage**
**Szenario:** Eine Funktion `fetch_api_data` soll Daten von einer API abrufen und **benutzerdefinierte Exceptions** für verschiedene Fehlerfälle auslösen.

**Lösung:**
```python
import requests

class APIError(Exception):
    """Basisklasse für API-Fehler."""
    pass

class NetworkError(APIError):
    """Wird ausgelöst, wenn ein Netzwerkfehler auftritt."""
    pass

class InvalidResponseError(APIError):
    """Wird ausgelöst, wenn die API-Antwort ungültig ist."""
    pass

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Löst HTTPError für 4xx/5xx aus
    except requests.exceptions.RequestException as e:
        raise NetworkError(f"Netzwerkfehler: {e}") from e

    try:
        data = response.json()
    except ValueError:
        raise InvalidResponseError("Ungültige JSON-Antwort!")

    return data

# Beispielnutzung
try:
    data = fetch_api_data("https://api.example.com/data")
    print(data)
except APIError as e:
    print(f"API-Fehler: {e}")
```

---
### **Beispiel 4: Exception Handling in einer Datenvalidierungs-Klasse**
**Szenario:** Eine Klasse `UserValidator` soll Benutzereingaben validieren und **benutzerdefinierte Exceptions** für ungültige Eingaben auslösen.

**Lösung:**
```python
class ValidationError(Exception):
    """Basisklasse für Validierungsfehler."""
    pass

class InvalidEmailError(ValidationError):
    """Wird ausgelöst, wenn eine E-Mail ungültig ist."""
    def __init__(self, email):
        self.email = email
        super().__init__(f"Ungültige E-Mail: {email}")

class InvalidAgeError(ValidationError):
    """Wird ausgelöst, wenn ein Alter ungültig ist."""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Ungültiges Alter: {age}")

class UserValidator:
    @staticmethod
    def validate_email(email):
        if "@" not in email or "." not in email:
            raise InvalidEmailError(email)
        return True

    @staticmethod
    def validate_age(age):
        if age < 0 or age > 120:
            raise InvalidAgeError(age)
        return True

    @staticmethod
    def validate_user(email, age):
        UserValidator.validate_email(email)
        UserValidator.validate_age(age)
        return True

# Beispielnutzung
try:
    UserValidator.validate_user("user@example.com", 25)
    print("Benutzer ist gültig!")
except ValidationError as e:
    print(f"Validierungsfehler: {e}")

try:
    UserValidator.validate_user("user.example.com", -5)
except ValidationError as e:
    print(f"Validierungsfehler: {e}")  # Validierungsfehler: Ungültige E-Mail: user.example.com
```

---
### **Beispiel 5: Exception Handling mit Logging**
**Szenario:** Eine Funktion `process_data` soll Daten verarbeiten und **Exceptions loggen**, bevor sie weitergegeben werden.

**Lösung:**
```python
import logging

# Logging konfigurieren
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataProcessingError(Exception):
    """Wird ausgelöst, wenn ein Fehler bei der Datenverarbeitung auftritt."""
    pass

def process_data(data):
    try:
        # Simulierte Datenverarbeitung
        if not isinstance(data, list):
            raise TypeError("Daten müssen eine Liste sein!")
        if len(data) == 0:
            raise ValueError("Datenliste darf nicht leer sein!")
        return [x * 2 for x in data]
    except (TypeError, ValueError) as e:
        logging.error(f"Datenverarbeitungsfehler: {e}", exc_info=True)
        raise DataProcessingError(f"Fehler bei der Datenverarbeitung: {e}") from e

# Beispielnutzung
try:
    result = process_data("keine Liste")
    print(result)
except DataProcessingError as e:
    print(f"Fehler: {e}")  # Fehler: Fehler bei der Datenverarbeitung: Daten müssen eine Liste sein!
```

---
---
## **9. Häufige Fehler und Lösungen**

| **Problem** | **Ursache** | **Lösung** |
|-------------|-------------|------------|
| **`Exception not caught`** | Falscher Exception-Typ im `except`-Block. | Überprüfen Sie den Typ der Exception (z. B. mit `type(e).__name__`). |
| **`Too many except blocks`** | Zu viele spezifische `except`-Blöcke. | Fassen Sie ähnliche Exceptions zusammen (z. B. `(ValueError, TypeError)`). |
| **`Bare except`** | `except:` ohne Angabe des Exception-Typs. | Vermeiden Sie `except:` – fangen Sie **spezifische Exceptions** oder verwenden Sie `except Exception:`. |
| **`Exception swallowed`** | Exception wird gefangen, aber nicht behandelt. | Loggen Sie die Exception oder geben Sie sie weiter (`raise`). |
| **`Resource leak`** | Ressourcen (z. B. Dateien) werden nicht freigegeben. | Verwenden Sie `finally` oder `with`-Blöcke. |
| **`Custom Exception not raised`** | Benutzerdefinierte Exception wird nicht ausgelöst. | Überprüfen Sie die Bedingung, die die Exception auslösen soll. |
| **`Exception not documented`** | Exceptions sind nicht in der Dokumentation vermerkt. | Dokumentieren Sie mögliche Exceptions in Docstrings. |
| **`Exception Chaining lost`** | Ursprüngliche Exception geht verloren. | Verwenden Sie `raise ... from ...` für Exception-Chaining. |

---
---
## **10. Zusammenfassung: Exceptions in Python**

| **Thema** | **Wichtige Konzepte** | **Beispiele** |
|-----------|------------------------|--------------|
| **Built-in Exceptions** | `ValueError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError` | `try-except` für spezifische Fehler |
| **`try-except`** | Grundlegendes Exception Handling | `try: ... except Exception as e: ...` |
| **`else` und `finally`** | `else` für erfolgreiche Ausführung, `finally` für Cleanup | `try: ... except: ... else: ... finally: ...` |
| **`raise`** | Manuelles Auslösen von Exceptions | `raise ValueError("Fehlermeldung")` |
| **`assert`** | Bedingungen prüfen | `assert condition, "Fehlermeldung"` |
| **Benutzerdefinierte Exceptions** | Eigene Exception-Klassen erstellen | `class MyError(Exception): pass` |
| **Exception-Chaining** | Verbindung von Exceptions | `raise NewError from original_error` |
| **`suppress`** | Exceptions unterdrücken | `with suppress(FileNotFoundError): ...` |
| **Exception Handling in Klassen** | Exceptions in Methoden | `try-except` in Klassenmethoden |
| **Exception Handling mit `with`** | Automatische Ressourcenfreigabe | `with open(...) as f: ...` |
| **Best Practices** | Spezifische Exceptions fangen, nicht für Flusskontrolle verwenden | `except (ValueError, TypeError):` |

---
---
## **11. Fazit: Exceptions in Python**
Exceptions sind ein **zentraler Bestandteil** der Python-Programmierung und ermöglichen es, **robuste, fehlerresistente und wartbare Anwendungen** zu erstellen. Durch das Verständnis von:
- **Built-in Exceptions**,
- **`try-except-else-finally`**,
- **benutzerdefinierten Exceptions**,
- **Exception-Chaining** und
- **Best Practices**

können Sie **Fehler gezielt behandeln**, **Debugging erleichtern** und **die Qualität Ihrer Codebasis verbessern**.

### **Empfehlungen für die Praxis:**
1. **Fangen Sie spezifische Exceptions** (vermeiden Sie `except:`).
2. **Verwenden Sie `finally` oder `with`** für Ressourcenfreigabe.
3. **Dokumentieren Sie Exceptions** in Ihren Funktionen/Klassen.
4. **Loggen Sie Exceptions** für Debugging-Zwecke.
5. **Erstellen Sie benutzerdefinierte Exceptions** für domänenspezifische Fehler.
6. **Vermeiden Sie Exceptions für Flusskontrolle** (verwenden Sie `if`-Bedingungen für erwartete Fälle).

