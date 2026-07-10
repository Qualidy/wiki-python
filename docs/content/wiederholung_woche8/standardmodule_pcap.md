# PCAP-Standardmodule: `math`, `random`, `platform`

Diese Einheit schließt Lücken, die in den PCAP-Testfragen besonders oft auftauchen: kleine Unterschiede in Funktionssignaturen, Rückgabetypen und Importvarianten.

## `math`

Vor der Nutzung muss das Modul importiert werden.

```python
import math
```

Wichtige Funktionen:

| Funktion | Ergebnis / Besonderheit |
| --- | --- |
| `math.ceil(x)` | kleinster Integer `>= x` |
| `math.floor(x)` | größter Integer `<= x` |
| `math.trunc(x)` | Nachkommastellen abschneiden, Richtung `0` |
| `math.factorial(n)` | nur nicht-negative Integer |
| `math.sqrt(x)` | Quadratwurzel als `float` |
| `math.hypot(...)` | euklidische Länge, Ergebnis als `float` |

Beispiele:

```python
import math

print(math.ceil(-1.1))   # -1
print(math.floor(-1.1))  # -2
print(math.trunc(-1.9))  # -1
print(math.sqrt(1))      # 1.0
print(math.hypot(3, 4))  # 5.0
```

Wichtig für aktuelle Python-Versionen:

```python
import math

math.factorial(3)     # 6
math.factorial(3.0)   # TypeError
math.factorial(-3)    # ValueError
```

## `random`

```python
import random
```

| Funktion | Ergebnis / Besonderheit |
| --- | --- |
| `random.random()` | `float` im Bereich `0.0 <= x < 1.0` |
| `random.seed(value)` | macht Zufallsfolgen reproduzierbar |
| `random.choice(seq)` | ein Element aus einer Sequenz |
| `random.choices(seq, k=n)` | Liste mit `n` Elementen, mit Zurücklegen |
| `random.sample(population, k=n)` | Liste mit `n` eindeutigen Elementen |

```python
import random

print(random.random() * 100)              # float zwischen 0 und 100
print(random.choice(["spam", "ham"]))     # ein Element
print(random.sample(["a", "b", "c"], k=1))  # Liste mit einem Element
```

Typische Fallen:

- `math.random()` gibt es nicht.
- `random.random(100)` ist falsch, `random.random()` nimmt keine Argumente.
- `random.sample(..., k=1)` gibt eine Liste zurück, nicht direkt ein einzelnes Element.

## `platform`

```python
import platform
```

Wichtige Funktionen:

```python
print(platform.platform())
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.python_implementation())
print(platform.python_version_tuple())
```

Typische Falle:

```python
platform.system()
```

liefert Informationen zum Betriebssystem, nicht zur Python-Implementierung. Für die Implementierung ist `platform.python_implementation()` zuständig.

## `dir()` und `sys.path`

`dir()` liefert Namen, nicht Dateinamen.

```python
print(dir())        # Namen im aktuellen Scope
print(dir(math))    # Namen im Modul math
```

`sys.path` ist eine Liste von Suchpfaden für Imports.

```python
import sys

print(type(sys.path))  # <class 'list'>
sys.path.append("my_modules")
```

## Aufgaben

### Aufgabe 1: `ceil`, `floor`, `trunc`

Was wird ausgegeben?

```python
import math

print(math.ceil(-2.8))
print(math.floor(-2.8))
print(math.trunc(-2.8))
```

??? success "Lösung"
    ```text
    -2
    -3
    -2
    ```

### Aufgabe 2: `factorial`

Welche Aufrufe funktionieren?

```python
math.factorial(4)
math.factorial(4.0)
math.factorial(-4)
```

??? success "Lösung"
    Nur `math.factorial(4)` funktioniert. `4.0` ist kein Integer, `-4` ist negativ.

### Aufgabe 3: `random.sample`

Was ist der Typ des Ergebnisses?

```python
import random

result = random.sample(["spam", "ham", "eggs"], k=1)
print(type(result))
```

??? success "Lösung"
    `<class 'list'>`

### Aufgabe 4: `random.random`

Welche Variante liefert einen Wert zwischen `0` und `100`?

```python
random.random(100)
random.random() * 100
random.random(0, 100)
```

??? success "Lösung"
    `random.random() * 100`

### Aufgabe 5: Plattform unterscheiden

Welche Funktion liefert die Python-Implementierung, z. B. `CPython`?

??? success "Lösung"
    `platform.python_implementation()`

### Aufgabe 6: `dir()`

Warum ist diese Aussage falsch?

> `dir(math)` liefert alle Dateien im Ordner des Moduls `math`.

??? success "Lösung"
    `dir(math)` liefert Namen der Attribute/Funktionen im Modul, keine Dateien.
