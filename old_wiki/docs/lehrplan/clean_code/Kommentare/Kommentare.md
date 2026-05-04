# Kommentare
[15 min]

Kommentare in Python spielen eine wichtige Rolle für die Lesbarkeit und Wartbarkeit von Code.
Sie ermöglichen es Entwicklern, ihre Gedanken und Absichten hinter bestimmten Codeabschnitten zu erläutern.
Es gibt zwei Hauptarten von Kommentaren in Python: normale Kommentare und Docstrings.

## Normale Kommentare
Diese werden mit einem #-Symbol eingeleitet und sind für kurze Erklärungen oder Anmerkungen gedacht.
Sie erscheinen direkt im Code und sind hilfreich für Entwickler, die an dem Code arbeiten oder ihn später überprüfen.
Ein Beispiel für einen normalen Kommentar ist:

```python
# Berechnung des Quadrats einer Zahl
quadrat = number * number
```
## Docstrings
Docstrings sind mehrzeilige Kommentare, die verwendet werden, um Module, Klassen, Methoden und Funktionen zu 
dokumentieren. Sie sind umschlossen von dreifachen Anführungszeichen (""") und bieten detailliertere Informationen, 
die auch für Anwender nützlich sein können. Diese Art von Kommentar wird oft von Dokumentationswerkzeugen wie 
Sphinx verwendet, um automatisch Dokumentation zu generieren. Ein Beispiel für ein Modul mit einer Klasse und 
Funktionen mit Docstrings könnte so aussehen:

```python
"""Modul zur Demonstration von Docstrings im Numpy-Stil in Python."""

class BeispielKlasse:
    """
    Beispielklasse zur Demonstration von Docstrings im Numpy-Stil.

    Attributes
    ----------
    wert : int
        Der Wert, der bei der Initialisierung des Objekts übergeben wird.

    Methods
    -------
    quadrat()
        Berechnet das Quadrat des Wertes.
    """

    def __init__(self, wert):
        """
        Initialisiert ein Beispielobjekt mit einem gegebenen Wert.

        Parameters
        ----------
        wert : int
            Der Wert, mit dem das Objekt initialisiert wird.
        """
        self.wert = wert

    def quadrat(self):
        """
        Gibt das Quadrat des Wertes zurück.

        Returns
        -------
        int
            Das Quadrat des initialisierten Wertes.
        """
        return self.wert * self.wert

def addiere(a, b):
    """
    Addiert zwei Zahlen und gibt das Ergebnis zurück.

    Parameters
    ----------
    a : int
        Die erste Zahl.
    b : int
        Die zweite Zahl.

    Returns
    -------
    int
        Die Summe von a und b.
    """
    return a + b
```
In diesem Beispiel enthält das Modul, die Klasse BeispielKlasse sowie die Methode quadrat und die Funktion addiere jeweils einen Docstring, der beschreibt, was sie tun. Docstrings sind besonders wertvoll, da sie nicht nur den Entwicklern helfen, den Code zu verstehen, sondern auch in der automatisierten Dokumentation oder in interaktiven Umgebungen wie Jupyter Notebooks verwendet werden können, um schnell Informationen über die Verwendung einer Klasse oder Funktion zu erhalten.

### Aufgabe: Ergänzen von Docstrings 🌶️🌶️
[30 min]

Gegeben ist folgender Code:
```python
class DatenAnalysator:
    def __init__(self, daten):
        if not daten:
            raise ValueError("Die Datenliste darf nicht leer sein.")
        self.daten = daten

    def mittelwert(self):
        return sum(self.daten) / len(self.daten)

    def maximum(self):
        return max(self.daten)

    def minimum(self):
        return min(self.daten)

    def daten_normalisieren(self):
        max_wert = self.maximum()
        min_wert = self.minimum()
        return [(x - min_wert) / (max_wert - min_wert) for x in self.daten]
```

Fügen Sie der Klasse DatenAnalysator einen Docstring hinzu, der die Klasse und ihre Funktion beschreibt.
Ergänzen Sie für jede Methode in der Klasse DatenAnalysator (init, mittelwert, maximum, minimum) einen Docstring, der deren Zweck, Parameter und Rückgabewerte beschreibt.
Fügen Sie der Funktion daten_normalisieren einen Docstring hinzu, der deren Zweck, Parameter und Rückgabewerte beschreibt. Hinweise:
Hinweise:

Beachten Sie, dass die Methoden mittelwert, maximum und minimum auf die Daten zugreifen, die bei der Initialisierung der Klasse übergeben werden.
Die Funktion daten_normalisieren nimmt eine Liste von Daten entgegen und normalisiert diese, so dass alle Werte zwischen 0 und 1 liegen.
Achten Sie darauf, dass Ihre Docstrings klar und präzise sind und dem Numpy-Stil folgen.
Wenn Sie die Docstrings in einer IDE wie PyCharm oder VS Code schreiben, erhalten Sie automatisch eine Vorschau der Docstrings, wenn Sie die Klasse oder Funktion aufrufen.

[Lösung](solution.md)
