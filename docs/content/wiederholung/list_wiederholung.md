# Listen & List-Methoden – Zusammenfassung

🔄 *Wiederholung / Zusammenfassung – Details siehe [Listen Einführung](../datenstrukturen/lists/lists.md) und [List Comprehensions](../comprehensions/list_comp/list_comp.md)*

## Eigenschaften

- **Geordnet** – Elemente haben eine feste Reihenfolge
- **Veränderlich (mutable)** – Elemente können geändert, hinzugefügt und entfernt werden
- **Duplikate erlaubt**
- **Dynamisch** – Größe passt sich automatisch an

```python
leer = []
zahlen = [1, 2, 3]
gemischt = [1, "Hallo", True, 3.14]
```

## Elemente hinzufügen

| Methode | Beschreibung | Beispiel |
|---------|-------------|----------|
| `append(x)` | Fügt **ein** Element am Ende hinzu | `[1, 2].append(3)` → `[1, 2, 3]` |
| `insert(i, x)` | Fügt Element an Position `i` ein | `[1, 3].insert(1, 2)` → `[1, 2, 3]` |
| `extend(iter)` | Fügt **alle** Elemente eines Iterables hinzu | `[1].extend([2, 3])` → `[1, 2, 3]` |

!!! warning "Häufiger Fehler"
    `append()` vs. `extend()` – `append` fügt das Objekt **als Ganzes** hinzu:

    ```python
    a = [1, 2]
    a.append([3, 4])   # [1, 2, [3, 4]]  ← verschachtelt!

    b = [1, 2]
    b.extend([3, 4])   # [1, 2, 3, 4]    ← flach
    ```

## Elemente entfernen

| Methode | Beschreibung | Fehler wenn nicht vorhanden? |
|---------|-------------|------------------------------|
| `remove(x)` | Entfernt **erstes** Vorkommen von `x` | `ValueError` |
| `pop(i)` | Entfernt Element an Index `i` und **gibt es zurück** | `IndexError` |
| `pop()` | Entfernt **letztes** Element und gibt es zurück | `IndexError` (bei leerer Liste) |
| `clear()` | Entfernt **alle** Elemente | – |
| `del liste[i]` | Löscht Element an Index `i` | `IndexError` |

## Suchen & Zählen

```python
farben = ["rot", "grün", "blau", "rot"]

farben.index("grün")   # 1
farben.count("rot")    # 2
"blau" in farben       # True
```

!!! warning "`index()` wirft `ValueError`, wenn das Element nicht existiert."

## Sortieren & Umkehren

```python
zahlen = [3, 1, 4, 1, 5]

# In-place (verändert die Liste)
zahlen.sort()              # [1, 1, 3, 4, 5]
zahlen.sort(reverse=True)  # [5, 4, 3, 1, 1]
zahlen.reverse()           # kehrt aktuelle Reihenfolge um

# Neue Liste (Original bleibt unverändert)
sortiert = sorted(zahlen)          # gibt neue Liste zurück
umgekehrt = list(reversed(zahlen)) # gibt neue Liste zurück
```

!!! warning "PCAP-Falle"
    `sort()` gibt `None` zurück, nicht die sortierte Liste!

    ```python
    ergebnis = [3, 1, 2].sort()  # ergebnis ist None!
    ```

## Slicing

```python
buchstaben = ["a", "b", "c", "d", "e"]

buchstaben[1:3]    # ["b", "c"]        – Index 1 bis 2
buchstaben[:3]     # ["a", "b", "c"]   – Anfang bis Index 2
buchstaben[2:]     # ["c", "d", "e"]   – Index 2 bis Ende
buchstaben[::2]    # ["a", "c", "e"]   – jedes zweite Element
buchstaben[::-1]   # ["e", "d", "c", "b", "a"] – umgekehrt
```

## Kopieren

```python
original = [1, 2, 3]

# Flache Kopie (shallow copy)
kopie1 = original.copy()
kopie2 = original[:]
kopie3 = list(original)

# Achtung bei verschachtelten Listen!
import copy
tiefe_kopie = copy.deepcopy(original)  # kopiert auch innere Objekte
```

## List Comprehensions

```python
# Grundform
quadrate = [x ** 2 for x in range(5)]          # [0, 1, 4, 9, 16]

# Mit Filter
gerade = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Mit bedingtem Ausdruck
label = ["gerade" if x % 2 == 0 else "ungerade" for x in range(4)]
# ["gerade", "ungerade", "gerade", "ungerade"]
```

## Übungsaufgaben

{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/01_append_extend.yaml") }}
{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/02_remove_pop.yaml") }}
{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/03_sort_sorted.yaml") }}
{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/04_slicing.yaml") }}
{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/05_index_count_in.yaml") }}
{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/06_list_comprehension.yaml") }}
{{ task(file="tasks/python_grundlagen/lists/lists_wiederholung/07_kopie_vs_referenz.yaml") }}
