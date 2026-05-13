# Lösungen für einfache Aufgaben

### Aufgabe: Elementweise Addition 

```python
[x * y for x, y in zip(liste1, liste2)]
```

### Aufgabe: Ungerade Summanden

```python
[x + y for x, y in zip(liste1, liste2) if x % 2]
```

### Aufgabe: Zuviel oder zu wenig

Die Schleife wird 10 Mal durchlaufen. `zip` liefert nur so viele Paare, bis
**einer** der Parameter erschöpft ist. D.h. nach der Ausgabe `9 9` ist Schluss,
da dann `range(10)` erschüpft ist, obwohl es noch weitere Elemente in `range(20)`
gäbe.

### Aufgabe: Zusammenführen von Wörtern 

```python
adjektive = ['rot', 'schnell']
nomen = ['Auto', 'Hund']

all_combinations = [adj + ' ' + nom for adj in adjektive for nom in nomen]

zipped = [adj + ' ' + nom for adj, nom in zip(adjektive, nomen)]
```

### Aufgabe: Anzahl der Übereinstimmungen zählen 

```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 2, 1, 4, 5]
anzahl_übereinstimmungen = sum(1 for x, y in zip(liste1, liste2) if x == y)
print(anzahl_übereinstimmungen)
```

# Was steckt dahinter

### Aufgabe: Dictionary erstellen 

Der folgende Code erstellt ein Dictionary. Dies ist möglich, da `zip(schlüssel, werte)`
einen generator von Paaren zurückgibt, die genau als als `(key, value)`-Paare interpretiert werden. 

```python
schlüssel = ['A', 'B', 'C']
werte = [1, 2, 3]
ergebnis = dict(zip(schlüssel, werte))
print(ergebnis) # {'A': 1, 'B': 2, 'C': 3}
```

### Aufgabe: Eigener Zipper

```python
def my_zipper(list1, list2):
    shortest_length = min(len(list1), len(list2))
    return [(list1[i], list2[i]) for i in range(shortest_length)]
```

## Verwendung von `zip` mit mehr als zwei Iterables

### Aufgabe: Maximaler Wert pro Position 

```python
liste1 = [5, 2, 8]
liste2 = [7, 1, 6]
liste3 = [3, 4, 0]
max_werte = [max(x, y, z) for x, y, z in zip(liste1, liste2, liste3)]
print(max_werte)
```

### Aufgabe: Mittelwert berechnen 

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [3, 4, 0]
mittelwerte = [(x + y + z) / 3 for x, y, z in zip(liste1, liste2, liste3)]
print(mittelwerte)
```

### Aufgabe: zip in slicing

```python
numbers = [1, 3, 5, 7, 8, 3, 0, 1, 1, 3]
triple_sum = [a + b + c for a, b, c in zip(numbers, numbers[1:], numbers[2:])]
```

## Komplexes Beispiel mit der `zip()`-Funktion in Python

### Aufgabe: Eine Welt ohne zip (Java)

```python
teilnehmer = ["Anna", "Bernd", "Carla"]
punkte = [[10, 20, 30], [15, 25, 35], [10, 30, 50]]

gesamtpunktzahl = dict()
for i in range(len(teilnehmer)):
    gesamtpunktzahl[teilnehmer[i]] = sum(punkte[i])

print(gesamtpunktzahl)
```
Bewertung: 🤮

# enumerate

### Aufgabe: Wo sind die größten

```python
numbers = [1,3,5,3,5,1]

maximum = max(numbers)

positions_of_maxima = [i for i, number in enumerate(numbers) if number == maximum]
```

### Aufgabe: Das kann ich doch auch

```python
def my_enumerate(iterable):
    return ((i, e) for i, e in zip(range(len(iterable)), iterable))
```

### 7: Sortierte Paare 

```python
liste1 = [5, 2, 8]
liste2 = [7, 1, 6]
paare = list(zip(liste1, liste2))
sortierte_paare = sorted(paare, key=lambda x: x[0] + x[1])
print(sortierte_paare)
```

# Lösungen Komplex Aufgaben

### Lösung 1: Datenanalyse mit `zip` und Bedingungen 

```python
temperaturen = [25, 30, 20, 35]
städte = ["Berlin", "München", "Hamburg", "Frankfurt"]

max_temperatur = max(temperaturen)
min_temperatur = min(temperaturen)

heißeste_stadt = [stadt for temperatur, stadt in zip(temperaturen, städte) if temperatur == max_temperatur]
kälteste_stadt = [stadt for temperatur, stadt in zip(temperaturen, städte) if temperatur == min_temperatur]

print(f"Die heißeste Stadt ist {', '.join(heißeste_stadt)} bei {max_temperatur}°C.")
print(f"Die kälteste Stadt ist {', '.join(kälteste_stadt)} bei {min_temperatur}°C.")
```
