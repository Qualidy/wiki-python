## Lösung

```python
rand_int = np.random.randint(50, size=15) # integer auf grid
rand_float = np.random.random(15) * 50 # floats auf grid

# taxi coordinates aber fahren alle nur auf der vertikalen
t_coords = np.vstack((rand_int, rand_float)).T
print(t_coords) 

# random bool array zum vertauschen von int und float koordinaten
flipmask = np.random.choice(a=[False, True], size=(15)) 
print(flipmask)

# Flippen der Koordinaten an den Stellen wo Flipmask True ist, um die Taxis zu verteilen
t_coords[flipmask] = np.flip(t_coords[flipmask], axis=1) 
print(t_coords)


 # Koordinaten der Kundin
k_coords = np.array([[31, 15.7]])

#Richtige Shape fürs Broadcasting
print(k_coords.shape)

# Differenz von taxis zu kundin (Broadcasting)
diff = t_coords - k_coords 

# Absolutwert aller Differenzen, dann summieren von x und y Differenz für jedes Taxi
absdiff = np.abs(diff).sum(axis = 1)

# Taxi-Index mit dem geringsten Abstand
closest_taxi_num = np.argmin(absdiff)

print(f"Das Taxi Nummer {closest_taxi_num} mit den Koordinaten {t_coords[closest_taxi_num]} ist am nächsten zur Kundin {k_coords}")
```

## Lösung Bonus
Für die Bonusaufgabe, bei der wir genau 15 Kund:innen
haben und jedem eine Taxi zuordnen wollen, so dass die Gesamtstrecke minimiert wird ("Assignment Problem"), verwenden wir den ungarischen Algorithmus oder das Munkres-Verfahren. Dieses Verfahren ist effizient und optimal für solche Zuordnungsprobleme.

Hier ist die Lösung für die Aufgabe und den Bonus:
```python
import numpy as np
from scipy.optimize import linear_sum_assignment

# Zufällige Positionen der Taxis
np.random.seed(0)
rand_int = np.random.randint(50, size=15)  # Ganzzahlige Koordinaten
rand_float = np.random.random(15) * 50     # Gleitkommakoordinaten

# Taxi-Koordinaten auf dem Straßennetz
t_coords = np.vstack((rand_int, rand_float)).T

# Randomisieren der Fahrtrichtungen (horizontal oder vertikal)
flipmask = np.random.choice(a=[False, True], size=(15))
t_coords[flipmask] = np.flip(t_coords[flipmask], axis=1)

print("Taxi-Koordinaten:")
print(t_coords)
print()

# Koordinaten der Kund:innen
num_customers = 15
k_coords = np.random.randint(50, size=(num_customers, 2)) + np.random.rand(num_customers, 2)

print("Kunden-Koordinaten:")
print(k_coords)
print()

# Distanzmatrix zwischen Taxis und Kund:innen mit Broadcasting
t_coords_expanded = t_coords[:, np.newaxis, :]  # (15, 1, 2) für Broadcasting
k_coords_expanded = k_coords[np.newaxis, :, :]  # (1, 15, 2) für Broadcasting

# Berechnung der Manhattan-Distanz
dist_matrix = np.sum(np.abs(t_coords_expanded - k_coords_expanded), axis=-1)

print("Distanzmatrix zwischen Taxis und Kunden:")
print(dist_matrix)
print()

# Lösung des Zuordnungsproblems mit dem ungarischen Algorithmus
row_ind, col_ind = linear_sum_assignment(dist_matrix)

# Ausgabe der Zuordnung
for i in range(num_customers):
    print(f"Kunde {i+1} wird Taxi {col_ind[i]+1} zugewiesen (Entfernung: {dist_matrix[row_ind[i], col_ind[i]]})")
```