### Aufgabe: Docstring von random
Im Sourcecode findet man genau den Docstring, der auch in der Dokumentation auftaucht.

### Aufgabe: Eigene Docstrings schreiben

```python
def calculate_area_rectangle(sideA, sideB):
    """
    Berechnet die Fläche eines Rechtecks basierend auf den beiden Seiten.
    Args:
        sideA: Erste Seite des Rechteeckes.
        sideB: Zweite Seite des Rechteckes.

    Returns:
        Fläche des Quadrates.
    """
    return sideA * sideB


def sum_positive_numbers(numbers):
    """
    Summiert die positiven Elemente in der Liste auf.
    Args:
        numbers: Liste von Zahlen

    Returns:
        Summe der positiven Zahlen in der Liste
    """
    return sum(number for number in numbers if number > 0)


def combine(list0, list1, func):
    """
    Wendet die Funktion *func* auf jeweils ein Element aus *list0* und ein Element aus *list1* an.
    Args:
        list0: Liste von Elementen mit den ersten Parametern.
        list1: Liste von Elementen mit den zweiten Parametern
        func: Funktion, die auf die Elemente in den Listen angewandt werden sollen.

    Returns:
        Liefert eine neue Liste, bei der je ein Element aus jeder Liste in die Funktion *func* eingesetzt wurde.
    """
    return [func(a, b) for a, b in zip(list0, list1)]
```

### Aufgabe: Hilfe ist unterwegs
`help` zeigt den Docstring in der Konsole an.

### Aufgabe: Selber Testen
```python
import doctest


def divide(a, b):
    """Compute and return the quotient of two numbers.

    Usage examples:
    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0

    >>> divide(42, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return float(a / b)


if __name__ == '__main__':
    doctest.testmod()

```