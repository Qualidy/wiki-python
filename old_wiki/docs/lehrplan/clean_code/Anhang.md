$$$ TODO 13: Prüfe ob etwas hiervon für dich nutzbar ist und füge es direkt ins skript ein, der rest weg.

# Anhang

## Globale Parameter

- **Aufgabe**: Beispiele für nyladische Funktionen

    - **`random.random()`:** Gibt eine Zufallszahl zwischen 0.0 und 1.0 zurück. Erfordert `import random`.
    - **`uuid.uuid4()`:** Erzeugt eine zufällige UUID. Erfordert `import uuid`.
    - **`os.urandom()`:** Gibt eine Zeichenfolge von n zufälligen Bytes zurück. Erfordert `import os`.
    - **`time.time()`:** Gibt die aktuelle Zeit in Sekunden seit der Epoche (1. Januar 1970) zurück.
      Erfordert `import time`.
    - **`datetime.datetime.now()`:** Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
      Erfordert `import datetime`.
    - **`itertools.count()`:** Erzeugt einen unendlichen Zähler. Erfordert `import itertools`.
    - **`sys.getsizeof()`:** Gibt die Größe eines Objekts in Bytes zurück. Erfordert `import sys`.
    - **`gc.collect()`:** Führt eine sofortige Garbage Collection aus. Erfordert `import gc`.

- **Aufgabe**: Beispiel für eine nyladische selbst verfasste Funktion:

```python
import random


def generate_random_numbers():
    """
    Die Funktion generiert eine Liste von 20 zufällige Zahlen zwischen 1 und 100 und gibt sie zurück.
    
    Args: keine
    """
    numbers = [random.randint(1, 100) for _ in range(20)]
    return numbers


# Beispielaufruf der Funktion
random_numbers = generate_random_numbers()
print(random_numbers)
```

## ListComprehension

**Frage:** Was macht der Code

```python
words = ["apple", "banana", "cherry", "date", "fig", "grape", "apple", "kiwi", "jamberry"]

print([(word.upper(), len(word)) for word in set(words) if len(word) > 3])
```

1. Es wird eine Liste von Worten verarbeitet.
2. Die `print` Anweisung gibt ein Array mit Tupeln aus Wörtern in Großbuchstaben und deren Länge aus.
3. `set(words)` erstellt ein neues Array aus dem words Array und stellt sicher, dass es keine Duplikate gibt.
4. `ìf` begrenzt die Ausgabe auf Wörter mit einer Länge größer als 3.

**Aufgabe:** Code umschreiben

```python
my_list = []
for x in range(20):
    if x % 2 == 0 and x % 3 == 0:
        my_list.append(x ** 2)
```

## DRY

**Aufgabe**: Komplexeres Beispiel

```python
def verarbeite_personendaten(personen, zusatzlogik=None):
    verarbeitete_daten = []
    for person in personen:
        verarbeitete_person = {
            "name": person["name"],
            "email": person["email"]
        }
        if zusatzlogik:
            zusatzlogik(verarbeitete_person, person)
        verarbeitete_daten.append(verarbeitete_person)
    return verarbeitete_daten


def kundenlogik(verarbeitete_person, person):
    # Spezifische Logik für Kunden
    pass


def mitarbeiterlogik(verarbeitete_person, person):
    # Spezifische Logik für Mitarbeiter
    pass


# Beispielaufrufe
kunden = [{"name": "Kunde1", "email": "kunde1@example.com"}, ...]
mitarbeiter = [{"name": "Mitarbeiter1", "email": "mitarbeiter1@example.com"}, ...]

verarbeitete_kunden = verarbeite_personendaten(kunden, kundenlogik)
verarbeitete_mitarbeiter = verarbeite_personendaten(mitarbeiter, mitarbeiterlogik)
```

**Aufgabe**: Ausnahmen zur Regel

