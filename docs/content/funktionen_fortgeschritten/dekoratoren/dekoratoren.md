# Dekoratoren

🟠 PCAP | 🔄 Vertiefung von Funktionen & OOP

## Einführung — Funktionen als Objekte

In Python sind Funktionen **First-Class Objects**. Das bedeutet: Funktionen können wie jeder andere Wert behandelt werden — sie können in Variablen gespeichert, als Argumente übergeben und als Rückgabewerte zurückgegeben werden.

```python
def begruessung(name):
    return f"Hallo, {name}!"

# Funktion in Variable speichern (ohne Klammern!)
meine_funktion = begruessung
print(meine_funktion("Anna"))  # Hallo, Anna!

# Funktion als Argument übergeben
def ausfuehren(funktion, wert):
    return funktion(wert)

print(ausfuehren(begruessung, "Bob"))  # Hallo, Bob!
```

Dieses Konzept kennen wir bereits von [Lambda-Funktionen](../lambda/lambda.md), wo wir Funktionen als `key`-Parameter an `sorted()` übergeben haben.

### Funktionen, die Funktionen zurückgeben

```python
def erstelle_multiplizierer(faktor):
    def multiplizierer(x):
        return x * faktor
    return multiplizierer

verdoppeln = erstelle_multiplizierer(2)
verdreifachen = erstelle_multiplizierer(3)

print(verdoppeln(5))      # 10
print(verdreifachen(5))   # 15
```

Genau dieses Muster — eine Funktion entgegennehmen und eine neue zurückgeben — ist die Grundlage von **Dekoratoren**.

---

## Was ist ein Dekorator?

Ein Dekorator ist eine Funktion, die eine **andere Funktion entgegennimmt**, sie mit zusätzlicher Funktionalität **umhüllt** und die neue Funktion **zurückgibt**.

```python
def mein_dekorator(func):
    def wrapper():
        print("Vor dem Funktionsaufruf")
        func()
        print("Nach dem Funktionsaufruf")
    return wrapper

def sage_hallo():
    print("Hallo!")

# Dekorieren: Die ursprüngliche Funktion wird "eingepackt"
sage_hallo = mein_dekorator(sage_hallo)

sage_hallo()
# Vor dem Funktionsaufruf
# Hallo!
# Nach dem Funktionsaufruf
```

### Schritt für Schritt

1. `mein_dekorator` nimmt `sage_hallo` als `func` entgegen
2. Er definiert eine neue Funktion `wrapper`, die `func()` aufruft — aber davor und danach etwas Zusätzliches tut
3. Er gibt `wrapper` zurück
4. `sage_hallo` wird durch `wrapper` **ersetzt**

---

## Die `@decorator`-Syntax

Die Zeile `sage_hallo = mein_dekorator(sage_hallo)` ist umständlich. Python bietet dafür **syntaktischen Zucker** — die `@`-Syntax:

```python
def mein_dekorator(func):
    def wrapper():
        print("Vor dem Funktionsaufruf")
        func()
        print("Nach dem Funktionsaufruf")
    return wrapper

@mein_dekorator
def sage_hallo():
    print("Hallo!")

sage_hallo()
# Vor dem Funktionsaufruf
# Hallo!
# Nach dem Funktionsaufruf
```

!!! info "Äquivalenz"
    `@mein_dekorator` über der Funktionsdefinition ist **exakt gleichbedeutend** mit:

    ```python
    sage_hallo = mein_dekorator(sage_hallo)
    ```

### Dekoratoren mit Argumenten weiterleiten

In der Praxis haben dekorierte Funktionen oft Parameter. Der Wrapper muss diese **weiterleiten**:

```python
def mein_dekorator(func):
    def wrapper(*args, **kwargs):
        print(f"Aufruf von {func.__name__}")
        ergebnis = func(*args, **kwargs)
        print(f"Ergebnis: {ergebnis}")
        return ergebnis
    return wrapper

@mein_dekorator
def addiere(a, b):
    return a + b

print(addiere(3, 5))
# Aufruf von addiere
# Ergebnis: 8
# 8
```

!!! warning "Wichtig"
    Verwende immer `*args, **kwargs` im Wrapper, damit der Dekorator mit **beliebigen**
    Funktionen funktioniert — egal wie viele Parameter sie haben.

---

## `functools.wraps`

Es gibt ein Problem: Nach dem Dekorieren geht die **Identität** der Originalfunktion verloren:

```python
def mein_dekorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@mein_dekorator
def sage_hallo():
    """Gibt eine Begrüßung aus."""
    print("Hallo!")

print(sage_hallo.__name__)  # wrapper (!)
print(sage_hallo.__doc__)   # None (!)
```

Die Lösung: `functools.wraps` kopiert die Metadaten der Originalfunktion auf den Wrapper:

```python
from functools import wraps

def mein_dekorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@mein_dekorator
def sage_hallo():
    """Gibt eine Begrüßung aus."""
    print("Hallo!")

print(sage_hallo.__name__)  # sage_hallo ✓
print(sage_hallo.__doc__)   # Gibt eine Begrüßung aus. ✓
```

!!! tip "Best Practice"
    Verwende **immer** `@functools.wraps(func)` im Wrapper. Das ist Standard in
    professionellem Python-Code.

