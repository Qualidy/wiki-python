# Factory Method Pattern
[60min]

## Erklärung:

Das Factory Method Pattern ist ein Erzeugungsmuster, das die Erstellung von Objekten in Unterklassen delegiert. Es definiert eine Schnittstelle zur Erstellung eines Objekts, lässt aber die Unterklassen entscheiden, welche Klasse instanziiert werden soll.

### Beispiel:

Im nachfolgenden Beispiel verwenden wir das Factory Method Pattern im verschiedene Autoarten zu erstellen. Die Klasse `Car` repräsentiert ein Auto mit einer Methode `drive`, die das Fahrverhalten beschreibt. Die konkreten Klassen `CompactCar` und `SUV` implementieren unterschiedliche Arten von Autos.

### Codebeispiel:

```python
class Car:
    def drive(self):
        pass

class CompactCar(Car):
    def drive(self):
        return "Fahre als Kleinwagen."

class SUV(Car):
    def drive(self):
        return "Fahre als SUV."

class CarFactory:
    def create_car(self, car_type):
        if car_type == "compact":
            return CompactCar()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("Ungültiger Autotyp")

# Hier wird die Factory verwendet
car_factory = CarFactory()

compact_car = car_factory.create_car("compact")
suv = car_factory.create_car("suv")

print(compact_car.drive())  # Ausgabe: Fahre als Kleinwagen.
print(suv.drive())          # Ausgabe: Fahre als SUV.
```

Die Klasse `Car` dient als Schnittstelle, und die konkreten Klassen `CompactCar` und `SUV` implementieren die spezifischen Details für Kleinwagen und SUVs. Die `CarFactory` erstellt Autos basierend auf dem angegebenen Autotyp.

# Aufgaben:
[220min]

{{ task(file="tasks/python_grundlagen/14_x2_factory_method/01_autorennen_mit_factory_method_pattern.yaml") }}
{{ task(file="tasks/python_grundlagen/14_x2_factory_method/02_kaffeemaschine.yaml") }}
