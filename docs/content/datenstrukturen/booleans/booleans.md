# Booleans

{{ youtube_video("https://www.youtube.com/embed/FRlTCZyJCKI?si=JBV2rSoK-cmDkbbV") }}

`bool` ist dein Datentyp, von dem es genau zwei Instanzen gibt: `True` und `False`.

Wir können diese Objekte mit `and`, `or` und `not` verknüpfen.
Dies funktioniert genau so, wie es aus der Mathematik mit den Operatoren ∧, ∨ und ¬.

```python
a = True
b = False
print(a and b)
print(a or b)
print(not b)
```

{{ task(file="tasks/python_grundlagen/booleans/booleans/01_mathe_hier.yaml") }}
## Kürzere if-Bedingungen

{{ youtube_video("https://www.youtube.com/embed/eY47LZDArlQ?si=3NZd3nWs5dSVIzGH") }}

In Python können viele Objekte in Booleans übersetzt werden. Dies ermöglicht einen kürzeren Code.
So werden z.B. leere Listen immer zu `False` in einer `if`-Bedingung ausgewertet.

[💻 Online Compiler](https://pythontutor.com/render.html#code=my_list%20%3D%20%5B1,2,3%5D%0A%0Aif%20len%28my_list%29%20%3E%200%3A%0A%20%20%20%20print%28%22Liste%20ist%20nicht%20leer%22%29%0Aelse%3A%0A%20%20%20%20print%28%22List%20ist%20leer%22%29%0A%0A%23%23%20Ist%20%C3%A4quivalent%20zu%3A%0A%0Aif%20my_list%3A%0A%20%20%20%20print%28%22Liste%20ist%20nicht%20leer%22%29%0Aelse%3A%0A%20%20%20%20print%28%22List%20ist%20leer%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
my_list = [1,2,3]

if len(my_list) > 0:
    print("Liste ist nicht leer")
else:
    print("List ist leer")

## Ist äquivalent zu:

if my_list:
    print("Liste ist nicht leer")
else:
    print("List ist leer")
```

Man muss sich zwar etwas an die Leseweise gewöhnen, wird aber vorzugsweise verwendet.

Um herauszufinden, wie zu welchem Wert ein Element auswertet, kann die Funktion `bool` genutzt werden.

```python
print(bool([])) # False
print(bool([1,2,3])) # True
```

{{ task(file="tasks/python_grundlagen/booleans/booleans/02_was_ist_eigentlich_noch_wahr_heut_zu_tage.yaml") }}
{{ task(file="tasks/python_grundlagen/booleans/booleans/03_bedingungen_kurzen.yaml") }}
{{ task(file="tasks/python_grundlagen/booleans/booleans/04_es_steckt_mehr_dahinter.yaml") }}
## Ternärer Operator

In Python gibt es noch eine schöne kurzschreibweise, um die bedingte Belegung von Varaiablen in einer Zeile
zu lösen:

```python
goals = ...

if goals > 5:
    comment = "Wow"
else:
    comment = "Okay"

# Same with Ternary expression:

comment_2 = "Super" if goals > 5 else "Aha"

print(comment_2)
```

Dies ist eine elegente Möglichkeit in **einfachen** Fällen den Code zu kürzen. Man sollte hier 
individuell schauen, ob der Code hier wirklich **leserlicher** wird.

{{ task(file="tasks/python_grundlagen/booleans/booleans/05_kurz_und_knapp.yaml") }}
{{ task(file="tasks/python_grundlagen/booleans/booleans/06_versternt.yaml") }}
