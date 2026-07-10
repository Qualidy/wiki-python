# OOP: Name Mangling, Introspection und MRO-Fallen

Diese Einheit ergänzt `super()` um typische PCAP-Fragen zu privaten Namen, Klassenstruktur und Introspection.

## Name Mangling

Namen mit zwei führenden Unterstrichen werden innerhalb einer Klasse umgeschrieben.

```python
class Spam:
    def __eggs(self):
        return "eggs"

    eggs = __eggs


s = Spam()
```

Gültige Zugriffe:

```python
s.eggs()
s._Spam__eggs()
```

Ungültig:

```python
s.__eggs()
```

Python speichert `__eggs` intern als `_Spam__eggs`.

## `__name__`, `__module__`, `__bases__`

```python
class Spam:
    pass
```

```python
print(Spam.__name__)     # Spam
print(Spam.__module__)   # meist __main__
print(Spam.__bases__)    # (<class 'object'>,)
```

Instanzen haben kein eigenes `__name__`:

```python
s = Spam()
print(s.__name__)  # AttributeError
```

## `hasattr`

`hasattr(obj, "name")` prüft, ob ein Attribut erreichbar ist.

```python
class Spam:
    ham = 36


spam = Spam()
print(hasattr(spam, "ham"))  # True
print(hasattr(Spam, "ham"))  # True
```

## `isinstance` und `issubclass`

```python
class X:
    pass


class Y:
    pass


class Z(X, Y):
    pass
```

```python
z = Z()
print(isinstance(z, X))          # True
print(isinstance(z, (list, X)))  # True
print(issubclass(Z, X))          # True
```

## `self.method()` vs. gespeicherte Methodenreferenz

Wenn eine Superclass in `__init__` `self.update()` aufruft, kann bei einer Unterklasse eine überschriebene Methode aufgerufen werden.

```python
class Ham:
    def __init__(self):
        self.update()

    def update(self):
        print("Ham.update")


class Spam(Ham):
    def update(self, param):
        print("Spam.update")


Spam()
```

Das endet mit `TypeError`, weil `Spam.update(self, param)` ohne `param` aufgerufen wird.

## Aufgaben

### Aufgabe 1: Private Methode

Welche Aufrufe funktionieren?

```python
class Spam:
    def __eggs(self):
        return 100

    eggs = __eggs


s = Spam()
```

```python
s.eggs()
s.__eggs()
s._Spam__eggs()
```

??? success "Lösung"
    `s.eggs()` und `s._Spam__eggs()` funktionieren. `s.__eggs()` nicht.

### Aufgabe 2: `__name__`

Was funktioniert?

```python
class Spam:
    pass


s = Spam()
```

```python
Spam.__name__
s.__name__
s.__class__.__name__
```

??? success "Lösung"
    `Spam.__name__` und `s.__class__.__name__` funktionieren. `s.__name__` erzeugt `AttributeError`.

### Aufgabe 3: `hasattr`

Was wird ausgegeben?

```python
class Spam:
    ham = 36


spam = Spam()
print(hasattr(spam, "ham"))
print(hasattr(Spam, "ham"))
print(hasattr("Spam", "ham"))
```

??? success "Lösung"
    ```text
    True
    True
    False
    ```

### Aufgabe 4: `isinstance`

Welche Ausdrücke sind `True`?

```python
class X:
    pass


class Y:
    pass


class Z(X, Y):
    pass


z = Z()
```

```python
isinstance(z, X)
isinstance(z, Y)
isinstance(z, (list, X, Y))
isinstance((list, X, Y), z)
```

??? success "Lösung"
    Die ersten drei sind `True`. Der letzte Ausdruck ist falsch verwendet.

### Aufgabe 5: Überschriebene Methode

Warum gibt es hier einen Fehler?

```python
class Ham:
    def __init__(self):
        self.update()

    def update(self):
        print("Ham.update")


class Spam(Ham):
    def update(self, param):
        print("Spam.update")


Spam()
```

??? success "Lösung"
    `Ham.__init__` ruft `self.update()` auf. Bei einem `Spam`-Objekt ist das `Spam.update`, aber diese Methode braucht `param`.
