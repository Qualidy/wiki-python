# Objektorientierte Programmierung (OOP) mit Python
[120min]

Die objektorientierte Programmierung (OOP) ist in Python weit verbreitet und basiert
auf den grundlegenden Konzepten von Klassen und Objekten.
Hier werfen wir einen Blick auf die Prinzipien der OOP in Python.

## Klassen und Objekte in Python

In Python werden Klassen erstellt, um Objekte zu definieren. Eine Klasse ist eine Bauplan für Objekte, die Attribute (Variablen) und Methoden (Funktionen) enthalten kann. Ein Objekt ist eine Instanz einer Klasse.

```python
class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def zeige_info(self):
        print(f"Marke: {self.marke}, Farbe: {self.farbe}")
```

In diesem Beispiel erstellen wir eine Klasse namens `Auto`.
Die Methode `__init__` wird beim Erstellen eines neuen Objekts aufgerufen und initialisiert die Attribute `marke` und `farbe`. Die Methode `zeige_info` gibt Informationen zum Auto aus.

Ein Objekt ist eine Instanz einer Klasse. Wenn wir die Klasse Auto instanziieren, erhalten wir ein konkretes Auto-Objekt.

Um eine Instanz, ein Objekt von der Klasse `Auto` zu erstellen schreiben wir:

```python
# Erstellen einer Instanz und speichern in Variable
tiguan = Auto("Volkswagen", "rot")

# Zugriff auf die Methode
tiguan.zeige_info()
```

Wir können demnach auch mehrere Objekte erstellen und diese beispielsweise in einer Liste speichern:

```python
# Erstellen einer Instanz und speichern in Variable
tiguan = Auto("Volkswagen", "rot")
golf = Auto("Volkswagen", "blau")
id4 = Auto("Volkswagen", "schwarz")

autos = [tiguan, golf, id4]

# Iteriere über alle Autos in der Liste
for a in autos:
    a.zeige_info()
```

## Attribute

Attribute sind Daten, die zu einem Objekt gehören und seinen Zustand repräsentieren. 
Im obigen Beispiel sind `marke` und `farbe` Attribute unseres `Auto`-Objekts.

## Methoden

Methoden sind Funktionen, die zu einer Klasse gehören und Operationen auf den Daten der Klasse ausführen.
Sie können auf Attribute zugreifen und diese verarbeiten.

Hier haben wir die Methode `zeige_infos` hinzugefügt, die Informationen über das Auto ausgibt.

In Python wird `self` als Parameter in den Methoden verwendet, um auf das aktuelle Objekt zuzugreifen. Es ist eine Konvention, `self` zu verwenden, kann aber auch anders benannt werden.

## Das `self` Schlüsselwort

In Python steht das `self` Schlüsselwort für die Instanz der Klasse selbst und wird als erster Parameter an 
alle Methoden übergeben. Es ermöglicht den Zugriff auf die Attribute und Methoden der Instanz innerhalb der Klasse.

```python
class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def zeige_info(self):
        print(f"Marke: {self.marke}, Farbe: {self.farbe}")
```

# Aufgaben zu Klassen
[360min]

{{ task(file="tasks/python_grundlagen/07_oop_python/01_bibliotheksverwaltungssystem.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/02_fahrzeugvermietungssystem.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/03_online_shop_mit_warenkorb.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/04_schuler_und_kursverwaltung.yaml") }}
## 5. **Zeitverwaltung mit Aufgabenliste 🌶️️🌶️️🌶️️🌶️️**
Entwickle eine Anwendung zur Zeitverwaltung. Erstelle Klassen für Aufgaben und eine Aufgabenliste. Die Aufgabenklasse sollte Attribute wie Titel, Beschreibung und Fälligkeitsdatum haben. Die Aufgabenlistenklasse sollte Methoden zum Hinzufügen, Löschen und Anzeigen von Aufgaben enthalten.

{{ task(file="tasks/python_grundlagen/07_oop_python/05_bankkonto_transaktionen.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/06_flugbuchungssystem.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/07_fitness_tracker.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/08_musikbibliothek.yaml") }}
{{ task(file="tasks/python_grundlagen/07_oop_python/09_restaurantreservierungssystem.yaml") }}
