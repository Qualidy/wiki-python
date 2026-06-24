# Wiederholung: Args und Kwargs

Diese Einheit wiederholt `*args`, `**kwargs` und das Entpacken mit `*` und
`**`. Ziel ist, dass die Teilnehmenden Funktionssignaturen lesen,
Funktionsaufrufe vorhersagen und flexible Funktionen selbst schreiben koennen.

## Lernziele

Am Ende kann ich ...

- erklaeren, warum `*args` ein Tupel ergibt.
- erklaeren, warum `**kwargs` ein Dictionary ergibt.
- eine Funktion mit Pflichtparametern, Defaults, `*args` und `**kwargs` lesen.
- Listen und Dictionaries beim Funktionsaufruf entpacken.
- entscheiden, wann `*args` oder `**kwargs` sinnvoll ist.

## Einstieg: Der Stern-Operator beim Aufruf

Die Teilnehmenden sollen erst alleine notieren, dann zu zweit vergleichen, dann
wird gemeinsam ausgefuehrt.

```python
values = [2, 4, 6]
settings = {"sep": " | ", "end": "\n\n"}

print(*values, **settings)
```

Der Aufruf ist dasselbe wie:

```python
print(2, 4, 6, sep=" | ", end="\n\n")
```

Ausgabe:

```text
2 | 4 | 6

```

Leitfragen:

- Was waere anders bei `print(values)`?
- Was waere anders bei `print(*values)`?
- Warum darf `settings` nicht einfach ohne `**` uebergeben werden?
- Welche Argumente sind Positionsargumente?
- Welche Argumente sind benannte Argumente?

## Was macht `*` beim Aufruf?

Ein einzelner Stern `*` entpackt eine Liste, ein Tupel oder eine andere
Sequenz in einzelne Positionsargumente.

```python
numbers = [10, 20, 30]

print(numbers)
print(*numbers)
```

Ausgabe:

```text
[10, 20, 30]
10 20 30
```

Ohne Stern bekommt `print()` ein einziges Argument: die ganze Liste.
Mit Stern bekommt `print()` drei einzelne Argumente: `10`, `20`, `30`.

Das funktioniert nicht nur mit `print()`:

```python
def add(a, b, c):
    return a + b + c


values = [2, 4, 6]

print(add(values))   # Fehler
print(add(*values))  # 12
```

`add(values)` ist falsch, weil `add()` drei Argumente erwartet, aber nur eine
Liste bekommt. `add(*values)` entpackt die Liste passend:

```python
add(2, 4, 6)
```

## Was macht `**` beim Aufruf?

Zwei Sterne `**` entpacken ein Dictionary in benannte Argumente.

```python
def create_user(name, active=False, role="user"):
    print(name)
    print(active)
    print(role)


data = {"name": "Ada", "active": True, "role": "admin"}

create_user(**data)
```

Der Aufruf ist dasselbe wie:

```python
create_user(name="Ada", active=True, role="admin")
```

Wichtig: Die Keys im Dictionary muessen zu Parameternamen passen.

```python
data = {"username": "Ada"}

create_user(**data)  # Fehler: unerwartetes Keyword-Argument
```

## `*` und `**`: Aufruf vs. Definition

Die Sterne haben je nach Ort eine andere Richtung:

| Ort | Beispiel | Bedeutung |
|-----|----------|-----------|
| Funktionsaufruf | `func(*values)` | Werte werden entpackt |
| Funktionsaufruf | `func(**data)` | Dictionary wird zu Keyword-Argumenten entpackt |
| Funktionsdefinition | `def func(*args):` | uebrige Positionsargumente werden gesammelt |
| Funktionsdefinition | `def func(**kwargs):` | uebrige Keyword-Argumente werden gesammelt |

Beim Aufruf bedeutet der Stern also: **auseinanderpacken**.
In der Definition bedeutet der Stern: **einsammeln**.

## `*args`

`*args` sammelt beliebig viele Positionsargumente in einem Tupel.

```python
def collect(*items):
    print(items)


collect("Monitor", "Tastatur", "Maus")
```

Ausgabe:

```text
('Monitor', 'Tastatur', 'Maus')
```

Der Funktionsaufruf liefert einzelne Argumente. Die Funktionsdefinition sammelt
sie in `items`.

```python
def total(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


print(total(2, 4, 6))
print(total())
```

Wichtig:

- Der Name `args` ist Konvention. Entscheidend ist der Stern.
- In der Funktion ist `args` ein Tupel.
- `*args` ist sinnvoll, wenn die Anzahl der Werte offen ist.

Der Name nach dem Stern kann auch anders heissen:

```python
def total(*numbers):
    return sum(numbers)
```

Das ist technisch genauso `*args`, nur mit einem sprechenderen Namen.

## `**kwargs`

`**kwargs` sammelt beliebig viele benannte Argumente in einem Dictionary.

```python
def build_profile(**data):
    print(data)


build_profile(name="Ada", role="Developer", active=True)
```

Ausgabe:

```text
{'name': 'Ada', 'role': 'Developer', 'active': True}
```

Der Funktionsaufruf liefert benannte Argumente. Die Funktionsdefinition sammelt
sie in `data`.

Typischer Einsatz:

```python
def build_profile(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


build_profile(name="Ada", role="Developer", active=True)
```

Wichtig:

- Der Name `kwargs` ist Konvention. Entscheidend sind die zwei Sterne.
- In der Funktion ist `kwargs` ein Dictionary.
- `**kwargs` ist sinnvoll, wenn optionale Einstellungen uebergeben werden.

Auch hier darf der Name anders sein:

```python
def configure(**settings):
    return settings
```

Das ist technisch genauso `**kwargs`, nur mit einem sprechenderen Namen.

## Kombination

`*args` und `**kwargs` koennen gemeinsam verwendet werden:

```python
def collect(*items, **options):
    print(items)
    print(options)


collect("Monitor", "Tastatur", urgent=True, owner="Ada")
```

Ausgabe:

```text
('Monitor', 'Tastatur')
{'urgent': True, 'owner': 'Ada'}
```

Positionsargumente landen in `items`. Benannte Argumente landen in `options`.

## Reihenfolge in Funktionssignaturen

Die typische Reihenfolge lautet:

```python
def function(required, default_value=0, *args, **kwargs):
    pass
```

Fuer die Gruppe reicht als robuste Faustregel:

1. normale Pflichtparameter
2. Parameter mit Defaultwerten
3. `*args`
4. `**kwargs`

## Typische Stolperstellen

| Stolperstelle | Korrektur |
|---------------|-----------|
| `args` fuer den Stern halten | Der Stern ist entscheidend, der Name ist Konvention |
| `*args` als Liste erwarten | `args` ist ein Tupel |
| `**kwargs` als Tupel erwarten | `kwargs` ist ein Dictionary |
| Liste ohne `*` uebergeben | Dann ist die ganze Liste ein einzelnes Argument |
| Dictionary ohne `**` uebergeben | Dann ist das ganze Dictionary ein einzelnes Argument |

## Aufgaben

{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/01_args_output.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/02_kwargs_output.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/03_args_kwargs_rechnung.yaml") }}
{{ task(file="tasks/python_grundlagen/wiederholung/args_module_oop/04_entpacken_debuggen.yaml") }}
