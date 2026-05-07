# Statische Methoden und Klassenmethoden in Python
[120min]

In Python gibt es zwei besondere Arten von Methoden, die direkt einer Klasse zugeordnet sind:
**statische Methoden** und **Klassenmethoden**. Diese Methoden haben spezielle Verwendungszwecke 
und werden mit den Dekoratoren `@staticmethod` und `@classmethod` definiert.

## Statische Methoden

Eine **statische Methode** ist eine Methode, die zu einer Klasse gehört, 
aber nicht auf eine Instanz zugreift. Sie wird mit dem Dekorator `@staticmethod` definiert 
und hat keinen Zugriff auf Instanzattribute. Statische Methoden sind in erster Linie nützlich,
wenn eine Methode nur auf Klassenebene operieren muss und keine Instanzinformationen benötigt.

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Aufruf der statischen Methode über die Klasse
result = MathUtils.add(3, 5)
print(result)  # Ausgabe: 8
```

## Klassenmethoden

Eine **Klassenmethode** ist eine Methode, die auf die Klasse selbst zugreift und nicht auf Instanzattribute.
Sie wird mit dem Dekorator `@classmethod` definiert und erhält die Klasse selbst als ersten Parameter (`cls`).
Klassenmethoden werden oft für alternative Konstruktoren oder zur Manipulation der Klasse selbst verwendet.

```python
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# Aufruf der Klassenmethode über die Klasse
total = Car.get_total_cars()
print(total)  # Ausgabe: 0 (vor der Instanziierung)

car1 = Car("Volkswagen")
car2 = Car("Toyota")

total_now = Car.get_total_cars()
print(total_now)  # Ausgabe: 2 (nach der Instanziierung von zwei Autos)
```

# Aufgaben:
[320min]

{{ task(file="tasks/python_grundlagen/09_class_staticmethod/01_statische_methode_erstellen.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/02_klassenmethode_fur_initialisierung.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/03_verwendung_von_statischen_und_klassenmethoden.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/04_statische_methode_fur_dateiverarbeitung.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/05_klassenmethode_fur_spezielle_instanziierung.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/06_logik_mit_statischer_methode.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/07_klassenmethode_zur_verfolgung_von_instanzen.yaml") }}
{{ task(file="tasks/python_grundlagen/09_class_staticmethod/08_kombination_von_statischen_und_klassenmethoden.yaml") }}
