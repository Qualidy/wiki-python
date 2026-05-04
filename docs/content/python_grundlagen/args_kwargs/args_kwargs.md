# Args & Kwargs

In Python gibt es zwei wichtige Konzepte im Zusammenhang mit Funktionen,
nämlich `*args` und `**kwargs`. Diese ermöglichen es, Funktionen flexibler zu gestalten 
und mit variabler Anzahl von Argumenten umzugehen.

## Beispiel 1

Angenommen wir wollen Funktionen zur Verfügung stellen, um eine beliebe Menge von Zahlen zu multiplizieren.

Derzeit haben wir keine gute Möglichkeit das umzusetzen, außer für jede Parameterzahl eine eigene Funktion zur Verfügung zu stellen:

```python
def multiply_2(a, b):
    return a * b

def multiply_3(a, b, c):
    return a * b * c
    
def multiply_4(a, b, c, d):
    return a * b * c * d

...
```

Das ist eine sehr unschöne Lösung. Sollen wir jetzt Milliarden von Funktionen vordefinieren, um mit jeder
beliebigen Anzahl von Argumenten zurechtzukommen?

Auch die Lösung eine Funktion zu erstellen, die mit eine Liste erwartet, ist keine wirkliche:

```python
def multiply(faktors):
    result = 1
    for faktor in faktors:
        result *= faktor
    return result


print(multiply([2, 3, 5]))  # 30
```

Denn wir wollen ja die Funktion aufrufen, ohne die Parameter vorher in eine Liste zu verpacken:
```python
print(multiply(2, 3, 5))
```

**Antwort:** Wir nutzen `*args` als einen Parameter in unserer Funktion, in dieser werden alle
Alle positionalen Argumente gelegt, die nicht an anderer Stelle zugeordnet sind:

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20multiply%28*faktors%29%3A%0A%20%20%20%20result%20%3D%201%0A%20%20%20%20for%20faktor%20in%20faktors%3A%0A%20%20%20%20%20%20%20%20result%20*%3D%20faktor%0A%20%20%20%20return%20result%0A%0A%0Aprint%28multiply%282,%203,%205%29%29%20%20%23%2030&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def multiply(*faktors):
    result = 1
    for faktor in faktors:
        result *= faktor
    return result


print(multiply(2, 3, 5))  # 30
```


durch das Asterisksymbol `*` vor dem `faktors`, sagen wir, dass alle positionalen Argumente, die noch nicht
an einen anderen Parameter bunden sind (hier gibt es keinen), in das Tupel `faktors` gespeichert werden sollen.

## Beispiel 2

Im folgenden Beispiel sehen wir, dass wir zunächst zwei Parameter `leiter` und `stellvertreter`
haben. Diese müssen beim Funktionsaufruf immer angegeben werden. Im Parameter `mitarbeiter` werden
alle weiteren positionalen Argumente in einem Tupel gesichert. Wenn es keine gibt, ist das Tupel leer.

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20print_abteilung_namen%28leiter,%20stellvertreter,%20*mitarbeiter%29%3A%0A%20%20%20%20print%28f%22Leitung%3A%20%7Bleiter%7D%22%29%0A%20%20%20%20print%28f%22Stellvertretung%3A%20%7Bstellvertreter%7D%22%29%0A%20%20%20%20for%20arbeiter%20in%20mitarbeiter%3A%0A%20%20%20%20%20%20%20%20print%28f%22Mitarbeiter%3A%20%7Barbeiter%7D%22%29%0A%20%20%20%20print%28f%22Neben%20Leitung%20und%20Stellvertretung%20gibt%20es%20%7Blen%28mitarbeiter%29%7D%20Mitarbeiter.%22%29%0A%0A%0Aprint_abteilung_namen%28%22Johanna%22,%20%22Klara%22,%20%22Bianca%22,%20%22Siegfried%22%29%0Aprint_abteilung_namen%28%22Tom%22,%20%22Jerry%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def print_abteilung_namen(leiter, stellvertreter, *mitarbeiter):
    print(f"Leitung: {leiter}")
    print(f"Stellvertretung: {stellvertreter}")
    for arbeiter in mitarbeiter:
        print(f"Mitarbeiter: {arbeiter}")
    print(f"Neben Leitung und Stellvertretung gibt es {len(mitarbeiter)} Mitarbeiter.")


print_abteilung_namen("Johanna", "Klara", "Bianca", "Siegfried")
print_abteilung_namen("Tom", "Jerry")
```


### Aufgabe: Typen prüfen🌶
Prüfe im obigen Beispiel den Typ von `faktors` und `mitarbeiter`.

