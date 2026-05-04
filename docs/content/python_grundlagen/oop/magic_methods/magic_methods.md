# Magic Methods

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Hh3WjbbNxc8?si=f5tWVjBhaW3eRcNb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

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

### Aufgabe: Weiter mit Punkten🌶🌶🌶
Implementiere die passende Methode, sodass die Subraktion `A - B` zweier Punkte möglich ist.

Implementieren sie außerdem die passende Methode, um die Prüfung `A == B` durchzuführen,
mit der man zwei Punkte auf Gleichheit prüfen kann. Zwei Punkte sind gleich,
wenn alle Attribute (`x` und `y` übereinstimmen).

Wenn alles richtig eingestellt wurde, müsste dieser Test funktionieren:

```python
from unittest import TestCase


class PunktTest(TestCase):

    def test_equality_0(self):
        self.assertEqual(Punkt(1, 2), Punkt(1, 2))

    def test_equality_1(self):
        self.assertNotEqual(Punkt(1, 2), Punkt(2, 1))

    def test_equality_2(self):
        self.assertNotEqual(Punkt(1, 2), (1, 2))

    def test_sub_0(self):
        a, b = Punkt(2, 1), Punkt(-1, 2)
        self.assertEqual(a - b, Punkt(3, -1))

    def test_sub_1(self):
        a = Punkt(2, 1)
        self.assertEqual(a - a, Punkt(0, 0))

    def test_sub_2(self):
        a = Punkt(2, 1)
        a -= Punkt(-1, 2)
        self.assertEqual(a, Punkt(3, -1))
    
    def test_sub_3(self):
        with self.assertRaises(TypeError):
            Punkt(3, 2) - 4
```

<details><summary>🍀Tipps</summary>Nutze <code>__eq__</code> und <code>__sub__</code></details>

