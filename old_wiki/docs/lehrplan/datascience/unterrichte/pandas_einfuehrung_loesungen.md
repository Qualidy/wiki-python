# Lösungen zu: Pandas Einführung


```python
import pandas as pd
```

## A1

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ThAGVYN1xa8?si=XXLka7hPyjkb5Ugj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
data = {'Spalte1': [1, 2, 3, 4],
        'Spalte2': ['a', 'b', 'c', 'd'],
        'Spalte3': [True, False, True, False]}
df = pd.DataFrame(data)
print(df)
```

       Spalte1 Spalte2  Spalte3
    0        1       a     True
    1        2       b    False
    2        3       c     True
    3        4       d    False


## A2

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/gYA7zDyB8t8?si=GXsOnD6uK9ow7pU2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
ser = pd.Series([10, 20, 30, 40, 50])
print(ser)
```

    0    10
    1    20
    2    30
    3    40
    4    50
    dtype: int64


## A3

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/zzIkoYRrxy8?si=zLBDCH12A1LxJkmc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
element = df.iloc[2, 1] # Drittes Element der zweiten Spalte
print(element)
```

    c


## A4

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/GmiFX3PzLcs?si=llVpdAiR9DLZZUHw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
zeile = df.loc[0] # Erste Zeile
print(zeile)
```

    Spalte1       1
    Spalte2       a
    Spalte3    True
    Name: 0, dtype: object


## A5

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/4kDDV7wPSvY?si=sF52dCxk_oJtiDqN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
spalte = df.iloc[:, 1] # Zweite Spalte
print(spalte)
```

    0    a
    1    b
    2    c
    3    d
    Name: Spalte2, dtype: object


## A6

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/LhWH5lCD3cA?si=EAnYOm0nVexPsLNr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
df_indexed = pd.DataFrame(data, index=['i1', 'i2', 'i3', 'i4'])
print(df_indexed)
```

        Spalte1 Spalte2  Spalte3
    i1        1       a     True
    i2        2       b    False
    i3        3       c     True
    i4        4       d    False


## A7

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/B-1NU_Tx5H8?si=VexzC9GAiFyYrqed" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
df.columns = ['NeueSpalte1', 'NeueSpalte2', 'NeueSpalte3']
print(df)
```

       NeueSpalte1 NeueSpalte2  NeueSpalte3
    0            1           a         True
    1            2           b        False
    2            3           c         True
    3            4           d        False


## A8

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/3byVCDN8XAI?si=h_MzuuB3iReyMxtk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
import pandas as pd

data = {'Spalte1': [1, 2, 3, 4],
        'Spalte2': ['a', 'b', 'c', 'd'],
        'Spalte3': [True, False, True, False]}
df = pd.DataFrame(data)
print("Vorher:")
print(df)

neue_zeile = pd.DataFrame({'Spalte1': [5], 'Spalte2': ['e'], 'Spalte3': [True]})
df = pd.concat([df, neue_zeile], ignore_index=True)

print("\nNachher:")
print(df)
```

    Vorher:
       Spalte1 Spalte2  Spalte3
    0        1       a     True
    1        2       b    False
    2        3       c     True
    3        4       d    False
    
    Nachher:
       Spalte1 Spalte2  Spalte3
    0        1       a     True
    1        2       b    False
    2        3       c     True
    3        4       d    False
    4        5       e     True



```python
pd.Series(neue_zeile)
```




    Spalte1       5
    Spalte2       e
    Spalte3    True
    dtype: object



## A9

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Xk7TriqGo1Y?si=LWhCt-jW-KbC-KAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
data = {'Spalte1': [1, 2, 3, 4],
        'Spalte2': ['a', 'b', 'c', 'd'],
        'Spalte3': [True, False, True, False]}
df = pd.DataFrame(data)

df['Spalte4'] = df['Spalte1'] * 2
print(df)
```

       Spalte1 Spalte2  Spalte3  Spalte4
    0        1       a     True        2
    1        2       b    False        4
    2        3       c     True        6
    3        4       d    False        8


## A10

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/eK5KwMaAl6k?si=KyprGb6Q-Gp0CcpS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>



```python
df = df.drop(columns=['Spalte2'])
print(df)
```

       Spalte1  Spalte3  Spalte4
    0        1     True        2
    1        2    False        4
    2        3     True        6
    3        4    False        8

