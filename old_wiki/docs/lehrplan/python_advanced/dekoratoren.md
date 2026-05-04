# Dekoratoren

Wir haben im Laufe der Vorlesungen verschiedene **Dekoratoren** kennengelernt.
Dekoratoren sind die Codezeilen, über Funktionen und Methoden, die mit einem `@` beginnen.

### Aufgabe: Was war so alles dekoriert?🌶

Welche Dekoratoren wurden bisher von uns verwendet und welchen Zweck haben sie erfüllt?

<details>
<summary>Lösung</summary>

Bei Properties wurden Dekoratoren verwendet, um einfach eine Property zu definieren:

<pre><code>class Buch:
    def __init__(self, titel, autor):
        self._titel = titel  # Privates Attribut mit Unterstrich
        self._autor = autor  # Privates Attribut mit Unterstrich

    @property
    def titel(self):
        return self._titel

    @titel.setter
    def titel(self, neuer_titel):
        self._titel = neuer_titel

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, neuer_autor):
        self._autor = neuer_autor

    def info_anzeigen(self):
        print(f"Titel: {self._titel}, Autor: {self._autor}")
</code></pre>

Mit Dekoratoren konnten Klassenmethoden definiert werden:
<pre><code>class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

total = Car.get_total_cars()
print(total)</code></pre>

Mit Dekoratoren konnten statische Methoden definiert werden:
<pre><code>class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Die statischen Methoden können direkt von der Klasse aufgerufen werden
celsius_temp = 25
fahrenheit_equivalent = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} Grad Celsius entsprechen {fahrenheit_equivalent:.2f} Grad Fahrenheit.")</code></pre>

Bei Flask wurden Dekoratoren verwendet, um Routen zu definieren:
<pre><code>from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/about")
def about():
    return "About Page"

if __name__ == "__main__":
    app.run()
</code></pre>
</details>

## Wie funktionieren Dekoratoren

Die obigen Beispiele sind alle extrem unterschiedlich und weisen wenig Gemeinsamkeiten auf.
Allen gemein ist jedoch, dass der Dekorator die Funktionsweise, der folgenden Funktion **ändert**!

Diese Erweiterung/Änderung der Funktionsweise einer Funktion ist genau das, was ein Dekorator bezwecken soll.

Doch dies können wir auch ohne Verwendung von Dekoratoren erreichen, wie das folgende Beispiel zeigt,
indem die Funktion so geändert wird, dass Sie bei jeder Funktionsausführung in der Konsole dokumentiert, dass
sie ausgeführt wurde:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=def%20add%28a,%20b%29%3A%0A%20%20%20%20return%20a%20%2B%20b%0A%0Aprint%28add%281,2%29%29%0A%0Adef%20log_usage%28func%29%3A%0A%20%20%20%20def%20new_func%28*args,%20**kwargs%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bfunc.__name__%7D%20wurde%20aufgerufen!%22%29%0A%20%20%20%20%20%20%20%20return%20func%28*args,%20**kwargs%29%0A%20%20%20%20%0A%20%20%20%20return%20new_func%0A%0Aadd%20%3D%20log_usage%28add%29%0A%0Aprint%28add%281,2%29%29%20&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
def add(a, b):
    return a + b

print(add(1,2)) # 3

def log_usage(func):
    def new_func(*args, **kwargs):
        print(f"{func.__name__} wurde aufgerufen!")
        return func(*args, **kwargs)
    
    return new_func

add = log_usage(add)

print(add(1,2)) # Gibt auf der Console "add wurde aufgerufen!" aus und "3" nacheinander aus.
```

**Gehen wir das Beispiel genau durch:**

* Es wird eine einfache Funktion `add` definiert, die zwei Zahlen addiert.
* Beim Ausführen der Methode genschieht genau das: Zwei zahlen werden addiert.
* Es wird eine Funktion `log_usage` definiert, die eine Funktion `func` als Parameter erwartet.
* In der Funktion `log_usage` wird eine neue Funktion `new_func` definiert.
* In der Funktion `new_func` wird zuerst eine Mitteilung auf der Konsole gegegeben. Dann ursprüngliche Funktion `func` ausgeführt. Das Ergebnis von `func` wird dann auch von `new_func` weitergegeben.
* Nun wird, wieder in der Funktion `log_usage` die neu definierte Funktion `new_func` zurückgegeben, aber ohne sie auszuführen (keine Klammern!).
* Wir sehen nun, dass `add` überschrieben wird und zwar mit dem Ergebnis von `log_usage(add)`.
* Nun wird das neue `add` ausgeführt. Dies führt aber in Wirklichkeit dazu, dass die innere Funktion `new_func` ausgeführt wird.
* Wir sehen, dass auf der Konsole "add wurde aufgerufen!" ausgegeben wird, gefolgt von der Addition, die das ursprüngliche `add` berechnet hat.

**Was ist also passiert?**

`log_usage` nimmt eine Funktion `func` entgegen und gibt eine andere Funktion `new_func` zurück, die `func` zwar verwendet,
aber noch weitere eigene Funktionalität mitbringt.

Weiterhin überschreiben wir in diesem Beispiel, den ursprünglichen Funktionsnamen durch die neue, erweiterte Funktion,
sodass wir zukünftig nur noch diese aufrufen können.

**Und was hat das mit Dekoratoren zu tun?**

Alles! Denn wir haben hier tatsächlich mit der Funktion `log_usage` bereits einen Dekorator definiert.

Denn ein Dekorator ist bloß eine Kurzschreibweise für folgenden Code:

```python
def my_func(args):
    ...

