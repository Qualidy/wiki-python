# NumPy: Slicing von Arrays

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/oQnyM0iszDU?si=BOITXoB3MeDnmtXw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [15min]

In der Welt der Datenverarbeitung und wissenschaftlichen Berechnungen ist NumPy eine unverzichtbare Bibliothek im Python-Ökosystem. Ein Kernkonzept von NumPy ist das 'Slicing' (Zuschneiden) von Arrays, eine Technik, die es ermöglicht, effizient auf Teile eines Arrays zuzugreifen und diese zu manipulieren.


## Grundlagen des Slicings

Das Slicing in NumPy ist eine Methode, um auf eine Untergruppe von Daten innerhalb eines Arrays zuzugreifen. Ein Array in NumPy ist eine Sammlung von Elementen, meist Zahlen, die in einer strukturierten Form wie einem Vektor (eindimensionales Array) oder einer Matrix (mehrdimensionales Array) angeordnet sind. Das Slicing ermöglicht es, bestimmte Bereiche dieses Arrays auszuwählen, sei es eine einzelne Spalte, eine Reihe oder sogar einen komplexeren Teilbereich.


## Syntax und Konzepte

Die Syntax für das Slicing in NumPy ist intuitiv und flexibel. Sie basiert auf der Verwendung von Indizes und dem Doppelpunkt-Symbol (:), um Bereiche anzugeben. Die grundlegende Idee ist, Start- und Endpunkte sowie Schrittweiten für das Slicing anzugeben. Diese Methode erweist sich als äußerst mächtig, da sie eine hohe Präzision bei der Auswahl von Daten ermöglicht.

## Anwendungsbereiche

Das Slicing von NumPy-Arrays ist in vielen Bereichen der Datenverarbeitung und Analyse von entscheidender Bedeutung. Zum Beispiel in der Bildverarbeitung, wo Teile eines Bildes (repräsentiert als Array von Pixelwerten) bearbeitet werden müssen, in der Signalverarbeitung, wo bestimmte Zeitabschnitte eines Signals analysiert werden, oder in der statistischen Datenanalyse, wo Teilmengen von Datensätzen für Berechnungen ausgewählt werden.

## Fortgeschrittene Techniken

Neben den grundlegenden Slicing-Operationen bietet NumPy auch fortgeschrittene Techniken, wie das bedingte Slicing, bei dem Elemente basierend auf bestimmten Bedingungen ausgewählt werden, oder das Slicing mit Schrittweiten, das eine effiziente Art der Datenabtastung ermöglicht. Diese fortgeschrittenen Techniken erweitern die Möglichkeiten der Datenmanipulation erheblich und bieten leistungsstarke Werkzeuge für komplexe analytische Aufgaben.


## Best Practices und häufige Fallstricke

Obwohl das Slicing ein mächtiges Werkzeug ist, gibt es auch einige Best Practices und Fallstricke, die beachtet werden sollten. Zum Beispiel ist es wichtig, die Dimensionalität des Arrays beim Slicing zu berücksichtigen, um unerwartete Ergebnisse zu vermeiden. Ebenso sollte man vorsichtig sein, um keine unbeabsichtigten Datenkopien zu erstellen, was die Leistung beeinträchtigen kann.

## Codebeispiele [30 min]

### Beispiel 1: Grundlegendes Slicing eines eindimensionalen Arrays


```python
import numpy as np

# Erstellen eines eindimensionalen Arrays
arr = np.array([1, 2, 3, 4, 5])

# Slicing des Arrays
sliced_arr = arr[1:4]

print(sliced_arr)
```

    [2 3 4]


In diesem Beispiel wird ein eindimensionales NumPy-Array arr erstellt. Dann wird ein Teil des Arrays durch Slicing ausgewählt. `arr[1:4]` wählt die Elemente an den Positionen 1 bis 3 aus (das Element an Position 4 ist nicht inbegriffen), was zu [2, 3, 4] führt.

### Beispiel 2: Slicing mit Schrittweiten


```python
# Erstellen eines eindimensionalen Arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing des Arrays mit einer Schrittweite von 2
sliced_arr = arr[::2]

print(sliced_arr)
```

    [1 3 5 7 9]


