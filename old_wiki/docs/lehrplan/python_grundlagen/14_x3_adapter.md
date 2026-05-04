# Adapter Pattern
[100min]

## Erklärung:

Das Adapter Pattern ermöglicht es, die Schnittstelle einer Klasse in eine andere Schnittstelle umzuwandeln, die ein Client erwartet. Es ermöglicht die Zusammenarbeit von Klassen, deren Schnittstellen ansonsten nicht kompatibel wären.

Hier ein Beispiel aus der echten Welt, welches wir auch programmatorisch (vereinfacht) umsetzen können.

![Sockets](res/sockets.jpg)

Beispiel:

```python
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 120

class EuropeanToUSAdapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        return self.european_socket.voltage() / 2

# Verwendung des Adapter Patterns
european_socket = EuropeanSocket()
adapter = EuropeanToUSAdapter(european_socket)

print(f"European Socket Voltage: {european_socket.voltage()}V")
print(f"Adapter Voltage: {adapter.voltage()}V (adapted)")
```


# Aufgaben:
[150min]

## 1. Fahrzeugservice 🌶️️🌶️️🌶️️

Angenommen, du hast eine Anwendung, die mit einem externen Fahrzeugservice kommuniziert. Der Service liefert Informationen über Fahrzeuge, jedoch nicht in dem Format, das deine Anwendung erwartet. Implementiere ein Adapter Pattern, um die Schnittstelle des Fahrzeugservices an die Anforderungen deiner Anwendung anzupassen.

**Teilschritte:**

a. Definiere eine Schnittstelle, die die erwarteten Funktionen für die Zusammenarbeit mit dem Fahrzeugservice festlegt.

b. Erstelle eine Klasse `FahrzeugAdapter`, die die Schnittstelle implementiert und den externen Fahrzeugservice integriert.

c. Integriere den `FahrzeugAdapter` in deine Anwendung und zeige, dass die Anwendung erfolgreich mit dem Fahrzeugservice zusammenarbeitet.

## Adapter für Temperaturkonvertierung 🌶️️🌶️️

Angenommen, du hast eine bestehende Klasse, die Temperaturen in Grad Celsius verarbeitet. Du möchtest diese Anwendung mit einer neuen Temperaturquelle verbinden, die Temperaturen in Fahrenheit bereitstellt. 
Implementiere ein Adapter Pattern, um die Integration zu ermöglichen.

Wichtig: Die bestehende Klasse für die Temperatur in Celcius soll nicht verändert werden.

### a. Verstehen der bestehenden Anwendung

Die bestehende Anwendung erwartet Temperaturen im folgenden Format:

```python
class CelsiusTemperature:
    def __init__(self, value):
        self.value = value
```

Die Anwendung verwendet diese Temperaturdaten für verschiedene Berechnungen.

### b. Neue Temperaturquelle vorbereiten

Die neue Temperaturquelle stellt Temperaturen in Fahrenheit bereit:

```python
class FahrenheitTemperature:
    def __init__(self, value):
        self.value = value
```

### c. Implementierung des Adapters

Implementiere ein Adapter Pattern, um `FahrenheitTemperature` in `CelsiusTemperature` umzuwandeln:

```python
class FahrenheitToCelsiusAdapter:
    def __init__(self, fahrenheit_temperature):
        self.fahrenheit_temperature = fahrenheit_temperature

    def adapt_temperature(self):
        # Hier implementiere die Logik zur Umwandlung von Fahrenheit zu Celsius
```

_Tipp:_ Die Formel für die Umrechnung lautet F = (9/5)C + 32


### d. Integration in die Anwendung

Passe die bestehende Anwendung an, um den Adapter zu verwenden:

```python
class ExistingApplication:
    def process_temperature(self, temperature):
        # Hier befindet sich die bestehende Logik, die CelsiusTemperature erwartet
        print(f"Processed temperature: {temperature.value}°C")

# Integriere den Adapter in die Anwendung
fahrenheit_source = FahrenheitTemperature(value=98.6)  # Beispielwert in Fahrenheit
adapter = FahrenheitToCelsiusAdapter(fahrenheit_temperature=fahrenheit_source)

existing_application = ExistingApplication()
existing_application.process_temperature(temperature=adapter.adapt_temperature())
```