my_func = log_usage(my_func)
```

kann auch kurz geschrieben werden als:

```python
@log_usage
def my_func(args):
    ...
```

Dementsprechen können wir auch unser Beispiel hier in der Länge reduzieren.
```python
def log_usage(func):
    def new_func(*args, **kwargs):
        print(f"{func.__name__} wurde aufgerufen!")
        return func(*args, **kwargs)
    
    return new_func

@log_usage
def add(a, b):
    return a + b

print(add(1,2)) # Gibt auf der Console "add wurde aufgerufen!" aus und "3" nacheinander aus.
```

Die Dekorator-Syntax ist also nur syntaktischer Zucker.

### Aufgabe: Verbessertes Logging🌶🌶
Erweitere `log_usage`, sodass nicht nur der Methodenname gelogt wird, sondern auch die Parameter und der Rückgabewert.

<details>
<summary>Lösung</summary>

<pre><code>def log_usage(func):
    def new_func(*args, **kwargs):
        print(f"{func.__name__} wurde aufgerufen aufgerufen mit den args: {args} und kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} wurde aufgerufen hat zurückgegeben: {result}!")
        return result

    return new_func</code></pre>
</details>

### Aufgabe: Türsteher🌶🌶

Schreibe einen Dekorator `int_args_only`, der von allen positionalen Arugementen prüft, ob es sich um `int` handelt und andernfalls
einen `TypeError` wirft.

<details>
<summary>Lösung</summary>

<pre><code>def int_args_only(func):
    def new_func(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            return func(*args, **kwargs)
        else:
            raise TypeError("Mindestens ein positionales Argument ist kein int!")

    return new_func


@int_args_only
def add(a, b):
    return a + b


print(add(1, 2)) # 3

print(add(1.0, 2)) # TypeError
</code></pre>
</details>


### Aufgabe: Immer das gleiche?🌶🌶🌶

Beschreibe, was der folgende Dekorator tut:

```python
def always_42(func):
    return (lambda *args, **kwargs : 42)
```

<details><summary>🍀Tipp</summary>
Der Dekorator sorgt dafür, dass immer 42 als Rückgabe der annotierten Funktion zurückgegeben wird.
</details>


### Aufgabe: Wer bist du denn nun?🌶🌶🌶

Untersuche den folgenden Code. Was fällt dir in der Ausgabe auf?
Recherchiere, wie man für die korrekte Ausgabe sorgen kann!

```python
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x * x

