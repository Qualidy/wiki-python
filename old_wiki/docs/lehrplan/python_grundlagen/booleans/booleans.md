# Booleans

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/FRlTCZyJCKI?si=JBV2rSoK-cmDkbbV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

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

### Aufgabe: Mathe, hier?!🌶🌶

Verwende im folgenden Code den Satz von De Morgan.

```python
x = 3
y = 8
z = 10

if not (x > 5 or y < 10):
    print("Die Bedingung ist nicht erfüllt.")
else:
    print("Die Bedingung ist erfüllt.")
```

[Lösung](solutions.md#aufgabe-mathe-hier)

## Kürzere if-Bedingungen

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/eY47LZDArlQ?si=3NZd3nWs5dSVIzGH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

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

### Aufgabe: Was ist eigentlich noch wahr heut zu Tage?🌶
Finde für die folgenden Werte heraus, zu welchen Boolschen Wert sie gecastet werden:

```python
a = []
b = [1]
c = set()
d = {1,2,1}
e = 0
f = 1
g = -1
h = 0.0
i = 1.0
j = -1.0
k = ""
l = " "
m = "hallo"
n = None
```

### Aufgabe: Bedingungen kürzen🌶🌶
Kürze den folgenden Code in den if-Bedingungen.

```python
zahl = ...

if zahl % 2 == 0: 
    print("Die Zahl ist gerade.") 
else:   
    print("Die Zahl ist ungerade.")
```

```python
value = ...

if value == True: 
    print("Case 1") 
else:   
    print("Case 2")
```

```python
value = ...
my_list = ...

if False == value and len(my_list) > 0: 
    print("Case 1") 
else:   
    print("Case 2")
```

```python
def func(var):
    if var > 5:
        return True
    else:
        return False
```


### Aufgabe: Es steckt mehr dahinter🌶🌶

Sage voraus, was bei folgendem Code ausgegeben wird. Beantworte daraufhin folgende Fragen:

* Wie werden dei Booleans `True` und `False` bei `*`, `+`, `-` interpretiert?
* Wie funktioniert `and`?
* Wie funktioniert `or`?

```python
print(True + 3)

print(True + True)
print(True + True + True)
print(True * True)
print(True * False)

print(True - True)

print(True and False)
print(True or False)

print(0 and 1)
print(1 and 2)
print(2 and 1)

print(0 or 1)
print([] or [1, 2, 3])
print(2 or 10)
print([1, 2, 3] or [4, 5, 6])
```

[Lösung](solutions.md#aufgabe-was-ist-eigentlich-noch-wahr-heut-zu-tage)

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

### Aufgabe: kurz und knapp🌶

Was ist hier die Konsolenausgabe?

```python
result = []
for i in ["Hallo", 3, " ", 0.0]:
    result.append(i if isinstance(i, str) else "no str")

print(result)
```

### Aufgabe: Versternt🌶🌶🌶
Schreibe eine Funktion `star_text(text, m, symbol)`, die einen Text enthält.
Es sollen alle Wörter mit einem symbol ersetzt werden,
die `m` oder weniger Zeichen sind.
Die Anzahl der Symbole soll der ursprünglichen Wortlänge entsprechen.
Wenn `m` und `symbol` nicht angegeben sind, soll `m=4` und `symbol='*'` gelten.

```python
my_text = "Python macht Spaß und wer das nicht glaubt der programmiert wohl Java oder C++"


def star_text(...):
    ...


star_text(my_text)  # "Python macht *** *** *** *** nicht glaubt *** programmiert **** **** *** ***"
```
