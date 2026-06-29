# Generatoren

🟠 PCAP | 🔄 Vertiefung von Comprehensions & Iteratoren

## Einführung

Generatoren sind eine besondere Art von Funktionen in Python, die Werte **nach Bedarf** erzeugen, statt sie alle auf einmal im Speicher zu halten. Sie sind damit ideal für große Datenmengen oder unendliche Sequenzen.

In der [Comprehension-Seite](../../comprehensions/list_comp/list_comp.md) haben wir bereits **Generator Expressions** kennengelernt — Ausdrücke in runden Klammern wie `(x**2 for x in range(10))`. Hier gehen wir einen Schritt weiter und lernen **Generator-Funktionen** mit dem Schlüsselwort `yield` kennen.

---

## Iteratoren & das Iterator-Protokoll

Bevor wir Generatoren verstehen, müssen wir das **Iterator-Protokoll** kennen. Ein Iterator ist ein Objekt, das zwei Methoden implementiert:

- `__iter__()` — gibt das Iterator-Objekt selbst zurück
- `__next__()` — gibt den nächsten Wert zurück oder löst `StopIteration` aus

```python
# Eine Liste ist iterierbar (iterable), aber kein Iterator
zahlen = [1, 2, 3]

# iter() erzeugt einen Iterator aus einem Iterable
iterator = iter(zahlen)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # StopIteration!
```

!!! info "Iterable vs. Iterator"
    Ein **Iterable** ist ein Objekt, das `__iter__()` implementiert (z.B. Liste, String, Dict).
    Ein **Iterator** ist ein Objekt, das zusätzlich `__next__()` implementiert.
    Jeder Iterator ist ein Iterable, aber nicht jedes Iterable ist ein Iterator.

### Eigener Iterator als Klasse

Man kann das Iterator-Protokoll auch selbst implementieren — das ist aber aufwendig:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        wert = self.current
        self.current -= 1
        return wert

for zahl in Countdown(5):
    print(zahl)  # 5, 4, 3, 2, 1
```

Generatoren machen genau das Gleiche — aber **viel einfacher**.

---

## Generator-Funktionen mit `yield`

Eine **Generator-Funktion** sieht aus wie eine normale Funktion, verwendet aber `yield` statt `return`:

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for zahl in countdown(5):
    print(zahl)  # 5, 4, 3, 2, 1
```

### Wie funktioniert `yield`?

Der entscheidende Unterschied zu `return`:

| | `return` | `yield` |
|---|---|---|
| Funktion endet | Ja, sofort | Nein, wird **pausiert** |
| Zustand | Geht verloren | Wird **gespeichert** |
| Rückgabetyp | Beliebiger Wert | Generator-Objekt |
| Mehrfach aufrufbar | Nein | Ja, bei jedem `next()` |

```python
def mein_generator():
    print("Vor dem ersten yield")
    yield 1
    print("Vor dem zweiten yield")
    yield 2
    print("Vor dem dritten yield")
    yield 3
    print("Generator ist fertig")

gen = mein_generator()
# Noch passiert nichts! Der Code wird erst bei next() ausgeführt.

print(next(gen))  # "Vor dem ersten yield" → 1
print(next(gen))  # "Vor dem zweiten yield" → 2
print(next(gen))  # "Vor dem dritten yield" → 3
# next(gen) → "Generator ist fertig" → StopIteration
```

!!! warning "Wichtig"
    Beim Aufruf einer Generator-Funktion wird der Code **nicht sofort** ausgeführt.
    Stattdessen wird ein **Generator-Objekt** zurückgegeben. Der Code läuft erst,
    wenn `next()` aufgerufen wird.

---

## `next()` und Iteration

### Manuelles Iterieren

```python
def zahlen():
    yield 10
    yield 20
    yield 30

gen = zahlen()

print(next(gen))  # 10
print(next(gen))  # 20
print(next(gen))  # 30
# print(next(gen))  # StopIteration!
```

### Iteration mit `for`-Schleife

Die `for`-Schleife ruft intern `next()` auf und fängt `StopIteration` automatisch ab:

```python
def zahlen():
    yield 10
    yield 20
    yield 30

for z in zahlen():
    print(z)  # 10, 20, 30
```

### Generator-Erschöpfung

Ein Generator kann nur **einmal** durchlaufen werden. Nach der Erschöpfung liefert er keine Werte mehr:

```python
gen = zahlen()

liste1 = list(gen)  # [10, 20, 30]
liste2 = list(gen)  # [] ← leer! Generator ist erschöpft

# Lösung: Neuen Generator erstellen
gen2 = zahlen()
liste3 = list(gen2)  # [10, 20, 30]
```