<details><summary>🍀Tipp</summary>
Typen lass sich mit <code>type</code> erfragen.</details>

<details><summary>Lösung</summary>
Beide sind vom Typ <code>tuple</code>.</details>

### Aufgabe: Konkatinieren von Strings🌶
Schreibe eine Funktion `concat`, die eine beliebige Anzahl von String zu einem einzigen String
konkatiniert.

```python
concat("Hallo", "Du", "wie", "geht") # "HalloDuwiegeht"
concat("Hallo", "Du") # "HalloDu"
concat() # ""
```

<details><summary>🍀Tipp</summary>
Strings können mit <code>+</code> konkatiniert werden.</details>

<details><summary>Lösung</summary>
<pre><code>def concat(*strings):
    result = ""
    for string in strings:
        result += string
    return result</code></pre>
</details>

### Aufgabe: Konkatenieren mit Trennzeichen🌶🌶
Erweitere die Lösung der letzten Aufgabe, sodass ein Paremeter `seperator` mit angegeben werden kann.
Dieser ist per default auf den leeren String `''` gesetzt. Folgender Code ist dann **zusätzlich** möglich:

An welcher Stelle muss ein Defaultparameter eingefügt werden?

Wandle diese und die letzten Beispiele in Unittests um.

```python
concat("Hallo", "Du", "wie", "geht", seperator=" ") # "Hallo Du wie geht"
concat("Hallo", "Du", seperator="~~") # "Hallo~~Du"
concat(seperator="*") # ""
```

<details><summary>🍀Tipp</summary>
Der Methodenkopf muss wie folgt aussehen:
<pre><code>def concat(*strings, seperator=""):</code></pre></details>

<details><summary>Lösung</summary>
<pre><code>def concat(*strings, seperator=""):
    result = ""
    for string in strings:
        result += string + seperator
    return result if not seperator else result[:-len(seperator)]


import unittest


class ConcatTest(unittest.TestCase):
    def test_concat_0(self):
        self.assertEqual(concat("Hallo", "Du", "wie", "geht"), "HalloDuwiegeht")

    def test_concat_1(self):
        self.assertEqual(concat("Hallo", "Du"), "HalloDu")

    def test_concat_2(self):
        self.assertEqual(concat(), "")

    def test_concat_3(self):
        self.assertEqual(concat("Hallo", "Du", "wie", "geht", seperator=" "), "Hallo Du wie geht")

    def test_concat_4(self):
        self.assertEqual(concat("Hallo", "Du", seperator="~~"), "Hallo~~Du")

    def test_concat_5(self):
        self.assertEqual(concat(seperator="*"), "")
</code></pre>
</details>

### Aufgabe: Gepaarte Summen🌶🌶
Erstelle eine Funktion `paired_sum`, die eine beliebige Anzahl von Parametern erlaubt.
Immer zwei Parameter werden addiert und zurückgegeben.
Die Rückgabe ist ein Tupel. 
Wenn eine ungerade Anzahl von Parametern übergeben wird,
dann wird eine Exception geworfen.

```python
paired_sum(1, 2, 3, 4) # (3, 7)
paired_sum(1, 2, 3) # 
paired_sum() # (,) leeres Tupel

```

<details><summary>🍀Tipp</summary>
Wie kann man mit Slicing jedes zweite Element erreichen?
Wie kann man mit <code>zip</code> zwei Teillisten paralell durchlaufen?</details>

<details><summary>Lösung</summary>
<pre><code>def paired_sum(*summands):
    if len(summands) % 2:
        raise Exception("Number of Arguments must be even.")

    return tuple(a + b for a, b in zip(summands[::2], summands[1::2]))
</code></pre></details>

### Aufgabe: Beliebig viele Zeilen in Datei speichern🌶🌶
Erstelle eine Funktion `save_lines_to_file`, die als ersten Parameter einen Speicherort
erwartet und dann eine beliebige Anzahl von Strings.
Diese Strings sollen jeweils als Zeilen in eine die vorgegebene Datei gespeichert werden.

```python
save_lines_to_file("test.txt", "Hallo", "wie", "geht", "es" , "dir denn heute so?")
```
Datei:
```
Hallo
wie
geht
es
dir denn heute so?
```

<details><summary>🍀Tipp</summary>
Das Symbol für einen Zeilenumbruch ist <code>\n</code></details>

<details><summary>Lösung</summary>
<pre><code>def save_lines_to_file(loc, *lines):
    with open(loc, "wt") as file:
        for line in lines:
            file.write(line+"\n")
</code></pre></details>

## Listen als positionale Parameter übergeben

