# Protected & Private

In Java kennen wir die Zugriffsmodifikatoren `private`, `protected` und `public`.
Python verfolgt hier eine andere Philosophie: **Es gibt keinen echten Zugriffsschutz.**
Stattdessen setzt Python auf Konventionen und einen Mechanismus namens _Name Mangling_.

## Public (kein Unterstrich)

Standardmäßig sind alle Attribute und Methoden in Python **public**.
Jeder kann von außen darauf zugreifen:

```python
class Auto:
    def __init__(self, marke):
        self.marke = marke

a = Auto("VW")
print(a.marke)  # VW
```

## Protected (`_attribut`) - Konvention

Ein einzelner Unterstrich vor dem Namen signalisiert:
**"Dieses Attribut ist für den internen Gebrauch gedacht."**

Es ist eine reine Konvention - technisch gibt es keinen Schutz.
Python-Entwickler respektieren diesen Hinweis und greifen von
außen nicht auf solche Attribute zu.

[Link zum Onlinecompiler](https://pythontutor.com/render.html#code=class%20Auto%3A%0A%20%20%20%20def%20__init__%28self%2C%20marke%2C%20kilometerstand%29%3A%0A%20%20%20%20%20%20%20%20self.marke%20%3D%20marke%0A%20%20%20%20%20%20%20%20self._kilometerstand%20%3D%20kilometerstand%20%20%23%20protected%0A%0A%20%20%20%20def%20info%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marke%7D%20mit%20%7Bself._kilometerstand%7D%20km%22%0A%0Aa%20%3D%20Auto%28%22VW%22%2C%2050000%29%0Aprint%28a.info%28%29%29%0Aprint%28a._kilometerstand%29%20%20%23%20Funktioniert%2C%20aber%20sollte%20vermieden%20werden&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
class Auto:
    def __init__(self, marke, kilometerstand):
        self.marke = marke
        self._kilometerstand = kilometerstand  # protected

    def info(self):
        return f"{self.marke} mit {self._kilometerstand} km"

a = Auto("VW", 50000)
print(a.info())
print(a._kilometerstand)  # Funktioniert, aber sollte vermieden werden
```

!!! info "Vergleich zu Java"
    In Java würde `protected` den Zugriff auf die eigene Klasse und
    Unterklassen beschränken. In Python ist `_attribut` nur ein **Hinweis**
    an andere Entwickler - es gibt keinen technischen Schutz.

## Private (`__attribut`) - Name Mangling

Zwei Unterstriche vor dem Namen aktivieren den Mechanismus
**Name Mangling**. Python benennt das Attribut intern um,
sodass es von außen nicht mehr unter dem ursprünglichen
Namen erreichbar ist.

[Link zum Onlinecompiler](https://pythontutor.com/render.html#code=class%20Konto%3A%0A%20%20%20%20def%20__init__%28self%2C%20inhaber%2C%20kontostand%29%3A%0A%20%20%20%20%20%20%20%20self.inhaber%20%3D%20inhaber%0A%20%20%20%20%20%20%20%20self.__kontostand%20%3D%20kontostand%20%20%23%20private%0A%0A%20%20%20%20def%20einzahlen%28self%2C%20betrag%29%3A%0A%20%20%20%20%20%20%20%20self.__kontostand%20%2B%3D%20betrag%0A%0A%20%20%20%20def%20get_kontostand%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.__kontostand%0A%0Ak%20%3D%20Konto%28%22Max%22%2C%201000%29%0Aprint%28k.get_kontostand%28%29%29%20%20%23%201000%0A%0A%23%20Direkter%20Zugriff%20schlaegt%20fehl%3A%0Atry%3A%0A%20%20%20%20print%28k.__kontostand%29%0Aexcept%20AttributeError%20as%20e%3A%0A%20%20%20%20print%28f%22Fehler%3A%20%7Be%7D%22%29%0A%0A%23%20Aber%20ueber%20Name%20Mangling%20erreichbar%3A%0Aprint%28k._Konto__kontostand%29%20%20%23%201000&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
class Konto:
    def __init__(self, inhaber, kontostand):
        self.inhaber = inhaber
        self.__kontostand = kontostand  # private

    def einzahlen(self, betrag):
        self.__kontostand += betrag

    def get_kontostand(self):
        return self.__kontostand

k = Konto("Max", 1000)
print(k.get_kontostand())  # 1000

# Direkter Zugriff schlägt fehl:
try:
    print(k.__kontostand)
except AttributeError as e:
    print(f"Fehler: {e}")

# Aber über Name Mangling erreichbar:
print(k._Konto__kontostand)  # 1000
```

### Wie funktioniert Name Mangling?

Python benennt `__attribut` intern um zu `_Klassenname__attribut`:

```
self.__kontostand  -->  self._Konto__kontostand
```

Das bedeutet:

- `k.__kontostand` erzeugt einen `AttributeError`
- `k._Konto__kontostand` funktioniert trotzdem

Name Mangling ist also **kein echter Schutz**, sondern soll
versehentliches Überschreiben in Unterklassen verhindern.

!!! warning "Achtung: Dunder Methods sind kein Name Mangling"
    Attribute mit doppeltem Unterstrich **vorne und hinten** (z.B. `__init__`, `__str__`)
    sind Magic Methods und werden **nicht** umbenannt. Name Mangling greift nur bei
    doppeltem Unterstrich **am Anfang ohne doppelten Unterstrich am Ende**.

## Name Mangling bei Vererbung

Der Hauptgrund für Name Mangling ist der Schutz vor
versehentlichem Überschreiben in Unterklassen:

[Link zum Onlinecompiler](https://pythontutor.com/render.html#code=class%20Tier%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.__sound%20%3D%20%22...%22%20%20%23%20wird%20zu%20_Tier__sound%0A%0A%20%20%20%20def%20sprich%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.__sound%0A%0Aclass%20Hund%28Tier%29%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20super%28%29.__init__%28%29%0A%20%20%20%20%20%20%20%20self.__sound%20%3D%20%22Wuff%22%20%20%23%20wird%20zu%20_Hund__sound%0A%0Ah%20%3D%20Hund%28%29%0Aprint%28h.sprich%28%29%29%20%20%23%20%22...%22%20%28nicht%20%22Wuff%22%21%29%0Aprint%28h._Tier__sound%29%20%20%23%20%22...%22%0Aprint%28h._Hund__sound%29%20%20%23%20%22Wuff%22&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
class Tier:
    def __init__(self):
        self.__sound = "..."  # wird zu _Tier__sound

    def sprich(self):
        return self.__sound

class Hund(Tier):
    def __init__(self):
        super().__init__()
        self.__sound = "Wuff"  # wird zu _Hund__sound

h = Hund()
print(h.sprich())  # "..." (nicht "Wuff"!)
print(h._Tier__sound)  # "..."
print(h._Hund__sound)  # "Wuff"
```

Hier sehen wir: `Tier.__sound` und `Hund.__sound` sind durch Name Mangling
**zwei verschiedene Attribute**. Die Methode `sprich()` in `Tier` greift auf
`_Tier__sound` zu, nicht auf `_Hund__sound`.

## Zusammenfassung

| Konvention | Beispiel | Bedeutung | Technischer Schutz |
|------------|----------|-----------|-------------------|
| Public | `self.name` | Für alle zugänglich | Keiner |
| Protected | `self._name` | Nur intern verwenden | Keiner (nur Konvention) |
| Private | `self.__name` | Nicht von außen zugreifen | Name Mangling (`_Klasse__name`) |

!!! tip "Pythons Philosophie"
    In Python gilt das Prinzip: **"We are all consenting adults here."**
    Anstatt den Zugriff technisch zu erzwingen, vertraut Python darauf,
    dass Entwickler die Konventionen respektieren.

## Ausblick: Getter & Setter

Auf der nächsten Seite lernen wir, wie wir mit `@property` den Zugriff
auf Attribute kontrollieren können - die pythonische Art, Getter und Setter
zu implementieren. Dabei spielt `_attribut` bzw. `__attribut` eine wichtige
Rolle als internes Speicherattribut.
