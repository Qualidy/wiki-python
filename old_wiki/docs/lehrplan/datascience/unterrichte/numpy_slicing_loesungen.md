# Lösungen

### A1: Wozu eigentlich Slicing? 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YTr8tDwVtCA?si=pWEMaa-U6SmZ2Xhi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Überlege dir Beispiele: Wo braucht man Slicing bei der Datenverarbeitung bzw. Datenanalyse?

Beispiele:

- ein Stück einer Zeitreihe (1D Array) "rausschneiden" 
- von mehreren Zeitreihen (2D Array) einen Abschnitt "rausschneiden", z.B. die letzten 100 Datenpunkte oder die mittleren 100 Datenpunkte
- ein Kanal (R,G,B) von einem Farbbild (RGB) (3D Array) "rausschneiden"
- einen Abschnitt aus einem Farb-Video (4D Array) "rausschneiden"

### A2: Grundlegendes Slicing 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/F7KLEMSCFyc?si=msYlVw1pAxuF96Pn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein eindimensionales NumPy-Array mit den Zahlen von 1 bis 10 und wählen Sie die Elemente von Index 3 bis 7 aus.


```python
import numpy as np

arr = np.arange(1, 11)
sliced_arr = arr[3:8]
print(sliced_arr)
```

    [4 5 6 7 8]


### A3: Slicing mit negativen Indizes 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/NaegO5Jt9so?si=Xg2NbgKsONLOAyUA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein Array mit den Zahlen von -5 bis 5 und wählen Sie die letzten drei und die ersten drei Elemente *nur* mithilfe negativer Indizes aus.


```python
arr = np.arange(-5, 6)
print(arr)

print(arr[-3:])
print(arr[-11:-8])
```

    [-5 -4 -3 -2 -1  0  1  2  3  4  5]
    [3 4 5]
    [-5 -4 -3]


### A4: Slicing mit Schrittweiten 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/WHV_U1yCC5Y?si=OuVw1gZlgdNtKShV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein Array von 1 bis 10 und slicen Sie das 2,4,6,... Element heraus!


```python
arr = np.arange(1, 11)
print(arr)

sliced_arr = arr[1::2]
print(sliced_arr)
```

    [ 1  2  3  4  5  6  7  8  9 10]
    [ 2  4  6  8 10]


### A5: Reverse Slicing 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fdsLWN4xKU8?si=WlpNbMewtL1G8E9C" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein Array mit den Zahlen von 1 bis 10 und kehren Sie die Reihenfolge der Elemente durch Slicing um.


```python
arr = np.arange(1, 11)
reversed_arr = arr[::-1]
print(reversed_arr)
```

    [10  9  8  7  6  5  4  3  2  1]


### A6: Slicing von zweidimensionalen Arrays 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/frEQ49eirTs?si=gVzMNRmwHNkWc6l_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein 3x3-Array mit den Zahlen von 1 bis 9 und wählen Sie die zweite Zeile aus.


```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_row = arr[1, :]
print(second_row)
```

    [4 5 6]


### A7: Slicing von Spalten 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/irt-8lag8Lc?si=OU7yE5x0s9Vt8tnQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein 4x4-Array mit beliebigen Zahlen und wählen Sie die dritte Spalte aus.


```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
third_column = arr[:, 2]
print(third_column)
```

    [ 3  7 11 15]


### A8: Slicing mit Bedingungen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/w9fYXPho5bE?si=4fq7oBg-ou8j0mJm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein Array mit den Zahlen von -10 bis 10 und wählen Sie alle Elemente aus, die größer als 5 oder kleiner als -3 sind.


```python
# Erstellen des Arrays mit Zahlen von -10 bis 10
arr = np.arange(-10, 11)
print(arr)

# Bedingtes Slicing, um die gewünschten Elemente auszuwählen
selected_elements = arr[(arr > 5) | (arr < -3)]

print(selected_elements)
```

    [-10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7
       8   9  10]
    [-10  -9  -8  -7  -6  -5  -4   6   7   8   9  10]


- np.arange(-10, 11) erstellt ein Array mit Zahlen von -10 bis 10 (da der obere Grenzwert exklusiv ist, geben wir 11 an).  
- (arr > 5) | (arr < -3) ist die Bedingung, die für jedes Element im Array überprüft wird. | steht für den logischen ODER-Operator, was bedeutet, dass jedes Element, das die Bedingung erfüllt, im resultierenden Array enthalten sein wird.
- arr[(arr > 5) | (arr < -3)] wählt alle Elemente aus, die entweder größer als 5 oder kleiner als -3 sind.

### A9: Diagonales Slicing 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ujmEDIt_IH4?si=aD5hzShQLSETXUD-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein 3x3-Array mit den Zahlen von 1 bis 9 und wählen Sie die Elemente der Diagonale aus.


```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

diagonal = arr.diagonal()
print(diagonal)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [1 5 9]


### A10: Slicing von Submatrizen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/1mkRWaqSFtg?si=D_mcdBgsuk9xRBro" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein 4x4-Array und wählen Sie eine 2x2-Submatrix aus der oberen linken Ecke des Arrays aus.


```python
arr = np.arange(1,17).reshape(4,4)
print(arr)

sub_matrix = arr[:2, :2]
print(sub_matrix)
```

    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]]
    [[1 2]
     [5 6]]


### A11: Komplexes Slicing 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/N0c8ojZfZH0?si=lhEM1nfLqQbQtCan" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie ein 5x5-Array mit den Zahlen von 1 bis 25 und wählen Sie jede zweite Zeile und Spalte aus.


```python
# Erstellen eines 5x5-Arrays mit Zahlen von 1 bis 25
arr = np.arange(1, 26).reshape(5, 5)
print(arr)

# Auswählen jeder zweiten Zeile und jeder zweiten Spalte
sliced_arr = arr[::2, ::2]

print(sliced_arr)
```

    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]
     [11 12 13 14 15]
     [16 17 18 19 20]
     [21 22 23 24 25]]
    [[ 1  3  5]
     [11 13 15]
     [21 23 25]]


- np.arange(1, 26) erstellt ein eindimensionales Array mit Zahlen von 1 bis 25.
- .reshape(5, 5) formt dieses Array in eine 5x5-Matrix um.
- arr[::2, ::2] wendet Slicing an, um jede zweite Zeile und jede zweite Spalte auszuwählen. ::2 bedeutet, dass wir mit einer Schrittweite von 2 durch das Array gehen, wodurch wir jede zweite Zeile und Spalte erhalten


```python

```
