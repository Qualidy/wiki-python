# Anonyme Funktionen

Anonyme Funktionen, auch lambda-Funktionen genannt, können dazu genutzt werden, schnell kleine Funktionen
zu definieren, ggf. sogar ohne ihnen einen Namen zu geben.

Betrachten wir die folgende Funktion:

```python
def add_one(x):
    return x + 1
```

lässt sich kurz notieren mit Hilfe des Schlüsselwortes `lambda`. Nach dem `lambda` folgen die Parameter
und nach einem Doppelpunkt der Funktionsrumpf. Dieser muss in eine Zeile passen. Der Funktionsrumpf
wird automatisch zurückgegeben.

```python
lambda x: x + 1
```

Die Funktion oben lässt sich dann so schreiben:

```python
add_one = lambda x: x + 1
print(add_one(2)) # 3
```

Hier ein weiteres Beispiel:

```python
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))
```

Und noch ein Beispiel:

```python
my_add = lambda x, y: x + y
print(my_add(1, 3)) # 4
```

### Aufgabe: In Lambdas ausgedrückt🌶
Verwandle die folgende Funktion in einen lambda-Ausdruck:

```python
def is_even(n):
    return n % 2 == 0
```

<details>
<summary>Lösung</summary>
<pre><code>is_even = lambda n: n % 2 == 0</code></pre>
</details>

```python
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
```

<details>
<summary>Lösung</summary>
<pre><code>maximum = lambda a, b: a if a > b else b</code></pre>
</details>

```python
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
<details>
<summary>Lösung</summary>
<pre><code>fib = lambda n: max(0,n) if n <= 1 else fib(n-1) + fib(n-2)</code></pre>
</details>

```python
def min_max(iterable):
    return min(iterable), max(iterable)
```

<details>
<summary>Lösung</summary>
<pre><code>min_max = lambda iterable: (min(iterable), max(iterable))</code></pre>
</details>

```python
def multiply_with(iterable, number):
    result = []
    for i in iterable:
        result.append(i * number)
    return result
```

<details>
<summary>Lösung</summary>
<pre><code>multiply_with = lambda iterable, number: [i * number for i in iterable]</code></pre>
</details>

```python
def word_lengths(words):
    result = dict()
    for word in words.split(" "):
        result[word] = len(word)    
    return result
```

<details>
<summary>Lösung</summary>
<pre><code>word_lengths = lambda words: {word: len(word) for word in words.split(" ")}</code></pre>
</details>


### Aufgabe: klein, aber fein🌶🌶

Erstelle Lambda-Ausdrücke für die folgenden Fälle:

In einem Lambda-Ausdruck namens `first_and_last` sollen der erste und der letzte Buchstabe eines Strings
zurückgegeben werden.

<details>
<summary>Lösung</summary>
<pre><code>first_and_last = lambda s: (s[0], s[-1])</code></pre>
</details>

Ein Lambda-Ausdruck namens `finde_teiler` erhält eine Liste Ganzzahlen und eine Ganzzahl `n`. `finde Teiler`
soll alle Elemente aus der Liste zurückgeben, die sich Ganzzahlig durch `n` teilen lassen.

<details>
<summary>Lösung</summary>
<pre><code>finde_teiler = lambda lst, n: [i for i in lst if not i % n]</code></pre>
</details>


In einem Lambda-Ausdruck namens `second_biggest` soll das zweit-größte Element in einer Liste gefunden werden.
Gehe dabei davon aus, dass mindestens 2 Elemente in der Liste sind und alle Elmente verschieden.

<details>
<summary>Lösung</summary>

<pre><code>second_biggest = lambda lst: max(x for x in lst if x != max(lst))</code></pre>
</details>




### Aufgabe: Funktionen höherer Ordnung 🌶🌶🌶

Was wird hier auf der Konsole ausgegeben und warum?

```python
high_ord_func = lambda x, func: x + func(x)

print(high_ord_func(2, add_one))  # add_one von vorherigem Besipiel

