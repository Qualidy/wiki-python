# NumPy: Mathematik mit Arrays

Neben Datenanalyse eignen Numpy Arrays sich sehr gut um Matrizen-Rechnungen durchzuführen. Außerdem gibt es mit numpy.linalg eine Vielzahl an Tools der Linearen Algebra wie z.B. Berechnung von Inversen, Eigenwerten, etc.


## Array-Operationen

- **Erstellen von Arrays**: `np.array()`, `np.zeros()`, `np.ones()`, `np.eye()`, `np.random.random()`
- **Elementweise Operationen**: Addition (`+`), Subtraktion (`-`), Multiplikation (`*`), Division (`/`)
- **Skalar-Operationen**: Elementweise Operationen mit einem Skalar
- **Mathematische Funktionen**: `np.sum()`, `np.mean()`, `np.max()`, `np.min()`, `np.sqrt()`, `np.exp()`, `np.log()`, `np.sin()`, `np.cos()`, `np.tan()`
- **Aggregatfunktionen**: `np.sum()`, `np.mean()`, `np.max()`, `np.min()`

Da Numpy sehr viele Operationen auf Arrays erlaubt, ist es einfach möglich eigene Funktionen (z.B. Polynome) zu definieren:
```python
def func(x):
    return 2 * x**3 - 0.5 * x**2 + 10

x = np.arange(-10, 10)
print(func(x))
```

## Einfaches Plotten mit Pyplot
Matplotlib schauen wir uns nächste Woche im Detail, aber für erste simple Visualisierungen wollen wir es hier schon mal nutzen:

**Polynom plotten**
```python
import matplotlib.pyplot as plt

def func(x):
    return 2 * x**3 - 0.5 * x**2 + 10

x = np.arange(-10, 10)
y = func(x)
plt.plot(x, y)

```
**Sinus plotten**
```python
import matplotlib.pyplot as plt

x = np.linspace(start=0, stop=2*np.pi, num=100)

plt.plot(x, np.sin(x))

```
## Lineare Algebra mit `numpy.linalg`

### Grundlegende Funktionen

- **Matrizenmultiplikation**: `np.dot()`, `@` (Matrix-Multiplikationsoperator)
- **Transposition**: `.T`
- **Inverse einer Matrix**: `np.linalg.inv()`
- **Determinante**: `np.linalg.det()`
- **Eigenwerte und Eigenvektoren**: `np.linalg.eig()`
- **Singulärwertzerlegung (SVD)**: `np.linalg.svd()`
- **Lösen linearer Gleichungssysteme**: `np.linalg.solve()`
- **Norm einer Matrix oder eines Vektors**: `np.linalg.norm()`



### Aufgabe 1 🌶️

- Erstelle ein Array mit 60 zufälligen Zahlen zwischen 1 und 100.
- Konvertiere deine Liste in ein 2D Array der Dimension 6x10
- Berechne für jede Zeile das Maximum, Minimum und den Durchschnitt und sichere die Werte pro Zeile in einem 6x3 Array `statsarray`
- **Bonus:** 🌶️🌶️
    - Nutze nur das statsarray als Grundlage
    - Bestimme den Durchschnitt aller Durchschnittswerte der Zeilen
    - Bestimme den Median der Max-Werte
    - Wie groß ist im Durchschnitt der Unterschied zwischen Max- und Min- Wert in den Zeilen?
    - Wie groß ist die Varianz zwischen Durschnittswert und dem Mittel von Max & Min der Zeilen?

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
import numpy as np

# Schritt 1: Erstellen eines Arrays mit 60 zufälligen Zahlen zwischen 1 und 100
random_numbers = np.random.randint(1, 101, size=60)

# Schritt 2: Konvertieren des Arrays in ein 2D-Array der Dimension 6x10
data_array = random_numbers.reshape(6, 10)

# Schritt 3: Berechnen des Maximums, Minimums und Durchschnitts für jede Zeile
max_values = np.max(data_array, axis=1)
min_values = np.min(data_array, axis=1)
mean_values = np.mean(data_array, axis=1)

# Zusammenstellen der Ergebnisse in einem 6x3 Array (statsarray)
statsarray = np.column_stack((max_values, min_values, mean_values))

# Bonusfragen:
# 1. Durchschnitt aller Durchschnittswerte der Zeilen
avg_of_means = np.mean(statsarray[:, 2])

