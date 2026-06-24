# Wiederholung: Klassen, `super()` und Dunder Methods

Diese Einheit wiederholt die Klassenthemen, bei denen noch Unsicherheit
gemeldet wurde:

- `super()`
- Dunder Methods
- public, protected, private

Ziel ist, dass die Teilnehmenden fremden Klassencode lesen, Ausgaben
vorhersagen und kleine Klassen sauber implementieren koennen.

## Lernziele

Am Ende kann ich ...

- nach einem Konstruktor-Aufruf sagen, welche Attribute im Objekt liegen.
- erklaeren, warum `super().__init__()` wichtig ist.
- mindestens drei Dunder Methods einer Syntax zuordnen.
- public, protected und private in Python unterscheiden.
- Name Mangling in `obj.__dict__` erkennen.

## `super()`

`super()` bedeutet nicht einfach "die Elternklasse". Es bedeutet:
Rufe die naechste passende Methode in der Method Resolution Order auf.

Fuer einfache Vererbung kann man es so lesen:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
```

`super().__init__(brand)` sorgt dafuer, dass der Konstruktor von `Vehicle`
ausgefuehrt wird. Ohne diesen Aufruf fehlt `brand` auf dem Objekt.

!!! tip "Prueffrage"
    Nach jedem Konstruktor sollte man fragen: Welche Attribute stehen danach
    in `obj.__dict__`?

## Dunder Methods

Dunder Methods sind Methoden mit doppeltem Unterstrich vorne und hinten:
`__init__`, `__str__`, `__len__`, `__eq__`, `__add__`.

Sie werden meist nicht direkt aufgerufen. Python ruft sie automatisch auf:

| Ausdruck | ruft intern auf |
|----------|-----------------|
| `str(obj)` oder `print(obj)` | `obj.__str__()` |
| `len(obj)` | `obj.__len__()` |
| `a == b` | `a.__eq__(b)` |
| `a + b` | `a.__add__(b)` |
| `obj[key]` | `obj.__getitem__(key)` |

Wichtig:

- Eigene normale Methoden sollen nicht wie Dunder Methods benannt werden.
- Dunder Methods implementiert man nur, wenn man vorhandenes Python-Verhalten
  sinnvoll an die eigene Klasse anpasst.
- `__name` ist nicht dasselbe wie `__str__`: `__name` wird gemangled,
  `__str__` ist eine Magic Method.

## Public, protected, private

Python nutzt Konventionen statt harte Zugriffssperren.

| Schreibweise | Bedeutung | Zugriff technisch moeglich? |
|--------------|-----------|-----------------------------|
| `self.name` | public | ja |
| `self._name` | protected/interner Gebrauch | ja |
| `self.__name` | private durch Name Mangling | ja, aber umbenannt |

Beispiel:

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._active = True
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = Account("Ada", 100)
print(account.owner)
print(account._active)
print(account.__dict__)
```

`__balance` wird intern zu `_Account__balance`. Das ist kein echter Tresor,
sondern ein Schutz gegen versehentliches Ueberschreiben.

!!! warning "Wichtiger Hinweis"
    Python versteckt weniger als Java. Viele Dinge sind Konventionen. Wer Python
    verstehen will, muss deshalb nicht nur fragen: "Geht das technisch?", sondern
    auch: "Ist das so gedacht?"

## Aufgaben

{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/08_super_output.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/09_super_reparieren.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/10_dunder_book.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/11_dunder_inventory.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/12_public_protected_private.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/13_name_mangling_output.yaml") }}

## Integration

Diese Aufgaben verbinden Klassen mit `args/kwargs` und Modulen:

{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/14_resource_tracker_refactoring.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/15_abschlussprojekt_kursverwaltung.yaml") }}
