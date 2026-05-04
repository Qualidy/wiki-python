# Pandas für Datenimport und -export

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/B4b6tNP5_rE?si=rDhJMQ_Os-EayskJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung

Pandas ist eine leistungsstarke Python-Bibliothek, die für die Datenmanipulation und -analyse verwendet wird. Sie bietet speziell für den Import und Export von Daten eine Vielzahl an Funktionen, die das Arbeiten mit verschiedenen Datenformaten wie CSV, Excel, JSON, HTML und SQL-Datenbanken erleichtern.

## Lesen von CSV-Dateien

Eine der häufigsten Aufgaben beim Arbeiten mit Daten ist das Lesen von CSV-Dateien. Pandas macht dies mit der `read_csv()`-Funktion sehr einfach. Diese Funktion ist sehr flexibel und kann so angepasst werden, dass sie mit verschiedenen Trennzeichen, Kopfzeilen und Datentypen umgehen kann.

## Arbeiten mit Excel-Dateien

Für den Umgang mit Excel-Dateien bietet Pandas die `read_excel()`-Funktion. Diese Funktion ermöglicht es, Daten aus verschiedenen Blättern einer Excel-Datei zu lesen. Nutzer können spezifische Blätter auswählen und verschiedene Leseoptionen nutzen, um mit komplexen Excel-Dateien zu arbeiten.

## Import aus anderen Datenformaten

Pandas unterstützt auch das Lesen von anderen Datenformaten wie JSON, HTML und SQL-Datenbanken. Mit Funktionen wie `read_json()`, `read_html()` und `read_sql()` können Daten aus diesen Quellen einfach in Pandas-DataFrames importiert werden.

## Export in CSV-Dateien

Der Export von Daten in eine CSV-Datei ist mit der `to_csv()`-Methode eines DataFrame möglich. Diese Methode bietet ähnliche Flexibilität wie `read_csv()` und ermöglicht es, die Ausgabe nach Bedarf anzupassen.

## Speichern in Excel-Dateien

Um Daten in eine Excel-Datei zu exportieren, verwendet Pandas die `to_excel()`-Methode. Diese Methode erlaubt es, Daten in verschiedenen Blättern einer Excel-Datei zu speichern und die Formatierung anzupassen.

## Export in andere Formate

Ähnlich dem Import können Daten auch in Formaten wie JSON und SQL mit Methoden wie `to_json()` und `to_sql()` exportiert werden. Diese Methoden erleichtern die Integration von Pandas mit verschiedenen Datenquellen und -senken.

## Codebeispiele [20 min]

### Beispiel 1: Erstellen und Speichern einer CSV-Datei


```python
import pandas as pd
import numpy as np

# Erstellen eines DataFrame mit Zeitreihendaten
df = pd.DataFrame({
    'Datum': pd.date_range(start='2024-01-01', periods=31, freq='D'),
    'Messwert1': np.random.rand(31),
    'Messwert2': np.random.rand(31)
})
df.to_csv('zeitreihen.csv', index=False)
```

### Beispiel 2: Einlesen einer CSV-Datei


```python
df = pd.read_csv('zeitreihen.csv')
print(df)
```

             Datum  Messwert1  Messwert2
    0   2024-01-01   0.715180   0.487749
    1   2024-01-02   0.646316   0.251084
    2   2024-01-03   0.235191   0.267994
    3   2024-01-04   0.192810   0.138762
    4   2024-01-05   0.009358   0.370230
    5   2024-01-06   0.136815   0.254064
    6   2024-01-07   0.509401   0.879261
    7   2024-01-08   0.145421   0.544888
    8   2024-01-09   0.396517   0.212509
    9   2024-01-10   0.226344   0.413564
    10  2024-01-11   0.483345   0.711298
    11  2024-01-12   0.877620   0.302727
    12  2024-01-13   0.136273   0.270860
    13  2024-01-14   0.888815   0.941224
    14  2024-01-15   0.829374   0.672944
    15  2024-01-16   0.276770   0.703538
    16  2024-01-17   0.360558   0.031292
    17  2024-01-18   0.787631   0.987252
    18  2024-01-19   0.875882   0.484241
    19  2024-01-20   0.610185   0.252592
    20  2024-01-21   0.924740   0.611627
    21  2024-01-22   0.658885   0.457653
    22  2024-01-23   0.397643   0.755502
    23  2024-01-24   0.385756   0.134460
    24  2024-01-25   0.938252   0.972657
    25  2024-01-26   0.137411   0.676173
    26  2024-01-27   0.445229   0.452930
    27  2024-01-28   0.823604   0.303145
    28  2024-01-29   0.852368   0.983327
    29  2024-01-30   0.624762   0.262466
    30  2024-01-31   0.960239   0.724496


### Beispiel 3: Exportieren nach Excel


```python
df.to_excel('zeitreihen.xlsx', index=False)
```

Hinweis: hier ist es wichtig, dass du das `openpyxl` Modul installierst, damit du mit Excel-Dateien arbeiten kannst, sondern erhälst du eine Fehlermeldung:

    ModuleNotFoundError: No module named 'openpyxl'

Installiere das `openpyxl` Modul einfach mit:


```python
!pip install openpyxl
```

    Requirement already satisfied: openpyxl in /home/juebrauer/miniconda3/envs/env_qualidy/lib/python3.11/site-packages (3.1.2)
    Requirement already satisfied: et-xmlfile in /home/juebrauer/miniconda3/envs/env_qualidy/lib/python3.11/site-packages (from openpyxl) (1.1.0)


### Beispiel 4: Exportieren nach JSON


```python
df.to_json('zeitreihen.json', orient='records', lines=True)
```

### Beispiel 5: Exportieren nach HTML


```python
df.to_html('zeitreihen.html')
```

## Aufgaben [90min]

### A1: Selektives Lesen von Spalten 🌶️

Lese eine Tabelle aus einer `.csv`-Datei ein. Lese dabei aber nur bestimmte Spalten ein, d.h. nicht alle!

### A2: Erzeugen eines Python Dictionaries aus einer Tabelle? 🌶️🌶️

Wie kannst du eine Pandas Tabelle in Python Dictionary umwandeln?

### A3: Speichern einer Tabelle als Pickle-Datei 🌶️

Wie kann man eine Tabelle in eine Pickle-Datei serialisieren (=wegschreiben)?

### A4: Laden einer Tabelle aus einer Pickle-Datei 🌶️

Wie kann man dann eine Tabelle aus einer Pickle-Datei wieder einlesen?

### A5: Exportieren einer Tabelle in eine SQLite-Datenbank 🌶️🌶️🌶️

Wie kannst du eine Tabelle in eine SQLite-Datenbank schreiben?

### A6: Einlesen einer Tabelle aus einer SQLite-Datenbank 🌶️🌶️

Wie kannst du die Tabelle dann wieder aus der SQLite-Datenbank einlesen?

### A7: Einlesen einer .csv-Datei mit anderem Separator 🌶️

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



[Lösungen](pandas_import_export_loesungen.md)