# 2. Median der Max-Werte
median_of_max = np.median(statsarray[:, 0])

# 3. Durchschnittlicher Unterschied zwischen Max- und Min-Werten in den Zeilen
avg_diff_max_min = np.mean(statsarray[:, 0] - statsarray[:, 1])

# 4. Variation zwischen Durchschnittswert und dem Mittel von Max & Min der Zeilen
mean_of_max_min = (statsarray[:, 0] + statsarray[:, 1]) / 2
variation_mean_max_min = np.mean(statsarray[:, 2] - mean_of_max_min)

# Ausgabe der Ergebnisse
print("2D Array (6x10):")
print(data_array)
print("\nMaximum, Minimum und Durchschnitt pro Zeile (6x3):")
print(statsarray)
print("\nBonus-Lösungen:")
print("Durchschnitt aller Durchschnittswerte der Zeilen:", avg_of_means)
print("Median der Max-Werte:", median_of_max)
print("Durchschnittlicher Unterschied zwischen Max- und Min-Werten in den Zeilen:", avg_diff_max_min)
print("Variation zwischen Durchschnittswert und dem Mittel von Max & Min der Zeilen:", variation_mean_max_min)
```

### Ausgabe:

#### 2D Array (6x10):
```
[[99 58 59 89 56 25 84 40 18 56]
 [18 38 89 96 34  1 73 48 85 90]
 [99  4 47 35 21 71 34 55 28 10]
 [15 33 33 15 63 36 11 62 80 10]
 [98 31  8  8 92 43 41  1 33 33]
 [64 19 17 78 26 31 98 15 49 77]]

Maximum, Minimum und Durchschnitt pro Zeile (6x3):
[[ 99  18  54.2]
 [ 96   1  57.2]
 [ 99   4  38.4]
 [ 80  10  32.8]
 [ 98   1  34.6]
 [ 98  15  44.4]]

Bonus-Lösungen:
Durchschnitt aller Durchschnittswerte der Zeilen: 44.833333333333336
Median der Max-Werte: 98.5
Durchschnittlicher Unterschied zwischen Max- und Min-Werten in den Zeilen: 44.5
Variation zwischen Durchschnittswert und dem Mittel von Max & Min der Zeilen: 9.833333333333334
```

</details>


### Aufgabe 2 🌶️
- a) Erstelle eine Matrix A (5, 6) und fülle sie mit abwärts sortierten Zahlen von 30 bis 1
- b) Erstelle einen Vektor v (6,) der aus 5en besteht
- c) Multipliziere A und v und speichere in neuer Variablen w
- d) Hänge bei w eine 0 ans Ende
- e) Berechne und verstehe was passiert
    - v * w (6,)
    - v.T @ w (1,)   
    - v @ w.T (6,6)



<details>
<summary>🔍 Lösung anzeigen</summary>

```python
import numpy as np

# a) Matrix A (5, 6) mit abwärts sortierten Zahlen von 30 bis 1
A = np.arange(30, 0, -1).reshape(5, 6)
print("Matrix A:")
print(A)

# b) Vektor v (6,) der aus 5en besteht
v = np.ones(6) * 5
print("\nVektor v:")
print(v)

# c) Multiplikation von A und v, Ergebnis in w
w = A @ v
print("\nErgebnis w (A @ v):")
print(w)

# d) Hinzufügen einer 0 ans Ende von w
w = np.append(w, 0)
print("\nw nach Hinzufügen einer 0:")
print(w)

# e) Berechnungen und Erklärungen
# v * w (6,)
result1 = v * w
print("\nv * w (Elementweise Multiplikation, Ergebnis als Vektor):")
print(result1)

# v.T @ w (1,)
result2 = v.T @ w
print("\nv.T @ w (Skalarprodukt, Ergebnis als Skalar):")
print(result2)

