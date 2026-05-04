# Typehints

[30 min]

Python-Typenhinweise sind Annotationen, die zu Funktions- und Variablendeklarationen hinzugefügt werden, um die erwarteten Datentypen von Funktionsparametern, Rückgabewerten und Variablen anzugeben. Sie werden verwendet, um statische Typüberprüfungsinformationen an Tools wie Linter, IDEs und Typüberprüfer (z. B. mypy) bereitzustellen, ohne das Laufzeitverhalten des Codes zu beeinflussen. Typenhinweise helfen Entwicklern dabei, typbezogene Fehler frühzeitig im Entwicklungsprozess zu erkennen und den Code verständlicher zu machen.

Typenhinweise wurden in Python 3.5 eingeführt und sind mit der Einführung des Typisierungsmoduls (Typing-Modul) immer beliebter geworden. Hier sind einige häufige Typen-Annotationsanmerkungen:

**Funktionsannotationen:** Um den Typ der Parameter einer Funktion anzugeben, können Sie das `->`-Symbol verwenden, um den Rückgabetyp anzugeben.

```python
def grüße(name: str) -> str:
    return f"Hallo, {name}"
```

**Variablen:** Sie können Variablen mithilfe eines Doppelpunkts und des Typs nach dem Namen der Variable annotieren.

```python
anzahl: int = 10
```

**Optionale Typen:** Sie können angeben, dass eine Variable oder ein Funktionsparameter einen bestimmten Typ oder None (also optional) sein kann, indem Sie die Typenhinweis Union verwenden.

```python
from typing import Union

def addiere_oder_none(a: int, b: int) -> Union[int, None]:
   if a is not None and b is not None:
       return a + b
   else:
       return None
```

**Listen und Dictionaries:** Sie können Listen und Dictionaries mit den Typen ihrer Elemente oder Schlüssel und Werte annotieren.
```python
from typing import List, Dict

namen: List[str] = ["Alice", "Bob", "Charlie"]
person: Dict[str, int] = {"Alice": 30, "Bob": 25}
```

**Typaliasen:** Sie können benutzerdefinierte Typaliasen erstellen, indem Sie den Typenhinweis Type verwenden, um Ihre Typenanmerkungen leserlicher zu gestalten.

```python
from typing import Type

BenutzerId = int
BenutzerDict = dict[BenutzerId, str]
```

**Generika:** Python unterstützt Generika, mit denen Sie Funktionen und Klassen erstellen können, die mit mehreren Datentypen arbeiten können.

```python
from typing import List, TypeVar

T = TypeVar('T')  # Typvariable
def hole_erstes_element(elemente: List[T]) -> T:
    return elemente[0]
```

**Typenhinweise werden zur Laufzeit nicht durchgesetzt**, was bedeutet, dass Python keinen Fehler auslöst, wenn die tatsächlichen Datentypen nicht mit den Hinweisen übereinstimmen. Typüberprüfer wie mypy können jedoch Ihren Code analysieren und typbezogene Probleme melden, um Ihnen bei der Erstellung robusteren und wartbareren Code zu helfen.

### Aufgabe 1: Typehints hinzufügen 🌶️🌶️
[20 min]

Füge Typehints zu den folgenden Funktionen hinzu, um die erwarteten Datentypen der Parameter und Rückgabewerte anzugeben.

```python
def add(a, b):
    return a + b

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def find_max(data):
    max_value = data[0]
    for item in data:
        if item > max_value:
            max_value = item
    return max_value

def greet(name):
    return f"Hello, {name}"

# Beispielaufrufe der Funktionen
result1 = add(5, 3)
result2 = multiply([2, 4, 6])
result3 = find_max([10, 7, 15, 3])
message = greet("Alice")

# Ausgabe der Ergebnisse
print(result1)
print(result2)
print(result3)
print(message)
```

[Lösung](solution.md#lsung-aufgabe-1)

### Aufgabe 2: Typehints für komplexe Datentypen 🌶️🌶️🌶️
[20 min]

Füge Typehints zu den folgenden Funktionen hinzu, um die erwarteten Datentypen der Parameter und Rückgabewerte anzugeben.

```python
def add_or_subtract(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return "Invalid operation"

def process_data(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    else:
        return "Unsupported data type"

# Beispielaufrufe der Funktionen
result1 = add_or_subtract(5, 3, "add")
result2 = add_or_subtract(10, 4, "subtract")
result3 = add_or_subtract(5, 3, "multiply")  # Ungültige Operation
result4 = process_data(42)
result5 = process_data("hello")
result6 = process_data([1, 2, 3])  # Nicht unterstützter Datentyp

# Ausgabe der Ergebnisse
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
```

[Lösung](solution.md#lsung-aufgabe-2)

