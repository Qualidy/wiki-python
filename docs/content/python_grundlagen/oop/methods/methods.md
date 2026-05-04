# Methoden

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dd7Y42ZJKB8?si=2QSdO1pnBf1qFUle" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Wir wollen "Methoden" in einigen Schritten definieren:

Betrachten wir zunächst das folgende Beispiel einer (noch) leeren Roboterklasse. Wir erzeugen eine Instanz
und setzen das `baujahr`:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20pass%0A%0Arobo%20%3D%20Roboter%28%29%0A%0Arobo.baujahr%20%3D%201700%0Aprint%28robo.baujahr%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    pass

robo = Roboter()

robo.baujahr = 1700
print(robo.baujahr)
```


Nun wollen wir sicherstellen, dass das angegebene Baujahr nicht zu klein ist. 1700 gab es noch keine Roboter.
Daher erstellen wir eine Funktion, die als ersten Parameter eine `Roboter` Instanz erwartet und als zweite
das `baujahr`. Wenn das Baujahr zu klein ist, soll eine Exception geworfen werden:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20pass%0A%0A%0Adef%20set_baujahr%28roboter,%20baujahr%29%3A%0A%20%20%20%20if%20baujahr%20%3C%201800%3A%0A%20%20%20%20%20%20%20%20raise%20ValueError%28%22So%20fr%C3%BCh%20gab%20es%20noch%20keine%20Roboter!%22%29%0A%20%20%20%20roboter.baujahr%20%3D%20baujahr%0A%0A%0Arobo%20%3D%20Roboter%28%29%0A%0Aset_baujahr%28robo,%202000%29%0Aprint%28robo.baujahr%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    pass


def set_baujahr(roboter, baujahr):
    if baujahr < 1800:
        raise ValueError("So früh gab es noch keine Roboter!")
    roboter.baujahr = baujahr


robo = Roboter()

set_baujahr(robo, 2000)
print(robo.baujahr)
```


Soweit so gut, der Code funktioniert, aber eigentlich gehört die Methode `set_baujahr` ja eigentlich zu Klasse 
`Roboter`. Sie sollte nicht auch von anderen Instanzen anderer Klassen aufrufbar sein. Wir können die Funktion
daher in den Klassenrumpf verschieben und machen aus ihr so eine **Methode**.

Dadurch ändert sich noch ein weiteres Detail, um die Methode nun aufzurufen, müssen wir sie zunächst aus 
der Klasse  `Roboter` herausbekommen, indem wir `Roboter.set_baujahr(...)` aufrufen (ähnlich wie beim
abfragen eines Klassenattributes). Nun funktioniert der folgende Code:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20def%20set_baujahr%28roboter,%20baujahr%29%3A%0A%20%20%20%20%20%20%20%20if%20baujahr%20%3C%201800%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20ValueError%28%22So%20fr%C3%BCh%20gab%20es%20noch%20keine%20Roboter!%22%29%0A%20%20%20%20%20%20%20%20roboter.baujahr%20%3D%20baujahr%0A%0A%0Arobo%20%3D%20Roboter%28%29%0A%0ARoboter.set_baujahr%28robo,%202000%29%0A%0Aprint%28robo.baujahr%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    def set_baujahr(roboter, baujahr):
        if baujahr < 1800:
            raise ValueError("So früh gab es noch keine Roboter!")
        roboter.baujahr = baujahr


robo = Roboter()

Roboter.set_baujahr(robo, 2000)

print(robo.baujahr)
```


Wir haben nun unsere erste Methode definiert. 🎉

Wir können jedoch noch zwei Dinge verschönern, was wir auch auf jeden Fall tun sollten.

1. Wir sollten den Namen des ersten Parameters auf `self` setzen. Es ist Konvention den ersten Namen einer Methode `self` zu nennen, da dieser immer die Instanz referenziert, die gerade behandelt wird.
2. Wir können die Methode auch mit der Notation `robo.set_baujahr(2000)` aufrufen. Genauso wie bei Klassenattributen haben auch die Instanzen Zugriff auf die Methode. Wir müssen dann den ersten Parameter `self` nicht mehr setzen, da diese gleich der Instanz ist, die diese Methode aufgerufen hat.

Der Code sieht dann also wie folgt aus:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20def%20set_baujahr%28self,%20baujahr%29%3A%0A%20%20%20%20%20%20%20%20if%20baujahr%20%3C%201800%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20ValueError%28%22So%20fr%C3%BCh%20gab%20es%20noch%20keine%20Roboter!%22%29%0A%20%20%20%20%20%20%20%20self.baujahr%20%3D%20baujahr%0A%0A%0Arobo%20%3D%20Roboter%28%29%0A%0A%23%20Roboter.set_baujahr%28robo,%202000%29%0A%0Arobo.set_baujahr%282000%29%0A%0Aprint%28robo.baujahr%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    def set_baujahr(self, baujahr):
        if baujahr < 1800:
            raise ValueError("So früh gab es noch keine Roboter!")
        self.baujahr = baujahr


robo = Roboter()

# Roboter.set_baujahr(robo, 2000)

robo.set_baujahr(2000)

print(robo.baujahr)
```


