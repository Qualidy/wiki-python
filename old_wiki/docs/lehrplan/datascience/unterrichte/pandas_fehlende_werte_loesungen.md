# Lösungen


```python
import pandas as pd
import numpy as np
```

### A1: Anzahl fehlender Werte 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/P4wErO73j58?si=UXOIGyyMFuI97Sw4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Identifizieren Sie die Anzahl der fehlenden Werte in jeder Spalte des DataFrame df.


```python
df = pd.DataFrame({'A': [1, np.nan, 3],
                   'B': [4, 5, 6],
                   'C': [np.nan, np.nan, 9]})
```


```python
df.isnull().sum()
```




    A    1
    B    0
    C    2
    dtype: int64




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3 entries, 0 to 2
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   A       2 non-null      float64
     1   B       3 non-null      int64  
     2   C       1 non-null      float64
    dtypes: float64(2), int64(1)
    memory usage: 204.0 bytes


### A2: Schalter `thresh` von `dropna()` 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/39gnj0RNSxw?si=evrQrOEg8iJKG9g-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Finden Sie heraus was der Schalter `thresh` von `dropna()` macht!


```python
df = pd.DataFrame({'A': [1, 4,      7,      np.nan],
                   'B': [2, 5,      np.nan, np.nan],
                   'C': [3, np.nan, np.nan, np.nan]})
print("\ndf:\n", df)

print("\nNormales dropna:\n", df.dropna())

print("\ndropna mit thresh=1:\n", df.dropna(thresh=1))

print("\ndropna mit thresh=2:\n", df.dropna(thresh=2))

print("\ndropna mit thresh=3:\n", df.dropna(thresh=3))
```

    
    df:
          A    B    C
    0  1.0  2.0  3.0
    1  4.0  5.0  NaN
    2  7.0  NaN  NaN
    3  NaN  NaN  NaN
    
    Normales dropna:
          A    B    C
    0  1.0  2.0  3.0
    
    dropna mit thresh=1:
          A    B    C
    0  1.0  2.0  3.0
    1  4.0  5.0  NaN
    2  7.0  NaN  NaN
    
    dropna mit thresh=2:
          A    B    C
    0  1.0  2.0  3.0
    1  4.0  5.0  NaN
    
    dropna mit thresh=3:
          A    B    C
    0  1.0  2.0  3.0


### A3: Füllen einer Spalte 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/lqQh3AyCOBs?si=Myg56Lzs3Np_zMfJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


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



```python
df['A'] = df['A'].fillna(df['A'].mean())
print(df)
```

         A    B    C
    0  1.0  2.0  3.0
    1  4.0  5.0  NaN
    2  7.0  NaN  NaN
    3  4.0  NaN  NaN


### A4: Neue Spalte mit Median 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/7ITAh-FtVcU?si=Zf_WVa5Lpj3vA4Sq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


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



```python
df['D'] = df.median(axis=1)
print(df)
```

         A    B    C    D
    0  1.0  2.0  3.0  2.0
    1  4.0  5.0  NaN  4.5
    2  7.0  NaN  NaN  7.0
    3  NaN  NaN  NaN  NaN


### A5: Tabelle mit Lücken erzeugen, fehlende Werte auf 0 setzen 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vxkyYPYJikM?si=VA-UrOsCOfOudDLW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen neuen DataFrame df2 mit den Spalten 'X', 'Y', und 'Z', der zufällige Werte und einige fehlende Werte (NaN) enthält. Verwenden Sie dann die Methode `fillna()` um alle fehlenden Werte mit dem Wert 0 zu ersetzen.


```python
import numpy as np
import pandas as pd

np.random.seed(0)
df2 = pd.DataFrame(np.random.randn(5, 3), columns=['X', 'Y', 'Z'])
print("\nOhne Lücken:\n", df2)

df2.iloc[1:3, 1] = np.nan
df2.iloc[2:4, 2] = np.nan
print("\nMit Lücken:\n", df2)

df2.fillna(0, inplace=True)
print("\nMit gestopften Lücken:\n", df2)
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
    
    Mit gestopften Lücken:
               X         Y         Z
    0  1.764052  0.400157  0.978738
    1  2.240893  0.000000 -0.977278
    2  0.950088  0.000000  0.000000
    3  0.410599  0.144044  0.000000
    4  0.761038  0.121675  0.443863


### A6: Fehlende Werte durch Durchschnittswerte ersetzen 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/rilyi8I9vd0?si=vhxFknauet7zkzZB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


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



```python
df2['Y'].fillna(df2['Y'].mean(), inplace=True)
print(df2)
```

              X         Y         Z
    0  1.764052  0.400157  0.978738
    1  2.240893  0.221959 -0.977278
    2  0.950088  0.221959       NaN
    3  0.410599  0.144044       NaN
    4  0.761038  0.121675  0.443863


### A7: Interpolation fehlender Werte 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/t1zu9aM2nSs?si=QrGAka57WL8cL9hu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


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



```python
df.interpolate()
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
      <td>10.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>20.0</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>30.0</td>
      <td>300.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>40.0</td>
      <td>300.0</td>
    </tr>
  </tbody>
</table>
</div>



[Lösungen](pandas_fehlende_werte_loesungen.md)


```python

```
