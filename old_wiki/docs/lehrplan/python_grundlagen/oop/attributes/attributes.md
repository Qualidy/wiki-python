# Attribute

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Wa0DjW0Zn4Y?si=KNRedy36pi8kcgsH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Bisher hatten unsere Instanzen noch keine Eigenschaften. Eigenschaften werden auch als **Attribute** bezeichnet.

## Dynamische Attribute

Wir können unseren Instanzen händisch Attribute hinzufügen:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20pass%0A%0A%0Ax%20%3D%20Roboter%28%29%0Ay%20%3D%20Roboter%28%29%0A%0Ax.baujahr%20%3D%201990%0Ax.name%20%3D%20'Marvin'%0Ay.baujahr%20%3D%202005%0Ay.name%20%3D%20'Justin'%0A%0Aprint%28f'%7Bx.name%7D%20ist%20%7B2024%20-%20x.baujahr%7D%20Jahre%20alt'%29%0Aprint%28f'%7By.name%7D%20ist%20%7B2024%20-%20y.baujahr%7D%20Jahre%20alt'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    pass


x = Roboter()
y = Roboter()

x.baujahr = 1990
x.name = 'Marvin'
y.baujahr = 2005
y.name = 'Justin'

print(f'{x.name} ist {2024 - x.baujahr} Jahre alt')
print(f'{y.name} ist {2024 - y.baujahr} Jahre alt')
```


Beachte, dass jede Instanz ihre eigenen Attribute hat. Da wir den Instanzen erst nach deren Erstellung
Attribute hinzugefügt haben, nennt man diese auch _dynamische Attribute_. Wir werden später sehen, wie man
schon bei der Erzeugung einer Instanz die Attribute festlegen kann.

Wenn wir alle Attribute einer Instanz ansehen wollen, können wir das mit `x.__dict__` tun:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20pass%0A%0A%0Ax%20%3D%20Roboter%28%29%0Ay%20%3D%20Roboter%28%29%0A%0Ax.baujahr%20%3D%201990%0Ax.name%20%3D%20'Marvin'%0Ay.baujahr%20%3D%202005%0Ay.name%20%3D%20'Justin'%0A%0Aprint%28x.__dict__%29%0Aprint%28y.__dict__%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    pass


x = Roboter()
y = Roboter()

x.baujahr = 1990
x.name = 'Marvin'
y.baujahr = 2005
y.name = 'Justin'

print(x.__dict__)
print(y.__dict__)
```


### Aufgabe: Durchschnittsnote berechnen🌶
Erstelle eine Klasse `Student`. Erzeuge eine `Student` Instanz.
Setze bei der Instanz die Attribute `Mathenote`, `Englischnote` und `Deutschnote`.
Schreibe dann Code, der diese Attribute ausließt und die Durchschnittsnote berechnet.

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/wo1AvTRUIJU?si=8edJnXhyEt4t-ZEe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Student:
    pass


anna = Student()
anna.Mathenote = 2
anna.Englischnote = 1
anna.Deutschnote = 1

durchschnitt = (anna.Mathenote + anna.Englischnote + anna.Deutschnote) / 3
print(durchschnitt)</code></pre>

</details>

### Aufgabe: Passende Attribute finden🌶🌶
Im folgenden Code soll die Summe aller Felder berechnet werden, die das Wort `spending` enthalten.
Dazu soll `__dict__` und eine Schleife. Wie sieht die Lösung mit einer Listcomprehension aus?

```python
class Buchhaltung:
    pass

booking = Buchhaltung()
booking.food_spending = 100
booking.car_spending = 230
booking.february_income = 200
```
<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YPwcI1X8BdA?si=PBN9PXM8LYYL46PG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Buchhaltung:
    pass


booking = Buchhaltung()
booking.food_spending = 100
booking.car_spending = 230
booking.february_income = 200

summe = 0
for name, value in booking.__dict__.items():
    if 'spending' in name:
        summe += value

print(summe)

print(sum(value for name, value in booking.__dict__.items() if 'spending' in name))</code></pre>
</details>

### Aufgabe: Instanz als Parameter übergeben🌶🌶
Erstelle eine Klasse `Person`.
Erzeuge `Person` Instanzen und setze einen Namen.
Erstelle eine Funktion `getInitials(person)`, die eine Klasse der Instanz `Person` erwartet
und die ersten Buchstaben des Namens zurückliefert. Z.B.:

```python
anna = Person()
anna.name = "Anna Lena Zitrova"

karl = Person()
karl.name = "Karl Gustav"


def getInitials(person):
    ...


print(getInitials(anna)) # 'ALZ'
print(getInitials(karl)) # 'KG'
```

Tipp: Nutze die Methoden `split` und `join`. Am einfachsten ist das mit List-Comprehension. Ja, tatsächlich.

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/6fi7XA91uos?si=3ETKGAxL495ic8zM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Person:
    pass

anna = Person()
anna.name = "Anna Lena Zitrova"

karl = Person()
karl.name = "Karl Gustav"


def getInitials(person):
    return "".join(word[0] for word in person.name.split())

print(getInitials(anna)) # 'ALZ'
print(getInitials(karl)) # 'KG'</code></pre>
</details>

## Klassenattribute

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_YxyRGvUcpI?si=VqCvQuoxt8ktM3IX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Wir können auch der Klasse Attribute hinzufügen.
Lassen den folgenden Code ausführen, in der das Klassenattribut `marke`
hinzugefügt wird:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20marke%20%3D%20'VW'%0A%0Ax%20%3D%20Roboter%28%29%0Ay%20%3D%20Roboter%28%29%0A%0Ax.name%20%3D%20'Marvin'%0A%0Aprint%28x.marke%29%0Aprint%28y.marke%29%0Aprint%28Roboter.marke%29%0A%0Aprint%28f'Attribute%20von%20x%3A%20%7Bx.__dict__%7D'%29%0Aprint%28f'Attribute%20von%20y%3A%20%7By.__dict__%7D'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    marke = 'VW'

