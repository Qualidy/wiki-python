# Projekt: Dungeon Inventory & Battle Simulator

In diesem Projekt entwickelst du eine kleine textbasierte Dungeon-Simulation.
Das Projekt soll zeigen, dass du OOP nicht nur in Einzelaufgaben, sondern in
einem zusammenhängenden Programm anwenden kannst.

## Grundidee

Eine Spielfigur betritt einen Dungeon. Dort gibt es Räume, Gegenstände,
Hindernisse oder Gegner. Die Spielfigur kann Aktionen ausführen, Gegenstände
sammeln, einfache Kämpfe oder Ereignisse erleben und am Ende einen kleinen
Spielstand anzeigen oder speichern.

Das Projekt bleibt bewusst textbasiert. Es geht nicht um Grafik, sondern um
saubere Modellierung mit Klassen.

## Kreativer Rahmen

Du darfst die genaue Richtung selbst wählen:

- klassischer Fantasy-Dungeon
- Roboter-Labor
- Weltraumstation
- Museum bei Nacht
- Schulgebäude mit Rätseln
- Survival-Simulation
- eigenes Thema

Wichtig ist nicht das Thema, sondern die OOP-Struktur.

## Pflichtanforderungen

| Konzept | Mindestanforderung |
|---------|--------------------|
| Klassen | mindestens 6 eigene Klassen |
| Konstruktoren | Attribute über `__init__` initialisieren |
| Methoden | Verhalten in Methoden kapseln |
| Vererbung | mindestens eine sinnvolle Vererbungshierarchie |
| Overriding | mindestens eine Methode in einer Unterklasse überschreiben |
| Polymorphismus | mehrere Objekte über dieselbe Methode benutzen |
| Klassenattribute | mindestens ein sinnvolles Klassenattribut |
| Kapselung | mindestens ein `_attribut` oder `__attribut` begründet einsetzen |
| Magic Methods | mindestens `__str__`, zusätzlich optional `__len__` oder `__eq__` |
| Introspection | Debug-Ausgabe mit `__dict__`, `hasattr()`, `__name__`, `__bases__` |
| Fehlerbehandlung | mindestens eine eigene Exception oder bewusstes `raise` |
| Datei-I/O | Speichern oder Laden von einfachen Projektdaten |

## Was du selbst entscheiden sollst

Bevor du programmierst, entscheide:

- Welche Dinge existieren in deiner Welt?
- Welche davon sind Klassen?
- Welche Klassen sind spezielle Varianten anderer Klassen?
- Welche Klassen enthalten andere Objekte?
- Welche Methode könnte polymorph verwendet werden?
- Welche Daten müssen geschützt oder validiert werden?
- Was soll gespeichert werden?

## Mögliche Rollen im Projekt

Diese Liste ist keine fertige Klassenstruktur. Sie soll nur beim Denken helfen.

| Rolle im Programm | Mögliche Beispiele |
|-------------------|--------------------|
| aktive Figur | Spieler, Roboter, Agent, Forscher |
| Gegenspieler oder Hindernis | Gegner, Sicherheitssystem, Falle |
| Gegenstand | Werkzeug, Schlüssel, Trank, Karte |
| Sammlung | Inventar, Rucksack, Werkzeugkiste |
| Ort | Raum, Level, Station |
| Ereignis | Kampf, Rätsel, Fund, Dialog |
| Verwaltung | Spiel, Menü, Speicherfunktion |

Du musst nicht alle Rollen verwenden.

## Polymorphismus im Projekt

Überlege dir eine Methode, die mehrere Klassen gemeinsam anbieten. Beispiele:

| Methode | Idee |
|---------|------|
| `use()` | verschiedene Gegenstände werden benutzt |
| `interact()` | verschiedene Objekte reagieren auf Interaktion |
| `describe()` | verschiedene Dinge beschreiben sich selbst |
| `attack()` | verschiedene Figuren greifen unterschiedlich an |
| `trigger()` | verschiedene Ereignisse werden ausgelöst |

Der aufrufende Code soll nicht für jede Unterklasse komplett anders aussehen.

```python
for game_object in objects:
    print(game_object.describe())
```

## Introspection im Projekt

Baue eine kleine Debug-Funktion ein:

```python
def inspect_object(obj):
    print("Klasse:", obj.__class__.__name__)
    print("Modul:", obj.__class__.__module__)
    print("Attribute:", obj.__dict__)
    print("Direkte Oberklassen:", obj.__class__.__bases__)
```

Teste diese Funktion mit mindestens drei verschiedenen Objekten.

## Mindestablauf

Dein Programm soll am Ende einen kleinen Ablauf zeigen, zum Beispiel:

```text
Willkommen im Dungeon.
Du bist in Raum 1.
Du findest einen Gegenstand.
Du benutzt einen Gegenstand.
Ein Ereignis wird ausgelöst.
Der aktuelle Zustand wird angezeigt.
Debug-Informationen werden ausgegeben.
```

Das muss kein fertiges Spiel sein. Eine gut strukturierte Simulation reicht.

## Arbeitsphasen

### Phase 1: Idee und Modell

Erstelle eine kurze Projektskizze:

- Thema
- Ziel des Programms
- wichtigste Klassen
- wichtigste Beziehungen
- eine polymorphe Methode

### Phase 2: Minimalversion

Implementiere zuerst nur das Kernmodell:

- Klassen
- Konstruktoren
- einfache Methoden
- kurze Demo ohne Menü

### Phase 3: Vertiefung

Ergänze:

- Overriding
- Magic Method
- Exception
- Datei-I/O
- Introspection

### Phase 4: Dokumentation

Schreibe eine `README.md`:

- Projektidee
- Startanleitung
- Bedienung
- Klassenüberblick
- Beispielablauf
- bekannte Grenzen

{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/11_projekt_idee_modellieren.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/12_projekt_minimalversion.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/29_projekt_klassen_review.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/30_projekt_persistenz_debug.yaml") }}
