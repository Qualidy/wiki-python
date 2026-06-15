# Projekt: Ticket-System Backend

In diesem Projekt entwickelst du das Backend eines kleinen Ticket-Systems.
Das System soll noch kein Frontend benötigen. Es soll aber so aufgebaut sein,
dass später eine Oberfläche wie Streamlit angeschlossen werden kann.

## Grundidee

Ein Ticket-System wird in vielen Unternehmen genutzt, um Aufgaben, Fehler,
Support-Anfragen oder Verbesserungsvorschläge zu verwalten.

Ein Ticket hat zum Beispiel:

- Titel
- Beschreibung
- Typ
- Status
- Priorität
- Ersteller
- zuständige Person
- Kommentare
- Zeitpunkte für Erstellung und Änderungen

Das Projekt ist real-world-orientiert: Es geht um saubere Geschäftslogik,
gültige Statuswechsel, Persistenz und eine Struktur, die später von einer CLI
oder einem Frontend benutzt werden kann.

## Wichtiges Architekturziel

Die Fachlogik soll unabhängig von der Oberfläche sein.

Das bedeutet:

- Die Klassen sollen nicht direkt von `input()` abhängen.
- Die Klassen sollen nicht direkt von Streamlit abhängen.
- Die Kernlogik soll aus normalen Python-Objekten und Methoden bestehen.
- Eine CLI oder ein Frontend soll später nur Methoden aufrufen.

!!! note "Backend-first"
    Baue zuerst ein funktionierendes Backend. Wenn das Backend sauber ist,
    kann später relativ leicht eine Oberfläche darauf gesetzt werden.

## Mögliche Projektstruktur

```text
ticket_system/
├── main.py          # Demo-Ablauf oder CLI-Einstieg
├── models.py        # Ticket, User, Comment usw.
├── service.py       # TicketSystem: Geschäftslogik
├── storage.py       # Speichern und Laden
├── exceptions.py    # eigene Exceptions
└── data/
    └── tickets.json
```

Diese Struktur ist ein Vorschlag. Wichtig ist die Trennung:

| Datei | Verantwortung |
|-------|---------------|
| `models.py` | Datenmodelle und Verhalten einzelner Objekte |
| `service.py` | Abläufe: Ticket erstellen, Status ändern, suchen |
| `storage.py` | JSON-Dateien lesen und schreiben |
| `exceptions.py` | eigene Fehlerklassen |
| `main.py` | Beispielablauf oder CLI |

## Pflichtanforderungen

| Konzept | Mindestanforderung |
|---------|--------------------|
| Klassen | mindestens 7 eigene Klassen |
| Konstruktoren | Attribute über `__init__` initialisieren |
| Vererbung | mindestens eine sinnvolle Vererbungshierarchie |
| Overriding | mindestens eine Methode in einer Unterklasse überschreiben |
| Polymorphismus | mehrere Objekte über dieselbe Methode benutzen |
| Komposition | Tickets enthalten Kommentare oder Statusänderungen |
| Klassenattribute | mindestens ein sinnvolles Klassenattribut |
| Kapselung | mindestens ein `_attribut` oder `__attribut` begründet einsetzen |
| Magic Methods | mindestens `__str__`, zusätzlich `__len__` oder `__lt__` |
| Introspection | Debug-Ausgabe mit `__dict__`, `__name__`, `__bases__` |
| Exceptions | mindestens zwei eigene Exception-Klassen |
| Datei-I/O | Tickets als JSON speichern und laden |

## Fachliche Mindestfunktionen

Dein Backend soll mindestens diese Funktionen unterstützen:

1. Ticket erstellen
2. Ticket anzeigen
3. Kommentar hinzufügen
4. Status ändern
5. Tickets nach Status filtern
6. Tickets nach Priorität sortieren
7. Tickets speichern
8. Tickets laden
9. einfachen Report erzeugen

## Mögliche Klassen

Diese Liste ist bewusst kein fertiges Klassendiagramm. Entscheide selbst, was
du brauchst.

| Rolle im System | Mögliche Klassen |
|-----------------|------------------|
| Ticketarten | `Ticket`, `BugTicket`, `FeatureRequest`, `SupportRequest` |
| Personen | `User`, `Customer`, `SupportAgent`, `Admin` |
| Zusatzdaten | `Comment`, `StatusChange`, `Attachment` |
| Verwaltung | `TicketSystem`, `TicketRepository`, `JsonStorage` |
| Fehler | `TicketNotFoundError`, `InvalidStatusChangeError` |

