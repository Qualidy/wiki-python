# Capstone Projekt: CRUD Garagen Management API

[180 min]

Erstelle eine FLASK RESTful API mit CRUD Funktion für das Management von Stellplätzen in einer Garage.
Hierbei sollen Fahrzeuge mit ihrem Kennzeichen eingebucht und einem Stellplatz zugewiesen werden.
Beim Abholen des Fahrzeuges wird das Datum ebenfalls persistiert.
Zusätzlich soll es auch möglich sein, Fahrzeuge neue Stellplätze zuzuweisen.

![Projekt](../../images/postman_crud_collection.png)

## Anforderungen

- Flask API mit CRUD Funktionalität
  - Anzeigen aller Fahrzeuge in der Garage
  - Anzeigen des Stellplatzes eines einzelnen Fahrzeugs basierend auf dem Kennzeichen
  - Einbuchen eines neuen Fahrzeugs (und zuweisen des Parkplatzes)
  - Updaten einzelner Fahrzeuge um den Stellplatz zu ändern
  - Updaten einzelner Fahrzeuge bei Abholung
  - Löschen einzelner Fahrzeuge per ID
- Plane die API zuerst mit Stift und Papier
- Definiere dann die Integration Tests mit Postman als Collection für einen Test Driven Development Anstatz
- Nutze SQLALCHEMY als Toolkit

### Bonus

- **Automatische Parkplatzzuweisung** - Ändere die Parkplatzzuweisung von Nutzerangabe auf automatisch. Neue Fahrzeuge sollen automatisch auf leere Parkplatze zugewisen werden.
- **Größenbasiertes Parken** - Füge weitere Informationen zu Fahrzeugen und Stellplätzen hinzu. (Kleines Auto - kleiner Parkplatz)
- **Kostenberechnung** - Bei Abholung des Fahrzeuges soll die Zeitdifferenz mit einem Kostenfaktor berechnet und mit ausgegeben werden.

## Ressourcen

- [SQLAlchemy Dokumentation](https://docs.sqlalchemy.org/en/20/)
- [Postman Testing Docu](https://learning.postman.com/docs/writing-scripts/test-scripts/)

[Lösung](./solutions.md)