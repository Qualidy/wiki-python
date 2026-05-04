# Class- & Static Methods

In Python gibt es zwei besondere Arten von Methoden, die direkt einer Klasse zugeordnet sind:
**statische Methoden** und **Klassenmethoden**. Diese Methoden haben spezielle Verwendungszwecke 
und werden mit den Dekoratoren `@staticmethod` und `@classmethod` definiert.

## Statische Methoden

[//]: # (<details>)

[//]: # (<summary>)

[//]: # (🎦 Video)

[//]: # (</summary>)

[//]: # (<iframe width="560" height="315" src="https://www.youtube.com/embed/BQBcMf1cFB4?si=1BtB8qMroDTATEdE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>)

[//]: # (</details>)

Eine **statische Methode** ist eine Methode, die zu einer Klasse gehört, 
aber nicht auf eine Instanz zugreift. Sie wird mit dem Dekorator `@staticmethod` definiert 
und hat keinen Zugriff auf Instanzattribute. Statische Methoden sind in erster Linie nützlich,
wenn eine Methode nur auf Klassenebene operieren muss und keine Instanzinformationen benötigt.

Besonders gerne nutzt man statische Methoden für UtilityKlassen, wie zum Beispiel die folgende, die 
Fahrenheit in Celsius umrechnet und umgekehrt:

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20TemperatureConverter%3A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20celsius_to_fahrenheit%28celsius%29%3A%0A%20%20%20%20%20%20%20%20return%20celsius%20*%209/5%20%2B%2032%0A%0A%20%20%20%20%40staticmethod%0A%20%20%20%20def%20fahrenheit_to_celsius%28fahrenheit%29%3A%0A%20%20%20%20%20%20%20%20return%20%28fahrenheit%20-%2032%29%20*%205/9%0A%0A%23%20Die%20statischen%20Methoden%20k%C3%B6nnen%20direkt%20von%20der%20Klasse%20aufgerufen%20werden%0Acelsius_temp%20%3D%2025%0Afahrenheit_equivalent%20%3D%20TemperatureConverter.celsius_to_fahrenheit%28celsius_temp%29%0Aprint%28f%22%7Bcelsius_temp%7D%20Grad%20Celsius%20entsprechen%20%7Bfahrenheit_equivalent%3A.2f%7D%20Grad%20Fahrenheit.%22%29%0A%0Afahrenheit_temp%20%3D%2077%0Acelsius_equivalent%20%3D%20TemperatureConverter.fahrenheit_to_celsius%28fahrenheit_temp%29%0Aprint%28f%22%7Bfahrenheit_temp%7D%20Grad%20Fahrenheit%20entsprechen%20%7Bcelsius_equivalent%3A.2f%7D%20Grad%20Celsius.%22%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Die statischen Methoden können direkt von der Klasse aufgerufen werden
celsius_temp = 25
fahrenheit_equivalent = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} Grad Celsius entsprechen {fahrenheit_equivalent:.2f} Grad Fahrenheit.")

fahrenheit_temp = 77
celsius_equivalent = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} Grad Fahrenheit entsprechen {celsius_equivalent:.2f} Grad Celsius.")
```


### Aufgabe: jaja, das ist nützlich ohne Ende🌶🌶
Schreibe eine Klasse `StringUtil`, die diverse statische Methoden implementiert:

* `count_words(string)` zählt die Anzahl der Wörter in einem String.
* `count_vowels(string)` zählt die Vokale in einem String (dies kann sehr gut mit der `sum` Methode und List-Comprehension gelöst werden).
* `is_palindrom(string)` testet, ob ein Wort ein Palindrom ist (z.B. ist `Otto` ein Palindrom, da es vorwärts und rückwärts gelesen dasselbe Wort ergibt, wenn man Groß- und Kleinschreibung ignoriert).
* `count_substring(substring, string)` zählt, wie oft `substring` in `string` auftaucht (z.B. taucht `ana` zwei mal in `Banana` auf).

Schreibe die Methoden und versehe zusätzlich jede mit Docstring und jeweils mindesten 3 Doctests,
die verschiedene Anwendungen darstellen.

<details><summary>🍀Tipps</summary>
<ul>
<li><code>count_words(string)</code></li>: Wie trennt man einen String und wie bestimmt man die Länge einer Liste?
<li><code>count_vowels(string)</code></li>: Was macht <code>in</code> bei zwei Strings?
<li><code>is_palindrom(string)</code></li>: Wie kann man mit Slicing String umdrehen?
<li><code>count_substring(substring, string)</code></li>: Die Methode <code>find</code> hat mehr als einen Parameter...
</ul>
</details>

<details><summary>Lösung</summary>
a-c)
<iframe width="560" height="315" src="https://www.youtube.com/embed/i_x4xr_7cbw?si=YqHcHci5jyWU8WMV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe><br>
d)
<iframe width="560" height="315" src="https://www.youtube.com/embed/npcB0wsGRBE?si=IHi7TySEo4TBtsMm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<pre><code>class StringUtil:
    @staticmethod
    def count_words(string):
        """
        Zählt die Anzahl der Wörter in einem String.

        >>> StringUtil.count_words("Hello world")
        2
        >>> StringUtil.count_words("Python is awesome")
        3
        >>> StringUtil.count_words("  Spaces \t between words ")
        3
        """
        return len(string.split())

    @staticmethod
    def count_vowels(string):
        """
        Zählt die Vokale in einem String.

        >>> StringUtil.count_vowels("Hallo")
        2
        >>> StringUtil.count_vowels("ZDF")
        0
        >>> StringUtil.count_vowels("Eulenspiegel")
        6
        """
        return sum(1 for char in string.lower() if char in 'aeiou')

    @staticmethod
    def is_palindrome(string):
        """
        Testet, ob ein Wort ein Palindrom ist.

        >>> StringUtil.is_palindrome("Otto")
        True
        >>> StringUtil.is_palindrome("banana")
        False
        >>> StringUtil.is_palindrome("A man, a plan, a canal, Panama!")
        True
        """
        clean_string = ''.join(char.lower() for char in string if char.isalnum())
        return clean_string == clean_string[::-1]

    @staticmethod
    def count_substring(substring, string):
        """
        Zählt, wie oft `substring` in `string` auftaucht.

        >>> StringUtil.count_substring("ana", "Banana")
        2
        >>> StringUtil.count_substring("test", "This is a test. Another test. But not this Test")
        2
        >>> StringUtil.count_substring("abc", "defghi")
        0
        """
        count = 0
        start_index = 0
        while True:
            start_index = string.find(substring, start_index)
            if start_index == -1:
                break
            count += 1
            start_index += 1
        return count


# Doctests ausführen
import doctest
doctest.testmod()
</code></pre></details>

## Klassenmethoden

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fA8xpIm6sjM?si=txTrtUUPEPdCpG-K" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Eine **Klassenmethode** ist eine Methode, die auf die Klasse selbst zugreift und nicht auf Instanzattribute.
Sie wird mit dem Dekorator `@classmethod` definiert und erhält die Klasse selbst als ersten Parameter (`cls`).

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20Car%3A%0A%20%20%20%20total_cars%20%3D%200%0A%0A%20%20%20%20def%20__init__%28self,%20brand%29%3A%0A%20%20%20%20%20%20%20%20self.brand%20%3D%20brand%0A%20%20%20%20%20%20%20%20Car.total_cars%20%2B%3D%201%0A%0A%20%20%20%20%40classmethod%0A%20%20%20%20def%20get_total_cars%28cls%29%3A%0A%20%20%20%20%20%20%20%20return%20cls.total_cars%0A%0Atotal%20%3D%20Car.get_total_cars%28%29%0Aprint%28total%29%0A%0Acar1%20%3D%20Car%28%22Volkswagen%22%29%0Acar2%20%3D%20Car%28%22Toyota%22%29%0A%0Atotal_now%20%3D%20Car.get_total_cars%28%29%0Aprint%28total_now%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

total = Car.get_total_cars()
print(total)

car1 = Car("Volkswagen")
car2 = Car("Toyota")

total_now = Car.get_total_cars()
print(total_now)
```


Klassenmethoden werden oft für alternative Konstruktoren oder zur Manipulation der Klasse selbst verwendet.

[Link zum Online Compiler💻](https://pythontutor.com/render.html#code=class%20Date%3A%0A%20%20%20%20def%20__init__%28self,%20year,%20month,%20day%29%3A%0A%20%20%20%20%20%20%20%20self.year%20%3D%20year%0A%20%20%20%20%20%20%20%20self.month%20%3D%20month%0A%20%20%20%20%20%20%20%20self.day%20%3D%20day%0A%0A%20%20%20%20%40classmethod%0A%20%20%20%20def%20from_string%28cls,%20string%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20Erstellt%20ein%20String%20der%20Form%20'YYYY-MM-DD'%20ein%20Date.%0A%0A%20%20%20%20%20%20%20%20%3E%3E%3E%20print%28Date.from_string%28%221990-07-10%22%29%29%0A%20%20%20%20%20%20%20%2010.07.1990%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20year,%20month,%20day%20%3D%20string.split%28%22-%22%29%0A%20%20%20%20%20%20%20%20return%20cls%28year,%20month,%20day%29%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.day%7D.%7Bself.month%7D.%7Bself.year%7D%22%0A%20%20%20%20%0Aprint%28Date.from_string%28%221990-07-10%22%29%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, string):
        """
        Erstellt ein String der Form 'YYYY-MM-DD' ein Date.

        >>> print(Date.from_string("1990-07-10"))
        10.07.1990
        """
        year, month, day = string.split("-")
        return cls(year, month, day)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
print(Date.from_string("1990-07-10"))
```


```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, string):
        """
        Erstellt ein String der Form 'YYYY-MM-DD' ein Date.
        
        >>> print(Date.from_string("1990-07-10"))
        10.07.1990
        """
        year, month, day = string.split("-")
        return cls(year, month, day)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
```

### Aufgabe: verschiedene Ursprünge🌶🌶

Fülle die folgenden Methodenrümpfe aus und erstelle für jede Methode mindestens einen Unittest.

```python
class Person:


    def __init__(self, name, age):
        ...

    @classmethod
    def get_count(cls):
        """
        Gibt zurück, wie viele Personen bisher erstellt wurden.
        """
        ...

    @classmethod
    def from_dict(cls, person_dict):
        """
        Erstellt ein Person-Objekt aus einem Dictionary.

        :param person_dict: Ein Dictionary mit den Schlüsseln 'name' und 'age'.
        :return: Ein Person-Objekt.
        """
        ...

    @classmethod
    def from_person(cls, parent):
        """
        Erstellt eine Junior-Person basierend auf einer bestehenden Person.

        :param parent: Person, deren Namen als Grundlage dient.
        :return: Ein Person-Objekt mit Namenszusatz ' Jr.' und Alter 0.
        """
        ...
```

<details><summary>🍀 Tipps</summary>
<code>get_count</code> Wie kann man ein Attribut speichern, dass für alle Instanzen gleich ist?
<br>
Der folgende Code soll ausführbar sein:
<pre><code>>>> p = Person.from_dict({'name': 'Alice', 'age': 30})
>>> p.name, p.age
('Alice', 30)
>>> p = Person.from_person(Person("Walter", 50))
>>> p.name, p.age
('Walter Jr.', 0)
>>> Person.get_count()
3</code></pre>
</details>

<details><summary>Lösung</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/R-kMRMouH0g?si=0fCG5tnFnIw5evHG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Person:
    person_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.person_count += 1

    @classmethod
    def get_count(cls):
        """
        Gibt zurück, wie viele Personen bisher erstellt wurden.
        """
        return cls.person_count

    @classmethod
    def from_dict(cls, person_dict):
        """
        Erstellt ein Person-Objekt aus einem Dictionary.

        :param person_dict: Ein Dictionary mit den Schlüsseln 'name' und 'age'.
        :return: Ein Person-Objekt.
        """
        return cls(person_dict['name'], person_dict['age'])

    @classmethod
    def from_person(cls, parent):
        """
        Erstellt eine Junior-Person basierend auf einer bestehenden Person.

        :param parent: Person, deren Namen als Grundlage dient.
        :return: Ein Person-Objekt mit Namenszusatz 'Jr.' und Alter 0.
        """
        return cls(parent.name + " Jr.", 0)


import unittest

class TestPerson(unittest.TestCase):
    def setUp(self):
        # Vor jedem Test wird der Zähler zurückgesetzt
        Person.person_count = 0

    def test_init(self):
        p = Person("Alice", 30)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)

    def test_from_dict(self):
        p = Person.from_dict({'name': 'Bob', 'age': 40})
        self.assertEqual(p.name, "Bob")
        self.assertEqual(p.age, 40)

    def test_from_person(self):
        parent = Person("Walter", 50)
        p = Person.from_person(parent)
        self.assertEqual(p.name, "Walter Jr.")
        self.assertEqual(p.age, 0)

    def test_get_count(self):
        Person.from_person(Person("Walter", 50))
        self.assertEqual(Person.get_count(), 2)
</code></pre></details>