1. Über-Abstraktion

   Obwohl das DRY-Prinzip (Don't Repeat Yourself) generell als gute Praxis im Software-Engineering gilt, gibt es
   Situationen, in denen eine strikte Anwendung nicht ideal oder sogar kontraproduktiv sein kann. Hier sind einige
   Argumente, die gegen eine strikte Anwendung von DRY sprechen:
    - **Beschreibung:** Versuche, Wiederholungen zu vermeiden, können zu übermäßiger Abstraktion führen.
    - **Folge:** Der Code wird komplizierter und schwerer verständlich, besonders wenn die Abstraktionen nicht intuitiv
      oder schlecht dokumentiert sind.

2. Vorzeitige Optimierung

    - **Beschreibung:** Das vorzeitige Zusammenführen von Code in Funktionen oder Module kann problematisch sein.
    - **Folge:** Es entstehen starre Strukturen, die spätere Anpassungen erschweren.

3. Leichte Veränderungen in der Logik

    - **Beschreibung:** Ähnlicher, aber nicht identischer Code kann die Zusammenfassung komplex machen.
    - **Folge:** Es kann sinnvoller sein, ähnlichen Code separat zu halten, um Lesbarkeit und Wartbarkeit zu bewahren.

4. Leistungseinbußen

    - **Beschreibung:** In einigen Fällen kann die Vermeidung von Code-Duplikation zu Leistungseinbußen führen.
    - **Folge:** Ersetzen von Inline-Code durch Funktionsaufrufe kann Overhead verursachen, was in performance
      kritischen
      Anwendungen problematisch ist.

5. Erhöhte Kopplung

    - **Beschreibung:** Übermäßige Vermeidung von Duplikation kann zu einer erhöhten Kopplung zwischen Programmteilen
      führen.
    - **Folge:** Die Modularität kann beeinträchtigt werden, was den Code anfälliger für Fehler bei Änderungen macht.

6. Schwierigkeiten bei der Fehlerbehebung

    - **Beschreibung:** Wenn eine DRY-umsetzende Funktion einen Fehler aufweist, kann sich dieser auf mehrere
      Systemteile auswirken.
    - **Folge:** In manchen Fällen kann es sicherer sein, bestimmte Funktionalitäten zu duplizieren, besonders wenn sie
      kritisch sind und isoliert bleiben sollten.

### Zusammenfassung und Fazit

DRY ist ein Leitprinzip und sollte nicht als unumstößliches Gesetz angesehen werden. Die Entscheidung, wann und wie DRY
angewendet wird, sollte auf einem Gleichgewicht zwischen Code-Effizienz, Lesbarkeit und Wartbarkeit basieren. Eine
Dokumentation der Gründe erscheint angebracht.

## Funktionsgestaltung

**Diskussion:** Welche Funktionen sind denkbar, die den Regeln nicht entsprechen können?

### Allgemeine Ausnahmen

Die Regel des Clean Code, dass Funktionen nur eine Sache tun sollten, ist ein Leitprinzip, das darauf abzielt, die
Lesbarkeit, Wartbarkeit und Testbarkeit des Codes zu verbessern. Es gibt jedoch Situationen, in denen es schwierig sein
kann, diese Regel strikt zu befolgen:

1. **Legacy-Code:** In bestehenden Systemen, insbesondere in älteren oder Legacy-Codebasen, gibt es oft Funktionen, die
   aus historischen Gründen mehrere Aufgaben erfüllen. Das Refactoring solcher Funktionen kann riskant sein, besonders
   wenn es keine ausreichenden Tests gibt.

2. **Performance-Optimierungen:** In einigen Fällen kann das Zusammenfassen mehrerer Aufgaben in einer Funktion aus
   Performance-Gründen sinnvoll sein, insbesondere in zeitkritischen Anwendungen. Hierbei ist jedoch Vorsicht geboten,
   da dies die Lesbarkeit und Wartbarkeit beeinträchtigen kann.

3. **Framework- oder API-Beschränkungen:** Manchmal erfordern bestimmte Frameworks oder APIs, dass eine Funktion mehrere
   Dinge tut, insbesondere wenn sie als Callbacks oder Event-Handler fungieren.

4. **Komplexe Geschäftslogik:** In einigen Fällen kann die Geschäftslogik so komplex sein, dass eine Aufteilung in
   kleinere Funktionen die Verständlichkeit nicht unbedingt verbessert. In solchen Fällen kann es sinnvoller sein, die
   Funktion gut zu dokumentieren, anstatt sie künstlich aufzuteilen.

5. **Praktikabilität:** In der Praxis kann es manchmal pragmatischer sein, eine Funktion zu haben, die mehrere Dinge
   tut, besonders in kleineren oder weniger kritischen Anwendungen, wo die strikte Einhaltung von Clean Code-Prinzipien
   möglicherweise nicht gerechtfertigt ist.

In allen diesen Fällen ist es wichtig, einen ausgewogenen Ansatz zu wählen. Die Einhaltung von Clean Code-Prinzipien
sollte das Ziel sein, aber es ist auch wichtig, pragmatisch zu sein und den Kontext zu berücksichtigen, in dem der Code
geschrieben wird.

### Spezielle Ausnahme **switch**

#### Switch in Python mit `ìf`

```python
def switch_example(value):
    if value == 1:
        return "Eins"
    elif value == 2:
        return "Zwei"
    elif value == 3:
        return "Drei"
    else:
        return "Anderer Wert"

print(switch_example(2))  # Gibt "Zwei" aus
```

#### Switch in Python mit dictionary

```python
def switch_example(value):
    switcher = {
        1: "Eins",
        2: "Zwei",
        3: "Drei"
    }
    return switcher.get(value, "Anderer Wert")


print(switch_example(3))  # Gibt "Drei" aus
```

In beiden Varianten ist klar, dass diese Funktionen in der dargestellten Art nur eine Sache erledigen: sie geben einen
Wert zurück. In den meisten Fällen ist es aber so, dass im jeweiligen `ìf` oder dictionary Teil eine Funktion aufgerufen
wird. Damit ist die Do-One-Thing Regel umgangen.

Die Verwendung von `switch`-Anweisungen in der Programmierung, insbesondere im Kontext von Clean Code, ist ein Thema,
das oft diskutiert wird. Hier sind einige Überlegungen dazu:

1. **Komplexität:** `switch`-Anweisungen können schnell komplex und schwer zu warten werden, besonders wenn sie
   viele `case`-Zweige enthalten. Dies steht im Widerspruch zu den Clean Code-Prinzipien, die Einfachheit und Klarheit
   betonen.

2. **Verletzung des Open/Closed-Prinzips:** Jedes Mal, wenn ein neuer Fall hinzugefügt wird, muss die `switch`-Anweisung
   geändert werden. Dies verstößt gegen das Open/Closed-Prinzip, eines der SOLID-Prinzipien, das besagt, dass
   Software-Entitäten (Klassen, Module, Funktionen usw.) für Erweiterung offen, aber für Modifikation geschlossen sein
   sollten.

3. **Wiederholung und DRY-Prinzip:** `switch`-Anweisungen neigen dazu, Code zu wiederholen, insbesondere wenn ähnliche
   Aktionen in verschiedenen `case`-Zweigen ausgeführt werden. Dies kann gegen das DRY-Prinzip (Don't Repeat Yourself)
   verstoßen.

4. **Alternative Design-Patterns:** In vielen Fällen, in denen `switch`-Anweisungen verwendet werden, können
   Design-Patterns wie Strategy, State oder Command effektivere Lösungen bieten. Diese Patterns ermöglichen es, das
   Verhalten dynamisch zu ändern, ohne die `switch`-Anweisung zu modifizieren, und unterstützen eine sauberere und
   modularere Code-Struktur.

5. **Sprachspezifische Alternativen:** Einige moderne Programmiersprachen bieten fortgeschrittenere Konstrukte,
   die `switch`-Anweisungen ersetzen können, wie z.B. Pattern Matching in funktionalen Sprachen.

6. **Einsatz in begrenztem Umfang:** In einfachen Fällen, wo eine `switch`-Anweisung nur wenige `case`-Zweige hat und
   nicht oft geändert wird, kann ihr Einsatz gerechtfertigt sein. Wichtig ist, dass der Code klar und gut verständlich
   bleibt.

Insgesamt empfiehlt Clean Code, die Verwendung von `switch`-Anweisungen zu vermeiden oder zu minimieren, insbesondere in
komplexen oder sich häufig ändernden Systemen. Stattdessen sollten alternative Ansätze in Betracht gezogen werden, die
eine bessere Modularität, Erweiterbarkeit und Wartbarkeit des Codes ermöglichen.

**Begriffserklärung:** SOLID

Die SOLID-Prinzipien sind ein Satz von Design-Prinzipien in der objektorientierten Programmierung, die dazu dienen,
Softwareentwicklungen verständlicher, flexibler und wartbarer zu machen. Sie wurden von Robert C. Martin formuliert.

## Funktionsparameter

**Aufgabe:** Reduktion von Parametern

1. **Verwendung von Objekten:**
    - Anstatt mehrere Parameter zu übergeben, können diese in einem Objekt zusammengefasst werden. Dies ist besonders
      nützlich, wenn mehrere Funktionen ähnliche Parameter benötigen.
    - Beispiel: Statt `function(a, b, c, d)` zu verwenden, erstellen Sie ein Objekt `params = {a, b, c, d}` und rufen
      Sie `function(params)` auf.

2. **Parameter-Objekte:**
    - Ähnlich wie oben, aber spezifischer, können Sie spezielle Klassen oder Strukturen definieren, die als
      Datencontainer dienen. Dies ist besonders nützlich in objektorientierten Sprachen.
    - Beispiel: Erstellen Sie eine Klasse `FunctionParams` mit den erforderlichen Attributen und übergeben Sie eine
      Instanz dieser Klasse an die Funktion.

3. **Standardwerte für Parameter:**
    - Definieren Sie Standardwerte für Parameter, um die Notwendigkeit zu verringern, Werte für alle Parameter bei jedem
      Aufruf anzugeben.
    - Beispiel: In Python können Sie `def function(a, b=5)` verwenden, wobei `b` optional ist und standardmäßig den Wert
      5 hat.

4. **Builder-Muster:**
    - Das Builder-Muster ist nützlich, wenn ein Objekt mit vielen optionalen Parametern erstellt werden muss. Es
      ermöglicht eine schrittweise Konstruktion von Objekten.
    - Beispiel: Anstatt einen Konstruktor mit vielen Parametern zu verwenden, ermöglicht der Builder schrittweise das
      Hinzufügen von Parametern.

5. **Methoden-Ketten (Fluent Interface):**
    - Ähnlich wie das Builder-Muster, aber für Methodenaufrufe. Methoden geben das eigene Objekt zurück, sodass weitere
      Aufrufe gekettet werden können.
    - Beispiel: `objekt.setA(a).setB(b).setC(c)`

6. **Argumente gruppieren:**
    - Gruppieren Sie verwandte Argumente in Unterobjekte oder Strukturen.
    - Beispiel: Statt `drawRectangle(x1, y1, x2, y2, color)` könnten Sie `drawRectangle(point1, point2, color)`
      verwenden, wobei `point1` und `point2` Objekte sind.

7. **Verwendung von Konfigurationsobjekten:**
    - Für komplexere Funktionen, insbesondere solche, die in Konfigurationen oder Umgebungen verwendet werden, können
      Konfigurationsobjekte übergeben werden, die alle erforderlichen Einstellungen enthalten.

8. **Currying und partielle Anwendung:**
    - In funktionalen Programmiersprachen können Sie Currying oder partielle Anwendung verwenden, um Funktionen zu
      erstellen, die einige Parameter vorab festlegen.

## Was aus dem Code von Robert C. Martin am Ende wurde

Nach einigen Überlegungen und Aufräumarbeiten wird aus dem ehemals schwer verständlichen Code eine Geschichte, die gut
zu lesen und schneller zu verstehen ist.

```python
class SetupTeardownIncluder:
    def __init__(self, page_data):
        self.page_data = page_data
        self.test_page = page_data.get_wiki_page()
        self.page_crawler = self.test_page.get_page_crawler()
        self.new_page_content = []

    @staticmethod
    def render(page_data, is_suite=False):
        includer = SetupTeardownIncluder(page_data)
        return includer._render(is_suite)

    def _render(self, is_suite):
        self.is_suite = is_suite
        if self._is_test_page():
            self._include_setup_and_teardown_pages()
        return self.page_data.get_html()

    def _is_test_page(self):
        return self.page_data.has_attribute("Test")

    def _include_setup_and_teardown_pages(self):
        self._include_setup_pages()
        self._include_page_content()
        self._include_teardown_pages()
        self._update_page_content()

    def _include_setup_pages(self):
        if self.is_suite:
            self._include_suite_setup_page()
        self._include_setup_page()

    def _include_suite_setup_page(self):
        self._include(SuiteResponder.SUITE_SETUP_NAME, "-setup")

    def _include_setup_page(self):
        self._include("SetUp", "-setup")

    def _include_page_content(self):
        self.new_page_content.append(self.page_data.get_content())

    def _include_teardown_pages(self):
        self._include_teardown_page()
        if self.is_suite:
            self._include_suite_teardown_page()

    def _include_teardown_page(self):
        self._include("TearDown", "-teardown")

    def _include_suite_teardown_page(self):
        self._include(SuiteResponder.SUITE_TEARDOWN_NAME, "-teardown")

    def _update_page_content(self):
        self.page_data.set_content(''.join(self.new_page_content))

    def _include(self, page_name, arg):
        inherited_page = self._find_inherited_page(page_name)
        if inherited_page is not None:
            page_path_name = self._get_path_name_for_page(inherited_page)
            self._build_include_directive(page_path_name, arg)

    def _find_inherited_page(self, page_name):
        return PageCrawlerImpl.get_inherited_page(page_name, self.test_page)

    def _get_path_name_for_page(self, page):
        page_path = self.page_crawler.get_full_path(page)
        return PathParser.render(page_path)

    def _build_include_directive(self, page_path_name, arg):
        self.new_page_content.append(f"\n!include {arg} .{page_path_name}\n")
```

## Zusätzliche Ressourcen

### Inhalt

Eine Liste von Büchern, Websites und Tools, die für weiterführende Studien zum Thema Clean Code nützlich sind.

---
