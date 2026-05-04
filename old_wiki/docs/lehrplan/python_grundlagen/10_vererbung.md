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

## 1. **Auto und Elektroauto:** 🌶️️🌶️️

Erstelle die Klassen `Auto` und `Elektroauto` mit entsprechenden Attributen. Die `Elektroauto`-Klasse erbt von der `Auto`-Klasse.

- **Methodenüberschreibung:** Überschreibe die `starten`-Methode in der `Elektroauto`-Klasse, um den Elektromotor zu aktivieren.

-  **Instanzen erstellen und Methoden aufrufen:** Erzeuge Instanzen beider Klassen und rufe ihre Methoden auf.

- **Polymorphismus:** Erkläre, wie Polymorphismus durch Vererbung in diesem Beispiel umgesetzt wird.

- **Weitere Attribute:** Füge den Klassen `Auto` und 

## 2. **Figur-Hierarchie:** 🌶️️🌶️️🌶️️

Erstelle eine Basisklasse `Figur`, die grundlegende Eigenschaften wie Farbe und Position enthält. Implementiere dann zwei abgeleitete Klassen: `Kreis` und `Rechteck`. Jede dieser Klassen sollte spezifische Eigenschaften und Methoden haben, die zur jeweiligen geometrischen Form passen.

   - Verwende in der `Figur`-Klasse das Attribut `farbe` und die Methode `bewegen()`.
   - Die `Kreis`-Klasse sollte das Attribut `radius` haben und eine Methode `fläche_berechnen()` implementieren.
   - Die `Rechteck`-Klasse sollte die Attribute `länge` und `breite` haben und eine Methode `umfang_berechnen()` implementieren.

## 3. **Personen-Vererbung:** 🌶️️🌶️️🌶️️

Implementiere eine Basisklasse `Person` mit grundlegenden Informationen wie Name und Alter. Leite dann zwei Klassen ab: `Teilnehmer` und `Dozent`. Jede dieser Klassen sollte zusätzliche Informationen und Methoden haben, die zu einem Teilnehmeren bzw. Dozent passen.

   - Verwende in der `Person`-Klasse die Attribute `name` und `alter` sowie die Methode `geburtstag_feiern()`.
   - Die `Teilnehmer`-Klasse sollte das Attribut `matrikelnummer` haben und eine Methode `prüfung_schreiben()` implementieren.
   - Die `Dozent`-Klasse sollte das Attribut `fachgebiet` haben und eine Methode `prüfungen_korrigieren()` implementieren.
