# Lösungen

### A1: Erstellung eines Multiindex DataFrame nach Vorgaben 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/yu7-a0O2nT0?si=j9bfqLYa9r13J2aR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen Pandas DataFrame mit einem Multiindex, der aus zwei Ebenen besteht: 'Stadt' und 'Jahr'. Fügen Sie eine Datenreihe mit dem Namen 'Bevölkerung' hinzu. Verwenden Sie folgende Städte und Jahre: Städte - ['Berlin', 'Hamburg'], Jahre - [2020, 2021].


```python
import pandas as pd

arrays = [['Berlin', 'Berlin', 'Hamburg', 'Hamburg'], [2020, 2021, 2020, 2021]]
index = pd.MultiIndex.from_arrays(arrays, names=('Stadt', 'Jahr'))
df = pd.DataFrame({'Bevölkerung': [3500000, 3550000, 1800000, 1815000]}, index=index)
print(df)
```

                  Bevölkerung
    Stadt   Jahr             
    Berlin  2020      3500000
            2021      3550000
    Hamburg 2020      1800000
            2021      1815000


### A2: Zugriff auf Multiindex Daten 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/PblNyLpd-RI?si=z1yRxIdKwYvBWsV6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Gegeben sei der in Aufgabe 1 erstellte DataFrame. Greifen Sie auf die Daten für 'Berlin' im Jahr 2021 zu.


```python
print(df.loc[('Berlin', 2021)])
```

    Bevölkerung    3550000
    Name: (Berlin, 2021), dtype: int64


### A3: Aggregation auf Multiindex Ebene 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/yiIx8bXIpmQ?si=HPF6dBT1N7U5dkbW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Aggregieren Sie die Bevölkerungsdaten aus Aufgabe 1, um die Gesamtbevölkerung pro Stadt über alle Jahre zu erhalten.

Aggregieren Sie dann die Bevölkerungsdaten aus Aufgabe 1, um die Gesamtbevölkerung pro Jahr über alle Städte zu erhalten.


```python
print(df.groupby(level='Stadt').sum())
```

             Bevölkerung
    Stadt               
    Berlin       7050000
    Hamburg      3615000



```python
print(df.groupby(level='Jahr').sum())
```

          Bevölkerung
    Jahr             
    2020      5300000
    2021      5365000


### A4: Multiindex mit from_product 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/eUy_m9JhIJM?si=jQkhVOpWX13rDdVI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen Multiindex DataFrame mit `pd.MultiIndex.from_product`. Verwenden Sie die Produktkategorien ['Elektronik', 'Lebensmittel'] und die Jahre [2020, 2021] als Index. Fügen Sie eine Spalte 'Umsatz' mit beliebigen Werten hinzu.


```python
kategorien = ['Elektronik', 'Lebensmittel']
jahre = [2020, 2021]
multi_index = pd.MultiIndex.from_product([kategorien, jahre],
                                          names=['Kategorie', 'Jahr'])
df = pd.DataFrame({'Umsatz': [200000, 210000, 150000, 155000]},
                   index=multi_index)
print(df)
```

                       Umsatz
    Kategorie    Jahr        
    Elektronik   2020  200000
                 2021  210000
    Lebensmittel 2020  150000
                 2021  155000


### A5: Sortieren eines Multiindex DataFrame 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/edLfuCux4Cc?si=t_xTfr3VcbvSNbCD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Sortieren Sie den DataFrame aus Aufgabe 4 zuerst nach 'Jahr' und dann nach 'Kategorie'.


```python
print(df)

sortierter_df = df.sort_index(level=['Jahr', 'Kategorie'])
print("\n\n", sortierter_df)
```

                       Umsatz
    Kategorie    Jahr        
    Elektronik   2020  200000
                 2021  210000
    Lebensmittel 2020  150000
                 2021  155000
    
    
                        Umsatz
    Kategorie    Jahr        
    Elektronik   2020  200000
    Lebensmittel 2020  150000
    Elektronik   2021  210000
    Lebensmittel 2021  155000