# v @ w.T (6,6)
v = v.reshape(6,1) # add empty dimension (6,) -> (6,1)
w = w.reshape(6,1) # add empty dimension (6,) -> (6,1)
print(v) # v ist jetzt erst wirklich ein Spaltenvektor
result3 = v @ w.T
print("\nv @ w.T (Matrix-Multiplikation, Ergebnis als Matrix):")
print(result3)
```

</details>

### Aufgabe 3 🌶️🌶️
- a) Erinnere dich, wie man das Inverse einer 2x2 Matrix einfach berechnen kann
- b) Implementiere diese Formel in eine Funktion inv_2x2() 
- c) Vergleiche deine Funktion mit np.linalg.inv() 
    - Was passiert bei einer nicht invertierbaren Matrix?
- d) (Bonus) 🌶️🌶️🌶️
    - Schreibe eine eigene Funktion zur Berechnung der Determinante einer 3x3 Matrix
    - Eine Möglichkeit ist die Matrizen mit `np.hstack()`nebeneinander zu schreiben und dann die Diagonalformel anzuwenden

<details>
<summary>🔍 Lösung anzeigen</summary>


a) Das Inverse einer 2x2 Matrix 
$$ \begin{pmatrix} a & b \\ c & d \end{pmatrix} $$
kann mit der folgenden Formel berechnet werden:
$$ A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$

b) Implementierung der Funktion `inv_2x2()`:

```python
import numpy as np

def inv_2x2(matrix):
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("Matrix is not invertible")
    inv_matrix = np.array([[d, -b], [-c, a]]) / determinant
    return inv_matrix
```

c) Vergleich mit `np.linalg.inv()` und Behandlung einer nicht invertierbaren Matrix:

```python
# Test der Funktionen
matrix1 = np.array([[2, 1], [1, 2]])
matrix2 = np.array([[1, 2], [2, 4]])  # Diese Matrix ist nicht invertierbar

# Berechnung mit eigener Funktion
try:
    inv1 = inv_2x2(matrix1)
    print("Inverse von matrix1 (mit eigener Funktion):\n", inv1)
except ValueError as e:
    print("Fehler:", e)

try:
    inv2 = inv_2x2(matrix2)
    print("Inverse von matrix2 (mit eigener Funktion):\n", inv2)
except ValueError as e:
    print("Fehler:", e)

# Vergleich mit np.linalg.inv()
inv_np1 = np.linalg.inv(matrix1)
print("\nInverse von matrix1 (mit np.linalg.inv):\n", inv_np1)

try:
    inv_np2 = np.linalg.inv(matrix2)
    print("Inverse von matrix2 (mit np.linalg.inv):\n", inv_np2)
except np.linalg.LinAlgError as e:
    print("Fehler:", e)
```

d) Bonus: Eigene Funktion zur Berechnung der Determinante einer 3x3 Matrix:

```python
import numpy as np

def det_3x3(matrix):
    if matrix.shape != (3, 3):
        raise ValueError("Input matrix must be 3x3")
    
    extended_matrix = np.hstack((matrix, matrix[:, :2]))
    
    pos = sum([np.prod(np.diag(extended_matrix[:, i:i+3])) for i in range(3)])
    neg = sum([np.prod(np.diag(extended_matrix[::-1, i:i+3])) for i in range(3)])
    return pos - neg

# Test der Determinanten-Funktion
matrix3x3 = np.array([[2, 1, 2], [1, 4, 1], [3, 2, 2]])
determinant = det_3x3(matrix3x3)

print("Determinante von matrix3x3 mit det_3x3:", determinant, "\nMit np.linalg:", np.linalg.det(matrix3x3))
```
</details>


## Exkurs:
### Mini-Projekt: Hoch- und Tiefpunkte finden

**Schritt 1**
- Geeignete Funktion wählen (Polynom mit Hoch oder Tiefpunkt)
- Funktion in numpy umsetzen `def f(x):` und geeigneten Definitionsbereich und Schrittweite festlegen mit `x = np.linspace(...)`
- Funktion plotten 

**Schritt 2**
-Wie finden wir einen Hoch oder Tiefpunkt?
    
*Option 1 - Lokale Umgebung absuchen*: <br>
Wenn umliegende Punkte links und rechts von a alle größer sind als a, dann ist a ein Tiefpunkt.

*Option 2 - Erst Gradienten bilden:* <br>
Schreibe eine Python-Funktion, die aus deinem y-Array die Ableitung wieder als Array bildet. 

Dazu muss die Steigung zweier benachbarten Punkte für alle Punkte im Array berechnet werden. 

Dort, wo die Steigung ungefähr 0 ist, befindet sich ein Extrempunkt. 

**Schritt 3**
- Anwenden und mit verschiedenen mathematischen Funktionen überprüfen, z.B. graphisch mit `plt.plot()``
- Vergleicht die Schnelligkeit eurer Extremstellenfinder untereinander