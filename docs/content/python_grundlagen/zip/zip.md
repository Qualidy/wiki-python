# `zip`-Funktion

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/KUty_pblHtU?si=TmgZ3i6cMXFTH8Hc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Die `zip`-Funktion in Python ist ein nützliches Werkzeug, um mehrere iterierbare Objekte – wie Listen oder Tupel –
parallel zu durchlaufen. Sie fasst die Elemente mehrerer Iteratoren zu Tupeln zusammen und gibt einen Iterator über
diese Tupel zurück. Am häufigsten wird `zip` direkt in Schleifen genutzt:

[💻 Online Compiler](https://pythontutor.com/render.html#code=names%20%3D%20%5B%22Karl%22,%20%22Gustav%22,%20%22Olga%22%5D%0Aages%20%3D%20%5B13,%2045,%2028%5D%0A%0Afor%20name,%20age%20in%20zip%28names,%20ages%29%3A%0A%20%20%20%20print%28f%22%7Bname%7D%20ist%20%7Bage%7D%20Jahre%20alt.%22%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
names = ["Karl", "Gustav", "Olga"]
ages = [13, 45, 28]

for name, age in zip(names, ages):
    print(f"{name} ist {age} Jahre alt.")
```


### Aufgabe: Elementweise Multiplikation 🌶️️🌶️️

Nimm zwei Listen von Ganzzahlen und multipliziere sie elementweise mithilfe von `zip`.

```python
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]

result = [5, 12, 21, 36]
```

### Aufgabe: Ungerade Summanden 🌶️️🌶️️

Schreibe eine Funktion, zwei elementweise addiert, wenn das erste Elemente ungerade ist.

```python
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]

result = [6, 10]
```

### Aufgabe: Zuviel oder zu wenig🌶
Wie oft wird die folgende Schleife durchlaufen?

```python
for i, j in zip(range(10), range(20)):
    print(i, j)
```

### Aufgabe: Zusammenführen von Wörtern 🌶️️🌶️️

Gegeben sind zwei Listen von Strings `adjektive` und `nomen`.
Schreibe zwei list Comprehensions. Bei der ersten sollen alle möglichen Kombinationen aus 
Adjektiven und Nomen entstehen und bei der zweiten nur das erste Adjektiv mit dem ersten Nomen,
das zweite mit dem zweiten, usw.

### Aufgabe: Anzahl der Übereinstimmungen zählen 🌶️️🌶️️🌶️️

Erstelle eine Funktion, die mithilfe von `zip` die Anzahl der Übereinstimmungen zwischen zwei Listen `liste1`
und `liste2` zählt. Das heißt. sie zählt, an wie vielen Stellen die beiden Listen den gleichen Eintrag haben.

[Lösung](solutions.md#lösungen-für-einfache-aufgaben)

## Was steckt dahinter?

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dW9S8YKIf6A?si=UetIRpY-8NJkG3sg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Wir sehen im folgenden Code, dass die Funktion `zip` uns eine Klasse von Typ `zip` zurückgibt, höhö.
Diese ist ein Iterable und liefert über die Methode `next` nach und nach
die erstellten Paare.

[💻 Online Compiler](https://pythontutor.com/render.html#code=zahlen%20%3D%20%5B1,%202,%203%5D%0Abuchstaben%20%3D%20%5B'a',%20'b',%20'c'%5D%0Agezippt%20%3D%20zip%28zahlen,%20buchstaben%29%0A%0Aprint%28type%28gezippt%29%29%0A%0Aprint%28next%28gezippt%29%29%0Aprint%28next%28gezippt%29%29%0Aprint%28next%28gezippt%29%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
zahlen = [1, 2, 3]
buchstaben = ['a', 'b', 'c']
gezippt = zip(zahlen, buchstaben)

print(type(gezippt))

print(next(gezippt))
print(next(gezippt))
print(next(gezippt))
```


Wenn wir `list` auf `gezipped` anwenden, sehen wir, dass wir praktisch eine Liste von Paaren (Tupeln) erhalten.