### Aufgabe: Koordinaten setzen🌶🌶

Erstelle in der folgenden Klasse `Point` mit zwei Methoden `set_coordinates(self, x, y)` und `get_coordinates(self)`.

* `set_coordinates` setzt das `x` und das `y` Attribut des Objektes.
* `get_coordinates` gibt die beiden Punkte als zwei Rückgabewerte zurück.

Der folgende Code soll dann funktionieren: 
```python
point = Point()
point.set_coordinates(3, 5)
x, y = point.get_coordinates()
print(f"Punkt hat den x-Wert {x} und den y-Wert {y}")
```

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/9ZYOFONkGF4?si=hN8OTjXWYgTrtb0J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<pre><code>class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


point = Point()
point.set_coordinates(3, 5)
x, y = point.get_coordinates()
print(f"Punkt hat den x-Wert {x} und den y-Wert {y}")</code></pre>
</details>

## Jede Instanz hat eigene Attribute

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YcqvbaaGDCQ?si=eSXbxIbZk9X23bP6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Wir sehen im folgenden Beispiel, dass jede Instanz ihre eigenen Attribute hat und wir auf diese in Methoden
zugreifen können:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20def%20sage_hallo%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22Hallo,%20ich%20bin%20%7Bself.name%7D.%22%29%0A%0Ax%20%3D%20Roboter%28%29%0Ay%20%3D%20Roboter%28%29%0A%0Ax.name%20%3D%20%22Marvin%22%0Ay.name%20%3D%20%22Justin%22%0A%0Ax.sage_hallo%28%29%0Ay.sage_hallo%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    def sage_hallo(self):
        print(f"Hallo, ich bin {self.name}.")

x = Roboter()
y = Roboter()

x.name = "Marvin"
y.name = "Justin"

x.sage_hallo()
y.sage_hallo()
```


Beachte, wie hier innerhalb der Methode auf das Attribut `name` zugegriffen wurde, indem
`self.name` abgefragt wurde, denn `self` referenziert ja die Instanz, die die Methode aufruft.

### Instanziieren mit `__init__`

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/jaP7wFz8KYo?si=cdUKryfkJ5PerABP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Der obige Code hat aber noch ein Problem: wenn eine Instanz kein Attribut `name` besitzt, kommt es zu einer Exception:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20def%20sage_hallo%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22Hallo,%20ich%20bin%20%7Bself.name%7D.%22%29%0A%0Ay%20%3D%20Roboter%28%29%0A%0Ay.sage_hallo%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    def sage_hallo(self):
        print(f"Hallo, ich bin {self.name}.")

y = Roboter()

y.sage_hallo()
```


Wir möchten also gerne, dass jede Roboterinstanz ein Attribut `name` besitzt.

In Klassen können wir die Methode `__init__` definieren, die aufgerufen wird, wenn eine neue Instanz erstellt wird.
Hier können wir dann z.B. direkt bestimmte Attribute festlegen:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20def%20__init__%28self,%20name%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20name%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20sage_hallo%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22Hallo,%20ich%20bin%20%7Bself.name%7D.%22%29%0A%0Ay%20%3D%20Roboter%28%22Karl%22%29%0A%0Ay.sage_hallo%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    def __init__(self, name):
        self.name = name
        
    def sage_hallo(self):
        print(f"Hallo, ich bin {self.name}.")

y = Roboter("Karl")

