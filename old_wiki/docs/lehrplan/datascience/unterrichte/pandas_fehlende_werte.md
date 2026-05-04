# Pandas: Umgang mit fehlenden Daten in Tabellen mit Pandas

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/kWOgUzCRFHU?si=ahSWXNBVHLQR5PeC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [20min]

In der Welt der Datenanalyse und des maschinellen Lernens ist der Umgang mit fehlenden Daten ein häufiges und herausforderndes Problem. Daten können aus vielen Gründen unvollständig sein, wie z.B. durch Fehler bei der Datenerfassung, fehlende Einträge in den Quelldaten oder durch die Art der Datensammlung selbst. Die Python-Bibliothek Pandas bietet uns hier viele Hilfestellungen für die Handhabung solcher unvollständigen Datensätze.

## Erkennung fehlender Daten

Der erste Schritt im Umgang mit fehlenden Daten ist ihre Identifizierung. In Pandas werden fehlende Daten typischerweise als `NaN` (Not a Number) oder `None` dargestellt. Die Methoden `isna()` oder `isnull()` können verwendet werden, um eine boolesche Maske zu erstellen, die angibt, wo in einem DataFrame oder einer Series fehlende Werte vorliegen. Dies ist ein entscheidender Schritt, da das Verständnis des Ausmaßes und der Verteilung fehlender Daten die Strategie für deren Behandlung beeinflussen kann.


## Entfernung vs. Imputation

Nach der Identifizierung gibt es im Wesentlichen zwei Wege, mit fehlenden Daten umzugehen: Entfernen oder Imputation (Einfügen von Werten). Die Entfernung ist der einfachste Ansatz und beinhaltet das Entfernen von Zeilen oder Spalten, die fehlende Daten enthalten. Dies kann mit den Methoden `dropna()` erreicht werden. Allerdings kann dieser Ansatz zu einem signifikanten Datenverlust führen, insbesondere wenn die Menge der fehlenden Daten groß ist.

Die Imputation hingegen versucht, fehlende Werte durch Schätzungen zu ersetzen. Dies kann durch verschiedene Strategien erreicht werden, wie z.B. das Ersetzen durch den Mittelwert, den Median oder den häufigsten Wert einer Spalte. Fortgeschrittenere Techniken beinhalten das Modellieren der fehlenden Daten anhand anderer Merkmale im Datensatz. Pandas bietet einfache Funktionen wie `fillna()` zur Durchführung grundlegender Imputationen.

## Berücksichtigung des Kontexts

Die Entscheidung zwischen Entfernung und Imputation sollte nicht leichtfertig getroffen werden. Es ist wichtig, den Kontext der Daten und die spezifischen Anforderungen der Analyse zu berücksichtigen. In einigen Fällen kann die Imputation zu verzerrten Ergebnissen führen, insbesondere wenn die Annahmen, die der Imputationsmethode zugrunde liegen, nicht zutreffen.

## Vorbeugende Maßnahmen

Neben der direkten Behandlung fehlender Daten ist es ebenfalls wichtig, präventive Strategien zu entwickeln, um die Häufigkeit fehlender Daten zu minimieren. Dies kann durch die Verbesserung der Datenerfassungsmethoden, die Validierung von Dateneingaben und die Schulung derjenigen, die mit der Datenerfassung betraut sind, erreicht werden.

## Codebeispiele [30min]

### Beispiel 1: Erkennen von fehlenden Daten


```python
import pandas as pd
import numpy as np

# Erstellen eines Beispiel-DataFrames
df = pd.DataFrame({'A': [1, np.nan, 3],
                   'B': [4, 5, 6],
                   'C': [np.nan, np.nan, 9]})
# Erkennen von fehlenden Daten
print(df)
print(df.isnull())
```

         A  B    C
    0  1.0  4  NaN
    1  NaN  5  NaN
    2  3.0  6  9.0
           A      B      C
    0  False  False   True
    1   True  False   True
    2  False  False  False


### Beispiel 2: Entfernen von Zeilen/Spalten mit fehlenden Daten


```python
# Entfernen aller Zeilen mit mindestens einem fehlenden Wert
print(df.dropna())
```

         A  B    C
    2  3.0  6  9.0



```python
# Entfernen aller Spalten mit mindestens einem fehlenden Wert
print( df.dropna(axis=1) )
```

       B
    0  4
    1  5
    2  6


### Beispiel 3: Füllen von fehlenden Daten mit einem festen Wert