Wir wissen nun, wie wir eine beliebige Anzahl von Parametern erlauben.
Aber was ist, wenn unsere Parameter in einer Liste gesammelt sind?

In so einem Fall müssen wir eine Liste entpacken, wenn wir die Elemente
als einzelne Parameter übergeben wollen. Dieses Entpacken funktioniert 
wieder mit dem Asterisk-Operator `*` wie folgt:

**Beispiel 1:**

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20multiply%28*faktors%29%3A%0A%20%20%20%20result%20%3D%201%0A%20%20%20%20for%20faktor%20in%20faktors%3A%0A%20%20%20%20%20%20%20%20result%20*%3D%20faktor%0A%20%20%20%20return%20result%0A%0A%0A%23%20Erst%20anlegen,%20dann%20entpacken%3A%0Anumbers%20%3D%20%5B1,2,3,4%5D%0Aprint%28multiply%28*numbers%29%29%0A%0A%23%20Anlegen%20und%20entpacken%20in%20einem%20Schritt%3A%0Aprint%28multiply%28*%5B2,%203,%205%5D%29%29%0A%0A%23%20H%C3%A4ndisch%20entpacken%0Aa,%20b,%20c,%20d%20%3D%20numbers%0Aprint%28multiply%28a,b,c,d%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def multiply(*faktors):
    result = 1
    for faktor in faktors:
        result *= faktor
    return result


# Erst anlegen, dann entpacken:
numbers = [1,2,3,4]
print(multiply(*numbers))

# Anlegen und entpacken in einem Schritt:
print(multiply(*[2, 3, 5]))

# Händisch entpacken
a, b, c, d = numbers
print(multiply(a,b,c,d))
```


**Beispiel 2:**

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20print_abteilung_namen%28leiter,%20stellvertreter,%20*mitarbeiter%29%3A%0A%20%20%20%20print%28f%22Leitung%3A%20%7Bleiter%7D%22%29%0A%20%20%20%20print%28f%22Stellvertretung%3A%20%7Bstellvertreter%7D%22%29%0A%20%20%20%20for%20arbeiter%20in%20mitarbeiter%3A%0A%20%20%20%20%20%20%20%20print%28f%22Mitarbeiter%3A%20%7Barbeiter%7D%22%29%0A%20%20%20%20print%28f%22Neben%20Leitung%20und%20Stellvertretung%20gibt%20es%20%7Blen%28mitarbeiter%29%7D%20Mitarbeiter.%22%29%0A%0A%0Aprint_abteilung_namen%28%22Johanna%22,%20%22Klara%22,%20*%5B%22Bianca%22,%20%22Siegfried%22%5D%29%0Aprint_abteilung_namen%28*%5B%22Johanna%22,%20%22Klara%22,%20%22Bianca%22,%20%22Siegfried%22%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def print_abteilung_namen(leiter, stellvertreter, *mitarbeiter):
    print(f"Leitung: {leiter}")
    print(f"Stellvertretung: {stellvertreter}")
    for arbeiter in mitarbeiter:
        print(f"Mitarbeiter: {arbeiter}")
    print(f"Neben Leitung und Stellvertretung gibt es {len(mitarbeiter)} Mitarbeiter.")


print_abteilung_namen("Johanna", "Klara", *["Bianca", "Siegfried"])
print_abteilung_namen(*["Johanna", "Klara", "Bianca", "Siegfried"])
```


**Beispiel 3:**

Wir können diese Notation tatsächlich auch bei Funktionen benutzen, die gar keine variable Anzahl an Parametern erlauben:

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20add%28a,%20b%29%3A%0A%20%20%20%20return%20a%20%2B%20b%0A%0Asummands%20%3D%20%5B1,%204%5D%0Aprint%28add%28*summands%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def add(a, b):
    return a + b

summands = [1, 4]
print(add(*summands))
```



## Keyword Arguments

Im Moment haben wir uns nur mit positionalen Argumenten beschäftigt.
In Python ist es auch möglich Argumente über ein Keyword zu übergeben.
Wir sprechen dann von **Keyword Arguments**

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20sub%28a,%20b%29%3A%0A%20%20%20%20return%20a%20-%20b%0A%0Aprint%28sub%28a%20%3D%201,%20b%20%3D%202%29%29%0Aprint%28sub%28b%20%3D%201,%20a%20%3D%202%29%29%0Aprint%28sub%281,%20b%20%3D%202%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def sub(a, b):
    return a - b

print(sub(a = 1, b = 2))
print(sub(b = 1, a = 2))
print(sub(1, b = 2))
```


