# Getter, Setter und @property in Python
[80min]

In Python gibt es verschiedene Ansätze, um den Zugriff auf Attribute zu steuern. Der Unterstrich `_` vor einem Attribut kennzeichnet es als "privat" und signalisiert, dass es nicht direkt von außerhalb der Klasse geändert werden sollte. Hier betrachten wir die Verwendung von nativen Getter- und Setter-Methoden sowie die Verwendung von `@property`.

## Sichtbarkeit und Unterstrich `_`:

In Python gibt es keine strikte Privatsphäre wie in einigen anderen Programmiersprachen, aber ein vorangestellter Unterstrich `_` signalisiert, dass ein Attribut als privat betrachtet wird. Das bedeutet, dass es von außerhalb der Klasse nicht direkt zugegriffen oder geändert werden sollte. Es ist eher eine Konvention als eine Durchsetzung.

```python
class Buch:
    def __init__(self, titel, autor):
        self._titel = titel  # Privates Attribut mit Unterstrich
        self._autor = autor  # Privates Attribut mit Unterstrich

    def info_anzeigen(self):
        print(f"Titel: {self._titel}, Autor: {self._autor}")
```

## Native Getter und Setter:

Eine Möglichkeit, den Zugriff auf Attribute zu steuern, besteht darin, Getter- und Setter-Methoden zu verwenden.

```python
class Buch:
    def __init__(self, titel, autor):
        self._titel = titel  # Privates Attribut mit Unterstrich
        self._autor = autor  # Privates Attribut mit Unterstrich

    def get_titel(self):
        return self._titel

    def set_titel(self, neuer_titel):
        self._titel = neuer_titel

    def get_autor(self):
        return self._autor

    def set_autor(self, neuer_autor):
        self._autor = neuer_autor

    def info_anzeigen(self):
        print(f"Titel: {self._titel}, Autor: {self._autor}")
```

Hier werden Getter- und Setter-Methoden verwendet, um auf die privaten Attribute `titel` und `autor` zuzugreifen.

## @property für Getter und Setter:

Mit `@property` kann man Getter- und Setter-Funktionalität auf eine elegante Weise implementieren. Der Dekorator `@property` wird vor die Methode gesetzt, die als Getter fungiert, und `@<property_name>.setter` wird vor die Methode gesetzt, die als Setter fungiert.

```python
class Buch:
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
```

# Aufgaben:
[240min]

{{ task(file="tasks/python_grundlagen/08_getter_setter/01_buchverwaltung_mit_getter_setter_und_property.yaml") }}
{{ task(file="tasks/python_grundlagen/08_getter_setter/02_kreisberechnungen_mit_property.yaml") }}
{{ task(file="tasks/python_grundlagen/08_getter_setter/03_temperaturumrechner_mit_eigenschaften.yaml") }}
{{ task(file="tasks/python_grundlagen/08_getter_setter/04_benutzerkonto_mit_guthaben_und_transaktionen.yaml") }}
{{ task(file="tasks/python_grundlagen/08_getter_setter/05_autoverwaltung_mit_kilometerstand.yaml") }}
{{ task(file="tasks/python_grundlagen/08_getter_setter/06_warenkorb_mit_produkten_und_preisen.yaml") }}
{{ task(file="tasks/python_grundlagen/08_getter_setter/07_schulerverwaltung_mit_noten.yaml") }}
