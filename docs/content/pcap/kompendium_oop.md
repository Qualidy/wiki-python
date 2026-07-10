# PCAP-Kompendium: Object-Oriented Programming

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Class | Bauplan für Objekte |
| Object / instance | konkretes Objekt einer Klasse |
| Attribute / property | gespeicherter Zustand |
| Method | Funktion, die zu einer Klasse gehört |
| `self` | Konvention für die aktuelle Instanz |
| Encapsulation | Zustand/Verhalten in Klassen bündeln |
| Inheritance | Klasse übernimmt von Superclass |
| Superclass / subclass | Elternklasse / Kindklasse |
| Polymorphism | gleicher Aufruf, unterschiedliches Verhalten |
| MRO | Method Resolution Order bei Vererbung |

## Klasse und Instanz

```python
class Spam:
    class_value = 1

    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)
```

```python
s = Spam(10)
s.show()
```

## Klassenattribute vs. Instanzattribute

```python
class Spam:
    counter = 0

    def __init__(self):
        self.value = 1
```

| Ausdruck | Bedeutung |
| --- | --- |
| `Spam.counter` | Klassenattribut |
| `s.value` | Instanzattribut |
| `Spam.__dict__` | Mapping der Klassenattribute |
| `s.__dict__` | Mapping der Instanzattribute |
| `vars(Spam)` | ähnlich `Spam.__dict__` |
| `vars(s)` | ähnlich `s.__dict__` |

## Konstruktor

```python
class Spam:
    def __init__(self, value=0):
        self.value = value
```

```python
Spam()
Spam(10)
```

Beim Aufruf `Spam(10)` übergibt Python die neue Instanz automatisch als `self`.

## Methoden

```python
class Spam:
    def method(self):
        print("method")
```

```python
s = Spam()
s.method()
```

`s.method()` entspricht konzeptionell `Spam.method(s)`.

## `super()`

```python
class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
```

Alte, aber gültige Form:

```python
super(Admin, self).__init__(name)
```

## Overriding

```python
class A:
    def run(self):
        print("A")


class B(A):
    def run(self):
        print("B")
        super().run()
```

`B().run()` gibt `B`, dann `A` aus.

## Name Mangling

```python
class Spam:
    __hidden = 1

    def __method(self):
        return 100

    method = __method
```

Python speichert `__hidden` als `_Spam__hidden`.

```python
s = Spam()
s.method()         # funktioniert
s._Spam__method()  # funktioniert
s.__method()       # AttributeError
```

## Introspection

| Funktion / Attribut | Bedeutung |
| --- | --- |
| `hasattr(obj, name)` | prüft, ob Attribut erreichbar ist |
| `isinstance(obj, classinfo)` | prüft Instanzbeziehung |
| `issubclass(cls, classinfo)` | prüft Klassenbeziehung |
| `type(obj)` | tatsächliche Klasse |
| `obj.__class__` | Klasse eines Objekts |
| `Class.__name__` | Klassenname |
| `Class.__module__` | Modulname |
| `Class.__bases__` | direkte Basisklassen |

```python
class X:
    pass


class Y:
    pass


class Z(X, Y):
    pass


z = Z()
isinstance(z, X)              # True
isinstance(z, (list, X, Y))   # True
issubclass(Z, X)              # True
```

## `__str__`

```python
class Spam:
    def __str__(self):
        return "Spam"


print(Spam())  # Spam
```

`__str__` muss einen String zurückgeben.

## Typische Fallen

### Lokale Klasse vor Definition

```python
def spam():
    h = Ham()

    class Ham:
        pass
```

`Ham` ist lokal, aber beim Zugriff noch nicht gebunden. Das führt zu `UnboundLocalError`.

### Überschriebene Methode mit anderer Signatur

```python
class Ham:
    def __init__(self):
        self.update()

    def update(self):
        print("Ham")


class Spam(Ham):
    def update(self, param):
        print("Spam")
```

`Spam()` führt zu `TypeError`, weil `Ham.__init__` `self.update()` ohne `param` aufruft.

## Mini-Checks

```python
class Spam:
    ham = 36


spam = Spam()
print(hasattr(spam, "ham"))
print(hasattr(Spam, "ham"))
```

??? success "Lösung"
    Beide Ausgaben sind `True`.

```python
class Spam:
    pass


s = Spam()
print(s.__name__)
```

??? success "Lösung"
    `AttributeError`, Instanzen haben kein eigenes `__name__`.
