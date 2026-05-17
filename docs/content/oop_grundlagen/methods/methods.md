# Methoden

{{ youtube_video("https://www.youtube.com/embed/dd7Y42ZJKB8?si=2QSdO1pnBf1qFUle") }}

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

{{ task(file="tasks/python_grundlagen/oop/methods/methods/01_koordinaten_setzen.yaml") }}
## Jede Instanz hat eigene Attribute

{{ youtube_video("https://www.youtube.com/embed/YcqvbaaGDCQ?si=eSXbxIbZk9X23bP6") }}

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

{{ youtube_video("https://www.youtube.com/embed/jaP7wFz8KYo?si=cdUKryfkJ5PerABP") }}

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

{{ task(file="tasks/python_grundlagen/oop/methods/methods/02_koordinaten_von_vornherein_setzen.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/methods/methods/03_auf_in_den_kampf.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/methods/methods/04_ab_in_die_arena.yaml") }}
