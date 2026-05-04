# Exkurs: Pandas: Multiindex

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/tbNBbmbWAeY?si=nvLJ82w3BVYHxDuW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [10 min]

### Was ist Pandas Multiindex?

Eines der leistungsstarken Features von Pandas ist der Multiindex, auch bekannt als hierarchischer Index. Diese Funktionalität ermöglicht es, mehrere Indexebenen auf einer Achse zu haben. Dies kann besonders nützlich sein, um mit komplexen Datenstrukturen zu arbeiten, die mehrdimensionale Daten in einer zweidimensionalen Tabelle darstellen.

### Wann und warum wird ein Multiindex verwendet?

Multiindex kommt in vielen realen Anwendungsfällen zum Einsatz. Ein klassisches Beispiel ist die Organisation von zeitbezogenen Daten. Angenommen, ein Unternehmen möchte seine Verkaufsdaten nach Jahr, Monat und Produktkategorie analysieren. Mit einem Multiindex können diese drei Dimensionen in einem einzigen DataFrame effektiv dargestellt werden, wodurch komplexe Analysen und Gruppierungen vereinfacht werden.

Ein weiteres Beispiel könnte in der Finanzwelt gefunden werden, wo Multiindices dazu verwendet werden könnten, Finanzdaten nach verschiedenen Ebenen wie Ländern, Unternehmen und Finanzkennzahlen zu organisieren. So kann ein Analyst schnell und effizient Daten auf verschiedenen Ebenen aggregieren und vergleichen.

### Vorteile des Multiindex

Die Verwendung eines Multiindex bietet mehrere Vorteile. Erstens ermöglicht es eine bessere Organisation von Daten, was insbesondere bei großen und komplexen Datensätzen nützlich ist. Zweitens erleichtert es die Durchführung von Operationen auf verschiedenen Ebenen der Datenstruktur, wie Gruppierung, Slicing und Pivotierung. Schließlich verbessert der Multiindex die Lesbarkeit und Struktur der Daten, indem er eine klare Hierarchie und Strukturierung bietet.

### Beispielhafte Anwendungsszenarien

In der Wissenschaft könnten Forscher den Multiindex verwenden, um experimentelle Daten zu organisieren, die über verschiedene Bedingungen und Zeitpunkte hinweg gesammelt wurden. In der Logistik könnte ein Multiindex dazu verwendet werden, Lieferinformationen nach Region, Produkttyp und Lieferdatum zu strukturieren. Im Bildungsbereich könnte er genutzt werden, um Schülerleistungen nach Schule, Klasse und Fach zu organisieren.

## Codebeispiele [30 min]

### Beispiel 1: Erstellung eines Multiindex DataFrame