## Polymorphismus im Ticket-System

Eine gute polymorphe Methode wäre zum Beispiel:

| Methode | Idee |
|---------|------|
| `calculate_priority()` | verschiedene Ticketarten berechnen Priorität anders |
| `render_summary()` | verschiedene Ticketarten stellen sich anders dar |
| `can_handle(ticket)` | verschiedene Rollen dürfen andere Tickets bearbeiten |
| `to_dict()` | verschiedene Objekte können gespeichert werden |

Beispielidee:

```python
tickets = [
    BugTicket("Login kaputt", "User kann sich nicht einloggen"),
    FeatureRequest("Dark Mode", "Oberfläche soll dunkles Theme bekommen"),
]

for ticket in tickets:
    print(ticket.calculate_priority())
```

## Statuslogik

Definiere klare Statuswerte, zum Beispiel:

```text
open -> in_progress -> resolved -> closed
```

Nicht jeder Wechsel soll erlaubt sein. Ein geschlossenes Ticket darf zum
Beispiel nicht einfach wieder auf `in_progress` gesetzt werden, außer du
implementierst bewusst eine `reopen()`-Methode.

Bei ungültigen Statuswechseln soll eine eigene Exception geworfen werden.

## JSON-Persistenz

Damit später eine CLI oder ein Frontend dieselben Daten nutzen kann, sollen
Tickets gespeichert werden.

Ein Ticket könnte als Dictionary so aussehen:

```python
{
    "id": "T-1001",
    "title": "Login kaputt",
    "description": "User kann sich nicht einloggen",
    "type": "bug",
    "status": "open",
    "comments": [
        {
            "author": "Ada",
            "text": "Tritt seit heute Morgen auf."
        }
    ]
}
```

Nutze dafür das Modul `json`.

## Frontendfähigkeit

Das Backend soll später leicht von Streamlit genutzt werden können.

Dafür ist wichtig:

- Methoden geben Werte zurück, statt nur zu printen.
- Daten können als Listen, Dictionaries oder Objekte abgefragt werden.
- Die Geschäftslogik liegt nicht in der Oberfläche.
- Speichern und Laden ist in einer eigenen Klasse oder Funktion gekapselt.

Beispiel:

```python
system = TicketSystem()
ticket = system.create_ticket("Login kaputt", "User kann sich nicht einloggen", ticket_type="bug")
system.add_comment(ticket.id, "Ada", "Ich prüfe das.")
system.change_status(ticket.id, "in_progress")
```

So eine Schnittstelle kann später sowohl von einer CLI als auch von Streamlit
verwendet werden.

## Optionaler Ausblick: Streamlit

Wenn das Backend funktioniert, kann später eine kleine Streamlit-Oberfläche
daraufgesetzt werden:

- Tickets als Tabelle anzeigen
- Formular für neues Ticket
- Selectbox für Status
- Textfeld für Kommentar
- Kennzahlen anzeigen: offene Tickets, kritische Tickets, gelöste Tickets

Streamlit ist **kein Pflichtteil** dieser Aufgabe. Das Backend soll aber so
geschrieben sein, dass dieser Bonus möglich bleibt.

## Arbeitsphasen

### Phase 1: Modell planen

Erstelle eine kurze Skizze:

- Welche Klassen brauchst du?
- Welche Attribute hat ein Ticket?
- Welche Ticketarten gibt es?
- Welche Statuswechsel sind erlaubt?
- Welche Methoden sollen Werte zurückgeben?

### Phase 2: Kernmodell implementieren

Implementiere zuerst ohne Menü:

- Ticket-Klassen
- User-Klassen oder einfache User-Objekte
- Kommentare
- TicketSystem als Verwaltungslogik
- Demo-Ablauf mit festen Beispielobjekten

### Phase 3: Regeln und Fehler

Ergänze:

- eigene Exceptions
- Statusprüfung
- Sortierung nach Priorität
- Reports

### Phase 4: Persistenz

Ergänze:

- `to_dict()`
- `from_dict()`
- Speichern in JSON
- Laden aus JSON

### Phase 5: Dokumentation

Schreibe eine `README.md`:

- Projektidee
- Startanleitung
- Klassenüberblick
- Beispielablauf
- Speicherformat
- mögliche Streamlit-Erweiterung

{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/11_projekt_idee_modellieren.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/12_projekt_minimalversion.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/29_projekt_klassen_review.yaml") }}
{{ task(file="tasks/python_grundlagen/oop/vertiefung_teil2/30_projekt_persistenz_debug.yaml") }}
