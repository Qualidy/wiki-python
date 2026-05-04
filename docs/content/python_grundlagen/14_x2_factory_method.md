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

## 1. Autorennen mit Factory Method Pattern 🌶️️🌶️️🌶️️

### Teilschritte:

a. Definiere eine Schnittstelle `Vehicle` mit einer Methode `start_engine`, die den Motor startet.

b. Implementiere konkrete Fahrzeugtypen, die von `Vehicle` erben, z. B. `Car`, `Motorcycle`, und `Truck`.

c. Erstelle eine abstrakte Klasse `RaceFactory` mit der Factory-Methode `create_vehicle`, die ein Fahrzeug erstellt.

d. Implementiere konkrete Fabriken, die von `RaceFactory` erben, z. B. `CarFactory`, `MotorcycleFactory`, und `TruckFactory`.

e. Demonstriere die Verwendung, indem du eine Rennsimulation erstellst und verschiedene Fahrzeugtypen erstellst.

## 2. Kaffeemaschine 🌶️️🌶️️

### Teilschritte:

a. Definiere eine Schnittstelle `Beverage` mit einer Methode `brew`, die das Getränk zubereitet.

b. Implementiere konkrete Getränketypen, die von `Beverage` erben, z. B. `Coffee`, `Tea`, und `HotChocolate`.

c. Erstelle eine abstrakte Klasse `BeverageFactory` mit der Factory-Methode `create_beverage`, die ein Getränk erstellt.

d. Implementiere konkrete Fabriken, die von `BeverageFactory` erben, z. B. `CoffeeFactory`, `TeaFactory`, und `HotChocolateFactory`.

e. Zeige die Anwendung, indem du eine Kaffeemaschinen-Simulation erstellst und verschiedene Getränketypen zubereitest.
