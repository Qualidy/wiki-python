# Polymorphismus & Introspection

Polymorphismus und Introspection sind zwei unterschiedliche, aber sehr
prüfungsnahe OOP-Themen.

- **Polymorphismus**: Der gleiche Methodenaufruf kann bei verschiedenen
  Objekten unterschiedliches Verhalten auslösen.
- **Introspection**: Ein Programm kann zur Laufzeit Informationen über Objekte
  und Klassen untersuchen.

## Polymorphismus

Polymorphismus bedeutet wörtlich "Vielgestaltigkeit". In OOP heißt das:
Verschiedene Klassen können dieselbe Methode anbieten, aber unterschiedlich
implementieren.

```python
class Document:
    def export(self):
        return "Exportiere Dokument"


class PdfDocument(Document):
    def export(self):
        return "Exportiere PDF"


class HtmlDocument(Document):
    def export(self):
        return "Exportiere HTML"


documents = [
    PdfDocument(),
    HtmlDocument(),
    Document(),
]

for document in documents:
    print(document.export())
```

Die Schleife ruft immer `document.export()` auf. Python entscheidet aber zur
Laufzeit, welche konkrete Methode ausgeführt wird.

## Runtime-Polymorphismus in Python

In manchen Sprachen unterscheidet man zwischen Compile-Time-Polymorphismus und
Runtime-Polymorphismus.

| Begriff | Idee | Python-Bezug |
|---------|------|--------------|
| Compile-Time-Polymorphismus | Entscheidung schon beim Übersetzen, z.B. Method Overloading | Python hat kein klassisches Method Overloading wie Java |
| Runtime-Polymorphismus | Entscheidung zur Laufzeit anhand des tatsächlichen Objekts | sehr wichtig in Python |

Python entscheidet Methodenaufrufe dynamisch zur Laufzeit. Deshalb ist
Runtime-Polymorphismus für Python besonders relevant.

!!! warning "Kein klassisches Method Overloading"
    In Java kann es mehrere Methoden mit gleichem Namen, aber unterschiedlichen
    Parametern geben. In Python ersetzt eine spätere Definition mit gleichem
    Namen die vorherige.

```python
class Example:
    def show(self, value):
        return f"ein Wert: {value}"

    def show(self, value_1, value_2):
        return f"zwei Werte: {value_1}, {value_2}"


example = Example()
print(example.show(1, 2))
# print(example.show(1))  # TypeError
```

## Overriding

**Overriding** bedeutet: Eine Unterklasse definiert eine Methode neu, die es
in der Oberklasse bereits gibt.

```python
class Notification:
    def send(self, message):
        return f"Sende Nachricht: {message}"


class EmailNotification(Notification):
    def send(self, message):
        return f"Sende E-Mail: {message}"


class SmsNotification(Notification):
    def send(self, message):
        return f"Sende SMS: {message}"


notifications = [
    EmailNotification(),
    SmsNotification(),
]

for notification in notifications:
    print(notification.send("Hallo"))
```

Der aufrufende Code muss nicht wissen, ob es eine E-Mail oder SMS ist.
Er braucht nur die gemeinsame Methode `send()`.

## Polymorphismus ohne Vererbung

Polymorphismus funktioniert in Python auch ohne gemeinsame Oberklasse. Wichtig
ist, dass die Objekte die erwartete Methode besitzen.

```python
class CsvExporter:
    def export(self, rows):
        return "CSV exportiert"


class JsonExporter:
    def export(self, rows):
        return "JSON exportiert"


def run_export(exporter, rows):
    return exporter.export(rows)


print(run_export(CsvExporter(), []))
print(run_export(JsonExporter(), []))
```

Dieses Prinzip wird oft **Duck Typing** genannt:

!!! note "Duck Typing"
    Entscheidend ist nicht der deklarierte Typ, sondern ob ein Objekt die
    benötigte Methode oder Eigenschaft hat.

## `isinstance()` statt `type()`

`type()` prüft den exakten Typ. `isinstance()` berücksichtigt Vererbung.

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()

print(type(car) == Car)          # True
print(type(car) == Vehicle)      # False
print(isinstance(car, Car))      # True
print(isinstance(car, Vehicle))  # True
```

Für OOP-Aufgaben ist `isinstance()` oft die bessere Wahl.

## `is`, `not is` und `==`

`==` prüft Gleichheit. `is` prüft Identität.

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)      # True
print(list_a is list_b)      # False
print(list_a is list_c)      # True
print(list_b is not list_c)  # True
```

Bei eigenen Klassen hängt `==` vom Verhalten von `__eq__` ab. Ohne `__eq__`
verhalten sich `==` und `is` bei vielen eigenen Objekten ähnlich, weil dann
die Objektidentität verglichen wird.

## Introspection

Introspection bedeutet: Ein Programm untersucht zur Laufzeit seine eigenen
Objekte, Klassen und Attribute.

```python
class Product:
    tax_rate = 0.19

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def gross_price(self):
        return self.price * (1 + self.tax_rate)


product = Product("Tastatur", 40)

print(product.__dict__)
print(Product.__dict__)
print(hasattr(product, "price"))
print(hasattr(product, "tax_rate"))
print(Product.__name__)
print(Product.__module__)
print(Product.__bases__)
```

Wichtig ist der Unterschied zwischen Objekt und Klasse:

| Ausdruck | Bedeutung |
|----------|-----------|
| `product.__dict__` | Attribute dieser Instanz |
| `Product.__dict__` | Attribute und Methoden der Klasse |
| `hasattr(product, "price")` | prüft, ob Zugriff auf `product.price` möglich ist |
| `Product.__name__` | Name der Klasse |
| `Product.__module__` | Modul, in dem die Klasse definiert wurde |
| `Product.__bases__` | direkte Oberklassen |

!!! warning "Achtung bei `hasattr()`"
    `hasattr(product, "tax_rate")` ist `True`, obwohl `tax_rate` nicht in
    `product.__dict__` steht. Python sucht auch in der Klasse.

## Name Mangling mit Introspection

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance


account = Account("Ada", 100)

print(account.__dict__)
print(hasattr(account, "__balance"))
print(hasattr(account, "_Account__balance"))
```

Das Attribut `__balance` wird intern zu `_Account__balance`.

## Zusammenfassung

| Konzept | Bedeutung |
|---------|-----------|
| Polymorphismus | gleicher Aufruf, unterschiedliches Verhalten |
| Overriding | Unterklasse ersetzt Methode der Oberklasse |
| Duck Typing | Objekt muss Verhalten besitzen, nicht zwingend bestimmten Typ |
| `isinstance()` | prüft Typ inklusive Oberklassen |
| `type()` | prüft exakten Typ |
| `is` | prüft Identität |
| `==` | prüft Gleichheit |
| Introspection | Objekte und Klassen zur Laufzeit untersuchen |

{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/03_polymorphismus_vorhersagen.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/04_duck_typing_exporter.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/05_introspection_dict.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/20_notification_polymorphismus.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/21_type_isinstance_output.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/22_inspect_function_coden.yaml") }}
