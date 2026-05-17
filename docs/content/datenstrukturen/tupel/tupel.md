# Tupel in Python

[//]: # ([15min])

{{ youtube_video("https://www.youtube.com/embed/Si2Rc2VeCDg?si=PhWoEfpzEclNC0Xx") }}

In Python ist ein Tupel eine grundlegende Datenstruktur, die einer Liste ähnlich ist, aber einen entscheidenden
Unterschied aufweist: Sie ist **unveränderlich**. 

Das bedeutet, dass die vom Tupel referenzierten Objekte nicht mehr geändert werden können.
Dies ist nützlich, um die Integrität der Daten im gesamten Programm zu gewährleisten.

Tupel werden definiert, indem Elemente in Klammern `( )` eingeschlossen werden, wobei die Elemente durch Kommas getrennt
sind.

[//]: # ([10min])
Ein einfaches Beispiel für ein Tupel zum Beispiel die Definition von Koordinaten als ein Paar von zwei Fließkommazahlen:

```python
treasure_coordinates = (50.8215, -0.1372)
```

Das Tupel `treasure_coordinates` enthält zwei Fließkommazahlen und stellt einen festen Punkt auf einer Fläche dar.
Da dieser Punkt unveränderlich sein soll, entscheidet sich der Entwickler dazu, es als Tupel und nicht als Liste 
zu speichern.

## Eigenschaften von Tupeln

[//]: # ([30min])
**Immutability:**
Einmal erstellt, können wir keine Elemente zu einem Tupel hinzufügen, entfernen oder neu referenziert werden. 

**Indizierung und Slicing:**
Ähnlich wie Listen unterstützen Tupel die Indizierung und das Slicing. Die nutzung ähnelt daher sehr der von Listen.

**Iterierbarkeit:** Tupel können in Schleifen zur Iteration verwendet werden, genau wie Listen.

**Gemischte Datentypen:**
Tupel können eine Mischung aus verschiedenen Datentypen enthalten: `('Hallo', 42, 3.14)` ist ein gültiges Tupel.

## Vorteile der Verwendung von Tupeln

**Effizienz:** Tupel können hinsichtlich Speicherplatz und Leistung effizienter sein als Listen, besonders bei großen
Datensätzen.

**Sicherheit:** Da sie unveränderlich sind, können Tupel verwendet werden, um sicherzustellen, dass Daten im gesamten
Programm unverändert bleiben.

**Funktionalität:** Tupel können als Schlüssel in Dictionaries als Schlüssel verwendet werden, Listen hingegen nicht.

Hier sehen wir einige Code-Beispiele, die verschiedene Aspekte von Tupeln in Python veranschaulichen:

## Arbeiten mit Tupels

[//]: # ([60min])
### Erstellung und Zugriff auf Elemente:

{{ youtube_video("https://www.youtube.com/embed/H9D9uD16QPk?si=9U1zMCWWd2bPoEFf") }}

```python
# Ein Tupel erstellen
fruechte = ("Apfel", "Banane", "Kirsche")

# Auf Elemente zugreifen
print(fruechte[0])  # Gibt 'Apfel' aus
print(fruechte[-1])  # Gibt 'Kirsche' aus (letztes Element)
```

Mit sogenannten Slices kann man auch direkt auf mehrere Elemente zugreifen:

```python
print(fruechte[0:2]) # gibt ('Apfel', 'Banane') aus
```

Dies ist exakt identische zum [Slicing bei Listen](../lists/lists.md#slicing) und Strings.

Um ein Einelementige Tupel zu erstellen, gibt es die folgende Syntax:

```python
singleton = (9000,)
```

Das `,` nach der `9000` ist nötig, da bei der Notation `(9000)` nicht klar wäre,
ob es sich um die Erstellung eines Tupels handeln würde, oder um die priorisierenden Klammern in einer 
mathematischen Rechnung.

### Unveränderlichkeit von Tupeln
{{ youtube_video("https://www.youtube.com/embed/LpxtHaf41Yk?si=TiG5RpPwMryrQ66L") }}

Versuch, ein Element zu auzutauschen (führt zu einem Fehler):

```python
fruechte[0] = "Erdbeere"  # Dies verursacht einen TypeError
```

Unveränderlichkeit eines Tupels bedeutet, dass die Einträge eines Tupels nicht auf andere Objekte geändert werden können.
Jedoch ist es durchaus möglich, die interne Struktur eines Elementes zu ändern, auf das ein Tupel verweist.
Klicke im folgenden Beispiel auf "Next >", und achte dabei darauf, wie die Werte der Listen verändert werden.

[💻Link zum Online Compiler](https://pythontutor.com/render.html#code=first_list%20%3D%20%5B'a',%20'b',%20'c'%5D%0Asecond_list%20%3D%20%5B1,2,3,4,5%5D%0A%0Amy_tuple%20%3D%20%28first_list,%20second_list%29%0A%0A%23%20Ver%C3%A4ndere%20Liste,%20NICHT%20das%20Tupel%3A%0Afirst_list%5B0%5D%20%3D%20'tada'%20%0Amy_tuple%5B1%5D%5B-1%5D%20%3D%201000&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
first_list = ['a', 'b', 'c']
second_list = [1,2,3,4,5]

my_tuple = (first_list, second_list)

# Verändere Liste, NICHT das Tupel:
first_list[0] = 'tada' 
my_tuple[1][-1] = 1000
```

### Tupel-Operationen

{{ youtube_video("https://www.youtube.com/embed/QIPpHCfMjwo?si=m41D25i7OucNyLYY") }}

Zur Verkettung und Wiederholung wird die selbe Syntax wie bei Listen verwendet:

```python
# Tupel Verkettung
tupel1 = (1, 2, 3)
tupel2 = (4, 5, 6)
verkettetes_tupel = tupel1 + tupel2
print(verkettetes_tupel)  # Gibt (1, 2, 3, 4, 5, 6) aus

# Tupel wiederholen
wiederholtes_tupel = tupel1 * 2
print(wiederholtes_tupel)  # Gibt (1, 2, 3, 1, 2, 3) aus
```

### Tupel mit gemischten Datentypen

Die Einträge in Tupeln können von verschiedenen Typen sein. Der Fachbegriff für diese Eigenschaft ist übrigens
**Polymorphismus**.

```python
gemischtes_tupel = ("Max", 28, 1.75, True)
print(gemischtes_tupel)
```

### Tupel-Packen und -Entpacken

{{ youtube_video("https://www.youtube.com/embed/BE861o0r5yc?si=krZx0AiApreRet_J") }}

Im folgenden Beispiel wird jedes Element eines Tupels in eine Variable gespeichert. 
Das nennt sich *entpacken*. Dabei müssen genau die richtige Anzahl an Variablen vorgegeben werden.
Nämlich so viele, wie das Tupel lang ist.

```python
# Jedes Element in eine Variable speichern
name, alter, groesse = ("Lisa", 30, 1.68)
```

Es ist möglich, über den Asterisk-Operator `*` Tupel zu entpacken. Hiermit kann angezeigt werden, dass in der 
Variablen nach dem `*` alle übrigen Variablen gespeichert werden sollen.

```python
# Tupel entpacken
first, *rest = (1, 4, 9, 16, 25)

print(first) # 1
print(rest) # (4, 9, 16, 25)
```

### Verwendung von Tupeln als Schlüssel in einem Dictionary
{{ youtube_video("https://www.youtube.com/embed/ppSZtdwbIz8?si=XELGK8RvY9pDo6JI") }}

Tupel, deren Einträge unveränderlich sind, lassen sich als Schlüssel in Dictionaries verwenden.

```python
# Koordinaten als Schlüssel für Orte
orte = {(52.5200, 13.4050): "Berlin", (48.8566, 2.3522): "Paris"}
print(orte[(52.5200, 13.4050)])  # Gibt 'Berlin' aus
```

## Häufige Funktionen und Methoden für Tupel in Python

{{ youtube_video("https://www.youtube.com/embed/fUT0hwVX0gw?si=JgjWKzozhR4mLXS5") }}

[//]: # ([30min])
Hier ist eine Tabelle, die einige der häufigsten Funktionen und Methoden für Tupel in Python
zusammenfasst. Für jede Funktion/Methode gibt es eine kurze Beschreibung und ein kleines Beispiel.

| Funktionsname   | Kurzbeschreibung                                       | Beispiel                              |
|-----------------|--------------------------------------------------------|---------------------------------------|
| `len(tupel)`    | Gibt die Anzahl der Elemente im Tupel zurück.          | `len((1, 2, 3)) # Ergebnis: 3`        |
| `max(tupel)`    | Gibt das größte Element im Tupel zurück.               | `max((1, 4, 2)) # Ergebnis: 4`        |
| `min(tupel)`    | Gibt das kleinste Element im Tupel zurück.             | `min((1, 4, 2)) # Ergebnis: 1`        |
| `sum(tupel)`    | Berechnet die Summe der Elemente im Tupel.             | `sum((1, 2, 3)) # Ergebnis: 6`        |
| `tupel.index()` | Sucht nach einem Element und gibt dessen Index zurück. | `(1, 2, 3).index(2) # Ergebnis: 1`    |
| `tupel.count()` | Zählt, wie oft ein Element im Tupel vorkommt.          | `(1, 2, 2, 3).count(2) # Ergebnis: 2` |

### Anmerkungen:

- `len()`, `max()`, `min()`, und `sum()` sind eingebaute Python-Funktionen, die auf Tupel anwendbar sind.
- `tupel.index()` und `tupel.count()` sind Methoden, die spezifisch für Tupel-Objekte sind. Hierbei ist `tupel` ein
  Platzhalter für das jeweilige Tupel-Objekt.

# Aufgaben

[//]: # ([60min])

{{ task(file="tasks/python_grundlagen/tupel/tupel/01_tupel_erstellen.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/02_auf_tupelelemente_zugreifen.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/03_tupelelemente_andern.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/04_ist_das_element_im_tupel.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/05_zahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/06_umgekehrte_reihenfolge.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/07_tupel_vom_tupel.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/08_tupel_kombinieren.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/09_multiplikation.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/10_tupel_verschachteln.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/11_index_zum_element_finden.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/12_summe_der_tupelelemente.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/13_sortieren.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/14_subtupel.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/15_reingelegt.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/16_entpacken.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/17_entpacken_bei_listen.yaml") }}
{{ task(file="tasks/python_grundlagen/tupel/tupel/18_alles_entpackbar.yaml") }}
