# NumPy: Broadcasting, Boolean Arrays und Masking

## Einführung

In diesem Modul werden wir uns mit drei wichtigen Konzepten von NumPy beschäftigen: Broadcasting, Boolean Arrays und Masking. Diese Konzepte bilden die Grundlage für effiziente numerische Berechnungen und erweiterte Datenmanipulationen in NumPy und sind unerlässlich für die effektive Anwendung der Bibliothek.

## Broadcasting: Ein Überblick

Broadcasting ist eine leistungsstarke Funktion von NumPy, die es ermöglicht, arithmetische Operationen zwischen Arrays unterschiedlicher Größen auszuführen. Das kleinere Array wird dabei automatisch erweitert, um die Dimensionalität des größeren Arrays zu erreichen, sodass die Operationen elementweise durchgeführt werden können, als ob beide Arrays identische Formen hätten. Dies vereinfacht den Code und verbessert die Performance, indem explizite Schleifen vermieden werden.

### Code-Beispiel: Broadcasting mit skalaren Werten


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = arr + 10

# result = arr + np.array([10, 10, 10, 10, 10])
# Dies würde zum selben Ergebnis führen.

print(result)
```

    [11 12 13 14 15]

    
In diesem Beispiel wird das Array arr mit dem Skalarwert 10 addiert. Dank Broadcasting wird der Skalarwert auf jedes Element des Arrays angewendet. Oder anders ausgedrückt: Die 10 wird 5-fach "gestreckt".

### Code-Beispiel: Broadcasting mit Arrays unterschiedlicher Formen

```python
arr1 = np.array([1, 2, 3]) # Reihe
arr2 = np.array([[10], [20], [30]]) # Spalte
result = arr1 + arr2
print(arr1, '--> shape:', arr1.shape, '\n')
print(arr2, '--> shape:', arr2.shape, '\n')
print(result, '--> shape:', result.shape)
```

    [1 2 3] --> shape: (3,) 

    [[10]
    [20]
    [30]] --> shape: (3, 1) 

    [[11 12 13]
    [21 22 23]
    [31 32 33]] --> shape: (3, 3)

## Kompatibilitätsregeln beim Broadcasting

1. Wenn `arr1` und `arr2` eine unterschiedliche Anzahl von Dimensionen haben, füge der Form des kürzeren Arrays Einsen voran.

2. Jede Achse der Länge 1 kann wiederholt (übertragen) werden, um der Länge des anderen Vektors in dieser Achse zu entsprechen.

3. Alle anderen Achsen müssen übereinstimmende Längen aufweisen.

Verwenden Sie diese Regeln, um zu berechnen, ob die Arrays kompatibel sind und, falls ja, welche übertragene Form sie haben.

### Beispiel 1 für Broadcasting-Kompatbilität
```python
x.shape == (2,3)

y.shape == (2,3) # kompatibel, Resultat hat shape == (2,3)
y.shape == (2,1) # kompatibel, Resultat hat shape == (2,3)
y.shape == (1,3) # kompatibel, Resultat hat shape == (2,3)
y.shape == (3,) # kompatibel, Resultat hat shape == (2,3)

y.shape == (3,2) # nicht kompatibel
y.shape == (2,) # nicht kompatibel
```

### Beispiel 2 für Broadcasting-Kompatbilität
```python
x.shape == (1, 2, 3, 5, 1, 11, 1, 17)
y.shape ==          (1, 7,  1, 1, 17) # kompatibel, Resultat hat ...
# shape == (1, 2, 3, 5, 7, 11, 1, 17)
```

### Konkretes Beispiel mit Arrays
```python
import numpy as np

arr1 = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]])
arr2 = np.array([1, 10, 100]).reshape(3, 1)