### A6: Umstrukturierung mit Pivot 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vZwPbKpPaJs?si=yeGHnZyh0W5cl93V" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit Spalten 'Stadt', 'Jahr' und 'Umsatz'. Verwenden Sie 'Stadt' als Index, 'Jahr' als Spalten und 'Umsatz' als Werte, um den DataFrame in einen Multiindex DataFrame zu pivotieren.


```python
df = pd.DataFrame({
    'Stadt': ['Berlin', 'Berlin', 'Hamburg', 'Hamburg'],
    'Jahr': [2020, 2021, 2020, 2021],
    'Umsatz': [100000, 105000, 50000, 52000]
})
print(df)

pivot_df = df.pivot(index='Stadt', columns='Jahr', values='Umsatz')
print("\n\n", pivot_df)

```

         Stadt  Jahr  Umsatz
    0   Berlin  2020  100000
    1   Berlin  2021  105000
    2  Hamburg  2020   50000
    3  Hamburg  2021   52000
    
    
     Jahr       2020    2021
    Stadt                  
    Berlin   100000  105000
    Hamburg   50000   52000


### A7: Multiindex Slicing 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/BqpRK7p8OF0?si=OH6d5v9mHWJpmYVB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Folgende Tabelle ist gegeben:


```python
arrays = [['Berlin', 'Berlin', 'Hamburg', 'Hamburg'], [2020, 2021, 2020, 2021]]
index = pd.MultiIndex.from_arrays(arrays, names=('Stadt', 'Jahr'))
df = pd.DataFrame({'Bevölkerung': [3500000, 3550000, 1800000, 1815000]}, index=index)
print(df)
```

                  Bevölkerung
    Stadt   Jahr             
    Berlin  2020      3500000
            2021      3550000
    Hamburg 2020      1800000
            2021      1815000


Führen Sie nun ein Slicing durch, um die Daten für 'Berlin' zu erhalten.

Führen Sie dann ein Slicing durch, um die Daten für das Jahr 2012 zu erhalten.


```python
print(df.loc['Berlin'])
```

          Bevölkerung
    Jahr             
    2020      3500000
    2021      3550000



```python
# Zugriff auf alle Daten für das Jahr 2021
jahr_2021 = df.xs(2021, level='Jahr')
print(jahr_2021)
```

             Bevölkerung
    Stadt               
    Berlin       3550000
    Hamburg      1815000


Um in dem gegebenen DataFrame df auf alle Zeilen zuzugreifen, die dem Jahr 2021 entsprechen, müssen Sie die xs (Cross Section)-Methode verwenden. Die loc-Methode ist hauptsächlich dafür gedacht, auf Zeilen basierend auf dem vollständigen Index oder einem Teil des Multiindex zuzugreifen, kann aber nicht direkt verwendet werden, um auf eine spezifische Ebene des Multiindex zu filtern, ohne die erste Ebene anzugeben.

Die xs-Methode ermöglicht es, eine bestimmte Ebene des Multiindex zu selektieren.

### A8: Umwandlung von Multiindex in Spalten 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ff5Szjd0-68?si=Xtl66SPTeZ4ahbjx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Wandeln Sie den Multiindex des DataFrame aus Aufgabe 8 in Spalten um, sodass 'Stadt' und 'Jahr' zu normalen Spalten werden.


```python
df_reset = df.reset_index()
print(df_reset)
```

         Stadt  Jahr  Bevölkerung
    0   Berlin  2020      3500000
    1   Berlin  2021      3550000
    2  Hamburg  2020      1800000
    3  Hamburg  2021      1815000


### A9: Hinzufügen einer Ebene zum Multiindex 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/uFJxKiB3UT4?si=7hsYRMmNsnZagqJf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Fügen Sie dem DataFrame aus Aufgabe 7 eine zusätzliche Ebene im Multiindex hinzu, ohne die bestehenden Daten zu verändern. Die neue Ebene soll 'Monat' heißen und für alle Einträge den Wert 'Januar' haben.


```python
# Hinzufügen einer neuen Ebene zum Multiindex
df['Monat'] = 'Januar'
df.set_index('Monat', append=True, inplace=True)
print(df)
```

                         Bevölkerung
    Stadt   Jahr Monat              
    Berlin  2020 Januar      3500000
            2021 Januar      3550000
    Hamburg 2020 Januar      1800000
            2021 Januar      1815000

