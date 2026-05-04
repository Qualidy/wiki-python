# Funktionsgestaltung
Grundlagen
[10 min]

Funktionen sollten die folgenden Eigenschaften haben:

**Kürze**: Funktionen sollten möglichst kurz gehalten werden. Das macht sie leichter zu verstehen und zu warten.

**Einzelne Aufgabe**: Jede Funktion sollte sich nur um eine Sache kümmern. Dieses Prinzip wird oft als "Do One Thing!" bezeichnet. Wenn eine Funktion nur eine Aufgabe hat, ist sie einfacher zu nutzen und zu überprüfen.

**Klare Benennung**: Der Name einer Funktion und die Namen ihrer Parameter sollten genau beschreiben, was die Funktion tut und was für Daten sie erwartet. Gute Namen machen den Code selbsterklärend. Die Bennenung folgt dem gleichen Prinzip wie die Benennung von Variablen.

**Abstraktionsebene**: Eine Funktion sollte sich nur um Aufgaben auf einer bestimmten Abstraktionsebene kümmern. Das bedeutet, dass alle Schritte in der Funktion ähnlich komplex sein sollten. Zum Beispiel sollte eine Funktion nicht gleichzeitig sehr detaillierte Berechnungen durchführen und hochgradig abstrakte Entscheidungen treffen.

**Wenige Argumente**: Funktionen sollten idealerweise nur wenige Parameter haben. Zu viele Parameter können den Code unübersichtlich und schwer zu handhaben machen.

**Fehlerbehandlung**: Funktionen sollten echte Fehler richtig verarbeiten, anstatt spezielle Fehlerwerte an den aufrufenden Code zurückzugeben. So wird es einfacher, Fehler direkt an der Quelle zu identifizieren und zu beheben, und der übergeordnete Code bleibt sauberer und klarer.

**Keine Seiteneffekte**: Funktionen sollten idealerweise keine Seiteneffekte haben, d.h. sie sollten den Zustand des Programms außerhalb ihrer selbst nicht verändern. Das macht den Code vorhersehbarer und reduziert die Wahrscheinlichkeit von Fehlern, die durch unerwartete Änderungen an Daten entstehen, die außerhalb der Funktion liegen.

### 1. Aufgabe: Code aufteilen
[30 min]
1. Teile den folgenden Code in mehrere Funktionen auf, die jeweils nur eine Sache tun.
2. Benenne die Funktionen und ihre Parameter entsprechend.

```python
import sys

def komplexe_funktion():
    # Eingaben einlesen
    if len(sys.argv) < 3:
        print("Bitte mindestens zwei Zahlen als Argumente eingeben.")
        return

    zahl1 = int(sys.argv[1])
    zahl2 = int(sys.argv[2])

    # Berechnungen durchführen
    summe = zahl1 + zahl2
    differenz = zahl1 - zahl2
    produkt = zahl1 * zahl2
    if zahl2 != 0:
        quotient = zahl1 / zahl2
    else:
        quotient = "Unendlich"

    # Ergebnisse ausgeben
    print(f"Summe: {summe}")
    print(f"Differenz: {differenz}")
    print(f"Produkt: {produkt}")
    print(f"Quotient: {quotient}")

if __name__ == "__main__":
    komplexe_funktion()
```

[Lösung](solution.md#lsung-aufgabe-1)

### Aufgabe 2: Code lesbarer machen 🌶️🌶️
[20 min]

Überarbeite den folgenden Python-Code, der eine Textanalyse durchführt. Der aktuelle Code nutzt unklare und
verwirrende Namen, die es schwierig machen, die Funktionalität und Absicht des Codes zu verstehen.
Deine Aufgabe ist es, den Code zu überarbeiten, um ihn klarer und verständlicher zu machen.

```python
def text(a):
b = a.split()
c = len(b)
d = {}
e = 0
         for f in b:
if f in d:
d[f] += 1
else:
d[f] = 1
e += len(f)
g = None
h = 0
         for i, j in d.items():
if j > h:
h = j
g = i
k = e / c
return c, g, k

if __name__ == "__main__":
l = text("Beispieltext mit einigen Wörtern. Einige Wörter wiederholen sich.")
print("Zählung:", l[0])
print("Oft:", l[1])
print("Durchschn:", l[2])
```

[Lösung](solution.md#lsung-aufgabe-2)

### Aufgabe 3: Listenmanipulation und String- Verarbeitung 🌶️🌶️
[30 min]
Gegeben ist eine Liste von Wörtern. Schreiben Sie eine Python-Funktion, die folgende Anforderungen erfüllt:

* Die Funktion soll alle Wörter in der Liste umkehren.
* Die Funktion soll dann die umgekehrten Wörter zu einem einzigen String zusammenfügen, wobei jedes Wort durch ein Komma und ein Leerzeichen getrennt ist.
* Schließlich soll die Funktion den so erstellten String zurückgeben.

  Beispiel:
```python
words = ["Python", "Entwicklung", "spaßig", "Lernen"]
```
Erwartete Ausgabe:
```
nohtyP, gnukcitnE, gißaps, nereL
```
Implementieren Sie die Funktion reverse_and_combine_words(words).

Hinweis: Verwenden Sie keine externen Bibliotheken oder Funktionen wie `join()` oder `reverse()`, sondern nur Schleifen und String-Operationen.

[Lösung](solution.md#lsung-aufgabe-3)
