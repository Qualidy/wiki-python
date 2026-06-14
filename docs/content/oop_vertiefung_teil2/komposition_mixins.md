# Komposition, Vererbung & Mixins

Bei OOP geht es nicht nur darum, Klassen zu schreiben. Eine wichtige Frage ist:

**Wie sollen Klassen miteinander verbunden werden?**

Dafür gibt es mehrere Möglichkeiten. Die wichtigsten sind Vererbung,
Komposition und Mixins.

## Vererbung: ist-ein

Vererbung passt, wenn eine Klasse eine speziellere Variante einer anderen
Klasse ist.

```python
class Vehicle:
    def start(self):
        return "Fahrzeug startet"


class Car(Vehicle):
    def open_trunk(self):
        return "Kofferraum offen"
```

Ein `Car` ist ein `Vehicle`. Deshalb ist Vererbung hier plausibel.

```python
car = Car()
print(isinstance(car, Vehicle))  # True
```

## Komposition: hat-ein

Komposition passt, wenn ein Objekt ein anderes Objekt enthält oder benutzt.

```python
class Engine:
    def start(self):
        return "Motor startet"


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

Ein `Car` ist kein `Engine`. Ein `Car` hat einen `Engine`. Deshalb ist
Komposition hier besser als Vererbung.

## Entscheidungsfrage

| Frage | Wahrscheinliche Lösung |
|-------|------------------------|
| Ist A eine spezielle Form von B? | Vererbung |
| Hat A ein B oder benutzt A ein B? | Komposition |
| Soll eine Klasse eine kleine Zusatzfähigkeit bekommen? | eventuell Mixin |
| Wird die Vererbung nur genutzt, um Code zu sparen? | eher Komposition prüfen |

!!! warning "Code-Wiederverwendung allein ist kein guter Grund"
    Vererbung sollte eine fachliche Beziehung ausdrücken. Wenn eine Klasse nur
    Code einer anderen Klasse benutzen will, ist Komposition oft klarer.

## Beispiel: falsch modelliert

```python
class Database:
    def save(self, data):
        return "gespeichert"


class User(Database):
    pass
```

Ein `User` ist keine `Database`. Das Modell ist fachlich falsch. Besser:

```python
class Database:
    def save(self, data):
        return "gespeichert"


class UserRepository:
    def __init__(self, database):
        self.database = database

    def save_user(self, user):
        return self.database.save(user)
```

Das Repository benutzt eine Datenbank. Das ist Komposition.

## Mixins

Ein **Mixin** ist eine Klasse, die eine kleine Zusatzfähigkeit bereitstellt.
Mixins sind meistens nicht dafür gedacht, allein instanziiert zu werden.

```python
class JsonMixin:
    def to_json(self):
        return self.__dict__


class Product(JsonMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Tastatur", 40)
print(product.to_json())
```

`JsonMixin` beschreibt keine fachliche Oberklasse. Es ergänzt nur eine Fähigkeit.

## Mixin-Namen

Mixins werden häufig mit dem Suffix `Mixin` benannt:

- `JsonMixin`
- `LoggingMixin`
- `ValidationMixin`
- `PrintableMixin`

Das macht sichtbar, dass die Klasse eine Zusatzfähigkeit und keine fachliche
Oberklasse ist.

## Mixins und Mehrfachvererbung

Mixins verwenden Mehrfachvererbung:

```python
class PrintableMixin:
    def print_info(self):
        print(self)


class Product(PrintableMixin):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


product = Product("Tastatur")
product.print_info()
```

Bei mehreren Mixins wird die MRO wichtig. Deshalb sollten Mixins klein bleiben
und möglichst wenig eigenen Zustand besitzen.

## Komposition oder Mixin?

| Situation | Empfehlung |
|-----------|------------|
| Objekt besitzt anderes Objekt | Komposition |
| Objekt nutzt austauschbaren Helfer | Komposition |
| mehrere Klassen brauchen dieselbe kleine Methode | Mixin möglich |
| Zusatzfähigkeit braucht viele Attribute | eher Komposition |
| Konstruktor wird kompliziert | eher Komposition |

## Mini-Beispiel mit Strategie

Komposition ist auch nützlich, wenn Verhalten austauschbar sein soll.

```python
class EmailSender:
    def send(self, text):
        return f"E-Mail: {text}"


class SmsSender:
    def send(self, text):
        return f"SMS: {text}"


class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, text):
        return self.sender.send(text)


service = NotificationService(EmailSender())
print(service.notify("Hallo"))

service.sender = SmsSender()
print(service.notify("Hallo"))
```

`NotificationService` erbt nicht von `EmailSender` oder `SmsSender`. Es benutzt
ein Sender-Objekt.

{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/06_komposition_oder_vererbung.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/07_mixin_json.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/23_vererbung_komposition_refactor.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/24_strategy_sender_coden.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/25_mixin_repr_len.yaml") }}
