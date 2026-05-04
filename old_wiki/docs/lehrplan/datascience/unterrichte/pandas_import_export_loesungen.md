# Lösungen


```python
import pandas as pd
```

### A1: Selektives Lesen von Spalten

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/TqFBU2-u1zA?si=zzWmIeoXNmhPL2OZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Lese eine Tabelle aus einer `.csv`-Datei ein. Lese dabei aber nur bestimmte Spalten ein, d.h. nicht alle!


```python
df = pd.read_csv('zeitreihen.csv', usecols=['Datum', 'Messwert1'])
print(df.head())
```

            Datum  Messwert1
    0  2024-01-01   0.774907
    1  2024-01-02   0.842221
    2  2024-01-03   0.297573
    3  2024-01-04   0.370413
    4  2024-01-05   0.073036


### A2: Erzeugen eines Python Dictionaries aus einer Tabelle?

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/AL-YkLWAFYs?si=AZXEGA8oNoApvCmS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Wie kannst du eine Pandas Tabelle in Python Dictionary umwandeln?


```python
daten_dict = df.to_dict(orient='list')
for key in daten_dict:
    print(key, "-->", daten_dict[key][:5])
```

    Datum --> ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
    Messwert1 --> [0.7749073594227915, 0.8422206112926868, 0.2975732189267037, 0.3704128537768418, 0.0730363259149011]


### A3: Speichern einer Tabelle als Pickle-Datei

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/QuBJZ6TuRGw?si=7Wm15yKdK5XZrg82" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Wie kann man eine Tabelle in eine Pickle-Datei serialisieren (=wegschreiben)?


```python
df.to_pickle('zeitreihen.pkl')
```

### A4: Laden einer Tabelle aus einerPickle-Datei

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/gKXs2BPY72I?si=QDRsWvqFKegc1bwJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Wie kann man dann eine Tabelle aus einer Pickle-Datei wieder einlesen?


```python
df = pd.read_pickle('zeitreihen.pkl')
print(df.head())
```

            Datum  Messwert1
    0  2024-01-01   0.774907
    1  2024-01-02   0.842221
    2  2024-01-03   0.297573
    3  2024-01-04   0.370413
    4  2024-01-05   0.073036


### A5: Exportieren einer Tabelle in eine SQLite-Datenbank

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/JZkgruA77jg?si=uPeoJX_b4u_kdutc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Wie kannst du eine Tabelle in eine SQLite-Datenbank schreiben?


```python
import sqlite3
import numpy as np

df = pd.DataFrame({
    'Datum': pd.date_range(start='2024-01-01', periods=31, freq='D'),
    'Messwert1': np.random.rand(31),
    'Messwert2': np.random.rand(31)
})

# Erstelle bzw. öffne eine SQLite-Datenbank
conn = sqlite3.connect('zeitreihen.db')

# Speichern des DataFrames in der SQLite-Datenbank
df.to_sql('zeitreihen', conn, if_exists='replace', index=False)

# Schließen der Verbindung zur Datenbank
conn.close()
```

Um deine Pandas-Tabelle in einer SQLite-Datenbank zu speichern, kannst du die Methode `to_sql()` von Pandas verwenden. Diese Methode ermöglicht es dir, einen DataFrame direkt in eine SQL-Datenbank zu schreiben. SQLite ist eine leichte, dateibasierte Datenbank, die keine separate Server-Installation erfordert, und eignet sich daher gut für kleinere Datenmengen und schnelle Anwendungen.

Der Parameter `if_exists='replace'` gibt an, dass die Tabelle überschrieben wird, falls sie bereits existiert. Der Parameter `index=False` verhindert, dass der DataFrame-Index als separate Spalte gespeichert wird.

### A6: Einlesen einer Tabelle aus einer SQLite-Datenbank

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/B-SKppkooFk?si=-1zZ_er0stlzHMp6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Wie kannst du die Tabelle dann wieder aus der SQLite-Datenbank einlesen?


```python
# Öffnen der Verbindung zur SQLite-Datenbank
conn = sqlite3.connect('zeitreihen.db')

# Einlesen der Tabelle mit SQL-Statement
df = pd.read_sql_query("SELECT * FROM zeitreihen", conn)

# Schließen der Verbindung zur Datenbank
conn.close()

# Anzeigen des "Kopfes" (ersten 5 Zeilen )des DataFrames
print(df.head())
```

                     Datum  Messwert1  Messwert2
    0  2024-01-01 00:00:00   0.450164   0.254697
    1  2024-01-02 00:00:00   0.110965   0.062751
    2  2024-01-03 00:00:00   0.254469   0.300646
    3  2024-01-04 00:00:00   0.635955   0.355277
    4  2024-01-05 00:00:00   0.337468   0.949891


### A7: Einlesen einer .csv-Datei mit anderem Separator

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/CYbAYlBnNy8?si=Mk7oBGRVKlHKkdKC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Führe folgenden Code aus, um eine `.csv-Datei` zu erzeugen.

Dann: Wie kann man diese weggeschriebene Tabelle mit Pandas wieder einlesen?


```python
data = {
    'Spalte1': [1, 2, 3, 4, 5],
    'Spalte2': ['A', 'B', 'C', 'D', 'E'],
    'Spalte3': [0.1, 0.2, 0.3, 0.4, 0.5]
}
df = pd.DataFrame(data)
file_path = 'beispiel.csv'
df.to_csv(file_path, sep=';', index=False)
```

Der folgende Befehl funktioniert nämlich nicht!


```python
pd.read_csv(file_path)
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
      <th>Spalte1;Spalte2;Spalte3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1;A;0.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2;B;0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3;C;0.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4;D;0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5;E;0.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv(file_path, sep=";")
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
      <th>Spalte1</th>
      <th>Spalte2</th>
      <th>Spalte3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>B</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>C</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>D</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>E</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</div>