```python
import pandas as pd

arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2],
]

tuples = list(zip(*arrays))
print("tuples:", tuples)

index = pd.MultiIndex.from_tuples(tuples, names=['Obergruppe', 'Untergruppe'])
df = pd.DataFrame(data={'Daten': [10, 20, 30, 40]}, index=index)

print(df)
```

    tuples: [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
                            Daten
    Obergruppe Untergruppe       
    A          1               10
               2               20
    B          1               30
               2               40


In diesem Beispiel wird ein einfacher Pandas DataFrame mit einem Multiindex erstellt. Zuerst importieren wir pandas. Dann definieren wir zwei Listen, die die Werte für die beiden Ebenen unseres Multiindex enthalten: 'Obergruppe' (mit den Werten 'A' und 'B') und 'Untergruppe' (mit den Werten 1 und 2). Diese Listen werden zu Tupeln kombiniert, die als Index für unseren DataFrame verwendet werden. Schließlich erstellen wir den DataFrame `df` mit einer Spalte 'Daten'. Der Multiindex ermöglicht es, Daten in einer hierarchischen Struktur zu organisieren und darauf zuzugreifen.

### Beispiel 2: Zugriff auf Daten in einem Multiindex DataFrame


```python
# Zugriff auf alle Daten in der Obergruppe 'A'
print("Daten in Obergruppe 'A':\n", df.loc['A'])

# Zugriff auf spezifische Untergruppe innerhalb einer Obergruppe
print("\nDaten in Obergruppe 'A', Untergruppe 2:\n", df.loc[('A', 2)])

# Zugriff auf alle Daten in der Untergruppe 1, unabhängig von der Obergruppe
print("\nDaten in allen Obergruppen, Untergruppe 1:\n", df.xs(1, level='Untergruppe'))

# Slicing auf Multiindex-Ebenen
print("\nSlicing von 'A'1 bis 'B'1:\n", df.loc[('A', 1):('B', 1)])
```

    Daten in Obergruppe 'A':
                  Daten
    Untergruppe       
    1               10
    2               20
    
    Daten in Obergruppe 'A', Untergruppe 2:
     Daten    20
    Name: (A, 2), dtype: int64
    
    Daten in allen Obergruppen, Untergruppe 1:
                 Daten
    Obergruppe       
    A              10
    B              30
    
    Slicing von 'A'1 bis 'B'1:
                             Daten
    Obergruppe Untergruppe       
    A          1               10
               2               20
    B          1               30


In diesem Beispiel zeigen wir verschiedene Arten des Zugriffs auf Daten in einem DataFrame mit Multiindex.

- Zugriff auf eine ganze Obergruppe: Mit `df.loc['A']` greifen wir auf alle Zeilen zu, in denen die 'Obergruppe' den Wert 'A' hat. Dies gibt uns alle Datenzeilen in dieser Gruppe.

- Zugriff auf eine spezifische Untergruppe innerhalb einer Obergruppe: Mit `df.loc[('A', 2)]` greifen wir spezifisch auf die Daten zu, bei denen die 'Obergruppe' 'A' und die 'Untergruppe' 2 ist.

- Zugriff auf eine bestimmte Untergruppe über alle Obergruppen hinweg: Mit `df.xs(1, level='Untergruppe')` erhalten wir alle Zeilen, in denen die 'Untergruppe' 1 ist, unabhängig davon, welcher 'Obergruppe' sie angehören.

- Slicing über Multiindex-Ebenen hinweg: Mit `df.loc[('A', 1):('B', 1)]` führen wir ein Slicing durch, das von der Obergruppe 'A', Untergruppe 1 bis zur Obergruppe 'B', Untergruppe 1 reicht.

### Beispiel 3: Multiindex aus Produkt von Arrays erstellen


```python
import pandas as pd

# Erstellung eines Multiindex aus dem Produkt zweier Arrays
obergruppe = ['X', 'Y']
untergruppe = [1, 2, 3]
multi_index = pd.MultiIndex.from_product([obergruppe, untergruppe],
                                          names=['Obergruppe', 'Untergruppe'])

# Erstellung des DataFrame mit dem Multiindex
df = pd.DataFrame(data={'Wert': range(6)}, index=multi_index)
print(df)
```

                            Wert
    Obergruppe Untergruppe      
    X          1               0
               2               1
               3               2
    Y          1               3
               2               4
               3               5


In diesem Beispiel erstellen wir einen Multiindex durch das kartesische Produkt von zwei Arrays: `obergruppe` und `untergruppe`. Der Multiindex `multi_index` wird dann verwendet, um einen DataFrame `df` zu erstellen. Dieser Ansatz ist besonders nützlich, wenn jede Kombination von Werten aus den beiden Arrays als Index verwendet werden soll. Der resultierende DataFrame hat für jede Kombination aus Ober- und Untergruppe einen entsprechenden Eintrag.

### Beispiel 4: Sortieren eines DataFrames mit Multiindex


```python
import pandas as pd

# Erstellung eines Multiindex DataFrame
arrays = [
    ['B', 'B', 'A', 'A'],
    [2, 1, 2, 1],
]

tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['Obergruppe', 'Untergruppe'])
df = pd.DataFrame(data={'Wert': [100, 200, 300, 400]}, index=index)

print("Vor dem Sortieren:\n", df)

# Sortieren des DataFrames nach dem Multiindex
sortierter_df = df.sort_index()
print("\nNach dem Sortieren:\n", sortierter_df)
```

    Vor dem Sortieren:
                             Wert
    Obergruppe Untergruppe      
    B          2             100
               1             200
    A          2             300
               1             400
    
    Nach dem Sortieren:
                             Wert
    Obergruppe Untergruppe      
    A          1             400
               2             300
    B          1             200
               2             100


In diesem Beispiel erstellen wir zuerst einen DataFrame `df` mit einem Multiindex, bei dem die Reihenfolge der Indexwerte zunächst nicht sortiert ist (zuerst kommt 'B', dann 'A').

Beim Ausdrucken des ursprünglichen DataFrames sehen Sie, dass die Indexwerte nicht in einer natürlichen Reihenfolge vorliegen. Dies kann das Verständnis und die Analyse der Daten erschweren.

Nachdem wir `df.sort_index()` aufgerufen haben, erstellen wir den DataFrame `sortierter_df`, bei dem die Indexwerte in einer logischen Reihenfolge sortiert sind (zuerst 'A', dann 'B', und innerhalb jeder Obergruppe sind die Untergruppen von 1 bis 2 sortiert).

Das Sortieren eines Multiindex DataFrame hilft, die Daten besser zu strukturieren und macht sie leichter lesbar, vor allem, wenn man auf bestimmte Abschnitte des DataFrames zugreifen oder diese analysieren möchte.

Und wenn man jetzt nach der Untergruppe sortieren wollte?

So geht das:


```python
# Sortieren des DataFrames nach der Untergruppe
sortierter_df = df.sort_values(by='Untergruppe')
print("\nNach dem Sortieren nach Untergruppe:\n", sortierter_df)
```

    
    Nach dem Sortieren nach Untergruppe:
                             Wert
    Obergruppe Untergruppe      
    B          1             200
    A          1             400
    B          2             100
    A          2             300


### Beispiel 5: Pivotieren eines DataFrames in einen Multiindex DataFrame


```python
import pandas as pd
import numpy as np

# Erstellung eines Beispieldatenrahmens
df = pd.DataFrame({
    'Region': ['Nord', 'Nord', 'Süd', 'Süd'],
    'Jahr': [2020, 2021, 2020, 2021],
    'Umsatz': [100, 150, 200, 250]
})
print("df:\n", df)

# Pivotieren des DataFrames in einen DataFrame mit Multiindex
pivot_df = df.pivot(index='Region', columns='Jahr', values='Umsatz')
print("\n\npivot_df:\n", pivot_df)

```

    df:
       Region  Jahr  Umsatz
    0   Nord  2020     100
    1   Nord  2021     150
    2    Süd  2020     200
    3    Süd  2021     250
    
    
    pivot_df:
     Jahr    2020  2021
    Region            
    Nord     100   150
    Süd      200   250


In diesem Beispiel erstellen wir zuerst einen einfachen DataFrame `df` mit den Spalten 'Region', 'Jahr' und 'Umsatz'. Dann verwenden wir die `pivot`-Methode, um diesen DataFrame in einen DataFrame mit einem Multiindex umzuwandeln.

Durch das Pivotieren wird 'Region' als Index und 'Jahr' als Spaltenüberschriften verwendet. Jeder Zellenwert entspricht dem 'Umsatz' für die jeweilige Region und das jeweilige Jahr. Das Ergebnis ist ein DataFrame, der eine zweidimensionale Darstellung unserer Daten bietet, wobei die Indexhierarchie klar ersichtlich ist. In diesem Fall haben wir einen einfachen Index (nur 'Region'), aber die Spalten bilden eine hierarchische Struktur, die einem Multiindex ähnelt, mit 'Jahr' als zweiter Ebene.

## Aufgaben [120 min]

### A1: Erstellung eines Multiindex DataFrame nach Vorgaben 🌶️

Erstellen Sie einen Pandas DataFrame mit einem Multiindex, der aus zwei Ebenen besteht: 'Stadt' und 'Jahr'. Fügen Sie eine Datenreihe mit dem Namen 'Bevölkerung' hinzu. Verwenden Sie folgende Städte und Jahre: Städte - ['Berlin', 'Hamburg'], Jahre - [2020, 2021].

### A2: Zugriff auf Multiindex Daten 🌶️

Gegeben sei der in Aufgabe 1 erstellte DataFrame. Greifen Sie auf die Daten für 'Berlin' im Jahr 2021 zu.

### A3: Aggregation auf Multiindex Ebene 🌶️🌶️

Aggregieren Sie die Bevölkerungsdaten aus Aufgabe 1, um die Gesamtbevölkerung pro Stadt über alle Jahre zu erhalten.

Aggregieren Sie dann die Bevölkerungsdaten aus Aufgabe 1, um die Gesamtbevölkerung pro Jahr über alle Städte zu erhalten.

### A4: Multiindex mit from_product 🌶️🌶️

Erstellen Sie einen Multiindex DataFrame mit `pd.MultiIndex.from_product`. Verwenden Sie die Produktkategorien ['Elektronik', 'Lebensmittel'] und die Jahre [2020, 2021] als Index. Fügen Sie eine Spalte 'Umsatz' mit beliebigen Werten hinzu.

### A5: Sortieren eines Multiindex DataFrame 🌶️🌶️

Sortieren Sie den DataFrame aus Aufgabe 4 zuerst nach 'Jahr' und dann nach 'Kategorie'.

### A6: Umstrukturierung mit Pivot 🌶️🌶️

Erstellen Sie einen DataFrame mit Spalten 'Stadt', 'Jahr' und 'Umsatz'. Verwenden Sie 'Stadt' als Index, 'Jahr' als Spalten und 'Umsatz' als Werte, um den DataFrame in einen Multiindex DataFrame zu pivotieren.

### A7: Multiindex Slicing 🌶️🌶️🌶️

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

### A8: Umwandlung von Multiindex in Spalten 🌶️🌶️

Wandeln Sie den Multiindex des DataFrame aus Aufgabe 8 in Spalten um, sodass 'Stadt' und 'Jahr' zu normalen Spalten werden.

### A9: Hinzufügen einer Ebene zum Multiindex 🌶️🌶️🌶️

Fügen Sie dem DataFrame aus Aufgabe 7 eine zusätzliche Ebene im Multiindex hinzu, ohne die bestehenden Daten zu verändern. Die neue Ebene soll 'Monat' heißen und für alle Einträge den Wert 'Januar' haben.

[Lösungen](pandas_multiindex_loesungen.md)
