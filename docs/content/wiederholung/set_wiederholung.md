# Sets – Zusammenfassung

🔄 *Wiederholung / Zusammenfassung – Details siehe [Sets Einführung](../datenstrukturen/sets/sets.md)*

## Eigenschaften

Ein **Set** ist eine **ungeordnete** Sammlung von **einzigartigen** Elementen.

- Keine Duplikate
- Kein Indexzugriff (kein `my_set[0]`)
- Elemente müssen **immutable** sein (z. B. `int`, `str`, `tuple`)
- Das Set selbst ist **mutable** (`add`, `remove`, …)

```python
# Erstellung
zahlen = {1, 2, 3}
aus_liste = set([1, 2, 2, 3])  # {1, 2, 3}
leer = set()                    # nicht {} – das wäre ein dict!
```

## Wichtige Operationen

| Operation | Methode | Operator | Ergebnis für `{1,2,3}` und `{2,3,4}` |
|-----------|---------|----------|---------------------------------------|
| Vereinigung | `a.union(b)` | `a \| b` | `{1, 2, 3, 4}` |
| Schnittmenge | `a.intersection(b)` | `a & b` | `{2, 3}` |
| Differenz | `a.difference(b)` | `a - b` | `{1}` |
| Symm. Differenz | `a.symmetric_difference(b)` | `a ^ b` | `{1, 4}` |

## Elemente hinzufügen & entfernen

```python
s = {1, 2, 3}

s.add(4)        # {1, 2, 3, 4}
s.discard(2)    # {1, 3, 4} – kein Fehler, wenn Element fehlt
s.remove(3)     # {1, 4}    – KeyError, wenn Element fehlt
```

## Subset & Superset

```python
a = {1, 2}
b = {1, 2, 3, 4}

a.issubset(b)    # True  (oder: a <= b)
b.issuperset(a)  # True  (oder: b >= a)
a.isdisjoint(b)  # False – sie haben gemeinsame Elemente
```

## Typischer Einsatz: Duplikate entfernen

```python
namen = ["Anna", "Ben", "Anna", "Clara", "Ben"]
eindeutig = list(set(namen))  # ["Anna", "Ben", "Clara"] (Reihenfolge nicht garantiert)
```

## Übungsaufgaben

{{ task(file="tasks/python_grundlagen/sets/sets_wiederholung/01_set_filtern.yaml") }}
{{ task(file="tasks/python_grundlagen/sets/sets_wiederholung/02_set_vergleich.yaml") }}
{{ task(file="tasks/python_grundlagen/sets/sets_wiederholung/03_set_komplett.yaml") }}
