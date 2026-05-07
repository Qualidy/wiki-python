# Vererbung in Python
[120min]

Die Vererbung ist ein fundamentales Konzept in der objektorientierten Programmierung (OOP), das die Wiederverwendbarkeit von Code ermöglicht. In Python wird Vererbung durch die Schaffung von Klassen als Unterklasse einer anderen Klasse realisiert.

## Erklärung

Eine Klasse erbt von einer anderen, indem sie die zu erbende Klasse in Klammern nach dem Klassennamen angibt:

```python
class Fahrzeug:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def get_info(self):
        return f"{self.marke} {self.modell}"

class Elektroauto(Fahrzeug):
    def __init__(self, marke, modell, reichweite):
        super().__init__(marke, modell)
        self.reichweite = reichweite

    def get_info(self):
        return f"{super().get_info()}, Reichweite: {self.reichweite} km"
```

Hier erbt `Elektroauto` von `Fahrzeug` und _überschreibt_ die `__init__`- und `get_info`-Methoden.

Das Konzept des **Überschreibens** in Python ermöglicht es einer abgeleiteten Klasse (Unterklasse), eine Methode der Basisklasse (Superklasse) mit einer eigenen Implementierung zu ersetzen. Dabei wird die gleiche Methode (gleicher Name und gleiche Signatur) in der Unterklasse neu implementiert.

## Beispiel: Auto und Elektroauto

```python
class Auto:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def starten(self):
        return f"{self.marke} {self.modell} wird gestartet."

class Elektroauto(Auto):
    def __init__(self, marke, modell, reichweite):
        super().__init__(marke, modell)
        self.reichweite = reichweite

    def starten(self):
        return f"{super().starten()} Elektromotor wird aktiviert."

    def aufladen(self):
        return f"{self.marke} {self.modell} wird aufgeladen."

# Instanzen erstellen
mein_auto = Auto("Volkswagen", "Golf")
mein_elektroauto = Elektroauto("Tesla", "Model S", 500)

# Methoden aufrufen
print(mein_auto.starten())          # Ausgabe: "Volkswagen Golf wird gestartet."
print(mein_elektroauto.starten())   # Ausgabe: "Tesla Model S wird gestartet. Elektromotor wird aktiviert."
print(mein_elektroauto.aufladen())  # Ausgabe: "Tesla Model S wird aufgeladen."
```

# Aufgaben:
[320min]

{{ task(file="tasks/python_grundlagen/10_vererbung/01_auto_und_elektroauto.yaml") }}
{{ task(file="tasks/python_grundlagen/10_vererbung/02_figur_hierarchie.yaml") }}
{{ task(file="tasks/python_grundlagen/10_vererbung/03_personen_vererbung.yaml") }}