print(high_ord_func(2, lambda x: x + 3))
```


<details>
<summary>Lösung</summary>
<a href="https://pythontutor.com/render.html#code=add_one%20%3D%20lambda%20x%3A%20x%20%2B%201%0A%0Ahigh_ord_func%20%3D%20lambda%20x,%20func%3A%20x%20%2B%20func%28x%29%0A%0Aprint%28high_ord_func%282,%20add_one%29%29%20%20%23%20von%20vorherigem%20Besipiel%0A%0Aprint%28high_ord_func%282,%20lambda%20x%3A%20x%20%2B%203%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false">
💻Link zum Onlinecompiler</a>

<code>high_ord_func</code> ist eine Lambda-Funktion, die als zweiten Parameter selbst eine Funktion erwartet.
Diese wird in den folgenden zwei Aufrufen bereitgestellt.

Beachte, dass die Funktion <code>lambda x: x+3</code> erstellt und genutzt wurde, ohne ihr einen Namen zu geben.
Sie ist also im wahrsten Sinne des Wortes "anonym" - es gibt keinen Namen unter dem man sie ansprechen könnte.
</details>


### Aufgabe: Schnell noch ne neue Spalte🌶🌶

Erkläre, was der folgende Code tut. Erweitere das DataFrame um eine weitere Spalte, in der Untersucht wird,
ob die Summe von `A` und `B` eine gerade Zahl ist.

```python
import pandas as pd

# Erstellen eines Beispiel-DataFrames
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})

# Verwenden von assign und einer Lambda-Funktion, um eine neue Spalte hinzuzufügen
df = df.assign(
    A_greater_than_B=lambda d: d['A'] > d['B'],
)

