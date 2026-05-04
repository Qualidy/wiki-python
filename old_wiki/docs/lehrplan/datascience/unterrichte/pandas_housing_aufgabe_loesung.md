# Pandas Housing Aufgabe Lösung


[housing_project.csv](pandas_housing_files/housing_project.csv)

### Beschreibung 
Ladet den Datensatz "housing_project.csv" und analysiert diesen mit den eben kennengelernten Funktionen. Gehen Sie dabei wie folgt vor:

#### 1. 
Analysieren Sie den Datensatz und entfernen Sie fehlerhafte Einträge, außer beim Einkommen. Achten Sie dabei darauf, dass Geodaten verzichtbar sind und alle Einträge, wo die Hälfte oder mehr der Einträge fehlerhaft sind, komplett entfernt werden.

#### 2. 
Füllen Sie fehlende Angaben, bei Angaben zu den Räumen, mit plausiblen Werten auf.

#### 3. 
Überprüfen Sie abschließend, ob die gesamte Datei bzw. das bearbeitet Pandas DataFrame keine fehlerhaften Werte mehr enthält. Geben Sie zudem die Durchschnittswerte und Median für alle Spalten aus, bei den dies sinnvoll ist.

### Was bedeuten die Schritte ...
#### 1
- Daten laden
- Fehlende Einträge (a) erkennen und (b) entfernen oder (c) zu füllen
- Über Spalten iterieren und komplett entfernen, wenn mehr als die Hälfte NaN ist
- In allen Spalten außer Einkommen und Geodaten die NaN finden
#### 2
- In allen Spalten außer Einkommen und Geodaten die NaN mit dem Durchschnitt (o. Ä.) ersetzen
#### 3
- Datei nach NaN durchforsten und Summe ausgeben
- Durchschnitt und Median für MedInc, HouseAge, AveRooms, AveBedrms, Population und AveOccup ausgeben

```python
import pandas as pd
```

```python
df = pd.read_csv('housing_project.csv', sep=',', encoding='utf-8')
```

```python
df.head()
```

```plaintext
Output:
   MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude
0  8.3252      41.0  6.984127   1.023810       322.0  2.555556     37.88    -122.23
1  8.3014       NaN  6.238137   0.971880      2401.0  2.109842     37.86    -122.22
2  7.2574      52.0  8.288136        NaN       496.0  2.802260     37.85    -122.24
3  5.6431      52.0  5.817352   1.073059       558.0  2.547945     37.85    -122.25
4  3.8462      52.0  6.281853   1.081081       565.0  2.181467     37.85    -122.25
```

```python
len(df)
```

```plaintext
Output:
2500
```

```python
df.isnull().sum()
```

```plaintext
Output:
MedInc        159
HouseAge      135
AveRooms      143
AveBedrms     141
Population    144
AveOccup      171
Latitude      149
Longitude     173
dtype: int64
```

```python
df["MedInc"].isnull().sum()
```

```plaintext
Output:
159
```

```python
len(df.columns)
```

```plaintext
Output:
8
```

```python
df_new = df.dropna(thresh=len(df.columns)/2)
len(df_new)
```

```plaintext
Output:
2500
```

```python
df['HouseAge'] = df['HouseAge'].fillna(df['HouseAge'].mean())
df['AveRooms'] = df['AveRooms'].fillna(df['AveRooms'].mean())
df['AveBedrms'] = df['AveBedrms'].fillna(df['AveBedrms'].mean())
df['Population'] = df['Population'].fillna(df['Population'].mean())
df['AveOccup'] = df['AveOccup'].fillna(df['AveOccup'].mean())
```

```python
df.isnull().sum()
```

```plaintext
Output:
MedInc        159
HouseAge        0
AveRooms        0
AveBedrms       0
Population      0
AveOccup        0
Latitude      149
Longitude     173
dtype: int64
```

```python
df.median()
```

```plaintext
Output:
MedInc           3.261900
HouseAge        30.042706
AveRooms         5.461001
AveBedrms        1.055637
Population    1078.000000
AveOccup         2.764706
Latitude        37.800000
Longitude     -122.030000
dtype: float64
```

```python
df.mean()
```

```plaintext
Output:
MedInc           3.697384
HouseAge        30.042706
AveRooms         5.777153
AveBedrms        1.145971
Population    1259.178693
AveOccup         2.798655
Latitude        37.798252
Longitude     -121.493446
dtype: float64
```

### Welche weiteren Werte sind auf ihre Sinnhaftigkeit zu prüfen?

```python
# Häuser im Meer ... ich schwimme gerne :D
```