# Magic Methods

{{ youtube_video("https://www.youtube.com/embed/Hh3WjbbNxc8?si=f5tWVjBhaW3eRcNb") }}

Magische Methoden (engl. _Magic Methods_), 
auch als Dunder (Double Underscore) Methods bekannt, 
sind spezielle Methoden in Python-Klassen, die durch doppelte Unterstriche
(`__`) am Anfang und Ende ihres Namens gekennzeichnet sind.
Diese Methoden bieten eine Möglichkeit, benutzerdefiniertes Verhalten
in Klassen zu implementieren, die mit Python-Operatoren und eingebauten
Funktionen interagieren.

⚠ Es dürfen niemals eigene Magic Methods definiert werden. Dieses
Vorrecht gilt nur für die Entwickler von Python selbst. Denn man weiß
nie, welche Dunder Method sie sich in zukunft ausdenken werden.
Und wenn diese zufällig denselben Namen trägt, wie unsere eigene,
so haben wir ein Problem.

## Beispiel 1: Punkte

Angenommen, wir haben eine Klasse `Punkt`,
die die Koordinaten eines Punkts im 2D-Raum repräsentiert.
Wir definieren zwei Methoden:

* `to_str` gibt einen für Menschen verständlichen String an, der den Inhalt von Punkt zurückgibt.
* `add` addiert zwei Punkte, indem die beiden `x`-Werte und die beiden `y`-Werte miteinander addiert werden und ein neuer Punkt erzeugt wird. 

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20Punkt%3A%0A%20%20%20%20def%20__init__%28self,%20x,%20y%29%3A%0A%20%20%20%20%20%20%20%20self.x%20%3D%20x%0A%20%20%20%20%20%20%20%20self.y%20%3D%20y%0A%0A%20%20%20%20def%20to_str%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%28%7Bself.x%7D,%20%7Bself.y%7D%29%22%0A%0A%20%20%20%20def%20add%28self,%20other%29%3A%0A%20%20%20%20%20%20%20%20if%20isinstance%28other,%20Punkt%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Punkt%28self.x%20%2B%20other.x,%20self.y%20%2B%20other.y%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20TypeError%28%22Unsupported%20operand%20type.%20Use%20with%20another%20Punkt%20object.%22%29%0A%0AA%20%3D%20Punkt%282,%201%29%0AB%20%3D%20Punkt%28-1,%202%29%0AC%20%3D%20A.add%28B%29%0Aprint%28f%22A%20%2B%20B%20%3D%20%7BA.to_str%28%29%7D%20%2B%20%7BB.to_str%28%29%7D%20%3D%20%7BC.to_str%28%29%7D%20%3D%20C%22%29%0Aprint%28C%29%20%23%20zeigt%20nicht%20die%20Attribute%20der%20Instanz%20an,%20sondern%20nur%20Klasse%20und%20Hash&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_str(self):
        return f"({self.x}, {self.y})"

    def add(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")

A = Punkt(2, 1)
B = Punkt(-1, 2)
C = A.add(B)
print(f"A + B = {A.to_str()} + {B.to_str()} = {C.to_str()} = C")
print(C) # zeigt nicht die Attribute der Instanz an, sondern nur Klasse und Hash
```

Die Addition von zwei Punkten kann man sich übrigens mit folgender Darstellung visualisieren:

<iframe src="https://www.geogebra.org/calculator/nvsg8kfd?embed" width="700" height="500" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Dieser Code ist funktionsfähig, aber kann komfortabler geschrieben werden.
Wir möchten nämlich statt `A.add(B)` gerne einfach `A + B` schreiben können.
Und statt `A` händisch mit `A.to_str()` in ein String umzuwandeln, wäre es schön,
wenn auch das automatisch im f-String passieren würde. Denn erinnern wir uns:
auf alle Variablen in einem f-String, die aufgelöst werden sollen, wird ja `str` ausgeführt.

Beide wünsche lassen sich mit entsprechenden Magic bzw. Dunder Methods lösen!

Um die Addition mit `+` zu ermöglichen können wir einfach `__add__` implementieren 
und für die automatische Konvertierung in Strings können wir `__str__` implementieren:

Angenommen, wir haben eine Klasse `Punkt`, die die Koordinaten eines Punkts im 2D-Raum repräsentiert:

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20Punkt%3A%0A%20%20%20%20def%20__init__%28self,%20x,%20y%29%3A%0A%20%20%20%20%20%20%20%20self.x%20%3D%20x%0A%20%20%20%20%20%20%20%20self.y%20%3D%20y%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%28%7Bself.x%7D,%20%7Bself.y%7D%29%22%0A%0A%20%20%20%20def%20__add__%28self,%20other%29%3A%0A%20%20%20%20%20%20%20%20if%20isinstance%28other,%20Punkt%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20Punkt%28self.x%20%2B%20other.x,%20self.y%20%2B%20other.y%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20TypeError%28%22Unsupported%20operand%20type.%20Use%20with%20another%20Punkt%20object.%22%29%0A%0AA%20%3D%20Punkt%282,%201%29%0AB%20%3D%20Punkt%28-1,%202%29%0AC%20%3D%20A%20%2B%20B%0Aprint%28f%22A%20%2B%20B%20%3D%20%7BA%7D%20%2B%20%7BB%7D%20%3D%20%7BC%7D%20%3D%20C%22%29%0Aprint%28C%29%20%23%20Zeigt%20die%20definierte%20Stringdarstellung%20der%20Klasse%20an.&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

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

A = Punkt(2, 1)
B = Punkt(-1, 2)
C = A + B
print(f"A + B = {A} + {B} = {C} = C")
print(C) # Zeigt die definierte Stringdarstellung der Klasse an.
```

# Magic Methods:

| Magic/Dunder Method | ermöglicht       | Beschreibung                                                                                                                                                                                         | Dokumentation                                                                           |
|---------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `__str__`           | `print(x)`       | Diese magische Methode wird aufgerufen, wenn die `str`-Funktion auf ein Objekt angewendet wird. Sie ermöglicht die Definition einer benutzerfreundlichen Zeichenfolge, die das Objekt repräsentiert. | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__str__)      | |
| `__add__`           | `x + y`          | Diese magische Methode wird aufgerufen, wenn das `+`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Addition von zwei Objekten der Klasse.                                | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__add__)      |
| `__len__`           | `len(x)`         | Diese magische Methode wird aufgerufen, wenn die `len`-Funktion auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Anzahl von Elementen in einem Objekt.                              | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__len__)      |
| `__sub__`           | `x - y`          | Diese magische Methode wird aufgerufen, wenn das `-`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Subtraktion von zwei Objekten der Klasse.                             | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__sub__)      |
| `__eq__`            | `x == y`         | Diese magische Methode wird aufgerufen, um die Gleichheit von zwei Objekten zu überprüfen.                                                                                                           | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__eq__)       |
| `__ne__`            | `x != y`         | Diese magische Methode wird aufgerufen, um die Ungleichheit von zwei Objekten zu überprüfen.                                                                                                         | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__ne__)       |
| `__lt__`            | `x < y`          | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt kleiner als ein anderes ist.                                                                                                 | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__lt__)       |
| `__le__`            | `x <= y`         | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt kleiner oder gleich einem anderen ist.                                                                                       | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__le__)       |
| `__gt__`            | `x > y`          | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt größer als ein anderes ist.                                                                                                  | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__gt__)       |
| `__ge__`            | `x >= y`         | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt größer oder gleich einem anderen ist.                                                                                        | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__ge__)       |
| `__getitem__`       | `x[key]`         | Diese magische Methode wird aufgerufen, um den Zugriff auf ein Element mittels Index zu ermöglichen.                                                                                                 | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__getitem__)  |
| `__setitem__`       | `x[key] = value` | Diese magische Methode wird aufgerufen, um das Setzen eines Elements mittels Index zu ermöglichen.                                                                                                   | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__setitem__)  |
| `__contains__`      | `x in y`         | Diese magische Methode wird aufgerufen, um zu prüfen, ob ein Objekt ein bestimmtes Element enthält.                                                                                                  | [Dokumentation](https://docs.python.org/3/reference/datamodel.html#object.__contains__) |

Es gibt noch weitere ... 😉

{{ task(file="tasks/python_grundlagen/oop/magic_methods/magic_methods/01_weiter_mit_punkten.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/magic_methods/magic_methods/02_was_ist_notig.yaml") }}
