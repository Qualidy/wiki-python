# Lösungen

### A1: Grundlegende Gruppierung 🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/SedImcrD0nk?si=Q_bEJd_5xJVQcOs6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Erstellen Sie einen Pandas DataFrame mit drei Spalten: 'Name', 'Kategorie' und 'Punkte'. Gruppieren Sie diesen DataFrame nach 'Kategorie' und berechnen Sie die durchschnittlichen Punkte je Kategorie.


```python
import pandas as pd

# DataFrame erstellen
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Kategorie': ['A', 'B', 'A', 'B', 'A'],
    'Punkte': [80, 90, 88, 72, 95]
})
print(df, "\n")

# Gruppierung nach 'Kategorie' und Berechnung des Durchschnitts
durchschnitt = df.groupby('Kategorie')['Punkte'].mean()
print(durchschnitt)
```

          Name Kategorie  Punkte
    0    Alice         A      80
    1      Bob         B      90
    2  Charlie         A      88
    3    David         B      72
    4      Eve         A      95 
    
    Kategorie
    A    87.666667
    B    81.000000
    Name: Punkte, dtype: float64


### A2: Aggregation mit mehreren Funktionen 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fBUp1INUJog?si=hJ721qOWoz0BSvTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Verwenden Sie den gleichen DataFrame wie in Aufgabe 1. Gruppieren Sie die Daten nach 'Kategorie' und wenden Sie mehrere Aggregatfunktionen an: Berechnen Sie für jede Kategorie die Gesamtanzahl, den Durchschnitt und die maximale Punktzahl.


```python
# Gruppierung und Anwendung mehrerer Funktionen
aggregiert = df.groupby('Kategorie')['Punkte'].agg(['count', 'mean', 'max'])
print(aggregiert)
```

               count       mean  max
    Kategorie                       
    A              3  87.666667   95
    B              2  81.000000   90


### A3: Erstellen einer Pivot-Tabelle 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/lIfMgmg0sHA?si=hiRGJlaWxLxn-X59" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit Spalten 'Datum', 'Produkt' und 'Verkaufsmenge'. Erzeugen Sie eine Pivot-Tabelle, die die Gesamtverkaufsmenge für jedes Produkt nach Datum gruppiert.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Datum': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane'],
    'Verkaufsmenge': [10, 15, 20, 25]
})
print(df, "\n")

# Pivot-Tabelle erstellen
pivot = df.pivot_table(values='Verkaufsmenge',
                       index='Datum',
                       columns='Produkt',
                       aggfunc='sum')
print(pivot)
```

            Datum Produkt  Verkaufsmenge
    0  2023-01-01   Apfel             10
    1  2023-01-01  Banane             15
    2  2023-01-02   Apfel             20
    3  2023-01-02  Banane             25 
    
    Produkt     Apfel  Banane
    Datum                    
    2023-01-01     10      15
    2023-01-02     20      25


### A4: Gruppierung nach mehreren Spalten 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/5OdoX0NqKjE?si=GDnTnbBzA70Kyr8i" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit den Spalten 'Region', 'Produkt' und 'Verkaufsmenge'. Gruppieren Sie die Daten nach 'Region' und 'Produkt' und berechnen Sie die Gesamtverkaufsmenge für jede Kombination.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Region': ['Nord', 'Süd', 'Nord', 'Süd'],
    'Produkt': ['Apfel', 'Apfel', 'Banane', 'Banane'],
    'Verkaufsmenge': [10, 20, 15, 25]
})
print(df, "\n")

# Gruppierung nach mehreren Spalten
gruppen = df.groupby(['Region', 'Produkt']).sum()
print(gruppen)
```

      Region Produkt  Verkaufsmenge
    0   Nord   Apfel             10
    1    Süd   Apfel             20
    2   Nord  Banane             15
    3    Süd  Banane             25 
    
                    Verkaufsmenge
    Region Produkt               
    Nord   Apfel               10
           Banane              15
    Süd    Apfel               20
           Banane              25


