# Schlüssel-Wert-Datenbanken:
[20 min]

Das Schlüssel-Wert-Datenbankmodell ist wie eine Sammlung von Dictionaries oder JSON-Einträgen aufgebaut. Jeder Eintrag hat einen eindeutigen Schlüssel, der einem bestimmten Wert zugeordnet ist. Dieses Modell eignet sich besonders für Anwendungsfälle wie Caching und einfache Datenzugriffe. Schlüssel-Wert-Datenbanken wie Redis, DynamoDB und Riak zeichnen sich durch ihre Geschwindigkeit und Skalierbarkeit aus, bieten jedoch nur begrenzte Abfragemöglichkeiten.


## Anwendungsfälle:

Schlüssel-Wert Datenbanken werden vor allem für Anwendungsfälle eingesetzt, bei denen die Daten schnell abgerufen werden müssen. Sie eignen sich besonders gut für die Speicherung von Daten, die **nicht in Beziehung** zueinander stehen. Beispiele für Anwendungsfälle sind:

**Caching:**
Schlüssel-Wert-Datenbanken sind ideal für das Zwischenspeichern häufig abgerufener Daten, um Antwortzeiten zu verbessern.

**Session Storage:**
In Webanwendungen können sie für die temporäre Speicherung von Sitzungsinformationen verwendet werden.

**Konfigurationsmanagement:**
Sie eignen sich gut für die Speicherung von Konfigurationsdaten, die schnell abgerufen werden müssen.

**Benutzerpräferenzen:**
Das Modell kann für die Verwaltung von Benutzereinstellungen oder Präferenzen genutzt werden.



Schlüssel-Wert-Datenbanken sind wegen ihrer Einfachheit und benutzerfreundlichkeit beliebt. Außerdem ermöglichen sie schnelle Lese- und Schreibzugriffe durch den direkten Zugriff über den Schlüssel. Die Abfragefähigkeiten sind jedoch begrenzt, da sie nur einfache Abfragen unterstützen. Zudem eignen sie sich weniger für die Datenmodellierung komplexer Strukturen mit vielen Beziehungen.


## Beispiele für Schlüssel-Wert-Datenbanken:

**Redis:**
[Redis](https://redis.io/) ist eine (open source) in-memory Datenbank mit verschiedenen Datentypen. Bei einer in-memory Datenbank werden die Daten im Hauptspeicher (RAM) des Computers gespeichert. Dies ermöglicht sehr schnelle Lese- und Schreibzugriffe. Weitere bekannte in-memory Datenbanken sind SAP HANA und Oracle TimesTen.

**DynamoDB:**
[Amazon DynamoDB](https://aws.amazon.com/de/pm/dynamodb/?trk=58f15612-f60c-490d-9d44-26c72f72475f&sc_channel=ps&ef_id=Cj0KCQiAtOmsBhCnARIsAGPa5yZ2Fe0j9OjxssBVbvPmKIu8RSaEO0I1iOPNl4pSJGO1EffS2jX68QwaAqK9EALw_wcB:G:s&s_kwcid=AL!4422!3!645186177823!e!!g!!dynamodb!19571721591!143945626974&gclid=Cj0KCQiAtOmsBhCnARIsAGPa5yZ2Fe0j9OjxssBVbvPmKIu8RSaEO0I1iOPNl4pSJGO1EffS2jX68QwaAqK9EALw_wcB) ist ein vollständig verwalteter NoSQL-Dienst von AWS mit automatischer Skalierung.

**Riak:**
[Riak](https://riak.com/index.html) ist eine verteilte Datenbank, die auf dem Schlüssel-Wert-Modell basiert und hohe Verfügbarkeit bietet. Verteilt bedeutet in diesem Fall, dass die datenbank über mehrere physische oder logische Standorte verteilt ist. Dies führt zu einer höheren Ausfallsicherheit zu einem besseren Lastenausgleich.