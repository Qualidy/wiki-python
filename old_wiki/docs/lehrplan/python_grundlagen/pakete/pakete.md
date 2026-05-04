# Module und Pakete

In Python ermöglichen Module und Pakete die Organisation von Code in wiederverwendbare Einheiten, um die Lesbarkeit zu verbessern
und die Codeverwaltung zu optimieren.

## Pakete

Packages (deutsch: "Pakete") sind Verzeichnisse, die Module und möglicherweise Unterpakete enthalten.

### Wofür braucht man Pakete?
Set the stage for [PyPi](https://pypi.org/)!

PyPI ist ein Online-Repository für öffentliche Python-Pakete. Entwickler können Pakete veröffentlichen, die jeder installieren und verwenden kann. Für jedes Paket gibt es hier eine Installationsanleitung, eine Beschreibung, Versionshinweise und Informationen zu Abhängigkeiten.

### Aufgabe: Erkunde PyPI 🌶️
Besuche [PyPi](https://pypi.org/) undschau dich um, suche nach einem beliebten Paket, zum Beispiel `requests`.

### Pakete selber packen
Ein Package enthält **immer** eine `__init__.py`. Diese zeigt an,
dass es sich bei dem Ordner um ein Python Package handelt.

```
my_package/
|-- __init__.py
|-- module1.py
|-- module2.py
|-- subpackage/
|   |-- __init__.py
|   |-- module3.py
```

### Aufgabe: Türen auf in unserem Casino 🌶
Unsere Casino-module aus [Module](../module/module.md) sollen jetzt in ein eigenes erstes Paket umgewandelt werden. Hierzu erstellen wir einen Ordner `my_casino` und füge alle bisher erstellten Dateien
darin ein.

Zusätzlich erstellen wir eine Datei `__init__.py` ohne Inhalt.

Die Ordnerstruktur sieht danach wie folgt aus:

```
my_casino/
|-- __init__.py
|-- casino_games.py
|-- my_random.py
|-- secure_input.py
```

In den Modulen (Files) wirst du die imports umbenennen müssen.

```python
from my_casino.secure_input import input_int_in_between
from my_casino.my_random import random_squares
```

Öffne nun eine Pythonkonsole und führe die folgenden Befehle aus:

```python
>>> from my_casino.casino_games import play_game
>>> play_game()
```

Auf gehts!🤑💰

[Lösung](solutions.md#aufgabe-türen-auf)


### Aufgabe: Noch mal auf Englisch 📺

Das folgende Video von [NeuralNine](https://www.youtube.com/watch?v=GxCXiSkm6no) 
fasst die Inhalte dieses Kapitels zusammen und vertieft sie.
Schau dir das Video an und stell mit deinem Tutor sicher, dass du alle Inhalte verstehst.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GxCXiSkm6no?si=s0zw6JnWV3lWkjSw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Auch [2MinutesPy](https://www.youtube.com/watch?v=mWaMSGwiSB0) hat ein schönes Video zu `__init__.py`:

<iframe width="560" height="315" src="https://www.youtube.com/embed/mWaMSGwiSB0?si=i-Qa1KO96IDlFLD_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Was ist Name == Main?
<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/57b8gJKZf6o?si=sBKUorE0e-MlfRoK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Wenn wir die folgende Datei `greetings.py` ausführen

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"

greet("Gustav")
```

so erhalten wir auf der Konsole folgenden Output:

```python
"Hello, Gustav"
```

Wenn wir diese Datei jedoch importieren, so wird die Methode `greet("Gustav")` auch ausgeführt:

```python
from greetings.py import greet

greet("Hanna")
```

Konsolenausgabe

```python
"Hello, Gustav"
"Hello, Hanna"
```

Genau hierfür gibt es die Bedingung `if __name__ == "__main__":`. Sie ermöglicht es, Code in einem Modul auszuführen, wenn es direkt ausgeführt wird, aber nicht, wenn es in einem anderen Skript importiert wird. 

Die Variable `__name__` ist eine besondere Variable in Python, die, je nachdem, wie ein Python-Skript verwendet wird, einen unterschiedlichen Wert annehmen kann. Es gibt zwei Hauptkontexte, in denen ein Python-Skript ausgeführt werden kann: entweder als Hauptprogramm oder als Modul, das in ein anderes Skript importiert wird.

1. Wenn das Skript direkt ausgeführt wird, setzt Python die Variable __name__ auf den Wert "__main__".
2. Wird das Skript jedoch importiert und in einem anderen Skript verwendet, wird __name__ auf den Namen des Skripts (genauer gesagt: auf den Namen des Moduls) gesetzt.

Diese Unterscheidung ist besonders nützlich, um zu bestimmen, welcher Code ausgeführt werden soll, je nachdem, ob das Skript direkt gestartet oder als Modul importiert wird

```python
# greetings.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Gustav"))
```

Führen wir die Datei `greetings.py` aus, erhalten wir weiterhin:
```python
"Hello, Gustav"
```

Wenn wir `greetings.py` aber nun importieren ...
```python
from greetings.py import greet

greet("Hanna")
```

erhalten wir auch die gewünschte Konsolenausgabe:

```python
"Hello, Hanna"
```