Hier wird ein eindimensionales Array arr erstellt und dann mit einer Schrittweite von 2 gesliced. `arr[::2]` wählt jedes zweite Element im Array aus, beginnend mit dem ersten, was zu [1, 3, 5, 7, 9] führt.

### Beispiel 3: Slicing von mehrdimensionalen Arrays


```python
# Erstellen eines zweidimensionalen Arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# Slicing, um die erste Zeile zu wählen
first_row = arr[0, :]

# Slicing, um die erste Spalte zu wählen
first_column = arr[:, 0]

print("Erste Zeile:", first_row)
print("Erste Spalte:", first_column)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Erste Zeile: [1 2 3]
    Erste Spalte: [1 4 7]


In diesem Beispiel wird ein zweidimensionales Array arr erstellt. Durch `arr[0, :]` wird die erste Zeile des Arrays ausgewählt und durch `arr[:, 0]` die erste Spalte. Die Ausgabe ist die erste Zeile [1, 2, 3] und die erste Spalte [1, 4, 7].

### Beispiel 4: Slicing mit negativen Indizes


```python
# Erstellen eines eindimensionalen Arrays
arr = np.array([1, 2, 3, 4, 5])

# Slicing unter Verwendung negativer Indizes
sliced_arr = arr[-3:]

print(sliced_arr)
```

    [3 4 5]


Wir "slicen" hier die letzten 3 Werte aus dem Array heraus.

### Beispiel 5: Slicing mit Bedingungen


```python
# Erstellen eines eindimensionalen Arrays
arr = np.array([1, 2, 3, 4, 5])

# Bedingtes Slicing
sliced_arr = arr[arr > 3]

print(sliced_arr)
```

    [4 5]


In diesem Beispiel wird ein Array `arr` erstellt und dann eine bedingte Slicing-Operation angewendet. `arr[arr > 3]` wählt alle Elemente aus, die größer als 3 sind. Das Ergebnis ist [4, 5].

## Aufgaben [120 min]

### A1: Wozu eigentlich Slicing? 🌶️

Überlegen Sie sich Beispiele: Wo braucht man Slicing bei der Datenverarbeitung bzw. Datenanalyse?

### A2: Grundlegendes Slicing 🌶️

Erstellen Sie ein eindimensionales NumPy-Array mit den Zahlen von 1 bis 10 und wählen Sie die Elemente von Index 3 bis 7 aus.

### A3: Slicing mit negativen Indizes 🌶️🌶️

Erstellen Sie ein Array mit den Zahlen von -5 bis 5 und wählen Sie die letzten drei und die ersten drei Elemente *nur* mithilfe negativer Indizes aus.

### A4: Slicing mit Schrittweiten 🌶️

Erstellen Sie ein Array von 1 bis 10 und slicen Sie das 2,4,6,... Element heraus!

### A5: Reverse Slicing 🌶️🌶️

Erstellen Sie ein Array mit den Zahlen von 1 bis 10 und kehren Sie die Reihenfolge der Elemente durch Slicing um.

### A6: Slicing von zweidimensionalen Arrays 🌶️

Erstellen Sie ein 3x3-Array mit den Zahlen von 1 bis 9 und wählen Sie die zweite Zeile aus.

### A7: Slicing von Spalten 🌶️

Erstellen Sie ein 4x4-Array mit beliebigen Zahlen und wählen Sie die dritte Spalte aus.

### A8: Slicing mit Bedingungen 🌶️🌶️

Erstellen Sie ein Array mit den Zahlen von -10 bis 10 und wählen Sie alle Elemente aus, die größer als 5 oder kleiner als -3 sind.

### A9: Diagonales Slicing 🌶️🌶️

Erstellen Sie ein 3x3-Array mit den Zahlen von 1 bis 9 und wählen Sie die Elemente der Diagonale aus.

### A10: Slicing von Submatrizen 🌶️🌶️

Erstellen Sie ein 4x4-Array und wählen Sie eine 2x2-Submatrix aus der oberen linken Ecke des Arrays aus.

### A11: Komplexes Slicing 🌶️🌶️🌶️

Erstellen Sie ein 5x5-Array mit den Zahlen von 1 bis 25 und wählen Sie jede zweite Zeile und Spalte aus.

[Lösungen](numpy_slicing_loesungen.md)