!!! warning "Häufige Prüfungsfalle"
    In der PCAP-Prüfung wird oft gefragt, was passiert, wenn man einen bereits
    erschöpften Generator erneut iteriert. Die Antwort: **Nichts** — er liefert
    keine Werte mehr.

---

## Speichereffizienz

Der Hauptvorteil von Generatoren ist die **Speichereffizienz**. Sie erzeugen Werte on-the-fly, statt alle auf einmal im Speicher zu halten.

```python
import sys

# Liste: Alle Werte im Speicher
liste = [x ** 2 for x in range(1_000_000)]
print(sys.getsizeof(liste))  # ~8 MB

# Generator: Nur ein Wert gleichzeitig im Speicher
gen = (x ** 2 for x in range(1_000_000))
print(sys.getsizeof(gen))  # ~200 Bytes (!)
```

### Wann Generatoren statt Listen?

| Situation | Liste | Generator |
|---|---|---|
| Alle Werte werden gleichzeitig benötigt | ✅ | ❌ |
| Nur einmal durchlaufen | ❌ | ✅ |
| Sehr große Datenmengen | ❌ (Speicher!) | ✅ |
| Unendliche Sequenzen | ❌ (unmöglich) | ✅ |
| Indexzugriff (`[i]`) nötig | ✅ | ❌ |
| Mehrfach iterieren | ✅ | ❌ |

---

## Generator Expressions vs. Generator-Funktionen

Wir kennen bereits **Generator Expressions** aus der Comprehension-Seite:

```python
# Generator Expression (eine Zeile)
quadrate = (x ** 2 for x in range(10))

# Generator-Funktion (mehrere Zeilen, komplexere Logik)
def quadrate_gen(n):
    for x in range(n):
        yield x ** 2
```

### Wann welche Form?

| Kriterium | Generator Expression | Generator-Funktion |
|---|---|---|
| Einfache Transformation | ✅ | Übertrieben |
| Komplexe Logik | ❌ | ✅ |
| Zustand zwischen Aufrufen | ❌ | ✅ |
| Unendliche Sequenzen | ❌ | ✅ |
| Mehrere `yield`-Punkte | ❌ | ✅ |

---

## Praxisbeispiele

### Unendliche Sequenz

```python
def natuerliche_zahlen(start=1):
    """Erzeugt unendlich viele natürliche Zahlen."""
    n = start
    while True:
        yield n
        n += 1

# Nur die ersten 5 nehmen
for i, zahl in enumerate(natuerliche_zahlen()):
    if i >= 5:
        break
    print(zahl)  # 1, 2, 3, 4, 5
```

### Pipeline-Pattern

Generatoren können wie eine Pipeline verkettet werden — jeder Generator verarbeitet die Ausgabe des vorherigen:

```python
def zahlen(n):
    """Erzeugt Zahlen von 1 bis n."""
    for i in range(1, n + 1):
        yield i

def quadriere(iterable):
    """Quadriert jeden Wert."""
    for x in iterable:
        yield x ** 2

def nur_gerade(iterable):
    """Filtert nur gerade Werte."""
    for x in iterable:
        if x % 2 == 0:
            yield x

# Pipeline: zahlen → quadriere → nur_gerade
ergebnis = nur_gerade(quadriere(zahlen(10)))

for wert in ergebnis:
    print(wert)  # 4, 16, 36, 64, 100
```

!!! tip "Vorteil der Pipeline"
    Jeder Wert fließt **einzeln** durch die gesamte Pipeline. Es wird nie eine
    komplette Zwischenliste im Speicher gehalten.

---

## Zusammenfassung

| Konzept | Beschreibung |
|---|---|
| `yield` | Pausiert die Funktion und gibt einen Wert zurück |
| Generator-Funktion | Funktion mit `yield` → erzeugt Generator-Objekt |
| Generator-Objekt | Iterator, der `__next__()` und `__iter__()` implementiert |
| `next(gen)` | Holt den nächsten Wert vom Generator |
| `StopIteration` | Wird ausgelöst, wenn der Generator erschöpft ist |
| Erschöpfung | Generator kann nur einmal durchlaufen werden |
| Speichereffizienz | Generatoren halten nur einen Wert gleichzeitig im Speicher |

---

## Aufgaben

{{ task(file="tasks/funktionen_fortgeschritten/generatoren/01_was_ist_die_ausgabe.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/02_countdown_generator.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/03_gerade_zahlen_generator.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/04_generator_erschoepfung.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/05_fibonacci_generator.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/06_datei_zeilenweise.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/07_generator_pipeline.yaml") }}
{{ task(file="tasks/funktionen_fortgeschritten/generatoren/08_eigener_range.yaml") }}
