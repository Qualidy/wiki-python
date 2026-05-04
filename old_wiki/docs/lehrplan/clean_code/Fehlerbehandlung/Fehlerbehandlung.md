# Fehlerbehandlung
[10min]
Beispiel:
```python
def divide(a, b):
    return a / b
```

Es ist wichtig, Ausnahmen zu behandeln, um unerwartete Abstürze zu vermeiden. 
Im Fall einer Division sollten wir insbesondere eine Division durch `0` abfangen. 
Beim Abfangen könnten wir den Code weiter laufen lassen:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        return None
```

oder wir lassen das programm abbrechen:

```python
import sys

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
        sys.exit(1)
```

Anderfalls wird die Exception als Rückgabe der Methode nach außen weitergeleitet und der Aufrufer von `divide` ist für
diese verantworlich. Entweder er fängt sie selbt in einem Try-Catch block oder gibt sie weiter.

## Das `finally` Statement

[10 min]

Um die reibungslose und ordnungsgemäße Abwicklung von Prozessen zu gewährleisten, ist der Einsatz eines "finally"
Blocks oft empfehlenswert. In Python dient dieser Block dazu, bestimmte Aufräum- oder Abschlussarbeiten zu garantieren,
unabhängig davon, ob während der Ausführung eine Ausnahme aufgetreten ist oder nicht.
Dies erweist sich als besonders vorteilhaft beim Umgang mit Ressourcen wie Dateien oder Netzwerkverbindungen,
da der "finally" Block sicherstellt, dass diese Ressourcen korrekt geschlossen oder freigegeben werden,
um das Entstehen von Ressourcenlecks zu verhindern.

```python
def datei_bearbeiten(dateipfad):
    try:
        datei = open(dateipfad, 'r')
        daten = datei.read()
        # Weiterverarbeitung der Daten
    except IOError:
        print("Fehler beim Lesen der Datei.")
    finally:
        # Dieser Block wird immer ausgeführt
        datei.close()
        print("Die Datei wurde geschlossen.")
    return daten

print(datei_bearbeiten("beispieldatei.txt"))
```

## Das "with" Statement
[10 min]

Das `with` Statement ist eine spezielle Form des `try` Statements, die es ermöglicht,
Ressourcen wie Dateien oder Netzwerkverbindungen zu öffnen und zu schließen.
Es ist eine gute Praxis, Ressourcen mit dem `with` Statement zu öffnen, da es sicherstellt,
dass die Ressource nach der Verwendung geschlossen wird, selbst wenn während der Ausführung eine Ausnahme auftritt.

Die Methoden `__enter__` und `__exit__` in Klassen sind Teil des sogenannten Context Management 
Protocols in Python und werden vom `with`-Statement angestuert. Sie ermöglichen es einer Klasse, als Kontextmanager zu agieren, 
wodurch bestimmte Aktionen beim Betreten und Verlassen eines Kontexts automatisiert werden können. 
Diese Methoden sind besonders nützlich für Ressourcenmanagement, wie das sichere Öffnen und Schließen von Dateien 
oder Netzwerkverbindungen.

`__enter__(self):`
* Diese Methode wird aufgerufen, wenn der Ausführungskontext durch das `with`-Statement betreten wird.
* Sie bereitet die Ressourcen vor oder führt Initialisierungen durch, die für den Kontext erforderlich sind.
* Der Rückgabewert von `__enter__` wird an die Variable zugewiesen, die optional nach dem as im with-Statement steht.

`__exit__(self, exc_type, exc_value, traceback):`
* Diese Methode wird aufgerufen, wenn der Ausführungskontext verlassen wird, das heißt am Ende des `with`-Blocks oder wenn innerhalb des Blocks eine Ausnahme auftritt.
* Sie ist verantwortlich für das Aufräumen oder Schließen von Ressourcen.
* Die Parameter `exc_type`, `exc_value` und `traceback` enthalten Informationen über eine etwaige Ausnahme, die im `with`-Block aufgetreten ist. Wenn der Block ohne Ausnahme verlassen wird, sind alle drei Werte None.

Anbei ein einfaches Beispiel für eine Klasse mit implementierten `__enter__` und `__exit__` Methoden:

```python
class MeinKontextManager:
    def __enter__(self):
        # Initialisierungen oder Ressourcen öffnen
        return self  # oder ein anderes Objekt

    def __exit__(self, exc_type, exc_value, traceback):
        # Aufräumen oder Ressourcen schließen
        # Kann True zurückgeben, um eine Ausnahme zu unterdrücken, sonst None
        ...
```

Dann können Methodeninstanzen im `with`-Block aufgerufen werden:

```python
with MeinKontextManager() as manager:
    # Aktionen innerhalb des Kontextes
    ...
```

### Aufgabe: Context Manager 🌶️🌶️🌶️
Gegeben ist eine Beispielklasse `MeineRessource`, die das Context Management Protocol implementiert,
um sicherzustellen, dass Ressourcen ordnungsgemäß geöffnet und geschlossen werden.
Ihre Aufgabe ist es, die Klasse so zu modifizieren, dass sie das `with`-Statement unterstützt,
um eine Ressource zu öffnen und automatisch zu schließen.

* Implementieren Sie die Methoden `__enter__` und `__exit__` in der Klasse MeineRessource.
* `__enter__` soll eine Nachricht ausgeben, die anzeigt, dass die Ressource geöffnet wird.
* `__exit__` soll eine Nachricht ausgeben, die anzeigt, dass die Ressource geschlossen wird und sie soll die Ressource schließen.
* Verwenden Sie die Klasse in einem with-Block, um zu demonstrieren, dass sie wie beabsichtigt funktioniert.

```python
class MeineRessource:
    def oeffnen(self):
        print("Ressource geöffnet")

    def schliessen(self):
        print("Ressource geschlossen")

# Beispiel zur Verwendung der Klasse (dies soll modifiziert werden)
ressource = MeineRessource()
ressource.oeffnen()
# Code zur Nutzung der Ressource
ressource.schliessen()
```

[Lösung](solution.md)
