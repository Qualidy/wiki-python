# CSS-Selektoren

## Was sind CSS-Selektoren?

CSS-Selektoren sind eine Syntax aus der Web-Entwicklung, mit der man HTML-Elemente gezielt auswählen kann. BeautifulSoup unterstützt CSS-Selektoren über die Methoden `.select()` und `.select_one()`.

Im Vergleich zu `find()` / `find_all()` sind CSS-Selektoren oft **kompakter** und **ausdrucksstärker**, besonders bei verschachtelten Strukturen.

---

## Grundlegende Selektoren

### Tag-Selektor

Wählt alle Elemente eines bestimmten Tags aus:

```python
# Alle <p>-Elemente
soup.select("p")

# Äquivalent zu:
soup.find_all("p")
```

### Klassen-Selektor (`.`)

Wählt Elemente mit einer bestimmten CSS-Klasse:

```python
# Alle Elemente mit class="text"
soup.select(".text")

# Tag + Klasse kombiniert
soup.select("span.text")

# Äquivalent zu:
soup.find_all("span", class_="text")
```

### ID-Selektor (`#`)

Wählt ein Element mit einer bestimmten ID (sollte eindeutig sein):

```python
# Element mit id="main"
soup.select_one("#main")

# Äquivalent zu:
soup.find(id="main")
```

---

## Kombinierte Selektoren

### Nachfahren-Selektor (Leerzeichen)

Wählt Elemente, die **irgendwo innerhalb** eines anderen Elements liegen:

```python
# Alle <a>-Tags innerhalb von <div class="tags">
soup.select("div.tags a")

# Alle <span>-Tags innerhalb von <div class="quote">
soup.select("div.quote span")
```

### Direktes Kind (`>`)

Wählt nur **direkte** Kinder (nicht tiefer verschachtelt):

```python
# Nur direkte <p>-Kinder von <div class="content">
soup.select("div.content > p")
```

### Mehrere Selektoren (`,`)

Wählt Elemente, die **einem von mehreren** Selektoren entsprechen:

```python
# Alle <h1> und <h2> Elemente
soup.select("h1, h2")
```

---

## Referenz-Tabelle

| Selektor | Beschreibung | Beispiel |
|----------|-------------|----------|
| `tag` | Nach Tag-Name | `soup.select("p")` |
| `.klasse` | Nach CSS-Klasse | `soup.select(".text")` |
| `#id` | Nach ID | `soup.select_one("#main")` |
| `tag.klasse` | Tag mit Klasse | `soup.select("span.text")` |
| `tag#id` | Tag mit ID | `soup.select_one("div#content")` |
| `parent child` | Nachfahre (beliebige Tiefe) | `soup.select("div.quote span")` |
| `parent > child` | Direktes Kind | `soup.select("div > p")` |
| `a, b` | Oder-Verknüpfung | `soup.select("h1, h2")` |
| `[attr]` | Hat Attribut | `soup.select("[href]")` |
| `[attr=wert]` | Attribut hat Wert | `soup.select('[class="text"]')` |

---

## `select()` vs `select_one()`

| Methode | Rückgabe | Wenn nichts gefunden |
|---------|----------|---------------------|
| `select()` | **Liste** von Elementen | Leere Liste `[]` |
| `select_one()` | **Ein** Element | `None` |

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")

# select() → Liste
alle_zitate = soup.select("span.text")
print(type(alle_zitate))  # <class 'bs4.element.ResultSet'>
print(len(alle_zitate))   # 10

# select_one() → einzelnes Element oder None
erstes_zitat = soup.select_one("span.text")
print(type(erstes_zitat))  # <class 'bs4.element.Tag'>
print(erstes_zitat.text)   # "The world as we..."
```

---

## Vergleich: `find()` vs `select()`

Beide Ansätze erreichen das gleiche Ziel. Hier ein direkter Vergleich am Beispiel von `quotes.toscrape.com`:

### Alle Zitate finden

```python
# Mit find_all()
zitate = soup.find_all("span", class_="text")

# Mit select()
zitate = soup.select("span.text")
```

### Alle Tags eines bestimmten Zitats

```python
# Ein Zitat-Div finden
quote_div = soup.find("div", class_="quote")

# Mit find_all() – innerhalb des Divs suchen
tags = quote_div.find_all("a", class_="tag")

# Mit select() – innerhalb des Divs suchen
tags = quote_div.select("a.tag")
```

### Verschachtelte Suche (Next-Link)

```python
# Mit find()
next_li = soup.find("li", class_="next")
if next_li:
    link = next_li.find("a")["href"]

# Mit select_one() – kompakter!
next_link = soup.select_one("li.next a")
if next_link:
    link = next_link["href"]
```

### Wann welche Methode?

| Situation | Empfehlung |
|-----------|-----------|
| Einfache Suche nach Tag + Klasse | Beides gleichwertig |
| Verschachtelte Suche | `select()` ist kompakter |
| Suche nach Attributen (nicht class/id) | `find()` mit `attrs={}` |
| Komplexe Selektoren | `select()` ist mächtiger |
| Gewohnheit aus Web-Entwicklung | `select()` nutzt CSS-Syntax |

---

## Praxisbeispiel: Zitate extrahieren

Ein vollständiges Beispiel mit CSS-Selektoren:

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")

# Alle Zitat-Container auswählen
for quote_div in soup.select("div.quote"):
    # Text, Autor und Tags extrahieren
    text = quote_div.select_one("span.text").text
    author = quote_div.select_one("small.author").text
    tags = [tag.text for tag in quote_div.select("a.tag")]

    print(f"'{text[:50]}...'")
    print(f"  – {author}")
    print(f"  Tags: {', '.join(tags)}")
    print()
```

---

## Aufgaben

{{ task('tasks/projekt_webscraping/05_css_selektoren.yaml') }}

{{ task('tasks/projekt_webscraping/06_daten_extrahieren.yaml') }}
