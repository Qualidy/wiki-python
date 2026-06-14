# OOP Wiederholung

Bevor neue OOP-Themen dazukommen, werden die Grundlagen wiederholt. Ziel ist,
Klassen nicht nur schreiben, sondern auch in fremdem Code sicher erkennen zu
können.

## Klasse und Objekt

Eine **Klasse** ist ein Bauplan. Ein **Objekt** ist ein konkretes Exemplar
dieses Bauplans.

```python
class Person:
    pass


person_1 = Person()
person_2 = Person()

print(type(person_1))
print(person_1 is person_2)
```

`person_1` und `person_2` haben denselben Typ, sind aber nicht dasselbe Objekt.

## Attribute

Attribute speichern Daten. Instanzattribute gehören zu einem konkreten Objekt.

```python
class Person:
    pass


person = Person()
person.name = "Ada"
person.age = 32

print(person.__dict__)
```

Die Ausgabe zeigt die Attribute dieser Instanz:

```python
{'name': 'Ada', 'age': 32}
```

## Konstruktor `__init__`

Mit `__init__` wird ein Objekt direkt beim Erzeugen initialisiert.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Ada", 32)
print(person.name)
print(person.__dict__)
```

`__init__` gibt normalerweise nichts zurück. Die Methode richtet das frisch
erstellte Objekt ein.

## Methoden und `self`

Methoden sind Funktionen, die zu einer Klasse gehören. Der erste Parameter
einer Instanzmethode heißt per Konvention `self`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hallo, ich bin {self.name}."


person = Person("Ada")
print(person.introduce())
```

`self` ist das Objekt, auf dem die Methode gerade aufgerufen wurde.

## Instanzattribute und Klassenattribute

Klassenattribute werden im Klassenrumpf definiert. Instanzattribute werden
meist im Konstruktor über `self` gesetzt.

```python
class Course:
    platform = "Python Wiki"

    def __init__(self, title):
        self.title = title


course = Course("OOP")

print(course.title)
print(course.platform)
print(course.__dict__)
print(Course.__dict__["platform"])
```

`platform` ist über die Instanz erreichbar, steht aber nicht in
`course.__dict__`.

## Kapselung

Kapselung bedeutet, dass Daten und Verhalten zusammen in einer Klasse liegen.
Python nutzt dafür Konventionen:

| Schreibweise | Bedeutung |
|--------------|-----------|
| `name` | öffentlich |
| `_name` | intern gedacht, Zugriff technisch möglich |
| `__name` | Name Mangling, wird intern umbenannt |

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = Account("Ada", 100)
print(account.__dict__)
```

`__balance` wird intern zu `_Account__balance`.

## Vererbung und `super()`

Eine Unterklasse kann Attribute und Methoden einer Oberklasse übernehmen.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} startet."


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


car = Car("VW", 4)
print(car.start())
print(car.__dict__)
```

`super().__init__(brand)` ruft den Konstruktor der nächsten Klasse in der
Vererbungskette auf.

## Overriding

Eine Unterklasse kann eine Methode der Oberklasse ersetzen.

```python
class Vehicle:
    def start(self):
        return "Das Fahrzeug startet."


class Bicycle(Vehicle):
    def start(self):
        return "Das Fahrrad rollt los."


print(Bicycle().start())
```

Das ist die Grundlage für Polymorphismus.

{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/01_oop_wiederholung_quiz.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/02_klassenattribute_dict.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/13_expected_output_basics.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/14_bankkonto_kapselung.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/15_kursverwaltung_modellieren.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/16_constructor_super_debug.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/17_refactoring_dict_to_class.yaml") }}