Es müssen immer zuerst die positionalen Argumente übergeben werden, bevor die Keyword Argumente übergeben werden.

Um eine beliebige Anzahl an Keyword Argumenten zu erlauben, können wir mit dem Doppelasterisk `**` einen Parameter
festlegen, in dem alle noch nicht gebundenen Argumente als Dictionary gespeichert sind.

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20print_abteilung%28leitung,%20vertretung,%20**mitarbeiter%29%3A%0A%20%20%20%20print%28f%22Leitung%3A%20%7Bleitung%7D%22%29%0A%20%20%20%20print%28f%22Vertretung%3A%20%7Bvertretung%7D%22%29%0A%20%20%20%20for%20stelle,%20name%20in%20mitarbeiter.items%28%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bstelle%7D%3A%20%7Bname%7D%22%29%0A%20%20%20%20%20%20%20%20%0A%0Aprint_abteilung%28leitung%3D%22Karl%22,%20vertretung%3D%22Steffi%22,%20b%C3%BCro%3D%22Jochen%22,%20it%3D%22Claudia%22%29%0A%0Aprint_abteilung%28%22Karl%22,%20%22Steffi%22,%20b%C3%BCro%3D%22Jochen%22,%20it%3D%22Claudia%22%29%0A%0Aprint_abteilung%28%22Karl%22,%20vertretung%3D%22Steffi%22,%20b%C3%BCro%3D%22Jochen%22,%20it%3D%22Claudia%22%29%0A%0Amitarb%20%3D%20%7B%0A%20%20%20%20%22Support%22%3A%20%22Steffi%22,%0A%20%20%20%20%22Powerhouse%22%3A%20%22Max%22,%0A%7D%0A%0Aprint_abteilung%28%22Karl%22,%20vertretung%3D%22Steffi%22,%20b%C3%BCro%3D%22Jochen%22,**mitarb%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def print_abteilung(leitung, vertretung, **mitarbeiter):
    print(f"Leitung: {leitung}")
    print(f"Vertretung: {vertretung}")
    for stelle, name in mitarbeiter.items():
        print(f"{stelle}: {name}")
        

print_abteilung(leitung="Karl", vertretung="Steffi", büro="Jochen", it="Claudia")

print_abteilung("Karl", "Steffi", büro="Jochen", it="Claudia")

print_abteilung("Karl", vertretung="Steffi", büro="Jochen", it="Claudia")

mitarb = {
    "Support": "Steffi",
    "Powerhouse": "Max",
}

print_abteilung("Karl", vertretung="Steffi", büro="Jochen",**mitarb)
```


Wir sehen in diesem Beispiel auch, dass man ein dictionary entpacken kann, um den Inhalt als Argumente
an eine Funktion zu übergeben.

## args und kwargs

In vielen Pythonfunktionen sehen wir, dass die beiden Parameter `*args` und `**kwargs` als letzte beiden Parameter
notiert sind. Dies sorgt dafür, dass eine beliebige Anzahl an Argumenten an diese Methoden übergeben werden kann.

[Link zum Onlinecompiler 💻](https://pythontutor.com/render.html#code=def%20print_abteilung%28leitung,%20vertretung,%20*andere,%20**mitarbeiter%29%3A%0A%20%20%20%20print%28f%22Leitung%3A%20%7Bleitung%7D%22%29%0A%20%20%20%20print%28f%22Vertretung%3A%20%7Bvertretung%7D%22%29%0A%20%20%20%20for%20stelle,%20name%20in%20mitarbeiter.items%28%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bstelle%7D%3A%20%7Bname%7D%22%29%0A%20%20%20%20for%20rest%20in%20andere%3A%0A%20%20%20%20%20%20%20%20print%28f%22weiterhin%3A%20%7Brest%7D%22%29%0A%20%20%20%20%20%20%20%20%0A%0Aprint_abteilung%28leitung%3D%22Karl%22,%20vertretung%3D%22Steffi%22,%20b%C3%BCro%3D%22Jochen%22,%20it%3D%22Claudia%22%29%0A%0Aprint_abteilung%28%22Karl%22,%20%22Steffi%22,%20%22Mirco%22,%20%22Claudia%22,%20b%C3%BCro%3D%22Jochen%22,%20it%3D%22Claudia%22%29%0A%0Aprint_abteilung%28%22Karl%22,%20vertretung%3D%22Steffi%22,%20b%C3%BCro%3D%22Jochen%22,%20it%3D%22Claudia%22%29%0A%0Amitarb%20%3D%20%7B%0A%20%20%20%20%22Support%22%3A%20%22Steffi%22,%0A%20%20%20%20%22Powerhouse%22%3A%20%22Max%22,%0A%7D%0A%0Arest%20%3D%20%5B%22Rainer%22,%20%22Walter%22%5D%0A%0Aprint_abteilung%28%22Karl%22,%20b%C3%BCro%3D%22Jochen%22,%20*rest,%20**mitarb%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def print_abteilung(leitung, vertretung, *andere, **mitarbeiter):
    print(f"Leitung: {leitung}")
    print(f"Vertretung: {vertretung}")
    for stelle, name in mitarbeiter.items():
        print(f"{stelle}: {name}")
    for rest in andere:
        print(f"weiterhin: {rest}")
        

print_abteilung(leitung="Karl", vertretung="Steffi", büro="Jochen", it="Claudia")

print_abteilung("Karl", "Steffi", "Mirco", "Claudia", büro="Jochen", it="Claudia")

print_abteilung("Karl", vertretung="Steffi", büro="Jochen", it="Claudia")

mitarb = {
    "Support": "Steffi",
    "Powerhouse": "Max",
}

rest = ["Rainer", "Walter"]

print_abteilung("Karl", büro="Jochen", *rest, **mitarb)
```