print(f.__name__)  # should print 'f'
print(f.__doc__)   # should print 'does some math'
```

<details><summary>🍀Tipp</summary>
<a href="https://stackoverflow.com/a/309000/21375352">stackoverflow Diskussion</a></details>

Schau dir auf jeden Fall, im Nachhinein die Lösung an:
<details>
<summary>Lösung</summary>
Da <code>f</code> mit <code>with_logging</code> ersetzt wird,
erhalten ändert sich der intern gespeicherte Name und die Dokumentation der Funktion.
Daher sollte immer aus <code>functools</code> das <code>wraps</code>
importiert werden und wie hier zu sehen genutzt werden. <b>IMMER💀</b>

<pre><code>from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'
</code></pre>
</details>


### Aufgabe: Schneller!🌶🌶🌶

Erstelle einen Dekorator, der misst, wie lange eine Funktionsausführung dauert.

<details>
<summary>Lösung</summary>
<pre><code>from functools import wraps
from time import sleep, time


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = orig_func(*args, **kwargs)
        t2 = time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper


@my_timer
def display_info(name, age):
    sleep(1.5)  # Stoppe Programmausführung für 1,5 Sekunden.
    print(f'Display function ran with arguments ({name}, {age})')


display_info('John', 30)

</code></pre>
</details>




### Aufgabe: Verwandlung 🌶
Schreibe ein Programm mit einem Dekorator `convert_to_string`, 
der den Ausgabewert einer Funktion in `str` umwandelt.

<details>
<summary>Lösung</summary>
<pre><code>from functools import wraps

def convert_to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wrapper

@convert_to_string
def add(a, b):
    return a + b

result_add = add(5, 3)

print(result_add)
print(type(result_add))
</code></pre>
</details>

### Aufgabe: Cache 🌶🌶🌶
Schreibe einen Dekorator, der ein Cache hat, in dem alte Werte gespeichert werden (z.B. für Binomialkoeffizient)

```python
def binomialkoeffizient(n, k):
    if k <= 0 or k >= n:
        return 1
    return binomialkoeffizient(n - 1, k - 1) + binomialkoeffizient(n - 1, k)


n_small = 5
k_small = 2
print(f"Binomialkoeffizient C({n_small}, {k_small}) = {binomialkoeffizient(n_small, k_small)}")

# Lässt sich ohne Caching nicht mehr berechnen:
n_big = 50000
k_big = 22220
print(f"Binomialkoeffizient C({n_big}, {k_big}) = {binomialkoeffizient(n_big, k_big)}")
```

<details>
<summary>Lösung</summary>
<pre><code>from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(n, k):
        if (n, k) not in cache:
            cache[(n, k)] = func(n, k)
        return cache[(n, k)]

    return wrapper

@memoize
def binomialkoeffizient(n, k):
    if k <= 0 or k >= n:
        return 1
    return binomialkoeffizient(n - 1, k - 1) + binomialkoeffizient(n - 1, k)


n_small = 5
k_small = 2
print(f"Binomialkoeffizient C({n_small}, {k_small}) = {binomialkoeffizient(n_small, k_small)}")

# Lässt sich ohne Caching nicht mehr berechnen:
n_big = 500
k_big = 220
print(f"Binomialkoeffizient C({n_big}, {k_big}) = {binomialkoeffizient(n_big, k_big)}")
</code></pre>
</details>


## Dekorator mit Parametern

Ein Dekorator kann auch Parameter annehmen,
indem man eine zusätzliche Funktionsebene hinzufügt.
Diese äußere Funktion nimmt die Parameter des Dekorators entgegen
und gibt den eigentlichen Dekorator zurück.

```python
from functools import wraps

def limit_calls(max_calls):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.calls < max_calls:
                wrapper.calls += 1
                return func(*args, **kwargs)
            else:
                print(f"Function {func.__name__} has exceeded the maximum call limit of {max_calls}")
        wrapper.calls = 0
        return wrapper
    return decorator

@limit_calls(3)
def say_hello(name):
    print(f"Hello, {name}!")

# Testing the function
say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")
say_hello("Dave")  # This call should trigger the limit message
```

### Aufgabe: Verzögerung🌶🌶

Schreibe einen Dekorator delay, der eine Funktion um eine bestimmte Anzahl von Sekunden verzögert, bevor sie ausgeführt wird. Der Dekorator sollte einen Parameter seconds annehmen, der die Verzögerungszeit angibt.

<details>
<summary>Lösung</summary>
<pre><code>from functools import wraps
from time import sleep

def delay(seconds):
    def decorator_delay(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Warte {seconds} Sekunden...")
            sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator_delay

@delay(seconds=2)
def greet():
    print("Hallo!")

greet()
</code></pre>
</details>


### Aufgabe: Verwandlung 🌶🌶🌶

Erweitere den Dekorator `convert_to_string` zu `convert_to`, 
sodass er einen beliebigen Typ als Parameter annimmt, 
in den der Rückgabewert der Funktion konvertiert wird.

<details>
<summary>Lösung</summary>
<pre><code>from functools import wraps

def convert_to_type(target_type):
    def decorator_convert(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return target_type(result)
        return wrapper
    return decorator_convert

@convert_to_type(str)
def add(a, b):
    return a + b

result_add = add(5, 3)

print(result_add)        # '8'
print(type(result_add))  # <class 'str'>

@convert_to_type(float)
def multiply(a, b):
    return a * b

result_multiply = multiply(5, 3)

print(result_multiply)        # 15.0
print(type(result_multiply))  # <class 'float'>
</code></pre>
</details>
