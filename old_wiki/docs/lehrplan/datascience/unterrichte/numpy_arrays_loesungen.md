# Lösungen

### A1: Erstellen eines NumPy Arrays 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/WXiLq-vmXww?si=RdpivN32J9fYm9Yq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstellen Sie ein NumPy Array mit den Werten von 10 bis 20.


```python
import numpy as np

arr = np.array(range(10, 21))
print(arr)
```

    [10 11 12 13 14 15 16 17 18 19 20]



```python
arr = np.arange(10,21)
print(arr)
```

    [10 11 12 13 14 15 16 17 18 19 20]


### A2: Summe der Elemente eines Arrays 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7fx5ETzCXq4?si=0ZkRnrtBhvAMAVOU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Berechnen Sie die Summe aller Elemente in einem NumPy Array [8, 4, 6, 0, 2].


```python
arr = np.array([8, 4, 6, 0, 2])
summe = np.sum(arr)
print(summe)
```

    20


### A3: Maximalwert in einem Array finden 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/jAwy_VNEkQY?si=ZX8AKjqIWjNoW3J7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Bestimmen Sie den größten Wert in dem Array [3, -1, 7, 4, 2]. Wie können wir herausfinden an welcher Stelle dieser Maximalwert steht?


```python
arr = np.array([3, 1, 7, 4, 2])
max_value = np.max(arr)
print(max_value)
```

    7



```python
max_pos = np.argmax(arr)
print(max_pos)
```

    2


### A4: 2D-Array erstellen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/p6VmUaFuMNA?si=uhHj1DvU5y6Pgqgf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein 2D-Array der Größe 3x3, das die Zahlen von 1 bis 9 enthält.


```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]



```python
arr = np.arange(1,10).reshape(3,3)
print(arr)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]


### A5: Zeilensummen einer Matrix berechnen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/QFdPRTw8JdI?si=nf1L31-3S_yQfkOL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Berechnen Sie die Summe jeder Zeile in der Matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].


```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

row_sums = np.sum(matrix, axis=1)
print(row_sums)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [ 6 15 24]


### A6: Spaltensummen einer Matrix berechnen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/C3SgGdinp1s?si=Hs7EzxyvnGIskje8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Berechnen Sie die Spaltensummen der Matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].


```python
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

col_sums = np.sum(matrix, axis=0)
print(col_sums)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [12 15 18]


### A7: Elementweise Multiplikation zweier Arrays 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/zofVh35CQ8o?si=obcwRMNzP0U1c1Xf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Multiplizieren Sie die Elemente der Arrays [1, 2, 3] und [4, 5, 6] elementweise.


```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
product = np.multiply(arr1, arr2)
print(product)
```

    [ 4 10 18]


### A8: Zufälliges Array erzeugen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/1h0NJ2pBXjQ?si=Cs1BNdX5z_E3o83O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erzeugen Sie ein eindimensionales Array mit 5 zufälligen Ganzzahlen zwischen 0 und 10.


```python
arr = np.random.randint(0, 11, 5)
print(arr)
```

    [4 1 7 1 3]


### A9: Negative Werte in einem Array 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/o_xGwNTSquQ?si=mn95k7k_vluw7GYb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Ersetzen Sie alle negativen Werte in dem Array [-1, 2, -3, 4, -5] durch 0.


```python
arr = np.array([-1, 2, -3, 4, -5])
arr[arr < 0] = 0
print(arr)
```

    [0 2 0 4 0]


### A10: Transposition einer Matrix 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/le7D2v3re4g?si=LsveH1sVL6VOcjO_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Transponieren Sie die Matrix [[1, 2], [3, 4], [5, 6]].


```python
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix)

transposed_matrix = np.transpose(matrix)
print(transposed_matrix)
```

    [[1 2]
     [3 4]
     [5 6]]
    [[1 3 5]
     [2 4 6]]

