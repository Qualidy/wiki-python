### Lösungen

### A1: Laden und Anzeigen der CSV-Datei 🌶️

```python
import pandas as pd

# Laden der CSV-Datei in einen DataFrame
df = pd.read_csv('planet_moon_data.csv')

# Anzeigen der ersten fünf Zeilen
print("Die ersten fünf Zeilen der CSV-Datei:")
print(df.head())
```

### A2: Auswahl von Spalten 🌶️

```python
# Auswahl der spezifischen Spalten
selected_columns = df[['Planet', 'Durchmesser (km)', 'Orbitzeit (Tage)', 'Anzahl Monde']]

print("Ausgewählte Spalten:")
print(selected_columns)
```

### A3: Berechnung von Daten 🌶️🌶️

```python
# Berechnung der durchschnittlichen Masse aller Planeten
durchschnittliche_masse = df['Masse (kg)'].mean()

print(f"Durchschnittliche Masse aller Planeten: {durchschnittliche_masse:.2e} kg")
```

### A4: Filtern mit `query()` 🌶️🌶️

```python
# Auswahl der Planeten mit einem Durchmesser größer als 50.000 km
filtered_planets = df.query('`Durchmesser (km)` > 50000')

print("Planeten mit einem Durchmesser größer als 50.000 km:")
print(filtered_planets)
```

### A5: Erweiterte Berechnung 🌶️🌶️🌶️

```python
# Filtern nach Gasriesen und Berechnung der durchschnittlichen Anzahl von Monden
gasriesen = ['Jupiter', 'Saturn', 'Uranus', 'Neptun']
gasriesen_df = df[df['Planet'].isin(gasriesen)]
durchschnittliche_mondzahl_gasriesen = gasriesen_df['Anzahl Monde'].mean()

print(f"Durchschnittliche Anzahl von Monden der Gasriesen: {durchschnittliche_mondzahl_gasriesen:.2f}")
```

### A6: Visualisierung der Daten 🌶️🌶️🌶️

```python
import matplotlib.pyplot as plt

# Erstellen eines Balkendiagramms für die Anzahl der Monde der Planeten
plt.figure(figsize=(10, 6))
plt.bar(df['Planet'], df['Anzahl Monde'], color='skyblue')
plt.xlabel('Planet')
plt.ylabel('Anzahl der Monde')
plt.title('Anzahl der Monde der Planeten')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### A7: Kombinierte Filter und Berechnung 🌶️🌶️🌶️

```python
# Finden des Planeten mit der größten Anzahl von Monden
planet_mit_den_meisten_monden = df.loc[df['Anzahl Monde'].idxmax()]

print("Planet mit der größten Anzahl von Monden:")
print(planet_mit_den_meisten_monden)
```
### A8: Ratespiel

```python
import pandas as pd
import random

# Laden der CSV-Datei
df = pd.read_csv('planet_moon_data.csv')

# Zufällige Auswahl von zwei verschiedenen Planeten
planet1, planet2 = random.sample(df['Planet'].tolist(), 2)

# Informationen über die ausgewählten Planeten
info_planet1 = df[df['Planet'] == planet1]
info_planet2 = df[df['Planet'] == planet2]

# Anzahl Monde der ausgewählten Planeten
anzahl_monde1 = info_planet1['Anzahl Monde'].values[0]
anzahl_monde2 = info_planet2['Anzahl Monde'].values[0]

# Ausgabe des Vergleichs und des Ratespiels
print(f"Willkommen zum Ratespiel!")
print(f"Vergleichen Sie die Anzahl der Monde der Planeten {planet1} und {planet2}:")
print(f"1. {planet1} hat {anzahl_monde1} Monde.")
print(f"2. {planet2} hat {anzahl_monde2} Monde.")

# Benutzer gibt seinen Tipp ab
tipp = input("Welcher Planet hat Ihrer Meinung nach mehr Monde? Geben Sie '1' oder '2' ein: ")

# Auswertung des Tipps
if tipp == '1':
    if anzahl_monde1 > anzahl_monde2:
        print("Richtig! Sie haben gewonnen.")
    else:
        print("Leider falsch. Der andere Planet hat mehr Monde.")
elif tipp == '2':
    if anzahl_monde2 > anzahl_monde1:
        print("Richtig! Sie haben gewonnen.")
    else:
        print("Leider falsch. Der andere Planet hat mehr Monde.")
else:
    print("Ungültige Eingabe. Bitte geben Sie '1' oder '2' ein.")

# Ausgabe der tatsächlichen Anzahl der Monde für beide Planeten
print(f"{planet1} hat {anzahl_monde1} Monde und {planet2} hat {anzahl_monde2} Monde.")
```
