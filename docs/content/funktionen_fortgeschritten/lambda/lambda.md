# Lambda-Funktionen

## Was sind Lambda-Funktionen?

Lambda-Funktionen sind **anonyme Funktionen** — Funktionen ohne Namen, die in einer einzigen Zeile definiert werden. Sie eignen sich für kurze, einfache Operationen, die nur an einer Stelle im Code benötigt werden.

```python
# Normale Funktion
def verdoppeln(x):
    return x * 2

# Gleiche Funktion als Lambda
verdoppeln = lambda x: x * 2
```

!!! info "Warum „Lambda"?"
    Der Name stammt aus dem **Lambda-Kalkül**, einem mathematischen Formalismus aus den 1930er-Jahren
    von Alonzo Church. In der Mathematik schreibt man λx.x² für eine anonyme Funktion, die x quadriert.

---

## Syntax

Die allgemeine Syntax einer Lambda-Funktion ist:

```python
lambda argumente: ausdruck
```

- **`lambda`** — Schlüsselwort (statt `def`)
- **`argumente`** — eine oder mehrere durch Komma getrennte Parameter
- **`ausdruck`** — ein einzelner Ausdruck, dessen Ergebnis automatisch zurückgegeben wird

### Beispiele

```python
# Ohne Parameter
gruss = lambda: "Hallo Welt!"
print(gruss())  # Hallo Welt!

# Ein Parameter
quadrat = lambda x: x ** 2
print(quadrat(4))  # 16

# Mehrere Parameter
addiere = lambda a, b: a + b
print(addiere(3, 5))  # 8

# Mit Standardwert
potenz = lambda basis, exp=2: basis ** exp
print(potenz(3))     # 9
print(potenz(3, 3))  # 27
```

### Vergleich mit `def`

| `def`-Funktion | Lambda-Funktion |
|---|---|
| Kann mehrere Anweisungen enthalten | Nur **ein** Ausdruck |
| Hat einen Namen | Anonym (kein eigener Name) |
| Kann Docstrings haben | Kein Docstring möglich |
| Besser für komplexe Logik | Besser für kurze Einzeiler |

---

## Lambda mit `sorted()`

Einer der häufigsten Anwendungsfälle für Lambda-Funktionen ist der **`key`-Parameter** von `sorted()`.
Der `key`-Parameter erwartet eine Funktion, die für jedes Element einen **Vergleichswert** liefert.

### Nach Stringlänge sortieren

```python
woerter = ["Python", "ist", "eine", "Programmiersprache"]

sortiert = sorted(woerter, key=lambda w: len(w))
print(sortiert)
# ['ist', 'eine', 'Python', 'Programmiersprache']
```

### Nach Dictionary-Wert sortieren

```python
personen = [
    {"name": "Anna", "alter": 25},
    {"name": "Ben", "alter": 19},
    {"name": "Clara", "alter": 32},
]

nach_alter = sorted(personen, key=lambda p: p["alter"])
print(nach_alter)
# [{'name': 'Ben', 'alter': 19}, {'name': 'Anna', 'alter': 25}, {'name': 'Clara', 'alter': 32}]
```

### Nach mehreren Kriterien sortieren

```python
schueler = [
    {"name": "Anna", "note": 2.0},
    {"name": "Ben", "note": 1.0},
    {"name": "Clara", "note": 2.0},
]

# Erst nach Note, dann alphabetisch nach Name
sortiert = sorted(schueler, key=lambda s: (s["note"], s["name"]))
print(sortiert)
# [{'name': 'Ben', 'note': 1.0}, {'name': 'Anna', 'note': 2.0}, {'name': 'Clara', 'note': 2.0}]
```

!!! tip "Tipp"
    Auch `list.sort()`, `min()`, und `max()` unterstützen den `key`-Parameter.

---

## Lambda mit `map()`

`map()` wendet eine Funktion auf **jedes Element** eines Iterables an und gibt einen Iterator zurück.

```python
map(funktion, iterable)
```

### Beispiele

```python
zahlen = [1, 2, 3, 4, 5]

# Quadratzahlen
quadrate = list(map(lambda x: x ** 2, zahlen))
print(quadrate)  # [1, 4, 9, 16, 25]

# Strings in Großbuchstaben
woerter = ["hallo", "welt"]
gross = list(map(lambda w: w.upper(), woerter))
print(gross)  # ['HALLO', 'WELT']

# Celsius in Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0]
```

!!! info "Hinweis"
    `map()` gibt einen **Iterator** zurück, kein Liste. Verwende `list()`, um das Ergebnis
    in eine Liste umzuwandeln.

---

## Lambda mit `filter()`

`filter()` filtert Elemente eines Iterables anhand einer Bedingung. Nur Elemente, für die die Funktion `True` zurückgibt, werden beibehalten.

```python
filter(funktion, iterable)
```

### Beispiele

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Gerade Zahlen
gerade = list(filter(lambda x: x % 2 == 0, zahlen))
print(gerade)  # [2, 4, 6, 8, 10]

# Positive Zahlen
werte = [-3, -1, 0, 2, 5, -8, 7]
positive = list(filter(lambda x: x > 0, werte))
print(positive)  # [2, 5, 7]

