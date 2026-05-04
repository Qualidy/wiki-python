# Lösung für Exkurs Rekursive Funktionen

### Aufgabe: Multiplizieren

```python
def multiply_up(box_or_value):
    if isinstance(box_or_value, list):
        product = 1 # Aus 0 eine 1

        for obj in box_or_value:
            product *= multiply_up(obj) # Aus += ein *=

    else:
        product = box_or_value

    return product


all_multiplied_up = multiply_up([[1, 2, 3], [4, 5, [6, 7, 8]]])
print(all_multiplied_up)
```
### Aufgabe: umständlich?
Sie summiert die Elemente einer Liste/Tupel... auf. Also wäre auch hier `sum_up`
oder `sigma` ein schöner Name😉


### Aufgabe: Fakultät berechnen
   
```python
def fak(n):
    if n <= 1:
        return 1
    return n * fak(n-1)
```


### Aufgabe: Binäre Suche

```python
def binary_search(my_list, element):
    if len(my_list) == 0:
        return False

    mid_index = len(my_list) // 2
    mid_element = my_list[mid_index]

    if mid_element < element:
        return binary_search(my_list[mid_index + 1:], element)
    elif mid_element > element:
        return binary_search(my_list[:mid_index], element)
    else:
        return True


print(binary_search([1, 2, 3, 5, 6, 9, 10], 9))  # True
print(binary_search([1, 2, 3, 5, 6, 9, 10], 8))  # False

```
