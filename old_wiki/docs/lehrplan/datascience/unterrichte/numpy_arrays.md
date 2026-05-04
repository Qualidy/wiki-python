# NumPy: Einführung und NumPy Arrays

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/c-u25uel9d0?si=Ld4LhIGjaH6v1bpb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [15min]

NumPy, ein Akronym für Numerical Python, ist eine wesentliche Bibliothek im Python-Ökosystem und dient als Grundlage für eine Vielzahl von wissenschaftlichen und numerischen Berechnungen. Entwickelt, um komplexe mathematische Operationen zu vereinfachen und zu beschleunigen, hat sich NumPy als unverzichtbares Werkzeug in den Bereichen Datenwissenschaft, Maschinelles Lernen, Ingenieurwesen und wissenschaftliche Forschung etabliert.

## Kernfunktionen von NumPy

Das Herzstück von NumPy ist das `ndarray`-Objekt, ein effizientes, multidimensionales Array, das schnelle Operationen auf großen Datenmengen ermöglicht. Diese Arrays unterscheiden sich von den Standard-Python-Listen durch ihre Fähigkeit, Operationen auf Vektorbasis durchzuführen, was eine bedeutende Beschleunigung gegenüber herkömmlichen Schleifenoperationen bietet.

NumPy bietet auch eine umfangreiche Sammlung von mathematischen Funktionen. Dazu gehören lineare Algebra, statistische Operationen, Fourier-Transformationen und vieles mehr. NumPy arbeitet hierbei eng mit anderen Bibliotheken wie scikit-learn und Pandas zusammen.

## Bedeutung im Bereich Data Science

Im Data Science Bereich hat sich NumPy als unerlässliches Werkzeug etabliert. Es ermöglicht die effiziente Manipulation und Analyse großer Datensätze, ein grundlegender Bestandteil vieler Datenverarbeitungs-Workflows. NumPy-Arrays dienen als Rückgrat für Pandas DataFrames, eine weitere Schlüsselkomponente in der Datenanalyse.

## Integration mit anderen Bibliotheken

NumPy interagiert eng mit anderen wichtigen Python-Bibliotheken. In Kombination mit Bibliotheken wie Matplotlib ermöglicht NumPy die Erstellung anspruchsvoller Datenvisualisierungen. In Verbindung mit maschinellem Lernen und Deep-Learning-Bibliotheken wie TensorFlow und PyTorch ermöglicht NumPy die Durchführung komplexer Berechnungen und Modellierungen.

## Performance-Aspekte

Einer der Hauptvorteile von NumPy ist seine Geschwindigkeit. Durch die Nutzung optimierter C-Bibliotheken bietet NumPy Leistungsverbesserungen, die mit reinem Python nicht zu erreichen sind. Diese Geschwindigkeit ist entscheidend für die Verarbeitung großer Datensätze und die Durchführung zeitintensiver Berechnungen.

## Codebeispiele [30 min]

### Beispiel 1: Erstellen eines einfachen NumPy Arrays


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

    [1 2 3 4 5]


Dieses Beispiel demonstriert das Erstellen eines einfachen eindimensionalen NumPy Arrays. Mit np.array(), einer grundlegenden Funktion von NumPy, wird eine Python-Liste in ein NumPy Array umgewandelt. Das Array arr speichert dann die Zahlen 1 bis 5 und identifiziert aufgrund der Initialisierungswerte auch einen geeigneten Datentyp:


```python
arr.dtype
```




    dtype('int64')



### Beispiel 2: Durchführen von mathematischen Operationen auf einem Array


```python
arr = np.array([1, 2, 3, 4, 5])
arr = arr * 2
print(arr)
```

    [ 2  4  6  8 10]


Hier wird ein Array mit den Zahlen 1 bis 5 erstellt und dann jede Zahl im Array verdoppelt. Die Operation arr * 2 multipliziert jedes Element im Array mit 2. Dies demonstriert die Vektorisierung, bei der Operationen auf jedes Element des Arrays angewendet werden, ohne eine Schleife zu verwenden.

### Beispiel 3: Erzeugen einer 2D-Matrix und Zugriff auf Elemente


```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix[0, 1])
```

    [[1 2 3]
     [4 5 6]]
    2


In diesem Beispiel wird eine 2D-Matrix (ein zweidimensionales Array) erstellt. Der Zugriff auf ein spezifisches Element erfolgt durch Angabe seiner Indizes - hier wird auf das Element in der ersten Zeile und zweiten Spalte zugegriffen (matrix[0, 1]), was den Wert 2 ergibt.

### Beispiel 4: Reshape eines Arrays


```python
arr = np.arange(1, 10)
reshaped_arr = arr.reshape(3, 3)
print(reshaped_arr)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]


Dieses Beispiel zeigt, wie ein eindimensionales Array in eine 3x3-Matrix umgeformt wird. np.arange(1, 10) erzeugt ein Array mit den Zahlen von 1 bis 9. reshape(3, 3) formt dieses Array dann in eine 3x3-Matrix um.

### Beispiel 5: Berechnung von statistischen Kennzahlen


```python
arr = np.array([1, 2, 3, 4, 5])
print("Mittelwert:", np.mean(arr))
print("Standardabweichung:", np.std(arr))
```

    Mittelwert: 3.0
    Standardabweichung: 1.4142135623730951


Hier werden grundlegende statistische Berechnungen auf einem Array durchgeführt. Mit np.mean(arr) wird der Durchschnittswert und mit np.std(arr) die Standardabweichung der Elemente im Array berechnet.

## Aufgaben [90 min]

### A1: Erstellen eines NumPy Arrays 🌶️

Erstellen Sie ein NumPy Array mit den Werten von 10 bis 20.



### A2: Summe der Elemente eines Arrays 🌶️

Berechnen Sie die Summe aller Elemente in einem NumPy Array [8, 4, 6, 0, 2].




### A3: Maximalwert in einem Array finden 🌶️

Bestimmen Sie den größten Wert in dem Array [3, -1, 7, 4, 2]. Wie können wir herausfinden an welcher Stelle dieser Maximalwert steht?





### A4: 2D-Array erstellen 🌶️🌶️

Erstellen Sie ein 2D-Array der Größe 3x3, das die Zahlen von 1 bis 9 enthält.



### A5: Zeilensummen einer Matrix berechnen 🌶️🌶️

Berechnen Sie die Summe jeder Zeile in der Matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].




### A6: Spaltensummen einer Matrix berechnen 🌶️🌶️

Berechnen Sie die Spaltensummen der Matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].




### A7: Elementweise Multiplikation zweier Arrays 🌶️

Multiplizieren Sie die Elemente der Arrays [1, 2, 3] und [4, 5, 6] elementweise.




### A8: Zufälliges Array erzeugen 🌶️🌶️

Erzeugen Sie ein eindimensionales Array mit 5 zufälligen Ganzzahlen zwischen 0 und 10.



### A9: Negative Werte in einem Array 🌶️🌶️🌶️

Ersetzen Sie alle negativen Werte in dem Array [-1, 2, -3, 4, -5] durch 0.




### A10: Transposition einer Matrix 🌶️🌶️

Transponieren Sie die Matrix [[1, 2], [3, 4], [5, 6]].




[Lösungen](numpy_arrays_loesungen.md)