result = arr1 + arr2
print(arr1, '--> shape:', arr1.shape, '\n')
print(arr2, '--> shape:', arr2.shape, '\n')
print(result, '--> shape:', result.shape)
```

    [[0 1 2]
    [3 4 5]
    [6 7 8]] --> shape: (3, 3) 

    [[  1]
    [ 10]
    [100]] --> shape: (3, 1) 

    [[  1   2   3]
    [ 13  14  15]
    [106 107 108]] --> shape: (3, 3)

### Aufgabe 1: 🌶️
Berechnen Sie das Ergebnis _ohne_ Nutzung von Broadcasting. Dabei sollen die Einträge im Ergebnis-Array innerhalb von `for`-Schleifen berechnet werden.

<details>
<summary>🔍 Lösung anzeigen</summary>
#### Lösung:
```python
myshape = (3, 3)
result2 = np.empty(myshape, dtype=int)
N0, N1 = myshape
for i in range(N0):
    for j in range(N1):
        # in der Dimension, die nur 1 Element hat, benutze genau dieses
        result2[i, j] = arr1[i, j] + arr2[i, 0]
print(result2)
```
</details>

### Aufgabe 2: 🌶️🌶️
Beginnend mit `N = 3`, erstellen Sie ein Array `arr1`, dass aus unterschiedlichen, fortlaufenden Zahlen besteht und `shape == (2, 3, N)` hat. `arr2` hat `shape == (?,)` und besteht aus den Zahlen 1, 10, 100, ..., <???> . Addieren die beiden Arrays einmal mit Broadcasting, einmal mit `for`-Schleifen.

<details>
<summary>🔍 Lösung anzeigen</summary>

#### Lösung:
```python
import numpy as np

# Array Definitionen
N = 3
arr1 = np.arange(2*3*N).reshape(2, 3, N)
arr2 = np.array([10**i for i in range(N)])

print(arr1)
print()
print(arr2)
```

```python
# Lösung mit Broadcasting
result_broadcast = arr1 + arr2
print("Ergebnis mit Broadcasting:")
print(result_broadcast)
```


```python
# Lösung mit Schleifen
myshape = (2, 3, N)
result_loops = np.empty(myshape, dtype=int)
N0, N1, N2 = myshape
for i in range(N0):
    for j in range(N1):
        for k in range(N2):
            result_loops[i, j, k] = arr1[i, j, k] + arr2[k]
print(result_loops)
```
</details>

### (Bonus-) Aufgabe 3: 🌶️🌶️
Sie haben N=1000 Bilder der Größe BxH=32x32, bei denen jedes Bild C=3 Kanäle hat (Rot-, Grün- und Blau-Pixelwerte von 0 bis 255) für jede Position im Bild.

Angenommen, Sie haben die Bilder in einem Array arr1 der Größe (N, C, B, H) == (1000, 3, 32, 32) gespeichert.

Mit welchem Array arr2 würden Sie multiplizieren, um jeden roten Pixel um den Faktor 2, jeden grünen Pixel um den Faktor 3 und jeden blauen Pixel um den Faktor 4 zu skalieren (Wir tun mal so, als gäbe es kein Überlauf-Problem)?


<details>
<summary>🔍 Lösung anzeigen</summary>


#### Lösung:
```python
# Dummy-Bilder erzeugen
myshape = (1000, 3, 32, 32)
arr1 = np.ones(myshape, dtype=np.uint8) # sehr dunkles Bild
```

```python
# Lösung mit Loops
arr2 = np.array([2, 3, 4]).reshape(1, 3, 1, 1)

out = np.empty(myshape, dtype=np.uint8)
N, C, B, H = myshape
for n in range(N):
    for channel in range(C):
        for b in range(B):
            for h in range(H):
                out[n, channel, b, h] = arr1[n, channel, b, h] * arr2[0, channel, 0, 0]
```

```python
# Lösung mit Broadcasting
out2 = arr1 * arr2