y.sage_hallo()
```


Oft verwirrt, dass es bei `__init__` auch erforderlich ist, dass der erste Parameter `self` ist.
`__init__` erstellt nämlich tatsächlich gar keine Instanz. Das wird über eine andere Methode, namens `__new__`
gesteuert. Diese sehen wir hier gar nicht und wird stillschweigend von Python aufgerufen, als 
wir `Roboter("Karl")` ausführen. Auf dieser frischen Instanz wird dann `__init__` ausgeführt und
die Attribute werden festgelegt. Wer mehr dazu erfahren möchte, lese die 
[Pythondoku](https://docs.python.org/3/reference/datamodel.html#object.__new__) 
oder [diesen Artikel](https://builtin.com/data-science/new-python).

🔅Merke: `__new__` instanziiert, `__init__` initialisiert.

### Aufgabe: Koordinaten von vornherein setzen🌶
Erweitere die Klasse `Point` aus der [Aufgabe Koordinaten setzen](#aufgabe-koordinaten-setzen) um eine 
`__init__` Methode, sodass direkt `x` und `y` Wert gesetzt werden können. Der folgende Code soll also Ausführbar sein:

```python
point = Point(4, 7)
x, y = point.get_coordinates()
print(f"Punkt hat den x-Wert {x} und den y-Wert {y}")
```

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/LGtuDOss4bM?si=eo4CxwZS8mxFX-EE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


point = Point(4, 7)
x, y = point.get_coordinates()
print(f"Punkt hat den x-Wert {x} und den y-Wert {y}")</code></pre>
</details>

### Aufgabe: Auf in den Kampf!🌶🌶🌶
Erstelle eine Klasse Gladiator nach der folgenden Vorlage:

```python
class Gladiator:
    def __init__(self,name, hitpoints, attackpower):
        ...
    
    def attack(self, enemy):
        ...
        
    def is_alive(self):
        ...
        
    def health_check(self):
        ... # Nutze hier is_alive


attacker = Gladiator(name="Glassy", hitpoints=10, attackpower=20)
defender = Gladiator(name="Tanky", hitpoints=30, attackpower=5)

print(defender.health_check()) # Tanky hat noch 30 HP
attacker.attack(defender)
print(defender.health_check()) # Tanky hat noch 10 HP
attacker.attack(defender)
print(defender.health_check()) # Tanky liegt am Boden
```

Sorge dafür, dass die richtigen Konsolentexte erscheinen. ⚔️

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/DBbwtUOTqko?si=746ca74y-0LiZFgS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Gladiator:
    def __init__(self,name, hitpoints, attackpower):
        self.name = name
        self.hitpoints = hitpoints
        self.attackpower = attackpower

    def attack(self, enemy):
        enemy.hitpoints -= self.attackpower
        
    def is_alive(self):
        return self.hitpoints > 0
    
    def health_check(self):
        if self.is_alive():
            return f"{self.name} hat noch {self.hitpoints} HP."
        else:
            return f"{self.name} liegt am Boden." 


attacker = Gladiator(name="Glassy", hitpoints=10, attackpower=20)
defender = Gladiator(name="Tanky", hitpoints=30, attackpower=5)

print(defender.health_check()) # Tanky hat noch 30 HP
attacker.attack(defender)
print(defender.health_check()) # Tanky hat noch 10 HP
attacker.attack(defender)
print(defender.health_check()) # Tanky liegt am Boden</code></pre>
</details>




### Aufgabe: Ab in die Arena!🌶🌶🌶

Erstelle eine Klasse `Arena`, bei der als Attribute zwei Gladiatoren festgelegt werden.
Die beiden Gladiatoren sollen sich hier gegenseitig angreifen, bis nurnoch einer steht.

Um den Kampf zu starten, soll eine Methode `fight` implementiert werden. Du kannst gerne Print-Messages
hinzufügen, die den Kampf spannend und nachvollziehbar gestalten. Der folgende Code soll durchführbar sein:

```python
a = Gladiator(name="Glassy", hitpoints=10, attackpower=20)
d = Gladiator(name="Tanky", hitpoints=30, attackpower=5)

arena = Arena(a, d)
arena.fight()
```

<details>
<summary>
Lösung
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/I9BhX2cqoR8?si=wjzPC0gQxRwE_OPE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<pre><code>class Arena:
    def __init__(self, attacker: Gladiator, defender: Gladiator):
        self.attacker = attacker
        self.defender = defender

    def fight(self):
        while self.attacker.is_alive() and self.defender.is_alive():
            self.attacker, self.defender = self.defender, self.attacker
            self.attacker.attack(self.defender)

        winner = self.attacker if self.attacker.is_alive() else self.defender

        print(f"The winner is {winner.name}!🎉🎉🎉")
</code></pre>
</details>
