# NumPy Aufgabe: Taxi-Operator in Manhatten

Auf einem quadratischen Staßennetz (50kmx50km) fahren 15 leere Taxis an zufälligen Punkten auf diesem Straßennetz. Jeder Block ist ein 1x1 Kilometer groß.

Eine Kundin ruft an und gibt ihren Standort an bei (31, 15.7).
Du musst das Taxi wählen, das die Kundin abholen soll. 

Findet das Taxi, welches am nächsten zu der Kundin ist, damit ihr es zu ihr navigieren könnt. Denkt daran, dass die Distanz die tatsächliche Fahrtstrecke sein soll und nicht die Luftlinie. Benutzt  Broadcasting bei der Distanzberechnung zu allen Taxis! Keine Schleifen - pure numpy :)

Erstellt zunächst die zufälligen Taxipositionen und denkt an folgenden Hinweis.
    
**Hinweis:** Taxis fahren auf Straßen entweder horizontal oder vertikal, dementsprechend ist immer eine Koordinate ganzzahlig während die andere ein float ist!

**Erweiterung 🌶️🌶️🌶️:**

Du hast jetzt genau 15 Kund:innen und möchtest jeder Person ein Taxi so zuordnen, dass die Gesamtstrecke zu den Kunden minimiert wird.

- Überlege dir wie du es grundsätzlich umsetzen müsstest.

- Finde ein Beispiel, wo die optimale Zuordnung nicht trivial ist. 

- Finde den passenden Matching-Algorithmus aus dem Matheskript. Implementiere den Algo selbst oder finde eine existierende Implementation (Tipp: scipy). Was sind die Kantengewichte?

[Lösungen](numpy_manhatten_aufgabe_loesung.md)