print(out2[517], " --> shape =", out2[517].shape) # Kontroll-Beispiel
```

</details>

## Boolesche Arrays

Boolesche Arrays, auch bekannt als 'Boolean Arrays', sind spezielle Arrays, die ausschließlich die Werte True oder False enthalten. Sie entstehen typischerweise durch die Anwendung boolescher Operatoren auf numerische NumPy-Arrays, wodurch jeder Elementwert gemäß einer definierten Bedingung als wahr oder falsch bewertet wird.


### Code-Beispiele: Erstellen von Booleschen Arrays


```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
bool_arr = arr > 3
print(bool_arr)
```

    [False False False  True  True]

```python
arr = np.arange(12).reshape(3,2,2)
bool_arr = arr%5==0
print(arr)
print()
print(bool_arr)
```

    [[[ 0  1]
    [ 2  3]]

    [[ 4  5]
    [ 6  7]]

    [[ 8  9]
    [10 11]]]

    [[[ True False]
    [False False]]

    [[False  True]
    [False False]]

    [[False False]
    [ True False]]]


### Aufgabe 4: 🌶️
Stellen Sie sich einen Würfel vor, der aus 3x3x3 kleinen Würfeln zusammen gebaut ist. Erstellen Sie ein Array, das diese kleinen Würfel darstellt, wobei die Zahlenwerte anzeigen sollen, wieviele Flächen nach außen zeigen, also z.B. 3 für einen kleinen Würfe in einer Ecke des großen Würfels. Erstellen Sie dann ein Boolesches Array, das anzeigt, ob eine gerade Anzahl an Flächen nach außen zeigt

<details>
<summary>🔍 Lösung anzeigen</summary>

#### Lösung:
```python
import numpy as np

# Erstellen eines 3x3x3 Arrays
cube = np.zeros((3, 3, 3), dtype=int)

# Durchlaufen aller Elemente im Array
for x in range(3):
    for y in range(3):
        for z in range(3):
            # Zählen, wie viele der Indizes am Rand liegen (0 oder 2)
            count = 0
            if x == 0 or x == 2:
                count += 1
            if y == 0 or y == 2:
                count += 1
            if z == 0 or z == 2:
                count += 1
            cube[x, y, z] = count



print(cube)
```


</details>

## Boolesche Arrays als Masken

Boolesche Arrays werden häufig als Masken eingesetzt, um Elemente in Arrays zu selektieren oder zu manipulieren. Sie ermöglichen es, gezielt auf Elemente zuzugreifen, diese zu ändern oder spezifische Operationen darauf basierend auf definierten Bedingungen auszuführen. Diese Technik ermöglicht eine effiziente Auswahl von Elementen, die bestimmte Kriterien erfüllen, ohne die Struktur des ursprünglichen Arrays zu verändern.

Wendet man ein Boolesches Array auf ein Array beliebiger Struktur ("shape") an, ist das Ergebnis immer eindimensional. Dies ist notwendig, da die Anzahl der nach dem Filtern verbleibenden Elemente auch eine Primzahl sein könnte.

### Code-Beispiel:
```python
arr = np.arange(6).reshape(3,2)
arr_bool = arr % 3 == 1

print(arr)
print()
print(arr_bool)
print()
print(arr[arr_bool])
```
    [[0 1]
    [2 3]
    [4 5]]

    [[False  True]
    [False False]
    [ True False]]

    [1 4]

Möchte man jedoch ein Array mit der ursprünglichen Struktur erstellen, in dem die unveränderten Elemente erhalten bleiben, während die herausgefilterten durch einen anderen Wert ersetzt werden, empfiehlt sich die Verwendung der Methode  `.where()`.


```python
print(np.where(arr_bool, arr, -9))
```
    [[-9  1]
    [-9 -9]
    [ 4 -9]]



### Aufgabe 5 🌶️: 
Stellen Sie sich vor, Sie haben ein 2D-Array, das Temperaturmessungen einer Stadt über eine Woche hinweg darstellt. Jede Zeile des Arrays repräsentiert die Temperaturen eines Tages, unterteilt in Stunden.

```python
import numpy as np

