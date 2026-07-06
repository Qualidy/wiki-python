# `super()` in Klassen

## Theorie

Die Grundlagen sind bereits gut abgedeckt:

- [Klassen, `super()` und Dunder Methods](../wiederholung/klassen_oop_wiederholung.md)

Wichtig für die Wiederholung:

- `super().__init__(...)` ruft den Konstruktor der Superclass auf.
- In überschriebenen Methoden ruft `super().methode()` die Version der Superclass auf.
- `self.methode()` in einer überschriebenen Methode ruft wieder die Methode der Unterklasse auf und kann Rekursion erzeugen.
- Klassenattribute sollten nicht nebenbei in Unterklassen verändert werden, wenn eine Klassenmethode in der Superclass sinnvoller wäre.

## Aufgaben

### Aufgabe 1: Lückencode Ausleihe

```python
class LibraryItem:
    total_items = 0

    def __init__(self, title):
        self.title = title
        self.borrowed = False
        LibraryItem.total_items += 1

    def borrow(self):
        if self.borrowed:
            print("Schon ausgeliehen")
        else:
            self.borrowed = True
            print(f"{self.title} wurde ausgeliehen")


class Book(LibraryItem):
    def __init__(self, title, author):
        # Ergänzen
        self.author = author

    def borrow(self):
        print(f"Buch von {self.author} wird verarbeitet")
        # Ergänzen
```

??? success "Lösung"
    In `__init__`: `super().__init__(title)`. In `borrow`: `super().borrow()`.

### Aufgabe 2: Rückgabe ergänzen

Erweitere `LibraryItem` um `return_item()`. Erweitere danach `Book.return_item()` so, dass zuerst eine Buch-Meldung kommt und danach die allgemeine Rückgabe genutzt wird.

??? success "Lösungsidee"
    Die gemeinsame Zustandslogik gehört in `LibraryItem.return_item()`. In `Book.return_item()` wird danach `super().return_item()` aufgerufen.

### Aufgabe 3: Rekursion erkennen

Warum ist dieser Code problematisch?

```python
class Book(LibraryItem):
    def borrow(self):
        print("Buch wird verarbeitet")
        self.borrow()
```

??? success "Lösung"
    `self.borrow()` ruft wieder `Book.borrow()` auf. Dadurch entsteht endlose Rekursion. Korrekt wäre `super().borrow()`.

### Aufgabe 4: Konstruktor-Aufruf ergänzen

```python
class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def __init__(self, username, level):
        # Ergänzen
        self.level = level
```

??? success "Lösung"
    `super().__init__(username)`

### Aufgabe 5: Reihenfolge erklären

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
    Erst `B`, dann `A`.

### Aufgabe 6: Klassenattribut kapseln

Warum ist eine Klassenmethode oft besser als direkt `Parent.counter -= 1` in einer Unterklasse?

??? success "Lösung"
    Die Regel zum Ändern des Klassenattributs bleibt an einer Stelle. Die Superclass kontrolliert ihre eigene Zustandslogik, statt dass Unterklassen sie direkt verändern.
