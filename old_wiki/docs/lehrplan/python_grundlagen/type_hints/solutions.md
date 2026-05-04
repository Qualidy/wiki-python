# Lösungen

### Aufgabe: Typehints betrachten

```commandline
something.py:5: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
something.py:7: error: Argument 2 to "addiere" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

### Aufgabe: Basistypen bestimmen 

Wir können `type` verwenden, um den Typ eines Objektes zu bestimmen.

```python
a: int = 1
b: int = 2
c: int = -1
d: float = 1.0
e: int = 0
f: float = 0.0
g: float = 0.5
h: float = 3.3333
i: bool = True
j: bool = False
k: str = "hiho"
l: str = "0"
m: str = '1'
n: complex = 1+3j
o: type = int
```

### **Typen finden** 🌶️🌶🌶️:

```python
def get_rest(zaehler: int, nenner: int) -> int:
    return zaehler // nenner


from typing import Optional


def greeting(name: str, alter: Optional[int] = None):
    if alter is not None and alter > 60:
        return f"Einen wunderschönen Tag, {name}."
    return f"Was geht, {name}?"


def calculate_average(list_of_ints: list[int]) -> float:
    return sum(list_of_ints) / len(list_of_ints)


from typing import Tuple, List


def min_max(list_of_floats: List[float]) -> Tuple[float, float]:
    return min(list_of_floats), max(list_of_floats)


from typing import Any


# def behave_different(value: tuple | int | Any) -> tuple | float | None:
def behave_different(value: tuple | int | Any) -> Optional[tuple | float]:
    if isinstance(value, tuple):
        return value[::-1]
    elif isinstance(value, int):
        return value / 2
    else:
        return None
```
