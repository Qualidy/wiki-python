import doctest
from random import sample


def create_shuffled_list(end, start=1):
    """
    ERstellt eine Liste von Zahlen von Start bis End die zufällig sortiert ist
    Args:
        end: Letzter Eintrag
        start: default=1. Erste Position in

    Returns: Liste mit den Zahlen von Start bis End (jeweils inklusive) mit zufälliger Ordnung

    >>> import random
    >>> random.seed(42)
    >>> create_shuffled_list(5)
    [1, 5, 3, 2, 4]
    >>> create_shuffled_list(start=5, end=10)
    [6, 10, 5, 7, 8, 9]
    """
    n = end - start + 1
    return sample(list(range(start, end + 1)), k=n)


if __name__ == "__main__":
    doctest.testmod()