---

## Praktische Beispiele

### Logging-Dekorator

```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"→ {func.__name__}({args}, {kwargs})")
        ergebnis = func(*args, **kwargs)
        print(f"← {func.__name__} → {ergebnis}")
        return ergebnis
    return wrapper

@log
def multipliziere(a, b):
    return a * b

multipliziere(3, 4)
# → multipliziere((3, 4), {})
# ← multipliziere → 12
```

### Zeitmessung

```python
import time
from functools import wraps

def zeitmessung(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ergebnis = func(*args, **kwargs)
        dauer = time.time() - start
        print(f"{func.__name__} dauerte {dauer:.4f} Sekunden")
        return ergebnis
    return wrapper

@zeitmessung
def langsame_funktion():
    time.sleep(1)
    return "Fertig"

langsame_funktion()
# langsame_funktion dauerte 1.0012 Sekunden
```

### Wiederholung bei Fehlern (Retry)

```python
import time
from functools import wraps

def retry(max_versuche=3, wartezeit=1):
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for versuch in range(1, max_versuche + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Versuch {versuch} fehlgeschlagen: {e}")
                    if versuch < max_versuche:
                        time.sleep(wartezeit)
            raise Exception(f"Alle {max_versuche} Versuche fehlgeschlagen")
        return wrapper
    return dekorator

@retry(max_versuche=3, wartezeit=0.5)
def instabile_funktion():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Server nicht erreichbar")
    return "Erfolg!"
```

---

## Dekoratoren mit Parametern

Manchmal soll der Dekorator selbst Parameter haben. Dafür braucht man **eine zusätzliche Verschachtelung**:

```python
from functools import wraps

def wiederhole(n):
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                ergebnis = func(*args, **kwargs)
            return ergebnis
        return wrapper
    return dekorator

@wiederhole(n=3)
def sage_hallo():
    print("Hallo!")

sage_hallo()
# Hallo!
# Hallo!
# Hallo!
```

### Wie funktioniert das?

Die drei Ebenen sind:

1. `wiederhole(n=3)` wird aufgerufen → gibt `dekorator` zurück
2. `dekorator(sage_hallo)` wird aufgerufen → gibt `wrapper` zurück
3. `wrapper()` wird aufgerufen → führt `sage_hallo()` dreimal aus

Das entspricht: `sage_hallo = wiederhole(n=3)(sage_hallo)`

---

## Mehrere Dekoratoren stapeln

Man kann mehrere Dekoratoren auf eine Funktion anwenden. Sie werden **von unten nach oben** angewendet:

```python
@dekorator_a
@dekorator_b
def meine_funktion():
    pass

# Entspricht:
meine_funktion = dekorator_a(dekorator_b(meine_funktion))
```

```python
from functools import wraps

def fett(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def kursiv(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@fett
@kursiv
def gruss(name):
    return f"Hallo, {name}"

print(gruss("Anna"))  # <b><i>Hallo, Anna</i></b>
```

!!! info "Reihenfolge"
    `@fett` wird **zuletzt** angewendet (äußerster Wrapper), `@kursiv` **zuerst** (innerster Wrapper).
    Die Ausführung geht von **außen nach innen**: fett → kursiv → gruss → kursiv → fett.

---

## Bekannte Dekoratoren aus OOP

Diese Dekoratoren kennen wir bereits aus der [OOP Vertiefung](../../oop_vertiefung/getter_setter/getter_setter.md):

| Dekorator | Herkunft | Funktion |
|---|---|---|
| `@property` | Built-in | Getter für Attributzugriff |
| `@attribut.setter` | Built-in | Setter für Attributzugriff |
| `@staticmethod` | Built-in | Methode ohne `self`/`cls` |
| `@classmethod` | Built-in | Methode mit `cls` statt `self` |

```python
class Kreis:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, wert):
        if wert < 0:
            raise ValueError("Radius muss positiv sein")
        self._radius = wert

    @staticmethod
    def ist_gueltig(radius):
        return radius > 0

    @classmethod
    def einheitskreis(cls):
        return cls(1)
```

Jetzt wissen wir: `@property` ist **kein magisches Schlüsselwort**, sondern ein ganz normaler Dekorator — eine Funktion, die eine Funktion entgegennimmt und eine neue zurückgibt.

---

## Zusammenfassung

| Konzept | Beschreibung |
|---|---|
| First-Class Functions | Funktionen sind Objekte — speicherbar, übergebbar |
| Dekorator | Funktion, die eine Funktion umhüllt und erweitert |
| `@decorator` | Syntaktischer Zucker für `func = decorator(func)` |
| `@wraps(func)` | Erhält `__name__` und `__doc__` der Originalfunktion |
| `*args, **kwargs` | Weiterleitung beliebiger Argumente |
| Dekorator mit Parametern | Drei Verschachtelungsebenen |
| Stapeln | Von unten nach oben angewendet |

---

## Aufgaben

{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/01_funktion_als_argument.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/02_was_ist_die_ausgabe.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/03_logging_dekorator.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/04_zeitmessung.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/05_functools_wraps.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/06_zugriffskontrolle.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/07_dekorator_mit_parameter.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/dekoratoren/08_mehrere_dekoratoren.yaml") }}
