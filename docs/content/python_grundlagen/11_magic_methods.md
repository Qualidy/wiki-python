# Magic Methods in Python
[120min]

Magische Methoden (engl. _Magic Methods_), 
auch als Dunder (Double Underscore) Methods bekannt, 
sind spezielle Methoden in Python-Klassen, die durch doppelte Unterstriche
(`__`) am Anfang und Ende ihres Namens gekennzeichnet sind.
Diese Methoden bieten eine Möglichkeit, benutzerdefiniertes Verhalten
in Klassen zu implementieren, die mit Python-Operatoren und eingebauten
Funktionen interagieren.

## Beispiel: `__str__` und `__add__`

Angenommen, wir haben eine Klasse `Punkt`, die die Koordinaten eines Punkts im 2D-Raum repräsentiert:

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")
```

In diesem Beispiel:

- Die `__str__`-Methode wird aufgerufen, wenn die `str`-Funktion auf ein Objekt angewendet wird. Sie gibt eine lesbare Zeichenfolge zurück, die das Objekt repräsentiert.

- Die `__add__`-Methode wird aufgerufen, wenn das `+`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Addition von zwei `Punkt`-Objekten.

## Weitere magische Methoden:

- `__len__`: Wird aufgerufen, wenn die `len`-Funktion auf ein Objekt angewendet wird. Implementiere diese Methode, um die Anzahl der Koordinaten im Punkt zurückzugeben.

- `__sub__`: Wird aufgerufen, wenn das `-`-Zeichen auf ein Objekt angewendet wird. Ergänze die `Punkt`-Klasse um diese Methode, um die Subtraktion von zwei `Punkt`-Objekten zu ermöglichen.

- `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`: Diese Methoden ermöglichen benutzerdefinierte Vergleichsoperationen zwischen Objekten.

- `__getitem__`, `__setitem__`: Ermöglichen den Zugriff auf Koordinaten über Indexe.

- `__contains__`: Wird aufgerufen, wenn die `in`-Keyword auf ein Objekt angewendet wird. Implementiere diese Methode, um zu überprüfen, ob eine bestimmte Koordinate in einem `Punkt`-Objekt vorhanden ist.

## Beispiel: Verwendung der magischen Methoden

```python
# Erstellen von Punkt-Objekten
punkt1 = Punkt(2, 3)
punkt2 = Punkt(1, 5)

# Verwendung von __str__
print(str(punkt1))  # Ausgabe: (2, 3)

# Verwendung von __add__
ergebnis = punkt1 + punkt2
print(str(ergebnis))  # Ausgabe: (3, 8)

# Verwendung von __len__
anzahl_koordinaten = len(punkt1)
print(anzahl_koordinaten)  # Ausgabe: 2

# Verwendung von __sub__ (Beispiel)
punkt3 = Punkt(4, 1)
differenz = punkt1 - punkt3
print(str(differenz))  # Ausgabe: (-2, 2)

# Weitere magische Methoden können ähnlich verwendet werden.
```

# Magic Methods:

- `__str__`: Diese magische Methode wird aufgerufen, wenn die `str`-Funktion auf ein Objekt angewendet wird. Sie ermöglicht die Definition einer benutzerfreundlichen Zeichenfolge, die das Objekt repräsentiert. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__str__)

- `__add__`: Diese magische Methode wird aufgerufen, wenn das `+`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Addition von zwei Objekten der Klasse. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__add__)

- `__len__`: Diese magische Methode wird aufgerufen, wenn die `len`-Funktion auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Anzahl von Elementen in einem Objekt. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__len__)

- `__sub__`: Diese magische Methode wird aufgerufen, wenn das `-`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Subtraktion von zwei Objekten der Klasse. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__sub__)

- `__eq__`: Diese magische Methode wird aufgerufen, um die Gleichheit von zwei Objekten zu überprüfen. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__eq__)

- `__ne__`: Diese magische Methode wird aufgerufen, um die Ungleichheit von zwei Objekten zu überprüfen. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__ne__)

- `__lt__`: Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt kleiner als ein anderes ist. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__lt__)

- `__le__`: Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt kleiner oder gleich einem anderen ist. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__le__)

- `__gt__`: Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt größer als ein anderes ist. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__gt__)

- `__ge__`: Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt größer oder gleich einem anderen ist. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__ge__)

- `__getitem__`: Diese magische Methode wird aufgerufen, um den Zugriff auf ein Element mittels Index zu ermöglichen. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__getitem__)

- `__setitem__`: Diese magische Methode wird aufgerufen, um das Setzen eines Elements mittels Index zu ermöglichen. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__setitem__)

- `__contains__`: Diese magische Methode wird aufgerufen, um zu prüfen, ob ein Objekt ein bestimmtes Element enthält. [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__contains__)

# Aufgaben
[240min]

## 1. **Punkt-Klasse erweitern** 🌶️️

   Gegeben ist eine einfache `Punkt`-Klasse mit den Koordinaten `x` und `y`. 

   ```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
   ```
     
Implementiere die magische Methode `__sub__`, um zwei `Punkt`-Objekte voneinander zu subtrahieren und ein neues `Punkt`-Objekt mit den subtrahierten Koordinaten zu erstellen.

_Tipp_: Du kannst dich an dem Beispiel zum addieren zweiter Punkte orientieren.

## 2. **Benutzerfreundliche Ausgabe** 🌶️️🌶️️

   Erstelle eine Klasse `Person` mit den Attributen `name` und `alter`. Implementiere die magische Methode `__str__`, um eine benutzerfreundliche Darstellung eines `Person`-Objekts zu ermöglichen, z.B., "Name: Max, Alter: 30".

## 3. **Listenvergleich** 🌶️️🌶️️🌶️️

   Implementiere eine Klasse `BenutzerListe`, die eine Liste von Benutzerobjekten speichert. Implementiere die magische Methode `__eq__`, um zwei `BenutzerListe`-Objekte zu vergleichen. Die Gleichheit soll bedeuten, dass beide Listen die gleichen Benutzerobjekte in der gleichen Reihenfolge enthalten.

## 4. **Matrizen addieren** 🌶️️🌶️️

   Erstelle eine Klasse `Matrix`, die eine 2D-Matrix repräsentiert. Implementiere die magische Methode `__add__`, um zwei `Matrix`-Objekte zu addieren. Beachte die Regeln der Matrixaddition.

## 5. **Indizierte Wörterbuchklasse** 🌶️️🌶️️🌶️️🌶️️

   Erstelle eine Klasse `IndiziertesWörterbuch`, die wie ein Wörterbuch funktioniert, aber zusätzlich zur normalen Funktionalität auch den Zugriff auf Einträge über den Index ermöglicht. Implementiere die magischen Methoden `__getitem__` und `__setitem__` entsprechend.