# Nicht-leere Strings
texte = ["Hallo", "", "Welt", "", "Python"]
nicht_leer = list(filter(lambda s: len(s) > 0, texte))
print(nicht_leer)  # ['Hallo', 'Welt', 'Python']
```

### `map()` und `filter()` kombinieren

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ungerade Zahlen quadrieren
ergebnis = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, zahlen)))
print(ergebnis)  # [1, 9, 25, 49, 81]
```

!!! tip "Vergleich mit List Comprehension"
    Die gleiche Operation als List Comprehension ist oft lesbarer:

    ```python
    ergebnis = [x ** 2 for x in zahlen if x % 2 != 0]
    ```

---

## Comprehensions statt `map()` und `filter()`

In der Praxis werden `map()` und `filter()` mit Lambda in Python eher selten verwendet. **List Comprehensions** und **Generator Expressions** lösen die gleichen Probleme — und sind dabei kürzer und lesbarer:

```python
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map + filter mit Lambda
ergebnis = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, zahlen)))

# Gleiche Operation als List Comprehension — deutlich lesbarer
ergebnis = [x ** 2 for x in zahlen if x % 2 == 0]
```

| Aufgabe | Lambda + map/filter | Comprehension |
|---|---|---|
| Transformieren | `list(map(lambda x: x*2, lst))` | `[x*2 for x in lst]` |
| Filtern | `list(filter(lambda x: x>0, lst))` | `[x for x in lst if x>0]` |
| Beides | `list(map(..., filter(...)))` | `[x*2 for x in lst if x>0]` |
| Lazy (Iterator) | `map(lambda x: x*2, lst)` | `(x*2 for x in lst)` |

!!! tip "Empfehlung"
    Bevorzuge **Comprehensions** gegenüber `map()`/`filter()` mit Lambda.
    Sie sind idiomatischer Python und in der Regel besser lesbar.

---

## Wann braucht man Lambda wirklich?

Lambda-Funktionen sind dann gefragt, wenn eine Funktion eine **andere Funktion als Parameter** erwartet — und sich das Problem **nicht** mit einer Comprehension lösen lässt.

Das häufigste Beispiel ist der **`key`-Parameter** bei Sortier- und Vergleichsfunktionen:

```python
# sorted() erwartet eine Funktion als key — hier geht keine Comprehension
sorted(personen, key=lambda p: p["alter"])

# Ebenso bei min() und max()
aelteste = max(personen, key=lambda p: p["alter"])
juengste = min(personen, key=lambda p: p["alter"])
```

Der Grund: `sorted()` ruft die `key`-Funktion **intern** für jedes Element auf, um den Vergleichswert zu bestimmen. Hier wird eine **Funktion als Argument übergeben** — und genau dafür sind Lambda-Funktionen gemacht.

### Weitere Beispiele für Funktionen als Parameter

```python
# tkinter: Button mit Callback
button = Button(root, command=lambda: print("Klick!"))

# functools.reduce: Akkumulation
from functools import reduce
produkt = reduce(lambda a, b: a * b, [1, 2, 3, 4])  # 24

# Eigene Funktion mit Funktions-Parameter
def anwenden(funktion, wert):
    return funktion(wert)

print(anwenden(lambda x: x ** 2, 5))  # 25
```

!!! info "Faustregel"
    **Comprehension** → wenn du eine Liste/ein Set/ein Dict **erzeugen** willst
    (transformieren, filtern, kombinieren).

    **Lambda** → wenn eine Funktion eine andere **Funktion als Argument** erwartet
    (`key=`, `command=`, `default=`, Callbacks, etc.).

---

## Lambda vs. def

### Lambda verwenden, wenn:

- Eine Funktion eine **andere Funktion als Parameter** erwartet (z.B. `key` bei `sorted()`)
- Die Logik in **einen Ausdruck** passt
- Die Funktion nur **einmal und inline** verwendet wird

### `def` verwenden, wenn:

- Die Funktion **mehrfach** verwendet wird
- Die Logik **mehrere Schritte** erfordert
- Ein **aussagekräftiger Name** die Lesbarkeit verbessert
- Ein **Docstring** zur Dokumentation nötig ist

### PEP 8 Empfehlung

!!! warning "PEP 8: Lambda nicht an Variablen zuweisen"
    Laut PEP 8 (Pythons Style Guide) soll man Lambda-Funktionen **nicht** an Variablen zuweisen.
    Wenn eine Funktion einen Namen braucht, verwende `def`:

    ```python
    # Schlecht (laut PEP 8)
    verdoppeln = lambda x: x * 2

    # Gut
    def verdoppeln(x):
        return x * 2
    ```

    Lambda-Funktionen sind für den **anonymen Inline-Gebrauch** gedacht:
    ```python
    # Gut — Lambda wird direkt als Argument verwendet
    sorted(woerter, key=lambda w: len(w))
    ```

---

## Aufgaben

{{ task(file="tasks/funktionen_fortgeschritten/lambda/01_einfache_lambda.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/02_lambda_vs_def.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/03_sortieren_nach_laenge.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/04_sortieren_nach_attribut.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/05_map_quadratzahlen.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/06_filter_gerade_zahlen.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/07_map_filter_kombiniert.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/lambda/08_lambda_in_funktionen.yaml") }}
