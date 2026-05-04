# Pandas Dataframe Analyse

Hier ist ein sehr nützliches Cheatsheet für Pandas mit den wichtigsten Methoden auf einen Blick:

[Cheat Sheet](pandas_einfuerung_files/Pandas_Cheat_Sheet.pdf)


## Statistische Zusammenfassungsfunktionen in Pandas

Pandas bietet eine Vielzahl von Funktionen zur statistischen Zusammenfassung an, die auf verschiedene Arten von pandas Objekten (DataFrame-Spalten, Series, GroupBy, etc.) angewendet werden können und einzelne Werte für jede Gruppe zurückgeben:

### Zusammenfassungsfunktionen (Aggregation)

- **`sum()`**: Summiert die Werte jeder Spalte.
- **`count()`**: Zählt die nicht-NA/NULL-Werte jeder Spalte.
- **`median()`**: Berechnet den Medianwert jeder Spalte.
- **`quantile([0.25, 0.75])`**: Berechnet Quantile (z.B. 25. und 75. Perzentil) jeder Spalte.
- **`apply(function)`**: Wendet eine Funktion auf jede Spalte an.
- **`min()`**: Findet den minimalen Wert in jeder Spalte.
- **`max()`**: Findet den maximalen Wert in jeder Spalte.
- **`mean()`**: Berechnet den Mittelwert jeder Spalte.

#### Beispielanwendungen:

```python
import pandas as pd

# DataFrame erstellen
data = {'Name': ['Anna', 'Jürgen', 'Charlie', 'Sophie', 'Max'],
        'Alter': [28, 47, 25, 32, 22],
        'Stadt': ['Berlin', 'Hamburg', 'München', 'Köln', 'Berlin']}
df = pd.DataFrame(data)

# Summe der Werte in jeder Spalte
print("Summe der Werte:")
print(df.sum())

# Anzahl der nicht-NA/NULL-Werte in jeder Spalte
print("\nAnzahl der nicht-NA/NULL-Werte:")
print(df.count())

# Medianwert jeder Spalte
print("\nMedianwerte des Alters:")
print(df['Alter'].median())

# 25. und 75. Perzentil jeder Spalte
print("\nQuantile (25. und 75. Perzentil):")
print(df['Alter'].quantile([0.25, 0.75]))

# Anwendung einer benutzerdefinierten Funktion auf jede Spalte (hier: Minimum)
print("\nMinimalwerte jeder Spalte:")
print(df.apply(min))

# Maximumwert in jeder Spalte
print("\nMaximale Werte jeder Spalte:")
print(df.max())

# Mittelwert jeder Spalte
print("\nMittelwert des Alters:")
print(df['Alter'].mean())
```

Diese Funktionen ermöglichen eine schnelle und einfache Analyse von numerischen Daten in einem DataFrame, indem sie grundlegende statistische Informationen liefern.


## "Subsets" von Dataframes

Im letzten Abschnitt haben wir bereits gelernt, wie wir einzelne Zeilen und Spalten auswählen können mit `loc` bzw. `iloc`. Oftmals wollen wir aber auch andere Subsets oder Unterauswahlen der Tabelle betrachten und analysieren.

Dazu können wir Slicing auf `iloc` und `loc` anwenden:

### Slicing mit `iloc` und `loc`

```python
import pandas as pd

# DataFrame erstellen
data = {'Name': ['Anna', 'Jürgen', 'Charlie', 'Sophie', 'Max'],
        'Alter': [28, 47, 25, 32, 22],
        'Stadt': ['Berlin', 'Hamburg', 'München', 'Köln', 'Berlin']}
df = pd.DataFrame(data)

# Slicing mit iloc: Auswahl der ersten drei Zeilen und der ersten zwei Spalten
subset_iloc = df.iloc[:3, :2]
print("Subset mit iloc:")
print(subset_iloc)

# Slicing mit loc: Auswahl der Zeilen 1 bis 3 und der Spalten 'Name' und 'Alter'
subset_loc = df.loc[1:3, ['Name', 'Alter']]
print("\nSubset mit loc:")
print(subset_loc)
```

### Spalten Auswahl

Manchmal möchten wir nur bestimmte Spalten auswählen und analysieren. Dies kann mithilfe von `[]` oder der `loc`-Methode erfolgen.

```python
# Auswahl der Spalten 'Name' und 'Stadt'
spalten_auswahl = df[['Name', 'Stadt']]
print("Spalten 'Name' und 'Stadt':")
print(spalten_auswahl)
```

### Zufällige Auswahl

Manchmal ist es nützlich, zufällige Zeilen aus einem DataFrame auszuwählen, beispielsweise für Stichproben.

