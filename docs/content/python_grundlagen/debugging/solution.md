# Lösungen

### Aufgabe: Von diesen sieben Tricks sollt ihr nichts wissen🌶

**Gründe für Fehler:**

* Eigener Code
* Fremder Code im eigenen Projekt
* Fehler in der genutzten Bibliothek
* Compiler hat einen Fehler
* Hardware hat einen Fehler

**7 Tips:**

* (Fremd-)Code und Fehlermeldungen lesen
* Nach Fehlermeldung in Internet suchen
* Logger nutzen
* Debugger nutzen
* Fehler repruduzieren
* Tests schreiben
* Statsiche Codechecker verwenden

### Aufgabe: Debugger bei verschachtelten if-Bedingunen 🌶🌶

{{ youtube_video("https://www.youtube.com/embed/-HcRBSCWV-I?si=FFRzMtc-c7l3hZjZ") }}

Bei der Belegungen `a = 25` und `b = 10` werden die Zeilen
4, 11, 12, 15 und 16 durchlaufen.

Um alle Fälle mindestens einmal durchzugehen, kann zum Beispiel gewählt werden:

* `a = 15` und `b = 10`: Zeilen 4, 11, 12, 13, 16
* `a = 10` und `b = 15`: Zeilen 4, 5, 6, 9, 16
* `a = 100` und `b = 150`: Zeilen 4, 5, 6, 7, 16
