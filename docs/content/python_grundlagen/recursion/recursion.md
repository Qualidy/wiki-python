# Exkurs: Rekursive Funktionen

![](recursion.jpg)

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/w_FmtAXTRdc?si=sVXyr44ODVGmXkY3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Es ist möglich eine Funktion in ihrem eigenen Funktionsrumpf aufzurufen. Das wirkt vllt etwas komisch,
da man sich denken könnte, wie kann ich etwas benutzen, wenn es noch gar nicht zu definiert ist. Aber das ist kein
Problem. Manchmal erfordert eine Prozedur, dass man sie erneut auf einem Teilproblem anwendet.

**Beispiel:** Angenommen, du hast eine Kiste mit kleineren Kisten und Geldstücken. In jeder Kiste können 
weiter Kisten und/oder Geldstücke sein. Was musst du jetzt tun, um alle Geldstücke zu finden?

Der folgende Ablaufplan kann erklären, wie der Prozess abläuft:

```mermaid
graph TD;
    S([Start])-->A["Nehme Objekt in die Hand"] 
    A ---> B{"Was ist <br/>das Objekt?"} 
    B --"Geld"--> D["Füge es dem Geldstapel hinzu"] 
    B --Kiste--> C["Öffne Kiste"] 

    C --"Für jedes Objekt in der Kiste"--> A
    
    
    D ---> E{"Ist noch ein<br/> Objekt in der<br/> Kiste?"}
    E --"Ja"--> A
    E --"Nein"--> F["Kehre zur Oberkiste zurück<br/>Füge alle Geldstapel zusammen"]-->A
```

Der folgende Code beschreibt, wie man dieses Problem in Python umsetzen könnte.

[💻 Online Compiler](https://pythontutor.com/render.html#code=def%20sum_up%28box_or_value%29%3A%0A%20%20%20%20%0A%20%20%20%20if%20isinstance%28box_or_value,%20list%29%3A%0A%20%20%20%20%20%20%20%20summe%20%3D%200%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20for%20obj%20in%20box_or_value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20summe%20%2B%3D%20sum_up%28obj%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20summe%20%3D%20box_or_value%0A%20%20%20%20%0A%20%20%20%20return%20summe%0A%20%20%20%20%0Aall_summed_up%20%3D%20sum_up%28%5B%5B1,2,3%5D,%20%5B4,5,%5B6,7,8%5D%5D%5D%29%0Aprint%28all_summed_up%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
def sum_up(box_or_value):
    
    if isinstance(box_or_value, list):
        summe = 0
        
        for obj in box_or_value:
            summe += sum_up(obj)
            
    else:
        summe = box_or_value
    
    return summe
    
all_summed_up = sum_up([[1,2,3], [4,5,[6,7,8]]])
print(all_summed_up)
```


In der Funktion `sum_up` wird zunächst geprüft, ob der übergebene Parameter eine Liste ist oder nicht.
Wenn nicht, so wird das Objekt selbst zurückgegben. Wenn doch, so wird die Funktion `sum_up` für jedes Objekt
in der Liste wieder aufgerufen. Das Ergebnis von `sum_up` ist am Ende ja eine Zahl und das können wir der
`summe` hinzufügen.

### Aufgabe: Multiplizieren🌶
Wie muss der obige Code angepasst werden, damit die Zahlen nicht summiert, sondern multipliziert werden?

### Aufgabe: umständlich?🌶🌶
Gebe der folgenden Funktion einen Namen, der beschreibt, was sie tut.

```python
def func(my_list):
    if len(my_list) == 0:
        return 0
    return my_list[0] + func(my_list[1:])

func([1,2,3])
```

### Aufgabe: Fakultät berechnen🌶🌶🌶
Man kann die Fakultät einer Zahl `n` mit der Formel folgenden Formel berechnen:
    
    n! = 1, wenn ≤ n
    n! = n * (n-1)!, andernfalls

Nutze das, um eine rekursive Implementierung von der Fakultätsfunktion zu programmieren.

### Aufgabe: Binäre Suche🌶🌶🌶
In dieser Aufgabe sollen sie die binäre Suche rekursiv implementieren.
Bei der binären Suche gehen hier davon aus, dass wir eine **sortierte** Liste haben.
In dieser Liste wird nach einem bestimmten Eintrag gesucht. Die Funktion `binary_search(my_list, element)` gibt also
`True` zurück, wenn der Eintrag in der Liste gefunden wurde und `False` anderfalls.

Ablauf der binären Suche: Man betrachtet zunächst das Element `m` genau in der Mitte der Liste.
Ist `m` bereits das gesuchte Element `e`, so sind wir fertig und können `True` zurückgeben.
Andernfalls suchen wir in der linken Teilliste von `m` weiter, wenn `m < e` ist.
Ist jedoch `m > e`, so suchen wir in der rechten Teilliste weiter. Die binäre Suche
beginnt also auf einem kleinen Problem immer wieder von vorn. Wenn wir jemals eine 
leere Liste durchsuchen sollen, wissen wir, dass `e` sich nicht in der Liste befindet
und wir können `False` zurückgeben.

```mermaid
graph TD;
    S(["Start<br/>Gesucht ist <b>e</b>"]) --> A{"Ist Liste leer?"}
    A --Ja--> F([return False])
    A --Nein--> M["Es sei <b>m</b> Element<br/>in der Mitte<br/>der Liste"]
    M --> B{"m ? e"}
    B --"m > e"--> C["Nehme die <br/>linke Teilliste"] --> A
    B --"m < e"--> D["Nehme die <br/>rechte Teilliste"] --> A
    B --"m == e"--> T(["return True"])
```
![](binary_sort_example.PNG)

[Lösung](solutions.md#rekursive-funktionen)