```python
# Zufällige Auswahl von 3 Zeilen
zufaellige_auswahl = df.sample(n=3)
print("Zufällige Auswahl von 3 Zeilen:")
print(zufaellige_auswahl)
```

### Nach logischem Kriterium mit `df.query()`

Eine häufige Aufgabe besteht darin, Zeilen auszuwählen, die bestimmten logischen Kriterien entsprechen, wie z.B. alle Personen über einem bestimmten Alter.

```python
# Auswahl aller Personen, die älter als 25 Jahre sind
logische_auswahl = df.query('Alter > 25')
print("Personen, die älter als 25 Jahre sind:")
print(logische_auswahl)

# Auswahl aller Personen, die in Berlin leben
berlin_auswahl = df.query('Stadt == "Berlin"')
print("\nPersonen, die in Berlin leben:")
print(berlin_auswahl)
```

### Kombination von Bedingungen mit `df.query()`

Sie können auch mehrere Bedingungen kombinieren, um komplexere Subsets zu erstellen.

```python
# Auswahl aller Personen, die älter als 25 Jahre sind und in Berlin leben
kombinierte_auswahl = df.query('Alter > 25 and Stadt == "Berlin"')
print("\nPersonen, die älter als 25 Jahre sind und in Berlin leben:")
print(kombinierte_auswahl)
```

### Verwendung von Variablen mit `df.query()`

Sie können auch Variablen in `df.query()` verwenden, indem Sie das `@`-Zeichen verwenden.

```python
# Variablen für Abfrage
alter_grenze = 30
stadt_name = 'Berlin'

# Auswahl aller Personen, die älter als eine bestimmte Altersgrenze sind und in einer bestimmten Stadt leben
abfrage_variablen = df.query('Alter > @alter_grenze and Stadt == @stadt_name')
print(f"\nPersonen, die älter als {alter_grenze} Jahre sind und in {stadt_name} leben:")
print(abfrage_variablen)
```
Natürlich! Hier sind die zusätzlichen Methoden mit kurzen Erklärungen, eingefügt unter "weitere Methoden" in Ihrem Skript:

### Weitere Methoden

#### `df.nlargest(n, 'value')`
Wählt die obersten n Einträge basierend auf einer bestimmten Spalte ('value') aus und ordnet sie absteigend an.

#### `df.nsmallest(n, 'value')`
Wählt die untersten n Einträge basierend auf einer bestimmten Spalte ('value') aus und ordnet sie aufsteigend an.

#### `df.head(n)`
Wählt die ersten n Zeilen des DataFrames aus.

#### `df.tail(n)`
Wählt die letzten n Zeilen des DataFrames aus.


## Aufgaben
[planet_moon_data.csv](pandas_einfuerung_files/planet_moon_data.csv)
### A1: Laden und Anzeigen der CSV-Datei 🌶️
Laden Sie die CSV-Datei `planet_moon_data.csv` in einen DataFrame und zeigen Sie die ersten fünf Zeilen an.

### A2: Auswahl von Spalten 🌶️
Wählen Sie die Spalten `Planet`, `Durchmesser (km)`, `Orbitzeit (Tage)` und `Anzahl Monde` aus dem DataFrame aus und zeigen Sie sie an.

### A3: Berechnung von Daten 🌶️🌶️
Berechnen Sie die durchschnittliche Masse aller Planeten im DataFrame.

### A4: Filtern mit `query()` 🌶️🌶️
Verwenden Sie `query()`, um alle Planeten auszuwählen, deren Durchmesser größer als 50.000 km ist.

### A5: Erweiterte Berechnung 🌶️🌶️🌶️
Berechnen Sie die durchschnittliche Anzahl von Monden der Gasriesen (Jupiter, Saturn, Uranus, Neptun).

### A6: Visualisierung der Daten 🌶️🌶️🌶️
Erstellen Sie ein Balkendiagramm für die Anzahl der Monde der Planeten im DataFrame.
Orientiere dich hierzu gerne auf dem Cheatsheet.

### A7: Kombinierte Filter und Berechnung 🌶️🌶️🌶️
Verwenden Sie eine Kombination aus Filtern und Berechnungen, um den Planeten mit der größten Anzahl von Monden zu finden.

### Bonus A8: Ratespiel - Welcher Planet hat mehr Monde? 🌶️🌶️
Wählen Sie zufällig zwei verschiedene Planeten aus der CSV-Datei `planet_moon_data.csv` aus. Vergleichen Sie die Anzahl der Monde der beiden ausgewählten Planeten und lassen Sie den Benutzer raten, welcher Planet mehr Monde hat.

[Lösungen](pandas_erste_analyse_loesungen.md)



