# Halftime Quiz: Woche 8

Dieses Quiz wiederholt die wichtigsten Themen der letzten Tage. Löse die Aufgaben zuerst ohne Python auszuführen. Klappe die Lösung erst danach auf.

## Scope und Closure

### Aufgabe 1: LEGB

Was wird ausgegeben?

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        print(x)

    inner()

outer()
print(x)
```

??? success "Lösung"
    Ausgabe:

    ```python
    outer
    global
    ```

    `inner()` findet `x` zuerst im enclosing scope von `outer()`. Das globale `x` bleibt unverändert.

### Aufgabe 2: Codelücke `nonlocal`

Ergänze genau eine Zeile.

```python
def make_counter():
    count = 0

    def counter():
        # Lücke
        count += 1
        return count

    return counter

c = make_counter()
print(c())
print(c())
```

??? success "Lösung"
    ```python
    nonlocal count
    ```

    Ohne `nonlocal` behandelt Python `count` in `counter()` als lokale Variable.

### Aufgabe 3: Closure erkennen

Welche Aussage ist richtig?

```python
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
print(square(5))
```

A. `exp` ist nach `make_power()` nicht mehr nutzbar.  
B. `power()` merkt sich `exp` aus dem enclosing scope.  
C. `square` ist ein Integer.  
D. Der Code erzeugt immer `NameError`.

??? success "Lösung"
    B ist richtig. `power()` ist ein Closure und merkt sich `exp`.

## `bytearray`

### Aufgabe 4: Bytes vs. Zeichen

Was wird ausgegeben?

```python
data = bytearray(b"abc")
print(data[0])
data[0] = ord("A")
print(data)
print(data.decode())
```

??? success "Lösung"
    Ausgabe:

    ```python
    97
    bytearray(b'Abc')
    Abc
    ```

    Indexing liefert einen Integer. `ord("A")` ist `65`.

### Aufgabe 5: Codelücke `append`

Ergänze die Lücke so, dass `bytearray(b"abcd")` entsteht.

```python
data = bytearray(b"abc")
data.append(____)
print(data)
```

??? success "Lösung"
    ```python
    ord("d")
    ```

    Alternativ geht `100`. `append()` erwartet einen Integer zwischen `0` und `255`, kein `bytes`-Objekt.

### Aufgabe 6: Fehlerfrage

Welche Zeile erzeugt einen Fehler?

```python
a = bytearray([65, 66])
b = bytearray([255])
c = bytearray([256])
d = bytearray(b"AB")
```

??? success "Lösung"
    `c = bytearray([256])` erzeugt `ValueError`, weil ein Byte nur Werte von `0` bis `255` haben darf.

## `map()`, `filter()` und `lambda`

### Aufgabe 7: Iterator verbraucht

Was wird ausgegeben?

```python
values = map(lambda x: x * 2, [1, 2, 3])
print(list(values))
print(list(values))
```

??? success "Lösung"
    Ausgabe:

    ```python
    [2, 4, 6]
    []
    ```

    `map()` liefert einen Iterator. Nach dem ersten `list(values)` ist er verbraucht.

### Aufgabe 8: Codelücke `filter`

Ergänze die Lücke, sodass nur Wörter mit mehr als drei Zeichen übrig bleiben.

```python
words = ["sun", "python", "cat", "code"]
result = list(filter(lambda word: ____, words))
print(result)
```

Erwartet:

```python
["python", "code"]
```

??? success "Lösung"
    ```python
    len(word) > 3
    ```

### Aufgabe 9: Kombiniert auswerten

Was wird ausgegeben?

```python
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x + 10, filter(lambda x: x % 2 == 1, numbers))
print(list(result))
```

??? success "Lösung"
    Ausgabe:

    ```python
    [11, 13, 15]
    ```

    Erst bleiben ungerade Zahlen: `1, 3, 5`. Danach werden `10` addiert.

## `chr()` und `ord()`

### Aufgabe 10: Codepoints

Was wird ausgegeben?

```python
print(ord("A"))
print(chr(66))
print(chr(ord("A") + 3))
```

??? success "Lösung"
    Ausgabe:

    ```python
    65
    B
    D
    ```

### Aufgabe 11: Codelücke Großbuchstaben

Ergänze die Bedingung.

```python
def only_uppercase(text):
    result = ""
    for char in text:
        if ____:
            result += char
    return result

print(only_uppercase("PyTHon 3!"))
```

Erwartet:

```python
PTH
```

??? success "Lösung"
    ```python
    "A" <= char <= "Z"
    ```

    Alternativ mit Codepoints:

    ```python
    ord("A") <= ord(char) <= ord("Z")
    ```

### Aufgabe 12: Fehlerfrage `ord`

Warum erzeugt dieser Code einen Fehler?

```python
print(ord("AB"))
```

??? success "Lösung"
    `ord()` erwartet genau ein einzelnes Zeichen. `"AB"` enthält zwei Zeichen.

## Operatoren und Precedence

### Aufgabe 13: `and` vor `or`

Was wird ausgegeben?

```python
a = True
b = True
c = False