[💻 Online Compiler](https://pythontutor.com/render.html#code=zahlen%20%3D%20%5B1,%202,%203%5D%0Abuchstaben%20%3D%20%5B'a',%20'b',%20'c'%5D%0Agezippt%20%3D%20zip%28zahlen,%20buchstaben%29%0A%0Azipped_list%20%3D%20list%28gezippt%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
zahlen = [1, 2, 3]
buchstaben = ['a', 'b', 'c']
gezippt = zip(zahlen, buchstaben)

zipped_list = list(gezippt)
```


### Aufgabe: Dictionary erstellen 🌶️️
Sage voraus, was der folgende Code tut und begründe warum.

```python
schlüssel = ['A', 'B', 'C']
werte = [1, 2, 3]
ergebnis = dict(zip(schlüssel, werte))
print(ergebnis)
```

### Aufgabe: Eigener Zipper 🌶🌶🌶

Baue eine Funktion `my_zip(list1, list2)`, die die Funktionalität von `zip` für zwei Listen imitiert, ohne
die Funktion `zip` zu verwenden. Dabei muss kein Generator erstellt werden, sondern es genügt direkt die
Liste von Paaren zurückzugeben.

[Lösung](solutions.md#was-steckt-dahinter)


## Verwendung von `zip()` mit mehr als zwei Iterables

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/RT2AcizCqIo?si=yQ9eUBnvY0alIKXF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Es ist bei `zip` erlaubt eine beliebige Anzahl von Parametern zu übergeben:

[💻 Online Compiler](https://pythontutor.com/render.html#code=zahlen%20%3D%20%5B1,%202,%203%5D%0Abuchstaben%20%3D%20%5B'a',%20'b',%20'c'%5D%0Asymbole%20%3D%20%5B'!',%20'%40',%20'%23'%5D%0Afor%20z,%20b,%20s%20in%20zip%28zahlen,%20buchstaben,%20symbole%29%3A%0A%20%20%20%20print%28f%22Zahl%3A%20%7Bz%7D,%20Buchstabe%3A%7Bb%7D,%20Symbol%3A%20%7Bs%7D%22%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
zahlen = [1, 2, 3]
buchstaben = ['a', 'b', 'c']
symbole = ['!', '@', '#']
for z, b, s in zip(zahlen, buchstaben, symbole):
    print(f"Zahl: {z}, Buchstabe:{b}, Symbol: {s}")
```


### Aufgabe: Maximaler Wert pro Position 🌶️️🌶️️

Gegeben sind drei Listen von Zahlen `liste1`, `liste2` und `liste3`. Verwende `zip`, um eine Liste der maximalen Werte pro
Position zu erstellen.

### Aufgabe: Mittelwert berechnen 🌶️️🌶️️

Berechne den Mittelwert von drei Listen `liste1`, `liste2` und `liste3`, indem du `zip` und eine Schleife verwendest.

### Aufgabe: zip in slicing🌶🌶🌶

Bilde alle Summen dreier aufeinanderfolgenden Elemente einer Liste.

```python
numbers = [1, 3, 5, 7, 8, 3, 0, 1, 1, 3]
triple_sum = [8, 15, 20, 18, 11, 4, 2, 5]
```

[Lösung](solutions.md#verwendung-von-zip-mit-mehr-als-zwei-iterables)

## Komplexes Beispiel mit der `zip()`-Funktion in Python

Stellen wir uns vor, wir haben einen Wettbewerb, bei dem Teilnehmer in verschiedenen Kategorien Punkte sammeln. Am Ende
möchten wir die Gesamtpunktzahl jedes Teilnehmers berechnen.

Wir haben zwei Listen: eine mit den Namen der Teilnehmer und eine weitere mit Listen von Punkten, die jeder Teilnehmer
in den einzelnen Kategorien gesammelt hat. Unser Ziel ist es, die Gesamtpunktzahl für jeden Teilnehmer zu berechnen.

### Schritt-für-Schritt-Anleitung

Wir bereiten einige Daten vor:

```python
teilnehmer = ["Anna", "Bernd", "Carla"]
punkte = [[10, 20, 30], [15, 25, 35], [10, 30, 50]]
```

Wir verwenden `zip()`, um die Namen der Teilnehmer mit ihren entsprechenden Punktelisten zu kombinieren.

```python
kombiniert = zip(teilnehmer, punkte)
```

Für jeden Teilnehmer addieren wir die Punkte aus allen Kategorien, um die Gesamtpunktzahl zu ermitteln.

Diese Zeile erstellt ein Dictionary, in dem jeder Teilnehmername einem Gesamtpunktwert zugeordnet ist.

```python
gesamtpunktzahl = {name: sum(punkte) for name, punkte in kombiniert}
print(gesamtpunktzahl)
```

Zusammengefasst macht das den folgenden Code:

[💻 Online Compiler](https://pythontutor.com/render.html#code=teilnehmer%20%3D%20%5B%22Anna%22,%20%22Bernd%22,%20%22Carla%22%5D%0Apunkte%20%3D%20%5B%5B10,%2020,%2030%5D,%20%5B15,%2025,%2035%5D,%20%5B10,%2030,%2050%5D%5D%0A%0Agesamtpunktzahl%20%3D%20%7Bname%3A%20sum%28punkte%29%20for%20name,%20punkte%20in%20zip%28teilnehmer,%20punkte%29%7D%0A%0Aprint%28gesamtpunktzahl%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
teilnehmer = ["Anna", "Bernd", "Carla"]
punkte = [[10, 20, 30], [15, 25, 35], [10, 30, 50]]

gesamtpunktzahl = {name: sum(punkte) for name, punkte in zip(teilnehmer, punkte)}

print(gesamtpunktzahl)
```


### Aufgabe: Eine Welt ohne zip (Java)
Schreibe den obigen Code, ohne List Comprehension und ohne `zip`.

[Lösung](solutions.md#komplexes-beispiel-mit-der-zip-funktion-in-python)


# enumerate

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/o5Q4vhIG5h4?si=Fc0zA2VhL1B-7n4a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Eine weitere sehr nützliche Methode ist `enumerate`. Sie gibt Zugriff auf den Index und
das Element eines Iterables gleichzeitig:

[💻 Online Compiler](https://pythontutor.com/render.html#code=for%20i,%20name%20in%20enumerate%28%5B%22Karl%22,%20%22Gustav%22,%20%22Franz%22%5D%29%3A%0A%20%20%20%20print%28f%22Person%20No.%20%7Bi%7D%20is%20%7Bname%7D%22%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
for i, name in enumerate(["Karl", "Gustav", "Franz"]):
    print(f"Person No. {i} is {name}")
```


Dies ist sehr, sehr, seeeehr nützlich in allen möglichen Fällen, in denen man nicht 
Zugriff auf das Element braucht, sondern tatsächlich auch auf die Position.

### Aufgabe: Wo sind die größten🌶🌶
Erstelle Code, der die Indizes aller größten Elemente in einer Liste von Zahlen ermittelt.

```python
numbers = [1,3,5,3,5,1]
positions_of_maxima = [2, 4]
```

### Aufgabe: Das kann ich doch auch🌶🌶🌶

Erstelle mithilfe von `zip` eine Funktion `my_enumerate`, das die Funktion `enumerate`
imitiert.

[Lösung](solutions.md#enumerate)
