# Args & Kwargs in Python 🌶️️🌶️️
[60min]

In Python gibt es zwei wichtige Konzepte im Zusammenhang mit Funktionen, nämlich `*args` und `**kwargs`. Diese ermöglichen es, Funktionen flexibler zu gestalten und mit variabler Anzahl von Argumenten umzugehen.

## Args (`*args`):

`*args` ermöglicht es einer Funktion, eine variable Anzahl von nicht-schlüsselwortbasierten Argumenten zu akzeptieren. Das bedeutet, dass die Anzahl der Argumente nicht im Voraus festgelegt ist.

```python
def funktionsname(arg1, *args):
    # Funktionscode
    pass
```

Beispiel:

```python
def addiere_zahlen(zahl1, *zahlen):
    ergebnis = zahl1
    for zahl in zahlen:
        ergebnis += zahl
    return ergebnis

summe = addiere_zahlen(1, 2, 3, 4, 5)
print(summe)  # Ausgabe: 15
```

## Kwargs (`**kwargs`):

`**kwargs` ermöglicht es einer Funktion, eine variable Anzahl von schlüsselwortbasierten Argumenten (Key-Value-Paaren) zu akzeptieren.

```python
def funktionsname(arg1, **kwargs):
    # Funktionscode
    pass
```

Beispiel:

```python
def drucke_infos(name, **infos):
    print(f"Name: {name}")
    for key, value in infos.items():
        print(f"{key}: {value}")

drucke_infos("Max", alter=23, stadt="Wolfsburg", beruf="Softwareentwickler")
```

# Aufgaben:
[240min]

{{ task(file="tasks/python_grundlagen/12_args_kwargs/01_args_verwendung.yaml") }}

{{ task(file="tasks/python_grundlagen/12_args_kwargs/02_kwargs_verwendung.yaml") }}

{{ task(file="tasks/python_grundlagen/12_args_kwargs/03_kombination_aus_beidem.yaml") }}

{{ task(file="tasks/python_grundlagen/12_args_kwargs/04_personalinformationen_verarbeiten.yaml") }}
