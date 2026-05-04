# Klassen definieren und instanziieren

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_Kzt2M7Osfs?si=_VqBodiJVy8snbGL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Die **objektorientierte Programmierung (OOP)** ist ein mächtiges Programmierparadigma, 
das auf dem Konzept von "Objekten" basiert. Im Gegensatz zu prozeduralen Programmieransätzen,
bei denen der Code als eine Abfolge von Aufgaben organisiert ist, 
legt die OOP den Fokus auf die Modellierung von reellen Entitäten und ihren Interaktionen.

## Minimalbeispiel:

Im Folgenden werden wir eine neue Klasse mit dem Schlüsselwort `class` erstellen:

```python
class Roboter:
    pass
```

Diese Klasse ist im Moment denkbar langweilig. Das `pass` sagt,
dass in diesem Block nichts passiert. Unsere Roboter haben also noch keine Eigenschaften
(das kommt noch im nächsten Kapitel)

Sie ist die Blaupause, mit der wir Instanzen der Klasse
erstellen können. Das sieht dann so aus:

[Link zum Onlinecompiler💻](https://pythontutor.com/render.html#code=class%20Roboter%3A%0A%20%20%20%20pass%0A%0A%0Ax%20%3D%20Roboter%28%29%0Ay%20%3D%20Roboter%28%29%0Ay2%20%3D%20y%0A%0Aprint%28f'id%20von%20x%3A%20%7Bid%28x%29%7D'%29%0Aprint%28f'id%20von%20y%3A%20%7Bid%28y%29%7D'%29%0Aprint%28f'id%20von%20y%3A%20%7Bid%28y2%29%7D'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
class Roboter:
    pass


x = Roboter()
y = Roboter()
y2 = y

print(f'id von x: {id(x)}')
print(f'id von y: {id(y)}')
print(f'id von y: {id(y2)}')
```


Wir haben hier insgesamt **drei** Objekte angelegt:

* Die Klasse `Roboter` selbst, wurde als ein Objekt bespeichert.
* Wir haben eine Instanz der Klasse Roboter mit dem Aufruf `Roboter()` erzeugt in der Variablen `x` eine Referenz zu diesem Objekt bespeichert.
* Wir haben dann eine **weitere** Instanz der Klasse Roboter erzeugt und eine Referenz zu dieser in `y` gespeichert.
* Wir haben danach eine neue Variable `y2` angelegt und in dieser die Referenz bespeichert, die auch in `y` gespeichert. ist

Bitte achte hier genau auf die Wortwahl! Ich schreibe **nicht** "In der Variablen `y` ist die Instanz gespeichert",
sondern "In der Variablen `y` ist eine **Referenz** zur Instanz gespeichert." Eine Referenz kannst du dir so vorstellen,
wie eine Anschrift, die dir Verrätt, wo du die Instanz im Speicher findest. Dieses Konzept kennen wir bereits von
zusammengesetzten Datentypen wie Listen.

![img.png](variablen.png)

🔅Merke dir: Die Klasse ist die Vorlage, mit der Instanzen gebaut werden.

🔅Vokabel: Eine neue Instanz zu erzeugen wird auch Instanziieren genannt.

🔅Merke dir: Variablen speichern eine Referenz zu Instanzen, nicht die Instanz selbst.


### Aufgabe: Typ untersuchen🌶
Untersuche mithilfe von `type` die Typen von `x`, `y`, `y2` und `Roboter` aus dem obigen Beispiel.

<details>
<summary>
Lösung
</summary>
`Roboter` ist vom Typ <code>type</code> und <code>x</code>, <code>y</code>, <code>y2</code> sind vom Typ
<code>__main__.Roboter</code>.
Das <code>__main__</code> entsteht hier nur, da wir die Datei direkt ausführen. Wenn wir Roboter
importiert hätten, wären diese einfach vom Typ <code>Roboter</code>.
</details>

### Aufgabe: mehrere Instanzen erzeugen🌶
Erstelle eine leere Klasse `Car` und erzeuge drei verschiedene Instanzen von `Car`. 
Wie kannst du überprüfen, dass die Instanzen wirklich verschieden sind?

<details>
<summary>
Lösung
</summary>
<pre><code>class Car:
    pass

a = Car()
b = Car()
c = Car()

print(id(a))
print(id(b))
print(id(c))</code></pre>
</details>

[//]: # (### Aufgabe: Identitätsvergleich🌶🌶)

[//]: # (Finde heraus, was `is` und `is not` in Python tun und an welcher Stelle wir sie im Beispielcode hätten nutzen können.)