## Exkurs: Groupby

Die `groupby`-Methode in Pandas ermöglicht es, Daten in Gruppen zu unterteilen und Aggregatfunktionen auf jede Gruppe anzuwenden. Dies ist besonders nützlich, um zusammenfassende Statistiken zu berechnen oder Daten nach bestimmten Kategorien zu analysieren.

### Beispiel: Durchschnittliche Anzahl von Monden pro Planetentyp

```python
import pandas as pd

# DataFrame erstellen
data = {'Planet': ['Merkur', 'Venus', 'Erde', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptun'],
        'Typ': ['Gesteinsplanet', 'Gesteinsplanet', 'Gesteinsplanet', 'Gesteinsplanet', 'Gasriese', 'Gasriese', 'Eisriese', 'Eisriese'],
        'Anzahl Monde': [0, 0, 1, 2, 79, 82, 27, 14]}
df = pd.DataFrame(data)

# Gruppieren nach Planetentyp und Berechnung der durchschnittlichen Anzahl von Monden
grouped = df.groupby('Typ')['Anzahl Monde'].mean().reset_index()
print("Durchschnittliche Anzahl von Monden pro Planetentyp:")
print(grouped)
```

**Ausgabe:**

```
Durchschnittliche Anzahl von Monden pro Planetentyp:
             Typ  Anzahl Monde
0  Eisriese           20.5
1  Gasriese           80.5
2  Gesteinsplanet      0.75
```
#### Aufgabe 1: Durchschnittliches Gewicht von Tieren nach Art 🌶️🌶️
Gegeben ist ein DataFrame `animal_data` mit den Spalten `Tier`, `Art`, `Gewicht (kg)`. Gruppieren Sie die Daten nach `Art` und berechnen Sie das durchschnittliche Gewicht für jede Tierart.

```python
animal_data = pd.DataFrame({
    'Tier': ['Hund', 'Katze', 'Hund', 'Vogel', 'Katze', 'Vogel'],
    'Art': ['Säugetier', 'Säugetier', 'Säugetier', 'Vogel', 'Säugetier', 'Vogel'],
    'Gewicht (kg)': [20, 5, 25, 0.1, 6, 0.15]
})
```

#### Aufgabe 2: Maximale und minimale Höhen von Gebäuden nach Stadt 🌶️🌶️🌶️
Gegeben ist ein DataFrame `building_data` mit den Spalten `Gebäude`, `Stadt`, `Höhe (m)`. Gruppieren Sie die Daten nach `Stadt` und berechnen Sie die maximale und minimale Höhe der Gebäude für jede Stadt.

```python
building_data = pd.DataFrame({
    'Gebäude': ['Gebäude1', 'Gebäude2', 'Gebäude3', 'Gebäude4', 'Gebäude5', 'Gebäude6'],
    'Stadt': ['Berlin', 'München', 'Berlin', 'Hamburg', 'München', 'Hamburg'],
    'Höhe (m)': [150, 200, 180, 130, 210, 100]
})

```

<details>
<summary><b>Lösungen</b></summary>

Lösung Aufgabe 1:

```python
# Gruppieren nach Art und Berechnung des durchschnittlichen Gewichts
grouped_weight = animal_data.groupby('Art')['Gewicht (kg)'].mean().reset_index()
print("Durchschnittliches Gewicht von Tieren nach Art:")
print(grouped_weight)
```

Ausgabe:

```
Durchschnittliches Gewicht von Tieren nach Art:
         Art  Gewicht (kg)
0     Säugetier        14.0
1        Vogel         0.125
```

Lösung Aufgabe 2:

```python
# Gruppieren nach Stadt und Berechnung der maximalen und minimalen Höhe
grouped_height = building_data.groupby('Stadt')['Höhe (m)'].agg(['max', 'min']).reset_index()
print("Maximale und minimale Höhen von Gebäuden nach Stadt:")
print(grouped_height)
```

Ausgabe:

```
Maximale und minimale Höhen von Gebäuden nach Stadt:
     Stadt  max  min
0   Berlin  180  150
1  Hamburg  130  100
2  München  210  200
```

</details>

## Exkurs: Reshaping

Pandas bietet Methoden zum Umformen von Daten, wie z.B. `pivot`, `melt`, `stack` und `unstack`. Diese Methoden helfen dabei, Daten von einem Format in ein anderes zu transformieren, was für die Analyse und Visualisierung nützlich ist.

### Beispiel: Umwandeln von DataFrame-Formaten mit `melt` und `pivot`

#### Melt

Die `melt`-Methode transformiert einen DataFrame von einem breiten in ein langes Format. Dies ist nützlich, um Daten für bestimmte Arten von Analysen oder Visualisierungen vorzubereiten.