<details>
<summary>Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Mk_lv8_puuE?si=qxUZPOy2Kb378q7-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>
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

    def __eq__(self, other):
        return (isinstance(other, Punkt)
                and self.x == other.x
                and self.y == other.y)

    def __sub__(self, other):
        if other.isinstance(other, Punkt):
            return Punkt(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type. Use with another Punkt object.")
</code></pre>
</details>

**Multiplizieren von Rechts**

Implementieren Sie nun die Möglichkeit einen Punkt mit einer Zahl zu skalieren,
sodass z.B. `Punkt(1,2) * 4` als Ergebnis `Punkt(4,8)` ergibt.
Wenn mit einem anderen Typ als `int` oder `float` multipliziert wird,
so werfe einen `TypeError`.

Kannst du `__sub__` so anpassen, dass die 
Multiplikation und die Addition verwendet wird?

P - Q = P + Q * (-1)

Achte darauf, 
dass die bisherigen Tests funktionieren
und diese neuen:

```python
    def test_mul_0(self):
        self.assertEqual(Punkt(1, 2) * 4, Punkt(4, 8))

    def test_mul_1(self):
        self.assertEqual(Punkt(0, 0) * 4, Punkt(0, 0))

    def test_mul_2(self):
        self.assertEqual(Punkt(1, 4) * 0, Punkt(0, 0))

    def test_mul_3(self):
        self.assertEqual(Punkt(3, -2) * -1, Punkt(-3, 2))

    def test_mul_4(self):
        self.assertEqual(Punkt(3.5, 0.5) * 2, Punkt(7, 1))

    def test_mul_5(self):
        self.assertEqual(Punkt(0.1, 0.2) * 1.5, Punkt(0.15, 0.3))

    def test_mul_6(self):
        a = Punkt(2, 1)
        a *= 0.2
        self.assertEqual(a, Punkt(0.4, 0.2))
        
    def test_mul_7(self):
        with self.assertRaises(TypeError):
            Punkt(2, 1) * "Hallo"
            
    def test_sub_3(self):
        with self.assertRaises(TypeError):
            Punkt(2, 1) - 1

```

<details><summary>🍀Tipps</summary>Nutze <code>__mul__</code>. Um Fließkommazahlen auf Gleichheit zu
prüfen, nutze <code>isclose</code> aus <code>math</code>.</details>

<details>
<summary>Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/-_XeHICvLvM?si=vDo5yApVZ-ecgY9A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>def __eq__(self, other):
        return (isinstance(other, Punkt) 
                and isclose(self.x, other.x) 
                and isclose(self.y, other.y))

    def __sub__(self, other):
        return self + other * (-1)

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Punkt(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type. Use int or float")
</code></pre></details>

**Zugriff wie bei Listen**

Sorge nun mit den richtigen Methoden dafür, dass es möglich ist auf den `x`-Wert über den Index `0` oder `-2`
erreichbar ist und dass der `y`-Wert über den Index `1` oder `-1` erreichbar ist. Die folgenden Tests
sollen grün werden:

```python
    def test_read_0(self):
        a = Punkt(2, 1)
        self.assertEqual(2, a[0])

    def test_read_1(self):
        a = Punkt(2, 1)
        self.assertEqual(1, a[1])

    def test_read_2(self):
        a = Punkt(2, 1)
        with self.assertRaises(IndexError):
            b = a[2]

    def test_read_4(self):
        a = Punkt(2, 1)
        self.assertEqual(2, a[-2])

    def test_read_5(self):
        a = Punkt(2, 1)
        self.assertEqual(1, a[-1])

    def test_read_6(self):
        a = Punkt(2, 1)
        with self.assertRaises(IndexError):
            b = a[-3]

    def test_set_0(self):
        a = Punkt(2, 1)
        a[0] = 0
        self.assertEqual(a, Punkt(0,1))

    def test_set_1(self):
        a = Punkt(2, 1)
        a[1] = 0
        self.assertEqual(a, Punkt(2,0))

    def test_set_2(self):
        a = Punkt(2, 1)
        with self.assertRaises(IndexError):
            a[3] = 4

    def test_set_4(self):
        a = Punkt(2, 1)
        a[-1] = 0
        self.assertEqual(a, Punkt(2, 0))

    def test_set_5(self):
        a = Punkt(2, 1)
        a[-2] = 0
        self.assertEqual(a, Punkt(0,1))

    def test_set_6(self):
        a = Punkt(2, 1)
        with self.assertRaises(IndexError):
            a[-3] = 4
```

Ganz schön viele Tests, wa? 😉

<details><summary>🍀Tipps</summary>
Nutze <code>__getitem__</code> und <code>__setitem__</code>.</details>

<details>
<summary>Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9grwdOYmjSo?si=fkbyyrGxp4ANYy1z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>
    def __getitem__(self, item):
        if item in [0, -2]:
            return self.x
        elif item in [1, -1]:
            return self.y
        else:
            raise IndexError("Index muss 0 für x oder 1 für y sein.")

    def __setitem__(self, key, value):
        if key in [0, -2]:
            self.x = value
        elif key in [1, -1]:
            self.y = value
        else:
            raise IndexError("Index muss 0 für x oder 1 für y sein.")
</code></pre></details>

### Aufgabe: Was ist nötig?🌶🌶

Für die folgende Klasse sollen die Magic Methods definiert werden, sodass die Tests grün werden.
Versuche hier so wenig wie möglich Magic Methods zu definieren.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    ...
```

```python
import unittest


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.anton_alt = Person("Anton", 65)
        self.jutta_jung = Person("Jutta", 12)
        self.jut_jung = Person("Jut", 12)

    def test_lt_0(self):
        self.assertTrue(self.jutta_jung < self.anton_alt)

    def test_lt_1(self):
        self.assertTrue(self.jutta_jung < 60)

    def test_lt_2(self):
        self.assertFalse(self.jutta_jung < 11)

    def test_lt_error(self):
        with self.assertRaises(TypeError):
            r = self.jutta_jung < ""

    def test_gt_0(self):
        self.assertTrue(self.anton_alt > self.jutta_jung)

    def test_gt_1(self):
        self.assertTrue(30 > self.jutta_jung)

    def test_ge_0(self):
        self.assertTrue(self.anton_alt >= self.jutta_jung)

    def test_ge_1(self):
        self.assertTrue(50 >= self.jutta_jung)

    def test_ge_error(self):
        with self.assertRaises(TypeError):
            r = self.jutta_jung <= ""

    def test_le_0(self):
        self.assertTrue(self.jutta_jung <= self.anton_alt)

    def test_le_1(self):
        self.assertTrue(self.jutta_jung <= 50)

    def test_contains_0(self):
        self.assertTrue("Jutta" in self.jutta_jung)

    def test_contains_1(self):
        self.assertTrue("Jut" in self.jutta_jung)

    def test_contains_2(self):
        self.assertFalse("Juttata" in self.jutta_jung)

    def test_contains_3(self):
        self.assertTrue("" in self.jutta_jung)

    def test_contains_error(self):
        with self.assertRaises(TypeError):
            self.assertTrue(self.jut_jung in self.jutta_jung)

```

<details><summary>🍀Tipps</summary>Es werden 3 Methoden benötigt.</details>


<details>
<summary>Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7KgaCe9i_3c?si=bdTmFu49R96ASvOB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        if isinstance(other, int | float):
            return self.age < other
        raise TypeError(f"Comperator operation only allowed for Persons and float and int")

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        if isinstance(other, int | float):
            return self.age <= other
        raise TypeError(f"Comperator operation only allowed for Persons and float and int")

    def __contains__(self, item):
        if not isinstance(item, str):
            raise TypeError(f"Item ist darf nicht vom Type {type(item)}, sondern muss vom Typ str sein.")
        return item in self.name
</code></pre></details>