### A5: Pivotisieren mit Multi-Index 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/amENE_A0304?si=b2XuaHhd_UHV0nvS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Verwenden Sie einen DataFrame mit den Spalten 'Datum', 'Region', 'Produkt' und 'Verkaufsmenge'. Erstellen Sie eine Pivot-Tabelle mit einem Multi-Index aus 'Datum' und 'Region', wobei 'Produkt' als Spalten verwendet wird.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Datum': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Region': ['Nord', 'Süd', 'Nord', 'Süd'],
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane'],
    'Verkaufsmenge': [10, 15, 20, 25]
})
print(df, "\n")

# Pivotisieren mit Multi-Index
pivot = df.pivot_table(values='Verkaufsmenge',
                       index=['Datum', 'Region'],
                       columns='Produkt',
                       aggfunc='sum')
print(pivot)
```

            Datum Region Produkt  Verkaufsmenge
    0  2023-01-01   Nord   Apfel             10
    1  2023-01-01    Süd  Banane             15
    2  2023-01-02   Nord   Apfel             20
    3  2023-01-02    Süd  Banane             25 
    
    Produkt            Apfel  Banane
    Datum      Region               
    2023-01-01 Nord     10.0     NaN
               Süd       NaN    15.0
    2023-01-02 Nord     20.0     NaN
               Süd       NaN    25.0


Beachten Sie, dass es NaN Einträge gibt, da wir nicht für jede Kombination Daten vorliegen haben!

### A6: Filtern nach Gruppierungsaggregat 🌶️🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/bBiuYFgIf6Q?si=4_FbPAfcJFsU1bbb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit den Spalten 'Team', 'Spieler' und 'Punkte'. Gruppieren Sie die Daten nach 'Team' und filtern Sie die Gruppen, sodass nur Teams mit einer durchschnittlichen Punktzahl von über 15 Punkten angezeigt werden.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Team': ['Team A', 'Team A', 'Team B', 'Team B', 'Team C'],
    'Spieler': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Punkte': [10, 20, 15, 25, 30]
})
print(df, "\n")

# Gruppierung und Filterung
gefiltert = df.groupby('Team').filter(lambda x: x['Punkte'].mean() > 15)
print(gefiltert)
```

         Team  Spieler  Punkte
    0  Team A    Alice      10
    1  Team A      Bob      20
    2  Team B  Charlie      15
    3  Team B    David      25
    4  Team C      Eve      30 
    
         Team  Spieler  Punkte
    2  Team B  Charlie      15
    3  Team B    David      25
    4  Team C      Eve      30


### A7: Erweiterte Pivot-Tabellen 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/-0hStraUinw?si=Gjm_YI-zNwmE2p-K" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit den Spalten 'Datum', 'Produkt', 'Region' und 'Verkaufsmenge'. Erzeugen Sie eine Pivot-Tabelle, die die durchschnittliche Verkaufsmenge für jedes Produkt nach Region und Datum gruppiert.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Datum': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01'],
    'Region': ['Nord', 'Süd', 'Nord', 'Süd', 'Ost'],
    'Produkt': ['Apfel', 'Banane', 'Apfel', 'Banane', 'Apfel'],
    'Verkaufsmenge': [10, 15, 20, 25, 30]
})
print(df, "\n")

# Pivot-Tabelle erstellen
pivot = df.pivot_table(values='Verkaufsmenge',
                       index=['Datum', 'Region'],
                       columns='Produkt',
                       aggfunc='mean')