```python
# DataFrame im breiten Format
df_wide = pd.DataFrame({
    'Planet': ['Merkur', 'Venus', 'Erde'],
    'Durchmesser (km)': [4879, 12104, 12742],
    'Anzahl Monde': [0, 0, 1]
})

# Umwandeln in ein langes Format
df_long = pd.melt(df_wide, id_vars=['Planet'], value_vars=['Durchmesser (km)', 'Anzahl Monde'], var_name='Eigenschaft', value_name='Wert')
print("Langes Format mit melt:")
print(df_long)
```

**Ausgabe:**

```
Langes Format mit melt:
   Planet      Eigenschaft   Wert
0  Merkur  Durchmesser (km)  4879
1   Venus  Durchmesser (km) 12104
2   Erde   Durchmesser (km) 12742
3  Merkur      Anzahl Monde     0
4   Venus      Anzahl Monde     0
5   Erde       Anzahl Monde     1
```

#### Pivot

Die `pivot`-Methode transformiert einen DataFrame von einem langen in ein breites Format. Dies ist nützlich, um Daten wieder in ein leicht lesbares und analysierbares Format zu bringen.

```python
# DataFrame im langen Format
df_long = pd.DataFrame({
    'Planet': ['Merkur', 'Venus', 'Erde', 'Merkur', 'Venus', 'Erde'],
    'Eigenschaft': ['Durchmesser (km)', 'Durchmesser (km)', 'Durchmesser (km)', 'Anzahl Monde', 'Anzahl Monde', 'Anzahl Monde'],
    'Wert': [4879, 12104, 12742, 0, 0, 1]
})

# Umwandeln in ein breites Format
df_wide = df_long.pivot(index='Planet', columns='Eigenschaft', values='Wert').reset_index()
print("Breites Format mit pivot:")
print(df_wide)
```

**Ausgabe:**

```
Breites Format mit pivot:
Eigenschaft  Planet  Anzahl Monde  Durchmesser (km)
0             Erde              1              12742
1           Merkur              0               4879
2            Venus              0              12104
```


#### Aufgabe 1: Daten umformen mit `melt` 🌶️🌶️
Gegeben ist ein DataFrame `sales_data` im breiten Format mit den Spalten `Jahr`, `Quartal1`, `Quartal2`, `Quartal3`, `Quartal4`, die die Verkaufszahlen für verschiedene Quartale enthalten. Transformieren Sie die Daten in ein langes Format mit den Spalten `Jahr`, `Quartal`, `Verkaufszahlen`.

```python
sales_data = pd.DataFrame({
    'Jahr': [2020, 2021, 2022],
    'Quartal1': [100, 110, 105],
    'Quartal2': [150, 160, 155],
    'Quartal3': [200, 210, 205],
    'Quartal4': [250, 260, 255]
})

```

#### Aufgabe 2: Daten umformen mit `pivot` 🌶️🌶️🌶️
Gegeben ist ein DataFrame `temperature_data` im langen Format mit den Spalten `Stadt`, `Monat`, `Temperatur`. Transformieren Sie die Daten in ein breites Format, sodass jede Stadt eine Zeile hat und die Spalten die Monate und Temperaturen darstellen.

```python
temperature_data = pd.DataFrame({
    'Stadt': ['Berlin', 'Berlin', 'Berlin', 'München', 'München', 'München'],
    'Monat': ['Januar', 'Februar', 'März', 'Januar', 'Februar', 'März'],
    'Temperatur': [-2, 0, 5, -1, 2, 8]
})
```
<details>
<summary><b>Lösungen</b></summary>


Lösung Aufgabe 1

```python
# Umwandeln in ein langes Format
sales_long = pd.melt(sales_data, id_vars=['Jahr'], value_vars=['Quartal1', 'Quartal2', 'Quartal3', 'Quartal4'], var_name='Quartal', value_name='Verkaufszahlen')
print("Langes Format mit melt:")
print(sales_long)
```

Ausgabe:

```
Langes Format mit melt:
    Jahr   Quartal  Verkaufszahlen
0   2020  Quartal1             100
1   2021  Quartal1             110
2   2022  Quartal1             105
3  

```

Lösung Aufgabe 2

```python
# Umwandeln in ein breites Format
df_wide = temperature_data.pivot(index='Stadt', columns='Monat', values='Temperatur').reset_index()
print("Breites Format mit pivot:")
print(df_wide)
```

Ausgabe:

```
Breites Format mit pivot:
Monat    Stadt  Februar  Januar  März
0       Berlin        0      -2     5
1      München        2      -1     8
```