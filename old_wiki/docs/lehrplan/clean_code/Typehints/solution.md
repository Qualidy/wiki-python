# Lösung Aufgabe 1
```python
from typing import List

def add(a: int, b: int) -> int:
    return a + b

def multiply(numbers: List[int]) -> int:
    result = 1
    for num in numbers:
        result *= num
    return result

def find_max(data: List[int]) -> int:
    max_value = data[0]
    for item in data:
        if item > max_value:
            max_value = item
    return max_value

def greet(name: str) -> str:
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

# Lösung Aufgabe 2
```python
from typing import Union

def add_or_subtract(a: Union[int, float], b: Union[int, float], operation: str) -> Union[int, float, str]:
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return "Invalid operation"

def process_data(data: Union[int, str]) -> Union[int, str]:
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
