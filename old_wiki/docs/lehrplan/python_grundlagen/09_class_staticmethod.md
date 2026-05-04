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

## 1. Statische Methode erstellen 🌶️️

Erstelle eine Klasse mit einer statischen Methode.
Die statische Methode soll eine einfache Berechnung durchführen und das Ergebnis zurückgeben. 
Demonstriere den Aufruf dieser Methode über die Klasse.

## 2. Klassenmethode für Initialisierung 🌶️️🌶️️

Implementiere eine Klassenmethode in einer Klasse `Person`, 
die für die Initialisierung von Instanzen verwendet wird. 
Die Klassenmethode sollte alternative Wege zur Instanzierung ermöglichen. 
Demonstriere den Gebrauch der Klassenmethode.

Hier als Hilfestellung eine allgemeine Struktur für die Implementierung der
Klassenmethode in der Klasse `Person`:

```python
class Person:
    def __init__(self, name, age):
        # Konstruktorcode hier

    @classmethod
    def alternative_instanzierung(cls, parameter):
        # Implementierung der Klassenmethode hier
        # Verwende 'cls', um auf die Klasse zuzugreifen und eine neue Instanz zu erstellen
        return cls(neue_parameter_werte)
```

## 3. Verwendung von statischen und Klassenmethoden 🌶️️🌶️️🌶️️

Erkläre in eigenen Worten, wann es sinnvoll ist, statische Methoden und Klassenmethoden zu verwenden. Beschreibe Situationen, in denen diese Methoden nützlich sein könnten.

## 4. Statische Methode für Dateiverarbeitung 🌶️️🌶️️

Erstelle eine Klasse, die eine statische Methode `read_file` enthält. Die Methode soll den Inhalt einer Textdatei einlesen und zurückgeben. Demonstriere die Verwendung dieser Methode, indem du eine Textdatei liest und den Inhalt ausgibst.

## 5. Klassenmethode für spezielle Instanziierung 🌶️️🌶️️🌶️️

Implementiere eine Klasse `Person`, die eine Klassenmethode `create_adult` enthält. Diese Methode soll eine Instanz der Person-Klasse zurückgeben, bei der das Alter auf 18 gesetzt ist. Erstelle anschließend eine Person-Instanz mithilfe dieser Klassenmethode.

## 6. Logik mit statischer Methode 🌶️️🌶️️

Erstelle eine Klasse `Calculator`, die eine statische Methode `is_prime` enthält. Die Methode soll überprüfen, ob eine übergebene Zahl eine Primzahl ist, und `True` oder `False` zurückgeben. Demonstriere den Einsatz dieser statischen Methode, indem du einige Zahlen auf ihre Primzahl-Eigenschaft prüfst.

## 7. Klassenmethode zur Verfolgung von Instanzen 🌶️️🌶️️🌶️️

Erweitere die Klasse `Car` um eine Klassenmethode `get_total_brand`. Diese Methode soll als Parameter eine Automarke erhalten und die Gesamtanzahl von Autos dieser Marke zurückgeben. Demonstriere die Funktionalität, indem du mehrere Autos unterschiedlicher Marken erstellst und die Gesamtanzahl für eine bestimmte Marke abrufst.

## 8. Kombination von statischen und Klassenmethoden 🌶️️🌶️️🌶️️🌶️️

Entwickle eine Klasse `StringManipulator` mit einer statischen Methode `reverse_string`, die einen übergebenen String umkehrt, und einer Klassenmethode `capitalize_string`, die einen übergebenen String in Großbuchstaben umwandelt. Kombiniere beide Methoden, indem du einen String erst umkehrst und dann das Ergebnis großschreibst. Demonstriere die Anwendung dieser Methoden.

Diese praktischen Aufgaben sollen dir helfen, die Konzepte der statischen Methoden und Klassenmethoden in Python besser zu verstehen und in realen Situationen anzuwenden.
