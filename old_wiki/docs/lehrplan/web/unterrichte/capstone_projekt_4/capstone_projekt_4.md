# Capstone Projekt: Interaktive Website für Testfahrten mit einem VW-Fahrzeug

[180 min]

Das Ziel dieses Projektes ist es, die zuvor erstellte HTML + CSS Website mit interaktivität zu versehen. Die Nutzer sollen einen vollen Kalender sehen, die dynamisch mit neuen Testfahrten befüllt wird. Anstelle einer echten Flask API sollen gebuchte Fahrten im Local Storage des Browsers gespeichert werden.
Außerdem soll bei Klick auf die einzelnen Tage angezeigt werden, wer die jeweilige Fahrt gebucht hat.

![Projekt](../../images/js_kalender_testfahrt.png)

## Anforderungen**

- Überlege eine passende Struktur um die Form-Daten im Local Storage zu speichern
- Nutzer Event-Listener um den Namen der Testfahrt bei Klick auf eine existierende Buchung anzuzeigen 
- Nutze die [FullCalendar](https://fullcalendar.io/docs) Javascript Library um eine interaktive Ansicht einzubauen.
- Implementiere eine Funktion, die den Kalender automatisch aktualisiert, wenn neue Buchungen hinzugeefügt werden.
- Stell sicher, dass die Nutzer gültige und vollständige Informationen eingeben, bevor sie ihre Buchung abschicken.

### Bonus

- **Design Upgrade**: Mache deine Website visuell noch schöner indem du mit einer richtigen Website-Struktur arbeitest. (Header, Farben, Logo)
- **Erweiterte Interaktivität**: Füge Funktionen wie die Möglichkeit hinzu, Buchungen zu bearbeiten oder zu löschen, direkt im Kalender.
- **Benutzer-Authentifizierung**: Implementiere eine Art von Benutzerverwaltung, damit Nutzer sich anmelden und nur ihre eigenen Buchungen verwalten können.
- **Flask API** Erstelle eine simple Flask API mit SQL Datenbank um die Testfahrten zu kommunizieren und persitieren.

## Ressourcen

- [FullCalendar-Dokumentation](https://fullcalendar.io/docs)
- [JavaScript-Formularvalidierung](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

[Lösung](./solutions.md) (keine `app.py` mit Flask nötig, Datenverarbeitung erfolgt clientseitig)

[Lösung.html](./solution.html)