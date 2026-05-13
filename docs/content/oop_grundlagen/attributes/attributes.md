# Attribute

{{ youtube_video("https://www.youtube.com/embed/Wa0DjW0Zn4Y?si=KNRedy36pi8kcgsH") }}

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

{{ task(file="tasks/python_grundlagen/oop/attributes/attributes/01_durchschnittsnote_berechnen.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/attributes/attributes/02_passende_attribute_finden.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/attributes/attributes/03_instanz_als_parameter_ubergeben.yaml") }}
## Klassenattribute

{{ youtube_video("https://www.youtube.com/embed/_YxyRGvUcpI?si=VqCvQuoxt8ktM3IX") }}

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

{{ task(file="tasks/python_grundlagen/oop/attributes/attributes/04_klassenattribute_gelten_fur_alle_instanzen.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/attributes/attributes/05_bei_unklarheit_nachfragen.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/attributes/attributes/06_auch_funktionen_sind_instanzen.yaml") }}