# Simulierte Temperaturdaten (in °C) für 7 Tage, 24 Stunden pro Tag
temperaturen = np.array([
    [18, 17, 16, 15, 14, 14, 14, 16, 20, 24, 27, 29, 30, 32, 33, 32, 31, 29, 25, 22, 21, 20, 19, 18],
    [19, 18, 17, 16, 15, 15, 15, 17, 21, 25, 28, 30, 31, 33, 34, 33, 32, 30, 26, 23, 22, 21, 20, 19],
    [20, 19, 18, 17, 16, 16, 16, 18, 22, 26, 29, 31, 32, 34, 35, 34, 33, 31, 27, 24, 23, 22, 21, 20],
    [21, 20, 19, 18, 17, 17, 17, 19, 23, 27, 30, 32, 33, 35, 36, 35, 34, 32, 28, 25, 24, 23, 22, 21],
    [22, 21, 20, 19, 18, 18, 18, 20, 24, 28, 31, 33, 34, 36, 37, 36, 35, 33, 29, 26, 25, 24, 23, 22],
    [23, 22, 21, 20, 19, 19, 19, 21, 25, 29, 32, 34, 35, 37, 38, 37, 36, 34, 30, 27, 26, 25, 24, 23],
    [24, 23, 22, 21, 20, 20, 20, 22, 26, 30, 33, 35, 36, 38, 39, 38, 37, 35, 31, 28, 27, 26, 25, 24]
])
```

a. Erstellen Sie ein Boolesches Array, das alle Zeitpunkte identifiziert, an denen die Temperatur über 34°C liegt.

b. Erstellen Sie ein neues Array, in dem Temperaturen über 34°C durch den Wert 35 ersetzt werden.

c. Extrahieren Sie ein weiteres Array, das ausschließlich die Werte über 34°C aus dem ursprünglichen Array enthält.


<details>
<summary>🔍 Lösung anzeigen</summary>

#### Lösung

```python
import numpy as np

# a. Boolesches Array für Temperaturen > 34°C
temp_greater_34 = temperaturen > 34

# b. Array mit ersetzen Werten, wo Temperatur > 34°C
temp_capped = np.where(temp_greater_34, 35, temperaturen)

# c. Array, das nur Werte über 34°C enthält
temp_only_above_34 = temperaturen[temp_greater_34]

# Ausgabe der Ergebnisse
print("Boolesches Array für Temperaturen > 34°C:")
print(temp_greater_34)
print("\nNeues Array mit Temperaturen über 34°C ersetzt durch 35:")
print(temp_capped)
print("\nArray der ursprünglichen Temperaturen über 34°C:")
print(temp_only_above_34)
```


</details>


### Aufgabe 6 🌶️🌶️:

a. Erstelle ein 5x5 Array A mit Zufallszahlen zwischen -100 und 100.

b. Gib alle Werte zurück, die positiv sind.

c. Gib alle Werte zurück, die zwischen -20 und 20 liegen.

d. Gib alle Indizes zurück wo die Werte von A entweder kleiner als 50 oder größer als 80 sind.
- Wie viele sind es?
- In welcher Form liegt die Indizemaske vor?

e. Erstelle selbst eine Indizemaske, die alle Indizes des 3x3 quadrats in der Mitte einer 5x5 Matrix enthält.
- Wende sie auf A an.
- Setze alle Werte in diesem Quadrat innerhalb von A auf 0



<details>
<summary>🔍 Lösung anzeigen</summary>

```python
import numpy as np

# a) Erstelle ein 5x5 Array A mit Zufallszahlen zwischen -100 und 100
np.random.seed(0)  # Für Reproduzierbarkeit der Zufallszahlen
A = np.random.randint(-100, 101, size=(5, 5))
print("Array A:")
print(A)

# b) Gib alle Werte zurück, die positiv sind
positiv = A[A > 0]
print("Positive Werte in A:")
print(positiv)

# c) Gib alle Werte zurück, die zwischen -20 und 20 liegen
zwischen_20 = A[(A >= -20) & (A <= 20)]
print("Werte in A zwischen -20 und 20:")
print(zwischen_20)

# d) Gib alle Indizes zurück, wo die Werte von A entweder kleiner als 50 oder größer als 80 sind
indizes = np.where((A < 50) | (A > 80))
print("Indizes, wo Werte in A kleiner als 50 oder größer als 80 sind:")
print(indizes)
print("Anzahl der betroffenen Indizes:", len(indizes[0]))

# e) Erstelle selbst eine Indizemaske für das 3x3 Quadrat in der Mitte einer 5x5 Matrix und setze diese Werte auf 0
meshy = np.array(np.meshgrid(np.arange(1,4), np.arange(1,4))) # meshgrid für das mittlere 3x3 Quadrat einer 5x5 matrix

meshy.resize(2,9)
mask = tuple(meshy)

print("Indizemaske für das 3x3 Quadrat in der Mitte:")
print(mask)

A[mask] = 0  # Setze alle Werte im 3x3 Quadrat auf 0
print("Matrix A nach Setzen der Werte im 3x3 Quadrat auf 0:")
print(A)

```

</details>