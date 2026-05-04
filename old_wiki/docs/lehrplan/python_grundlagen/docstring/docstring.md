# Docstring

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/C4WC5LDWEb8?si=JM7T_enN-rWAu3XO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Um unseren Code für den Entwickler verständlicher zu gestalten können wir Kommentare verwenden.
Dazu nutzen wir in Python das Symbol `#`, um den restlichen Teil der Codezeile von der Ausführung auszuschließen:

```python
print("Hallo") # Hier steht ein Hinweis für den Entwickler.
```

Dies ist eine gute Möglichkeit, um Hinweise über die Implementierung zu geben, wenn diese nicht mehr offensichtlich ist.
Diese Art Hinweise im Code zu geben beschränkt sich jedoch nur auf den Quellcode. Wer diese Hinweise sehen will,
muss den Code sehen. Die Hinweise sollen die Frage "Wie funktioniert das" beantworten.

Häufig stellt sich für einen Entwickler jedoch eine andere Frage, nämlich: **"Wie benutze ich das?"**

Diese Frage tritt auf, wenn wir Code von einer anderen Quelle nutzen wollen. Wir wollen meist nicht verstehen,
wie der Code intern funktioniert, sondern, wie wir ihn benutzen. Hierzu gibt es **Docstrings**

Docstrings werden z.B. nach dem Funktionskopf als Mehrzeiliger String eingefügt und sollen folgende Fragen beantworten:

* Was tut die Funktion?
* Was sind die Parameter der Funktion und welchen Einfluss haben sie (je nach Typ) auf die Ausgabe?
* Was ist die Ausgabe der Funktion?
* Ggf. Welche Exceptions können geworfen werden?
* Was gibt es sonst noch bei der Funktionsausführung zu beachten?
* Gibt es Beispiele für die Nutzung der Funktion?

Das ganze kann dann z.B. wie folgt aussehen:

```python
def input_int_in_between(prompt, minimum, maximum):
    """
    Fragt den Nutzer so lange nach einem Integer zwischen *minimum* und *maximum*,
    bis dieser ein korrektes eingibt.
    Args:
        prompt: Prompt, dass beim Nutzer erscheint und ihn um eine Zahl bittet.
        minimum: Kleinster erlaubter Integer (inklusive)
        maximum: Größter erlaubter Integer (inklusive)

    Returns:
        Der von Nutzer eingegebene Integer.
    """
    user_input = 0
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print(f"Eingabe ist nicht vom Typ int")

        if minimum <= user_input <= maximum:
            return user_input
        else:
            print(f"Eingabe ist nicht gültig.")
```

Ich gebe zu, dass das die Funktion extrem vergrößert, aber die Vorteile sind immens. Dieser Docstring
wir nämlich von deiner IDE erkannt und wird angezeigt, wenn die die Dokumentation der Funktion aufrufst.

Nicht nur das, mit fortgeschrittenen Mitteln ist es sogar möglich diese Inhalte automatisch auf einer Webseite
anzeigen zu lassen.