print(a or b and c)
print((a or b) and c)
```

??? success "Lösung"
    Ausgabe:

    ```python
    True
    False
    ```

    Ohne Klammern gilt `a or (b and c)`.

### Aufgabe 14: Codelücke Bedingung

Ergänze die Bedingung so, dass nur Werte zwischen `10` und `20` akzeptiert werden.

```python
def valid(value):
    return ____

print(valid(9))
print(valid(10))
print(valid(20))
print(valid(21))
```

Erwartet:

```python
False
True
True
False
```

??? success "Lösung"
    ```python
    10 <= value <= 20
    ```

    Möglich wäre auch:

    ```python
    value >= 10 and value <= 20
    ```

### Aufgabe 15: Short-Circuit

Was wird ausgegeben?

```python
def check(name, result):
    print(name)
    return result

print(check("A", False) and check("B", True))
print(check("C", True) or check("D", False))
```

??? success "Lösung"
    Ausgabe:

    ```python
    A
    False
    C
    True
    ```

    `and` bricht bei `False` links ab. `or` bricht bei `True` links ab.

## Mutable und Immutable

### Aufgabe 16: Liste als Referenz

Was wird ausgegeben?

```python
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)
```

??? success "Lösung"
    Ausgabe:

    ```python
    [1, 2, 3]
    [1, 2, 3]
    ```

    `a` und `b` zeigen auf dieselbe Liste.

### Aufgabe 17: Funktion mit immutable Typ

Was wird ausgegeben?

```python
def change(number):
    number += 1
    print("innen:", number)

value = 10
change(value)
print("außen:", value)
```

??? success "Lösung"
    Ausgabe:

    ```python
    innen: 11
    außen: 10
    ```

    `int` ist immutable. `number += 1` bindet nur den lokalen Namen `number` neu.

### Aufgabe 18: Codelücke Kopie

Ergänze die Lücke so, dass `original` unverändert bleibt.

```python
original = [1, 2, 3]
copy = ____
copy.append(4)

print(original)
print(copy)
```

Erwartet:

```python
[1, 2, 3]
[1, 2, 3, 4]
```

??? success "Lösung"
    Möglich sind:

    ```python
    original.copy()
    original[:]
    list(original)
    ```

## `super()`, Dunder und Vererbung

### Aufgabe 19: `super().__init__`

Ergänze die Lücke.

```python
class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def __init__(self, username, level):
        ____
        self.level = level


a = Admin("root", 5)
print(a.username)
print(a.level)
```

??? success "Lösung"
    ```python
    super().__init__(username)
    ```

### Aufgabe 20: Dunder `__str__`

Ergänze die Methode.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def ____(self):
        return f"{self.name}: {self.price}"


p = Product("Book", 12)
print(p)
```

??? success "Lösung"
    ```python
    __str__
    ```

    `print(p)` nutzt indirekt `str(p)`, also `p.__str__()`.

### Aufgabe 21: Vererbung und Methodenauflösung

Was wird ausgegeben?

```python
class A:
    def run(self):
        print("A")


class B(A):
    def run(self):
        print("B")
        super().run()


B().run()
```

??? success "Lösung"
    Ausgabe:

    ```python
    B
    A
    ```

    `B.run()` wird zuerst ausgeführt. Danach ruft `super().run()` die Methode aus `A` auf.

### Aufgabe 22: Dunder `__eq__`

Ergänze die Methode so, dass zwei Punkte mit gleichen Koordinaten als gleich gelten.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ____(self, other):
        return self.x == other.x and self.y == other.y


print(Point(1, 2) == Point(1, 2))
print(Point(1, 2) == Point(2, 1))
```

??? success "Lösung"
    ```python
    __eq__
    ```

    Der Operator `==` ruft bei eigenen Objekten `__eq__()` auf.

### Aufgabe 23: Rekursion durch falschen Methodenaufruf

Warum ist dieser Code problematisch?

```python
class Base:
    def save(self):
        print("Base save")


class Child(Base):
    def save(self):
        print("Child save")
        self.save()
```

??? success "Lösung"
    `self.save()` ruft wieder `Child.save()` auf. Dadurch entsteht endlose Rekursion. Gemeint wäre wahrscheinlich:

    ```python
    super().save()
    ```

### Aufgabe 24: Gemischte Wiederholung

Welche Aussagen sind richtig? Wähle alle passenden Aussagen.

A. `bytearray` ist mutable.  
B. `bytes` ist mutable.  
C. `ord("A")` ergibt `65`.  
D. `filter()` liefert sofort eine Liste.  
E. Eine Funktion kann eine innere Funktion zurückgeben.  
F. `and` hat höhere Precedence als `or`.

??? success "Lösung"
    Richtig sind A, C, E und F.

    - `bytes` ist immutable.
    - `filter()` liefert einen Iterator, keine Liste.

