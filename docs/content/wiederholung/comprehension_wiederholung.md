# Comprehensions – Zusammenfassung

🔄 *Wiederholung / Zusammenfassung – Details siehe [List Comprehensions](../comprehensions/list_comp/list_comp.md)*

## Gemeinsame Syntax

Alle Comprehensions folgen demselben Muster:

```
ergebnis = klammer( ausdruck  for variable in iterable  if bedingung )
```

| Typ | Klammern | Beispiel | Ergebnis |
|-----|----------|----------|----------|
| **List** Comprehension | `[ ]` | `[x * 2 for x in range(4)]` | `[0, 2, 4, 6]` |
| **Set** Comprehension | `{ }` | `{x % 3 for x in range(6)}` | `{0, 1, 2}` |
| **Dict** Comprehension | `{ : }` | `{x: x**2 for x in range(4)}` | `{0: 0, 1: 1, 2: 4, 3: 9}` |
| Generator Expression | `( )` | `(x for x in range(4))` | Generator-Objekt |

!!! danger "Es gibt keine Tuple Comprehension!"
    Runde Klammern `()` erzeugen **keinen** Tuple, sondern einen **Generator**:

    ```python
    result = (x * 2 for x in range(4))
    print(type(result))  # <class 'generator'>

    # Für ein Tuple stattdessen:
    result = tuple(x * 2 for x in range(4))
    print(type(result))  # <class 'tuple'>
    ```

## Grundform

Jede Comprehension ersetzt eine Schleife mit `append` / `add` / Zuweisung:

```python
# List Comprehension
quadrate = [x ** 2 for x in range(1, 6)]         # [1, 4, 9, 16, 25]

# Set Comprehension
anfangsbuchstaben = {name[0] for name in ["Anna", "Ali", "Ben", "Clara"]}
# {'A', 'B', 'C'}

# Dict Comprehension
laengen = {wort: len(wort) for wort in ["Hallo", "Welt", "Hi"]}
# {'Hallo': 5, 'Welt': 4, 'Hi': 2}
```

## Mit Filter (`if`)

Der `if`-Teil steht **am Ende** und filtert Elemente heraus:

```python
# Nur gerade Zahlen
gerade = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

# Nur lange Wörter als Set
lang = {w for w in ["Hi", "Hallo", "Hey", "Python"] if len(w) > 3}
# {'Hallo', 'Python'}

# Dict nur mit positiven Werten
noten = {"Mathe": 2, "Sport": 1, "Kunst": 4, "Bio": 1}
gute_noten = {fach: note for fach, note in noten.items() if note <= 2}
# {'Mathe': 2, 'Sport': 1, 'Bio': 1}
```

!!! warning "Position von `if` beachten"
    **Filtern** (weniger Elemente) → `if` **am Ende**:

    ```python
    [x for x in range(10) if x > 5]         # [6, 7, 8, 9]
    ```

    **Bedingter Ausdruck** (gleich viele Elemente, anderer Wert) → `if/else` **am Anfang**:

    ```python
    [x if x > 5 else 0 for x in range(10)]  # [0, 0, 0, 0, 0, 0, 6, 7, 8, 9]
    ```

## Verschachtelte Comprehension

Verschachtelte Schleifen lassen sich in eine Comprehension packen. Die **Reihenfolge der `for`-Klauseln** entspricht der Reihenfolge der verschachtelten Schleifen:

```python
# Traditionell:
paare = []
for farbe in ["rot", "blau"]:
    for groesse in ["S", "M", "L"]:
        paare.append((farbe, groesse))

# Als Comprehension:
paare = [(farbe, groesse) for farbe in ["rot", "blau"] for groesse in ["S", "M", "L"]]
# [('rot', 'S'), ('rot', 'M'), ('rot', 'L'), ('blau', 'S'), ('blau', 'M'), ('blau', 'L')]
```

## Übungsaufgaben

### List Comprehension

{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/01_list_comp.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/02_list_comp_filter.yaml") }}

### Set Comprehension

{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/03_set_comp.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/04_set_comp_filter.yaml") }}

### Dict Comprehension

{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/05_dict_comp.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/06_dict_comp_filter.yaml") }}

### Nested Comprehension

{{ task(file="tasks/python_grundlagen/list_comp/comp_wiederholung/07_nested_lesen.yaml") }}
