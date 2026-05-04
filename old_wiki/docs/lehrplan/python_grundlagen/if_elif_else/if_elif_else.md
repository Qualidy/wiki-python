# Verzweigungen
Verzweigungen sind ein wesentlicher Bestandteil der Programmierung. Sie ermöglichen es, Entscheidungen auf Basis 
bestimmter Bedingungen zu treffen. 

In Python verwenden wir dafür `if`, `elif` (else if) und `else` zur Steuerung des Programmflusses:

## Grundstruktur
<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/GA8Oj97qUXM?si=Ne0kUbnFBrmg-w0a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

[//]: # ([20min])
Die grundlegende Struktur einer `if-else`-Verzweigung in Python sieht folgendermaßen aus:

```python
if bedingung:
    # Anweisungen, wenn Bedingung wahr ist
else:
    # Anweisungen, wenn Bedingung falsch ist
```

Die `bedingung` ist ein Ausdruck, der entweder wahr (`True`) oder falsch (`False`) ergibt. Die Anweisungen müssen eingerückt sein! Dies ist ein fundamentales Prinzip in Python, mit dem wir sehr schnell vertraut sein werden.

### Bedingungen

[//]: # ([50min])
In Python werden Bedingungen in `if`-Abfragen verwendet, um zu bestimmen, ob bestimmte Anweisungen ausgeführt werden 
sollen oder nicht. Diese Bedingungen können auf unterschiedliche Weise formuliert werden, um die Logik des Programms 
zu steuern. 

Eine grundlegende Bedingung in einer `if`-Abfrage könnte so einfach sein wie der Vergleich zweier Werte. Zum Beispiel 
überprüft `if alter >= 18:` ob das Alter einer Person 18 Jahre oder älter ist. Hierbei wird ein Gleichheits- oder 
Ungleichheitsoperator verwendet, um zu entscheiden, ob der Code innerhalb des `if`-Blocks ausgeführt wird.

Komplexere Bedingungen können durch die Verwendung logischer Operatoren wie `and`, `or` und `not` erstellt werden. 
Eine solche Bedingung könnte lauten `if alter >= 18 and student == True:`, was bedeutet, dass der Code nur ausgeführt 
wird, wenn die Person 18 Jahre oder älter ist und gleichzeitig ein Student ist.

Python ermöglicht auch die Überprüfung von Mitgliedschaften mit dem `in`-Operator in Bedingungen. Ein Beispiel wäre 
`if frucht in ['Apfel', 'Banane', 'Kirsche']:`. Diese Bedingung prüft, ob der Wert der Variablen `frucht` in der 
angegebenen Liste enthalten ist. Dies ist eine sehr mächtige Bedingung, die man häufig praktisch verwenden kann 
und ein gutes Beispiel für 'pythonic' Code sind.

Bedingungen können auch komplexere Ausdrücke beinhalten, wie z.B. Funktionsaufrufe oder kombinierte Vergleiche. Zum 
Beispiel kann `if ist_regnerisch() and temperatur < 20:` eine Bedingung sein, die wahr ist, wenn die Funktion 
`ist_regnerisch()` `True` zurückgibt und die Temperatur unter 20 Grad liegt.

Insgesamt erlauben Bedingungen in `if`-Abfragen in Python, sehr flexible und leistungsfähige Kontrollstrukturen in 
Programmen zu erstellen, von einfachen Vergleichen bis hin zu komplexen logischen Ausdrücken.

Die Bausteine dafür sehen wir hier:

- Vergleichsoperatoren: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logische Operatoren: `and`, `or`, `not`
- Überprüfung auf Null/None: `is None`, `is not None`

**Beispiel**:
```python
alter = 18
if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")
```

##  if-elif-else-Abfragen

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/r-OHMDZNyzQ?si=2lp4Dxp_TS4immP2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

[//]: # ([30min])
Oft benötigen wir mehr als zwei Zweige, zum Beispiel wenn wir für verschiedene Altersklassen andere Aktionen ausführen 
müssen oder wollen.

`elif` erlaubt es, mehrere Bedingungen nacheinander zu überprüfen.

**Grundstruktur**
```python
if bedingung1:
    # Anweisungen, wenn bedingung1 wahr ist
elif bedingung2:
    # Anweisungen, wenn bedingung2 wahr ist
else:
    # Anweisungen, wenn keine Bedingung wahr ist
```

Es können beliebig viele Zweige entstehen. Hat der Code sehr viele Zweige, sollte man sich jedoch fragen, ob man das 
nicht anders lösen kann. Je mehr Einrückungsebenen es gibt, desto schwieriger wird es für andere den Code zu lesen.

**Beispiel**
```python
zahl = 15
if zahl > 10:
    print("Die Zahl ist größer als 10.")
elif zahl == 10:
    print("Die Zahl ist genau 10.")
else:
    print("Die Zahl ist kleiner als 10.")
```

Die Verwendung von `if`, `elif` und `else` in Python ermöglicht es, basierend auf Bedingungen unterschiedliche Wege im 
Programm einzuschlagen. Das findet man eigentlich in jedem Programm, da die Unterscheidung von Aktionen basierend auf
einer oder mehrere Bedingungen ein zentraler Bestandteil der Softwareentwicklung ist.


# Aufgaben

[//]: # ([70min])
### 1. **Einfache if-Abfrage**: 🌶️️
Schreibe ein Programm, das überprüft, ob eine Variable `x` größer als 10 ist. Gib eine 
entsprechende Nachricht aus.
### 2. **if-else**: 🌶️️
Überprüfe, ob eine Variable `zahl` gerade ist. Verwende dazu den Modulo-Operator `%`.
### 3. **Negativ oder Positiv**: 🌶️️
Schreibe ein Programm, das überprüft, ob eine Zahl positiv, negativ oder 0 ist.
### 4. **Größer oder kleiner**: 🌶️️
Überprüfe, ob eine Variable `a` größer, kleiner oder gleich einer anderen Variable `b` ist.
### 5. **Alter überprüfen**: 🌶️️🌶️️
Schreibe ein Programm, das überprüft, ob eine Person anhand ihres Alters volljährig ist.
### 6. **Passwortüberprüfung**: 🌶️️🌶️️
Erstelle ein Programm, das überprüft, ob ein eingegebenes Passwort mit einem gespeicherten 
Passwort übereinstimmt.
### 7. **Maximalwert**: 🌶️️🌶️️
Schreibe ein Programm, das den größeren Wert von zwei Zahlen ausgibt.
### 8. **Bewertung**: 🌶️️🌶️️
Überprüfe anhand einer Variable `note`, ob die Note "sehr gut", "gut", "befriedigend", "ausreichend" 
oder "nicht ausreichend" ist.
### 9. **Temperaturen**: 🌶️️🌶️️
Schreibe ein Programm, das unterschiedliche Meldungen für verschiedene Temperaturbereiche ausgibt 
(z.B. kalt, warm, heiß).
### 10. **Einfache Rechnung**: 🌶️️🌶️️
Schreibe ein Programm, das eine einfache mathematische Operation (Addition, Subtraktion, 
Multiplikation, Division) basierend auf Benutzereingaben ausführt.

### 11. **Jahreszeiten**: 🌶️️🌶️️
Schreibe ein Programm, das den Namen einer Jahreszeit ausgibt, basierend auf einer Monatsnummer (1 bis 12).
### 12. **Teilbarkeit**: 🌶️️
Überprüfe, ob eine Zahl durch eine andere Zahl ohne Rest teilbar ist.
### 13. **Einkaufsliste**: 🌶️️🌶️️
Schreibe ein Programm, das überprüft, ob ein Artikel in einer Einkaufsliste vorhanden ist.
### 14. **Größte von drei Zahlen**: 🌶️️
Bestimme die größte Zahl aus drei gegebenen Zahlen.
### 15. **Rabattaktion**: 🌶️️🌶️️
Schreibe ein Programm, das basierend auf dem Einkaufswert unterschiedliche Rabatte berechnet.
### 16. **Lichtschalter**: 🌶️️🌶️️
Simuliere einen Lichtschalter, der das Licht ein- und ausschaltet basierend auf der aktuellen 
Zustandsvariable.
### 17. **Fahrzeugklasse**: 🌶️️🌶️️
Schreibe ein Programm, das basierend auf dem Gewicht eines Fahrzeugs eine Kategorie
(Leicht, Mittel, Schwer) zuweist.
### 18. **Kinotag**: 🌶️️🌶️️
Erstelle ein Programm, das unterschiedliche Eintrittspreise basierend auf dem Wochentag berechnet.
### 19. **Schaltjahr**: 🌶️️🌶️️🌶️️
Schreibe ein Programm, das überprüft, ob ein gegebenes Jahr ein Schaltjahr ist oder nicht.

# Anspruchsvolle Aufgaben

[//]: # ([30min])
### **Benutzereingaben filtern und sortieren** 🌶️️🌶️️🌶️️

Aufgabenstellung:

- Fordere den Benutzer auf, mehrere Einträge mit Kundeninformationen einzugeben (Format: "Name, Alter, Email"). Beende 
die Eingabe bei Eingabe von "fertig".
- Filtere die Daten, um nur Kunden über 30 Jahre in die Ausgabe einzuschließen.
- Gib die gefilterten Daten auf der Konsole aus, sortiert nach dem Alter in absteigender Reihenfolge.


[Lösungen](solutions.md)


### **Entwickle ein textbasiertes Rollenspiel** 🌶️️🌶️️🌶️🌶️🌶️️

Aufgabenstellung:

- Du steuerst mit deiner Eingabe (input) einen Helden, der in einem Labyrinth gefangen ist.
- Du beschreibst mit Texten was passiert.
- Jede Runde kannst du eine Entscheidung treffenn zb vorwärst gehen... durch eine Tür gehen etc.
- Du bestitzt 20 Trefferpunkte
- Gelegentlich triffst du auf Feinde und musst Kämpfen.
- Die Feinde besitzen ebenfalls Trefferpunkte und du kannst Attacken ausführen.
- Eien Attacke ist erfolgreich, wenn du eine Quiz-Frage richtig beantwortest.
- Erstelle dazu ein Dictionary für deine Quiz-Fragen und benutze idealerweise Fragen um die Themen aus diesem Kurs (also Python und Mathematik)
- Überlege dir ein tolles End-Game mit einem Endboss.
- Solltest du auf 0 Trefferpunkte fallen, hast du das Spiel verloren.
- Tauscht später eure Fragen und Antworten aus und erstellt ein gemeinsames großes Deictionary, um euch mit dem Spiel auf die Prüfung vorzubereiten.