Dies ist besonders wertvoll, wenn die Methoden intern andere Funktionen mit diversen Parametern verwendet,
die wir von außen so ansteuerbar machen.

## Verpflichtende positionale und Keyword Argumente

Um zu erzwingen, dass Argumente als positionale Argumente übergeben werden,
kann ein `/` als ein Parameter eingefügt werden. Alle Argumente vor dem `/` können nicht als 
Keyword Argumente übergeben werden. Dies sieht man jedoch selten.

Wenn man erzwingen möchte, dass Parameter als Keyword Argument gesetzt werden, kann man ein einzelnes `*`
als Parameter setzen. Dann muss jedes nach dem `*` folgende Parameter als Keyword Argument übergeben werden.
Dies sieht man sehr häufig.

```python
def somefunc(p1, p2, /, p3, p4, *, p5, p6, **kwargs):
    ...
```

## Divide and Conquer

Prinzipiell kann man mit Hilfe von `*args` das zusammenfügen von Strings erleichtern, wie man in den vorherigen beispielen gesehen hat.
Hierfür eine Funktion, die gegebenen Parameter zu einem kebab-case string verwandelt (ein Minus zwischen die Wörter einfügt):
```python
def kebab(*strings):
    result = ""
    for string in strings:
        result += string + "-"
    return result[:-len("-")]

print(kebab("one", "two", "tree"))
# Das ergibt: one-two-three
```

Da `*args` zu benutzen nur eine konvention ist, kann man wie man in dem Beispiel sieht, auch einen anderen Namen 
vergeben. Natürlich muss trotzdem ein `*` benutzt werden.

Durch das entpacken von Listen kann auch listen zerteilen.

Wenn man nun einen ersten, normalen Parameter hinzufügt, kann man durch eine Rekursion die gesamte Funktion sogar auf 
zwei Zeilen code reduzieren:
```python
def variadic_kebab(first, *va):
    return first if not va else first + "-" + variadic_kebab(*va)

print(variadic_kebab("one", "two", "tree"))
```
Das ergibt: one-two-three

Die Funktion macht hier Gebrauch von einem Ternary um zu prüfen ob die Parameterliste `va` leer ist. 
Wenn das der Fall ist, wird nur `first` returned. Wenn die Liste NICHT leer ist, dann wird der erste eintrag aus
`va` innerhalb der Rekursion zu `first`.

Wenn man die beiden Versionen der Funktion vergleicht, merkt man vor allem dass `variadic_kebab` es ermöglicht dass man 
erzwingen kann dass mindestens ein Parameter übergeben werden muss. Logisch, denn der Parameter `first` ist ja auch ein normaler Parameter.

```python
print(kebab()) # OK
print(variadic_kebab()) # Error
```

### Aufgabe: Args zu Dictionary🌶
Schreibe eine Funktion, welche `*args` als Dictionary returned. Da Dictionaries für jedes value einen Key brauchen, sollte die Funktion logischerweise bei einer ungeraden Anzahl von Parametern trotzdem noch funktionieren.


<details><summary>Lösung</summary>
<pre><code>def dictify(*strings):
    thisdict = {}
    for i in range(len(strings)//2):
        thisdict.update({strings[i]:strings[i+1]})
    return thisdict

print(dictify("a", "b", "c"))</code></pre>
</details>

Hinweis: Zur lösung dieser Aufgabe gibt es eine zweite Variante welche der `variadic_kebab` Funktion stark ähnelt.