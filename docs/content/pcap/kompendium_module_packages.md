# PCAP-Kompendium: Modules and Packages

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Module | Eine Python-Datei, die Code, Funktionen, Klassen oder Variablen enthält |
| Package | Ordnerstruktur für Module; klassisch mit `__init__.py` |
| Namespace | Bereich, in dem Namen auf Objekte zeigen |
| Qualified name | Zugriff über den vollständigen Pfad, z. B. `package.module.function` |
| Absolute import | Import vom Projekt-/Suchpfad aus |
| Relative import | Import relativ zum aktuellen Package mit `.` oder `..` |
| `sys.path` | Liste der Suchpfade, in denen Python Module sucht |

## Import-Varianten

```python
import math
math.sqrt(9)
```

```python
import math as m
m.sqrt(9)
```

```python
from math import sqrt
sqrt(9)
```

```python
from math import sqrt as wurzel
wurzel(9)
```

```python
from math import *
sqrt(9)
```

`import *` ist prüfungsrelevant, aber in echtem Code meist schlechter Stil, weil Namen unklar in den Namespace gelangen.

## Relative Imports

Beispielstruktur:

```text
package/
  subpackage1/
    __init__.py
    moduleY.py
  subpackage2/
    moduleZ.py
  moduleA.py
```

Aus `subpackage1/__init__.py`:

```python
from .moduleY import spam
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```

Merke:

- `.` meint aktuelles Package.
- `..` meint ein Package höher.
- Relative Imports funktionieren sinnvoll innerhalb von Packages, nicht als beliebiger Skript-Trick.

## `dir()`

Signatur:

```python
dir()
dir(object)
```

Beispiele:

```python
import math

print(dir())
print(dir(math))
```

Wichtig:

- `dir()` liefert Namen im aktuellen Scope.
- `dir(obj)` liefert relevante Attribute/Namen eines Objekts.
- `dir()` listet keine Dateien eines Ordners.

## `sys.path`

```python
import sys

print(type(sys.path))  # list
sys.path.append("my_modules")
```

Python sucht Module unter anderem in:

- Ordner des gestarteten Skripts
- Einträge aus `PYTHONPATH`
- installationsabhängige Standardpfade
- Einträge in `sys.path`

## `math`

```python
import math
```

| Funktion | Parameter | Ergebnis / Falle |
| --- | --- | --- |
| `math.ceil(x)` | Zahl | kleinster Integer `>= x` |
| `math.floor(x)` | Zahl | größter Integer `<= x` |
| `math.trunc(x)` | Zahl | schneidet Richtung `0` ab |
| `math.factorial(n)` | nicht-negativer Integer | `float` ist nicht erlaubt |
| `math.sqrt(x)` | nicht-negative Zahl | Ergebnis ist `float` |
| `math.hypot(*coordinates)` | Zahlen | euklidische Länge als `float` |

```python
math.ceil(-1.1)    # -1
math.floor(-1.1)   # -2
math.trunc(-1.9)   # -1
math.sqrt(1)       # 1.0
math.factorial(3)  # 6
```

Fallen:

```python
math.factorial(3.0)  # TypeError
math.factorial(-3)   # ValueError
```

## `random`

```python
import random
```

| Funktion | Parameter | Ergebnis / Falle |
| --- | --- | --- |
| `random.random()` | keine | `float`, `0.0 <= x < 1.0` |
| `random.seed(a=None, version=2)` | Seed-Wert | reproduzierbare Zufallsfolge |
| `random.choice(seq)` | nicht-leere Sequenz | ein Element |
| `random.choices(population, weights=None, *, cum_weights=None, k=1)` | Population, optional Gewichte, `k` | Liste, mit Zurücklegen |
| `random.sample(population, k, *, counts=None)` | Population, `k` | Liste eindeutiger Elemente |

Fallen:

```python
random.random(100)       # TypeError
random.random() * 100    # Wert zwischen 0 und 100
random.sample(seq, k=1)  # Liste mit einem Element
```

## `platform`

```python
import platform
```

| Funktion | Bedeutung |
| --- | --- |
| `platform.platform()` | zusammenfassende Plattformbeschreibung |
| `platform.machine()` | Maschinentyp, z. B. Architektur |
| `platform.processor()` | Prozessorbezeichnung, kann leer sein |
| `platform.system()` | Betriebssystemname |
| `platform.version()` | Systemversion |
| `platform.python_implementation()` | z. B. `CPython` |
| `platform.python_version_tuple()` | Tupel aus Major, Minor, Patch als Strings |

## Mini-Check

```python
import math
print(math.ceil(-2.1), math.floor(-2.1), math.trunc(-2.1))
```

??? success "Lösung"
    `-2 -3 -2`

```python
import random
print(type(random.sample(["a", "b"], k=1)))
```

??? success "Lösung"
    `<class 'list'>`