print(df)
```

<details>
<summary>Lösung</summary>
Dem DataFrame wird eine neue Spalte hinzugefügt. Dies geschieht über eine anonyme Funktion.
<pre><code>
df = df.assign(
    A_greater_than_B=lambda d: d['A'] > d['B'],
    A_plus_B_is_even=lambda d: not bool((d['A'] + d['B']) % 2),
)</code></pre>
</details>

### Aufgabe: map, filter + lambdas 🌶🌶

Finde heraus, was die Built-in Funktions `map` und `filter` tun. 

Finde heraus, wie diese mit anonymen Funktionen genutzt werden können und baue dafür 3 Beispiele:
1. Ein Beispiel, bei dem jede Zahl einer Liste verdoppelt wird,
2. Ein Beispiel, bei dem jede Zahl einer Liste herausgeschmissen wird, wenn sie kleiner als 10 ist.
3. Ein Beispiel, bei dem zuerst jede Zahl einer Liste verdoppelt wird und aus dem Ergebnis jede Zahl entfernt wird, die kleiner als 10 ist.


<details>
<summary>Lösung</summary>
<pre><code>my_list = [2, 4, 6, 8, 15, 30]

doubling = list(map(lambda x: x * 2, my_list))
print(doubling)

small_out = list(filter(lambda x: x >= 10, my_list))
print(small_out)

doubling_then_small_out = list(filter(lambda x: x >= 10, doubling))
print(doubling_then_small_out)
</code></pre>
</details>

### Aufgabe: Zusammenfassen leicht gemacht🌶
Untersuchen sie den folgenden Code.

```python
from functools import reduce
print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow']))
```

Wie kann dies dabei helfen alle Zahlen in einer Liste zu multiplizieren?

<details>
<summary>Lösung</summary>
<pre><code>from functools import reduce
print(reduce(lambda acc, x: acc * x, [3, 2, 4]))
</code></pre>
</details>

## Statements sind verboten!
In einer Lambda-Funktion können keine Anweisungen verwendet werden.
Hier ist ein Beispiel, wenn versucht wird, assert im Körper einer Lambda-Funktion zu verwenden:

```python
(lambda x: assert x == 2)(2) # SyntaxError: invalid syntax
```

### Aufgabe: Weitere verbotene Statement

Finde weitere verbotene Statements heraus.

Versuche es mal mit folgenden Schlüsselwörtern:

* `if`
* `while`
* `try` & `except`
* `raise`
* `with`
* `import`

<details>
<summary>Lösung</summary>
<pre><code>(lambda x: if x > 0: x)(1)  # SyntaxError</code></pre>

<pre><code>(lambda x: while x > 0: x -= 1)(5)  # SyntaxError</code></pre>

<pre><code>(lambda x: try: x + 1 except: pass)(5)  # SyntaxError</code></pre>

<pre><code>(lambda x: raise Expection)(5)  # SyntaxError</code></pre>

<pre><code>(lambda x: with open(x) as f: f.read())("file.txt")  # SyntaxError</code></pre>

<pre><code>(lambda x: with open(x) as f: f.read())("file.txt")  # SyntaxError</code></pre>

</details>

## Exkurs: Type Annotations
Man kann auch Typanotationnen bei Anonymen Funktionen hinzufügen:

```python
lambda first: str, last: str: first.title() + " " + last.title() -> str
```

## Argumente
Wie bei einem normalen Funktionsobjekt, das mit def definiert ist,
unterstützen Python Lambda-Ausdrücke alle verschiedenen Arten der Argumentübergabe. Dazu gehören:

* Positionale Argumente
* Benannte Argumente (manchmal als Schlüsselwortargumente bezeichnet)
* Variable Liste von Argumenten (oft als Varargs bezeichnet)
* Variable Liste von Schlüsselwortargumenten
* Nur-Schlüsselwortargumente

Die folgenden Beispiele veranschaulichen die Möglichkeiten, wie Sie Argumente an Lambda-Ausdrücke übergeben können:

```python
(lambda x, y, z: x + y + z)(1, 2, 3)
(lambda x, y, z=3: x + y + z)(1, 2)
(lambda x, y, z=3: x + y + z)(1, y=2)
(lambda *args: sum(args))(1,2,3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
```


## Exkurs: Ein geschichtlicher Hintergrund

Alonzo Church hat in den 1930er Jahren die Lambda-Kalkül formalisiert, eine Sprache,
die auf reiner Abstraktion basiert. Lambda-Funktionen werden auch als Lambda-Abstraktionen bezeichnet,
was direkt auf das Abstraktionsmodell von Alonzo Church's Originalkreation verweist.

Der Lambda-Kalkül kann jede Berechnung codieren. Er ist Turing-vollständig,
aber im Gegensatz zum Konzept einer Turing-Maschine ist er rein und behält keinen Zustand.

Funktionale Sprachen haben ihren Ursprung in mathematischer Logik und dem Lambda-Kalkül,
während imperative Programmiersprachen das zustandsbasierte Berechnungsmodell von Alan Turing übernommen haben.

Die beiden Berechnungsmodelle, Lambda-Kalkül und Turing-Maschinen, können ineinander übersetzt werden.
Diese Äquivalenz wird als die Church-Turing-Hypothese bezeichnet.

Funktionale Sprachen übernehmen direkt die Philosophie des Lambda-Kalküls und setzen auf einen deklarativen
Programmieransatz, der Abstraktion, Datenverarbeitung, Komposition und Reinheit (kein Zustand und keine Seiteneffekte)
betont. Beispiele für funktionale Sprachen sind Haskell, Lisp oder Erlang.

Im Gegensatz dazu führte die Turing-Maschine zur imperativen Programmierung, die in Sprachen wie Fortran,
C oder Python zu finden ist.

Der imperative Stil besteht darin, mit Anweisungen zu programmieren und den Programmfluss schrittweise
mit detaillierten Anweisungen zu steuern. Dieser Ansatz fördert Mutation und erfordert das Management von Zuständen.

Die Trennung in beiden Sprachfamilien hat einige Nuancen, da einige funktionale Sprachen imperative Funktionen
integrieren, wie zum Beispiel OCaml, während funktionale Funktionen die imperative Sprachfamilie durch
die Einführung von Lambda-Funktionen in Java oder Python durchdrungen haben.

Python ist an sich keine funktionale Sprache, hat aber frühzeitig einige funktionale Konzepte übernommen.
Im Januar 1994 wurden map(), filter(), reduce() und der Lambda-Operator der Sprache hinzugefügt.