```python
# Füllen aller fehlenden Werte mit 0
df.fillna(0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>6</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



### Beispiel 4: Imputation von fehlenden Daten mit dem Mittelwert/Median


```python
# Mittelwert-Imputation
print(df)
print(df.fillna(df.mean()))
```

         A  B    C
    0  1.0  4  NaN
    1  NaN  5  NaN
    2  3.0  6  9.0
         A  B    C
    0  1.0  4  9.0
    1  2.0  5  9.0
    2  3.0  6  9.0



```python
# Median-Imputation
print(df.fillna(df.median()))
```

         A  B    C
    0  1.0  4  9.0
    1  2.0  5  9.0
    2  3.0  6  9.0


## Aufgaben [90min]

### A1: Anzahl fehlender Werte 🌶️🌶️

Identifizieren Sie die Anzahl der fehlenden Werte in jeder Spalte des DataFrame df.


```python
df = pd.DataFrame({'A': [1, np.nan, 3],
                   'B': [4, 5, 6],
                   'C': [np.nan, np.nan, 9]})
```

### A2: Schalter `thresh` von `dropna()` 🌶️🌶️

Finden Sie heraus was der Schalter `thresh` von `dropna()` macht!

### A3: Füllen einer Spalte 🌶️

Füllen Sie die fehlenden Werte in der Spalte 'A' mit dem Mittelwert dieser Spalte.


```python
df = pd.DataFrame({'A': [1, 4,      7,      np.nan],
                   'B': [2, 5,      np.nan, np.nan],
                   'C': [3, np.nan, np.nan, np.nan]})
print(df)
```

         A    B    C
    0  1.0  2.0  3.0
    1  4.0  5.0  NaN
    2  7.0  NaN  NaN
    3  NaN  NaN  NaN


### A4: Neue Spalte mit Median 🌶️

Erstellen Sie eine neue Spalte 'D', die den Median der Spalten 'A', 'B' und 'C' für jede Zeile enthält.


```python
df = pd.DataFrame({'A': [1, 4,      7,      np.nan],
                   'B': [2, 5,      np.nan, np.nan],
                   'C': [3, np.nan, np.nan, np.nan]})
print(df)
```

         A    B    C
    0  1.0  2.0  3.0
    1  4.0  5.0  NaN
    2  7.0  NaN  NaN
    3  NaN  NaN  NaN


### A5: Tabelle mit Lücken erzeugen, fehlende Werte auf 0 setzen 🌶️

Erstellen Sie einen neuen DataFrame df2 mit den Spalten 'X', 'Y', und 'Z', der zufällige Werte und einige fehlende Werte (NaN) enthält. Verwenden Sie dann die Methode `fillna()` um alle fehlenden Werte mit dem Wert 0 zu ersetzen.

### A6: Fehlende Werte durch Durchschnittswerte ersetzen 🌶️

Ersetzen Sie in df2 die fehlenden Werte in der Spalte 'Y' durch den Durchschnitt der vorhandenen Werte in dieser Spalte.


```python
np.random.seed(0)
df2 = pd.DataFrame(np.random.randn(5, 3), columns=['X', 'Y', 'Z'])
print("\nOhne Lücken:\n", df2)

df2.iloc[1:3, 1] = np.nan
df2.iloc[2:4, 2] = np.nan
print("\nMit Lücken:\n", df2)
```

    
    Ohne Lücken:
               X         Y         Z
    0  1.764052  0.400157  0.978738
    1  2.240893  1.867558 -0.977278
    2  0.950088 -0.151357 -0.103219
    3  0.410599  0.144044  1.454274
    4  0.761038  0.121675  0.443863
    
    Mit Lücken:
               X         Y         Z
    0  1.764052  0.400157  0.978738
    1  2.240893       NaN -0.977278
    2  0.950088       NaN       NaN
    3  0.410599  0.144044       NaN
    4  0.761038  0.121675  0.443863


### A7: Interpolation fehlender Werte 🌶️

Verwenden Sie die Methode `interpolate()` von Pandas, um die fehlenden Werte in folgender Tabelle linear zu interpolieren.


```python
df = pd.DataFrame({'A': [1, np.nan, 3, 4],
                   'B': [10,20,np.nan,40],
                   'C': [100,200,300,np.nan]})
print(df)
```

         A     B      C
    0  1.0  10.0  100.0
    1  NaN  20.0  200.0
    2  3.0   NaN  300.0
    3  4.0  40.0    NaN


[Lösungen](pandas_fehlende_werte_loesungen.md)
