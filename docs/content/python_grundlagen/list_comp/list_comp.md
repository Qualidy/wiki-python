# List Comprehensions

List Comprehensions in Python sind eine elegante und effiziente Möglichkeit um Listen zu erstellen und Operationen auf 
ihren Elementen auszuführen. Sie bieten eine klare und prägnante Alternative zu traditionellen Schleifen
und Funktionsaufrufen. List Comprehensions sind eine typische Struktur, die man in Python-Code häufig findet.

## Problemstellungen

{{ youtube_video("https://www.youtube.com/embed/Qj0obBFgKzE?si=_b4ZDnGz5QHvUmTj") }}

Stellen wir uns vor, wir möchten aus einer vorhandenen Liste eine neue Liste erstellen, in der jedes Element aufgrund
einer Bedingung oder einer Operation verändert wurde. Traditionell würden wir dazu eine for-Schleife verwenden, die
über die alte Liste iteriert, die Operation durchführt und das Ergebnis in einer neuen Liste speichert. Das würde dann
so aussehen:

[💻 Online Compiler](https://pythontutor.com/render.html#code=quadrate%20%3D%20%5B%5D%0Afor%20i%20in%20range%281,%206%29%3A%0A%20%20%20%20quadrate.append%28i%20*%20i%29%0A%0Aprint%28quadrate%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
quadrate = []
for i in range(1, 6):
    quadrate.append(i * i)

print(quadrate)
```

List Comprehensions vereinfachen diesen Code, indem sie die gesamte Logik in eine einzige, lesbare Zeile komprimieren. Sie
können Bedingungen anwenden, Funktionen aufrufen und die resultierende Liste direkt erzeugen, was den Code wesentlich
sauberer und eleganter macht.

[💻 Online Compiler](https://pythontutor.com/render.html#code=quadrate%20%3D%20%5Bi%20*%20i%20for%20i%20in%20range%281,%206%29%5D%0A%0Aprint%28quadrate%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
quadrate = [i * i for i in range(1, 6)]

print(quadrate)
```

<pre>
# Without List Comprehension
<span style="color: #1714db">quadrate = []</span>
<span style="color: #1f7d45">for i in range(1, 6):</span>
    <span style="color: #db2114">quadrate.append(i * i)</span>

# List Comprehension
<span style="color: #1714db">quadrate = [</span><span style="color: #db2114">i * i</span> <span style="color: #1f7d45">for i in range(1, 6)</span><span style="color: #1714db">]</span>
</pre>

Die einfachste Form der List Comprehension sieht also so aus:

`[ausdruck(item) for item in iterable]`

## Motivation für List Comprehensions

* **Kompakter Code**: List Comprehensions ermöglichen es, Schleifen und bedingte Anweisungen in einer Zeile zu 
schreiben, wodurch der Code kürzer und, wenn man es nicht übertreibt, auch leichter lesbar wird.

* **Performance**: Sie sind oft schneller als traditionelle Schleifen, besonders bei der Erstellung großer Listen.

List Comprehensions sind ein hervorragendes Beispiel für **pythonic** Code, also Code der typisch für Python-Programme
ist und die **jeder kennen und verstehen sollte**.

# Aufgaben zu einfachen List Comprehensions

{{ task(file="tasks/python_grundlagen/list_comp/list_comp/01_quadrate_erstellen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/02_zeichenkettenlangen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/03_absolute_werte.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/04_string_in_grobuchstaben.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/05_wurzeln_ziehen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/06_tupel_erstellen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/07_teile_von_strings.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/08_durchschnittswerte.yaml") }}
## Elemente filtern

{{ youtube_video("https://www.youtube.com/embed/uIyZYOW5jFA?si=liyEgrxkrb6cDEJd") }}

Es ist bei einer List Comprehension einfach möglich bestimmte Elemente
aus der Liste unter einer Bedingung zu entfernen. Der folgende Code:

[💻 Online Compiler](https://pythontutor.com/render.html#code=words%20%3D%20%5B%22Python%22,%20%22ist%22,%20%22cool%22%5D%0A%0Aresult%20%3D%20%5B%5D%0Afor%20word%20in%20words%3A%0A%20%20%20%20if%20len%28word%29%20%3E%203%3A%0A%20%20%20%20%20%20%20%20result.append%28word%29%0A%20%20%20%20%20%20%20%20%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
words = ["Python", "ist", "cool"]

result = []
for word in words:
    if len(word) > 3:
        result.append(word)
        
print(result)
```

lässt sich zu diesem vereinfachen:

[💻 Online Compiler](https://pythontutor.com/render.html#code=words%20%3D%20%5B%22Python%22,%20%22ist%22,%20%22cool%22%5D%0A%0Aresult%20%3D%20%5Bword%20for%20word%20in%20words%20if%20len%28word%29%20%3E%203%5D%0A%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=falsehttps://pythontutor.com/render.html#code=words%20%3D%20%5B%22Python%22,%20%22ist%22,%20%22cool%22%5D%0A%0Aresult%20%3D%20%5Bword%20for%20word%20in%20words%20if%20len%28word%29%20%3E%203%5D%0A%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
words = ["Python", "ist", "cool"]

result = [word for word in words if len(word) > 3]

print(result)
```

<pre>
# Without List Comprehension
<span style="color: #1714db">result = []</span>
<span style="color: #1f7d45">for word in words:</span>
    <span style="color: #bd9017">if len(word) > 3:</span>
        <span style="color: #db2114">result.append(word)</span>

# List Comprehension
<span style="color: #1714db">result = [</span><span style="color: #db2114">word</span> <span style="color: #1f7d45">for word in words</span><span style="color: #1714db"> <span style="color: #bd9017">if len(word) > 3</span>]</span>
</pre>

## Bedingte Einsetzung

{{ youtube_video("https://www.youtube.com/embed/3qrNUZzcBZA?si=D9D5bVlSibdZ2tr3") }}

Im letzten Beispiel haben wir gesehen, wie wir Elemente filtern können.
Manchmal möchte man aber auch verschiedene Operationen auf einem
Element durchführen, basierend auf einer Bedingung. Hier lässt sich
der ternäre Operater nutzen. Den folgendne Code

[💻 Online Compiler](https://pythontutor.com/render.html#code=result%20%3D%20%5B%5D%0Afor%20i%20in%20range%286%29%3A%0A%20%20%20%20if%20i%252%3A%0A%20%20%20%20%20%20%20%20result.append%28i%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20result.append%28i*i%29%0A%20%20%20%20%20%20%20%20%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
result = []
for i in range(6):
    if i%2:
        result.append(i)
    else:
        result.append(i*i)
        
print(result)
```

vereinfachen wir zunächst zu

[💻 Online Compiler](https://pythontutor.com/render.html#code=result%20%3D%20%5B%5D%0Afor%20i%20in%20range%286%29%3A%0A%20%20%20%20result.append%28i%20if%20i%20%25%202%20else%20i%20*%20i%29%0A%20%20%20%20%20%20%20%20%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
result = []
for i in range(6):
    result.append(i if i % 2 else i * i)
        
print(result)
```

und abschließend:

[💻 Online Compiler](https://pythontutor.com/render.html#code=result%20%3D%20%5Bi%20if%20i%20%25%202%20else%20i%20*%20i%20for%20i%20in%20range%286%29%5D%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
result = [i if i % 2 else i * i for i in range(6)]
print(result)
```

<pre>
# Without List Comprehension
<span style="color: #1714db">result = []</span>
<span style="color: #1f7d45">for i in range(6):</span>
    <span style="color: #db2114">quadrate.append(i if i % 2 else i * i)</span>

# List Comprehension
<span style="color: #1714db">result = [</span><span style="color: #db2114">i if i % 2 else i * i</span> <span style="color: #1f7d45">for i in range(6)</span><span style="color: #1714db">]</span>
</pre>

{{ task(file="tasks/python_grundlagen/list_comp/list_comp/09_gerade_zahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/10_filtern_nach_bedingung.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/11_nicht_leere_strings.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/12_fizz_buzz.yaml") }}
## Verschachtelte List Comprehension

{{ youtube_video("https://www.youtube.com/embed/jbmW7lw2JHk?si=Oca4jv2Qy76DIkNy") }}

Es ist auch möglich verschachtelte Schleifen in List Comprehensions
zu übersetzen. 

Ausgangscode:

[💻 Online Compiler](https://pythontutor.com/render.html#code=result%20%3D%20%5B%5D%0Afor%20i%20in%20range%284%29%3A%0A%20%20%20%20for%20j%20in%20range%284%29%3A%0A%20%20%20%20%20%20%20%20result.append%28i%20*%20j%29%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
result = []
for i in range(4):
    for j in range(4):
        result.append(i * j)
print(result)
```

Gekürzt:

[💻 Online Compiler](https://pythontutor.com/render.html#code=result%20%3D%20%5Bi%20*%20j%20for%20i%20in%20range%284%29%20for%20j%20in%20range%284%29%5D%0A%0Aprint%28result%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
result = [i * j for i in range(4) for j in range(4)]

print(result)
```

<pre>
# Without List Comprehension
<span style="color: #1714db">result = []</span>
<span style="color: #1f7d45">for i in range(4):</span>
    <span style="color: #bd9017">for j in range(4):</span>
        <span style="color: #db2114">result.append(i * j)</span>

# List Comprehension
<span style="color: #1714db">result = [</span><span style="color: #db2114">i * j</span> <span style="color: #1f7d45">for i in range(4)</span><span style="color: #1714db"> <span style="color: #bd9017">for j in range(4)</span>]</span>
</pre>

{{ task(file="tasks/python_grundlagen/list_comp/list_comp/13_bedingung_fehlt.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/14_liste_von_listen_abflachen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/15_verschachtelung.yaml") }}
## List Comprehensions nicht nur für Listen

{{ youtube_video("https://www.youtube.com/embed/SOLNaNL13xc?si=ZHdKm3A_8t3zwi_S") }}

Tatsächlich lassen sich List Comprehensions nicht nur für Listen
verwenden, man kann sie auch für Dictionaries oder Sets nutzen:

```python
new_set = {abs(x) for x in range(-3, 4)} # {0, 1, 2, 3}

new_dict = {word: len(word) for word in ["Hi", "was", "geht"]} # {"Hi": 2, "was": 3, "geht": 4}
```

{{ task(file="tasks/python_grundlagen/list_comp/list_comp/16_dictionary_comprehensions.yaml") }}
## Generator - was dahintersteckt

{{ youtube_video("https://www.youtube.com/embed/Uc3u3nqnhhU?si=h8P5pr2ItRvyT6QR") }}

Vielleicht ist dir aufgefallen, dass die folgende Syntax nicht
zu einem Tupel führt, sondern man einen Generator zurückbekommt:

```python
my_gen = (i * 2 for i in range(4))

print(my_gen) # <generator object <genexpr> at 0x000001F7191D7B50>
print(type(my_gen)) # <class 'generator'>
```

Tatsächlich handelt es sich hier in der ersten Zeile um eine 
[Generator Expression](https://docs.python.org/3/glossary.html#term-generator-expression).

Ein [generator](https://docs.python.org/3/glossary.html#term-generator)
kann mit der Methode `next` um das nächste Element gebeten werden.
Das geht so lange, bis eine `StopIteration` Exception geworfen wird.

```python
my_gen = (i * 2 for i in range(4))

print(next(my_gen)) # 0
print(next(my_gen)) # 2
print(next(my_gen)) # 4
print(next(my_gen)) # 6
print(next(my_gen)) # StopIteration
```

So ein `generator` lässt sich so auch klasse mit einer `for`-Schleife
durchlaufen, da diese intern immer wieder die `next`-Methode aufruft,
bis es zur `StopIteration` Exception kommt.

```python
summe = 0
for i in (i * 2 for i in range(4)):
    summe += i

print(summe)
```

Dieser Code lässt sich tatsächlich noch kürzen zu:

```python
summe = sum(i * 2 for i in range(4))
print(summe)
```

Es gibt diverse eingebaute Pythonmethoden, die so mit Iteratoren
umgehen können. Dazu gehören: `all`, `any`, `map` oder `tuple`. Du findest noch 
weiter [hier in der Dokumentation](https://docs.python.org/3/library/functions.html),
wenn du nach den Funktionen suchst, die `iterable`
als Parameter erwarten.

{{ task(file="tasks/python_grundlagen/list_comp/list_comp/17_anzahl_der_vokale_zahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/list_comp/list_comp/18_use_tuple.yaml") }}