x = Roboter()
y = Roboter()

x.name = 'Marvin'

print(x.marke)
print(y.marke)
print(Roboter.marke)

print(f'Attribute von x: {x.__dict__}')
print(f'Attribute von y: {y.__dict__}')
```


* Alle Instanzen der Klasse können auf das Klassenattribut zugreifen.
* Man kann über die Klasse auf das Klassenattribut zugreifen.
* Das Klassenattribut ist kein Attribut der Instanz.

Wir können das Klassenattribut auch dynamisch setzen:

```python
class Roboter:
    pass
    
Roboter.marke = 'VW'

...
```

In anderen Programmiersprachen sagt zu Klassenattributen "statische Felder" und zu Attributen der Instanz "Felder".
Die Möglichkeit Attribute oder Klassenattribute dynamisch nach Instanziierung hinzuzufügen, 
gibt es jedoch nicht bei allen Programmiersprachen.

### Aufgabe: Klassenattribute gelten für alle Instanzen🌶🌶
Sage voraus, was bei folgendem Code auf der Konsole erscheint.

Führe den Code aus.

Begründe, die Ausgabe.

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20marke%20%3D%20'VW'%0A%0Ax%20%3D%20Roboter%28%29%0Ay%20%3D%20Roboter%28%29%0A%0Aprint%28x.marke%29%0Aprint%28y.marke%29%0Aprint%28Roboter.marke%29%0A%0ARoboter.marke%20%3D%20'Porsche'%0A%0Aprint%28x.marke%29%20%0Aprint%28y.marke%29%0Aprint%28Roboter.marke%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    marke = 'VW'

x = Roboter()
y = Roboter()

print(x.marke)
print(y.marke)
print(Roboter.marke)

Roboter.marke = 'Porsche'

print(x.marke) 
print(y.marke)
print(Roboter.marke)
```


<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/A7N1sua2L7s?si=-dlmHpWy1n_eBTbS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Ein Klassenattribut gilt für alle Instanzen einer Klasse.
Wenn man es ändert, ändert man es für alle, da sie alle das Attribut an einer Stelle nachlesen.

<pre><code>class Roboter:
    marke = 'VW'

x = Roboter()
y = Roboter()

print(x.marke) # 'VW'
print(y.marke) # 'VW'
print(Roboter.marke) # 'VW'

Roboter.marke = 'Porsche'

print(x.marke) # 'Porsche'
print(y.marke) # 'Porsche'
print(Roboter.marke) # 'Porsche'
</code></pre>
</details>

### Aufgabe: Bei Unklarheit nachfragen🌶🌶

Was tut die `hasattr` Methode in diesem Codebeispiel? Was passiert, wenn man den if-Block entfernt?

```python
class Roboter:
    marke = "VW"

x = Roboter()

if not hasattr(x, "speed"):
    x.speed = 0

print(f"Roboter fährt {x.speed} km/h")

if hasattr(x, "marke"):
    print(f"Roboter hat die Marke {x.marke}")
```

Neben `hasattr` gibt es die vorimplementierten Funktionen `getattr` und `setattr`. 
Finde heraus, was diese Funktionen tun und ändere den obigen Code so, dass diese Funktionen verwendet werden.

Was macht der dritte Parameter von `getattr`?

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/isqU3A8-9a0?si=l_lWXQCJHFr8ug2D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

`hasattr` prüft, ob die Instanz ein Attribut oder Klassenattribut besitzt.

`setattr` setzt ein Attribut.

`getattr` gibt einem das Attribut mit dem gegebenen Namen zurück. Der dritte Parameter wird ist optional und wird 
zurückgegeben, wenn kein Attribut des angegebenen Namens gefunden wurde.

Der geänderte Code sieht wie folgt aus:

<pre><code>class Roboter:
    marke = "VW"


x = Roboter()

if not hasattr(x, "speed"):
    setattr(x, "speed", 0)

print(f"Roboter fährt {getattr(x, "speed")} km/h")

if hasattr(x, "marke"):
    print(f"Roboter hat die Marke {getattr(x, "marke")}")
</code></pre>
</details>


### Aufgabe: Auch Funktionen sind Instanzen🌶🌶🌶

Im Folgenden ist eine Funktion `say_hello` definiert. Führe den folgenden Code aus und erkläre das Verhalten.
Was ist der Typ von `say_hello`?

```python
def say_hello():
    if not hasattr(say_hello, "count"):
        say_hello.count = 0
    
    say_hello.count += 1
    
    print(f"Hallo zum {say_hello.count}-ten Mal.")

say_hello()
say_hello()
say_hello()
```

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/0JlOqTwW90g?si=s_5C7QW5Ib0Ox9Ue" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Innerhalb der Funktion, wird ein Attribut `count` von der Funktion (!) angelegt, beschrieben und ausgelesen.
Dann sehen wir immer wechselnden Output:

<pre><code>def say_hello():
    if not hasattr(say_hello, "count"):
        say_hello.count = 0

    say_hello.count += 1

    print(f"Hallo zum {say_hello.count}-ten Mal.")

say_hello() # Hallo zum 1-ten Mal.
say_hello() # Hallo zum 2-ten Mal.
say_hello() # Hallo zum 3-ten Mal.
</code></pre>
</details>
