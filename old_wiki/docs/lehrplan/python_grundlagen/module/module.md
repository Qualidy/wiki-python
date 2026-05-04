# Module und Pakete

In Python ermöglichen Module und Pakete die Organisation von Code in wiederverwendbare Einheiten, um die Lesbarkeit zu verbessern
und die Codeverwaltung zu optimieren.

## Module

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/NNJgJ7-EW10?si=vgr49JBc_nwKAQDh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Ein Modul in Python ist im Grunde genommen eine `.py`-Datei mit Python-Code.
In dieser Datei können Funktionen, Variablen und Klassen definiert werden,
die in anderen Python-Dateien wiederverwendet werden können. Es gibt

Angenommen, du erstellst eine Datei/Modul namens `greetings.py`:

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"
```

Und im selben Ordner eine andere Datei namens `main.py`.
Wir können das Modul `greetings.py` und die darin enthaltene Methode nun wie folgt
verwenden:

```python
# main.py

import greetings

print(greetings.greet("Alice"))
```

Du kannst auch Alias für Module verwenden, um den Code kompakter zu gestalten:

```python
# main.py

import greetings as gr

print(gr.greet("Bob"))
```

Wir können auch nur die einzelne Funktion zu importieren

```python
# main.py

from greetings import greet

print(greet("Bob"))
```

Oder alle Funktionen, die es in einem Modul gibt:

```python
# main.py

from greetings import *

print(greet("Bob"))
```

Es ist jedoch ratsam, selektiv zu importieren, um potenzielle Namenskonflikte zu vermeiden.

### Aufgabe: Zufälle gibts...🌶🌶
Erstelle eine Datei namens `my_random.py`.
Erstelle in dieser eine Funktion `random_squares`,
die eine Zahl `n` als Parameter erwartet.
Sie gibt dann eine zufällige Quadratzahl zwischen `1` und `n * n` zurück.

Beim Aufruf `random_squares(5)` könnten also `1`, `4`, `9`, `16` oder `25` zurückgegeben werden.

Importiere dazu eine passende Funktion aus dem Modul `random`.

Erstelle jetzt eine zweite Datei `main.py` und importiere deine `random_squares` Funktion aus `my_random.py`. Nutze ein `print()` um deine Methode zu testen.

[Lösung](solutions.md#aufgabe-zufälle-gibts)

### Aufgabe: Abzocke ausdenken🌶🌶
Erstelle eine neue Datei namens `casino_games.py`.
Erstelle darin eine Funktion `bet_under_squares(my_bet, faktor)`.
Die Funktion erwartet zwei Integer, `my_bet` und `faktor`. Der `faktor` soll hier die Risikobereitschaft des Spielers darstellen um höhre Gewinne zu bekommen.

In der Funktion soll eine quadratische Zufallszahl zwischen `1` und `faktor * faktor`
gewürfelt werden. Importiere und nutze dazu die Funktion `random_squares`

Um den späteren Spielern unseres Casino-Games das Geld aus der Tasche zu ziehen müssen wir jetzt die Gewinnbedingung setzen.
Wenn die quadratische Zufallszahl kleiner oder gleich `my_bet` ist,
soll `faktor * my_bet` returned werden, andernfalls `0`.

Der Spieler verliert also alles, falls die Zufallszahl kleiner als sein gebot ist (was mit höherem Risiko (`faktor`) exponentiell wahrscheinlicher wird).

[Lösung](solutions.md#aufgabe-abzocke-ausdenken)

### Aufgabe: Sicherheit muss sein🌶🌶🌶
Erstelle eine weitere Funktion `input_int_in_between(prompt, minimum, maximum)` 
in wieder einem neuen Modul `secure_input`.

In der Funktion wird ein `input` als Integer vom Nutzer abgefragt, der zwischen `minimum` und `maximum` liegt. Dabei wird
der übergebene `prompt` auf dem Bildschirm angezeigt.
Dieser Input wird von der Funktion als Integer zurückgegeben.

Wenn die Eingabe ungültig ist, soll
(z.B. mithilfe von Exceptionhandling)
erneut um eine gültige Eingabe gebeten werden.

[Lösung](solutions.md#aufgabe-sicherheit-muss-sein)

### Aufgabe: Tische bereit machen 🌶🌶🌶
Füge dem Modul `casino_game` eine neue Methode `play_game(rounds, money)` hinzu.
Diese Methode dient dazu, dass mehrere Runden (`rounds`) gespielt werden kann. Hier wird dann mehrfach `bet_under_square` ausgeführt.

Diese Methode `play_game` bittet den
Nutzer um einen Einsatz (der maximal die Höhe
seines Geldes `money` betragen darf).

Dann fragt `play_game` und um einen vom
Nutzer gewählten Faktor. Mit diesem Einsatz und Faktor wird die `bet_under_square` Methode ausgeführt und das Ergebnis
mit zum momentanen Geld hinzugefügt.

`rounds` soll defaultmäßig auf 5 gesetzt sein.
`money` soll defaultmäßig auf 10 gesetzt sein.

[Lösung](solutions.md#aufgabe-tische-bereit-machen)