print(pivot)
```

            Datum Region Produkt  Verkaufsmenge
    0  2023-01-01   Nord   Apfel             10
    1  2023-01-01    Süd  Banane             15
    2  2023-01-02   Nord   Apfel             20
    3  2023-01-02    Süd  Banane             25
    4  2023-01-01    Ost   Apfel             30 
    
    Produkt            Apfel  Banane
    Datum      Region               
    2023-01-01 Nord     10.0     NaN
               Ost      30.0     NaN
               Süd       NaN    15.0
    2023-01-02 Nord     20.0     NaN
               Süd       NaN    25.0


### A8: Kombiniertes Gruppieren und Pivotisieren 🌶️🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ofqW0XkEHo4?si=M4v8FGMo_KXc2Lf5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit den Spalten 'Monat', 'Verkäufer' und 'Verkaufsmenge'. Gruppieren Sie die Daten nach 'Verkäufer' und erstellen Sie eine Pivot-Tabelle, die die Gesamtverkaufsmenge pro Monat für jeden Verkäufer anzeigt.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Monat': ['Januar', 'Januar', 'Februar', 'Februar', 'Januar'],
    'Verkäufer': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie'],
    'Verkaufsmenge': [200, 150, 180, 220, 100]
})
print(df, "\n")

# Gruppieren nach 'Monat' und 'Verkäufer' und Summieren der 'Verkaufsmenge'
gruppiert = df.groupby(['Monat', 'Verkäufer']).sum().reset_index()
print(gruppiert, "\n")

# Erstellen einer Pivot-Tabelle aus der gruppierten Daten
pivot = gruppiert.pivot_table(values='Verkaufsmenge',
                              index='Verkäufer', 
                              columns='Monat',
                              fill_value=0)
print(pivot)
```

         Monat Verkäufer  Verkaufsmenge
    0   Januar     Alice            200
    1   Januar       Bob            150
    2  Februar     Alice            180
    3  Februar       Bob            220
    4   Januar   Charlie            100 
    
         Monat Verkäufer  Verkaufsmenge
    0  Februar     Alice            180
    1  Februar       Bob            220
    2   Januar     Alice            200
    3   Januar       Bob            150
    4   Januar   Charlie            100 
    
    Monat      Februar  Januar
    Verkäufer                 
    Alice        180.0   200.0
    Bob          220.0   150.0
    Charlie        0.0   100.0


### A9: Gruppieren und Berechnen von kumulativen Summen 🌶️🌶️🌶

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Vu9u100FYXM?si=OPMWDJ0ShdRGjVgK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit den Spalten 'Datum', 'Kategorie' und 'Wert'. Gruppieren Sie die Daten nach 'Kategorie' und berechnen Sie die kumulative Summe der Werte innerhalb jeder Kategorie.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Datum': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02']),
    'Kategorie': ['A', 'A', 'B', 'B'],
    'Wert': [100, 200, 150, 250]
})
print(df, "\n")

# Gruppieren und kumulative Summe berechnen
df['Kumulative_Summe'] = df.groupby('Kategorie')['Wert'].cumsum()
print(df)
```

           Datum Kategorie  Wert
    0 2023-01-01         A   100
    1 2023-01-02         A   200
    2 2023-01-01         B   150
    3 2023-01-02         B   250 
    
           Datum Kategorie  Wert  Kumulative_Summe
    0 2023-01-01         A   100               100
    1 2023-01-02         A   200               300
    2 2023-01-01         B   150               150
    3 2023-01-02         B   250               400


### A10: Erweitertes Pivotisieren mit Füllen von fehlenden Werten 🌶️🌶️

<details>
<summary>
🎦 Lösungsvideo
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/f8VWCPV2YjQ?si=DLbq3vBTO7Q8j_Ub" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Erstellen Sie einen DataFrame mit den Spalten 'Datum', 'Produkt' und 'Verkaufsmenge'. Erzeugen Sie eine Pivot-Tabelle, die die Gesamtverkaufsmenge für jedes Produkt nach Datum anzeigt, und füllen Sie fehlende Werte mit Nullen.


```python
# DataFrame erstellen
df = pd.DataFrame({
    'Datum': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Produkt': ['Apfel', 'Banane', 'Apfel'],
    'Verkaufsmenge': [10, 20, 15]
})
print(df, "\n")

# Pivot-Tabelle erstellen und fehlende Werte füllen
pivot = df.pivot_table(values='Verkaufsmenge', index='Datum', columns='Produkt', aggfunc='sum', fill_value=0)
print(pivot)
```

            Datum Produkt  Verkaufsmenge
    0  2023-01-01   Apfel             10
    1  2023-01-02  Banane             20
    2  2023-01-03   Apfel             15 
    
    Produkt     Apfel  Banane
    Datum                    
    2023-01-01     10       0
    2023-01-02      0      20
    2023-01-03     15       0