### Aufgabe: Docstring von random🌶
Schaue dir [die Dokumentation vom Package `random`](https://docs.python.org/3/library/random.html) an,
das im Python enthalten ist. Vergleiche diese Dann mit dem Source code. Auf diesen Code
wird am Amfang der Dokuentation verlinkt. Erkennst du, dass die Dokumentation im
Code selbst hinterlegt ist?

### Aufgabe: Eigene Docstrings schreiben🌶🌶
Erstelle einen Docstring für die folgenden Funktionen:

```python
def calculate_area_rectangle(sideA, sideB):
    return sideA * sideB


def sum_positive_numbers(numbers):
    return sum(number for number in numbers if number > 0)


def combine(list0, list1, func):
    return [func(a, b) for a, b in zip(list0, list1)]
```

### Aufgabe: Hilfe ist unterwegs🌶
Rufe `help(calculate_area_rectangle)`, `help(sum_positive_nubmers)`, `help(combine)` auf, nachdem du die 
letzte Aufgabe gelöst hast. Was siehst du?

[Lösung](solutions.md)

### Präsentationsthema: mkdocs👨‍🏫
Finde heraus, wie man mithilfe von [mkdocs](https://www.mkdocs.org/) eine Webseite erstellen kann, die
die Docstrings eines Projektes darstellt.

Wenn du dieses Thema vorbereiten und präsentieren möchtest, dann sprich gerne mit deinem Dozenten.

# Unittests in der Dokumentation

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/OWaHkJMybW8?si=1zRoKZzDSf0q2HP9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

In Python ist es gängig in der Dokumentation auch Beispiele für die die Ausführung der Funktion anzugeben.
Das besondere: Mit dem Modul `doctest` können wir überprüfen, ob diese Codebeispiele auch das gewünschte
liefern. Dies schafft Sicherheit in die Zuverlässigkeit des Programms und sollte gerne genutzt werden.


### Vorgehensweise:

Man muss das Modul `doctest` importieren. 
Dann kopiert man einen Auszug aus einer interaktiven Sitzung in den Docstring einer Funktion.

Im Folgenden zeigen wir das Vorgehen an einem simplen Beispiel.
Dazu haben wir das vorige fibonacci-Modul bis auf die Funktion fib abgespeckt:

```python
def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
```

Zur Erinnerung: Die Fibonaccizahlen beginnen mit `0` und `1`. Eine neue Generation von Fibonaccizahlen entsteht
aus der Summe der letzten beiden Fibonaccizahlen. Also:

* Die 0-te Generation ist 0.
* Die 1-te Generation ist 1.
* Die 2-te Generation ist 0 + 1 = 1.
* Die 3-te Generation ist 1 + 1 = 2.
* Die 4-te Generation ist 1 + 2 = 3.
* Die 5-te Generation ist 2 + 3 = 5.
* Die 6-te Generation ist 3 + 5 = 8.
* Die 7-te Generation ist 5 + 8 = 13.
* usw. ...

Dieses Modul rufen wir nun in einer interaktiven Python-Shell auf und lassen ein
paar Werte berechnen:

```bash
>>> from fibonacci import fib
>>> fib(0)
0
>>> fib(1)
1
>>> fib(10)
55
>>> fib(15)
610
>>> 
```

Diese Aufrufe mit den Ergebnissen kopieren wir aus der interaktiven Shell in den
Docstring unserer Funktion. Damit das Modul doctest aktiv wird, müssen wir die
Methode `testmod()` starten. Das vollständige Modul sieht nun wie folgt aus:

```python
import doctest

def fib(n):
    """ 
    Die Fibonacci-Zahl für die n-te 
    Generation wird iterativ berechnet 

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    610
    >>> 

    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__": 
    doctest.testmod()
```

Starten wir obiges Modul direkt mit dem Aufruf

```bash
$ python3 fibonacci.py
```

erhalten wir **keine Ausgabe, weil alles okay** ist.

Deshalb bauen wir wieder einen kleinen Fehler ein. Dazu ändern wir erneut die Zeile

```python
a, b = 0, 1
```

in

```python
a, b = 1, 1
```

um.

Nun erhalten wir folgende Ausgabe beim direkten Start des Moduls:

```bash
$ python3 fibonacci_doctest.py 
**********************************************************************
File "fibonacci.py", line 8, in __main__.fib
Failed example:
    fib(0)
Expected:
    0
Got:
    1
**********************************************************************
File "fibonacci.py", line 12, in __main__.fib
Failed example:
    fib(10) 
Expected:
    55
Got:
    89
**********************************************************************
File "fibonacci.py", line 14, in __main__.fib
Failed example:
    fib(15)
Expected:
    610
Got:
    987
**********************************************************************
1 items had failures:
   3 of   4 in __main__.fib
***Test Failed*** 3 failures.
```

Es werden alle Aufrufe angezeigt, die ein fehlerhaftes Ergebnis geliefert haben.
Wir sehen jeweils den Beispielaufruf hinter der Zeile "Failed example:". Hinter
"Expected:" folgt der erwartete Wert, also der korrekte Wert, und hinter "Got:"
folgt der von der Funktion produzierte Ausdruck, also der Wert, den doctest beim
Aufruf von fib erhalten hat.

Wir werden später mit Unittests ausgefeiltere Techniken sehen, um Code zu testen.
Dennoch ist dies ein wertvolles Feature, dass dem Nutzer deiner Library viel Freude
machen wird. Denn die Unittests, die wir später betrachten, sind genau so wie `#`-Kommentare
nicht so einfach einsehbar, wie die Dokumentation.

### Aufgabe: Selber Testen.🌶🌶
Erstelle für die folgende Funktion den docstring und gebe auch doctests an:

```python
def divide(a,b):
    return float(a / b)
```

Finde auch heraus, wie ein Doctest für `divide(42, 0)` angegeben werden kann, der ja
einen `ZeroDivisionError` wirft.

[Lösung](solutions.md#aufgabe-selber-testen)
