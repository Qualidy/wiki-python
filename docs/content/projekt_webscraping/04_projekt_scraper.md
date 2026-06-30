# Projektaufgabe: Zitat-Scraper

**Ziel:** Einen vollständigen Web Scraper entwickeln, der alle Zitate von `quotes.toscrape.com` extrahiert, strukturiert speichert und über ein CLI-Menü bedienbar ist.

---

## Anforderungen

### Must-Haves (Pflicht)

1. **Klasse `QuoteScraper`**
    - Attribut `base_url: str` – Basis-URL der Zielseite
    - Attribut `quotes: list[dict]` – Liste der gesammelten Zitate
    - Methode `scrape_page(url: str) -> list[dict]` – Zitate einer einzelnen Seite extrahieren
    - Methode `scrape_all() -> list[dict]` – Alle Seiten automatisch durchgehen (Pagination)
    - Methode `save_to_csv(filename: str) -> None` – Ergebnisse als CSV speichern
    - Methode `save_to_json(filename: str) -> None` – Ergebnisse als JSON speichern

2. **Datenstruktur pro Zitat**
    - `text`: Zitattext (ohne typografische Anführungszeichen)
    - `author`: Autorenname
    - `tags`: Liste der Tags
    - `author_url`: Link zur Autorenseite

3. **Fehlerbehandlung**
    - `try/except` bei Netzwerkfehlern (`requests.exceptions.RequestException`)
    - `raise_for_status()` nach jedem Request
    - Sinnvolle Fehlermeldungen bei Verbindungsproblemen

4. **CLI-Menü (`main.py`)**
    - Option 1: Alle Zitate scrapen
    - Option 2: Zitate nach Autor filtern
    - Option 3: Zitate nach Tag filtern
    - Option 4: Ergebnisse speichern (CSV oder JSON)
    - Option 5: Statistik anzeigen (Anzahl Zitate, Autoren, häufigste Tags)
    - Option 6: Beenden

5. **Git-Workflow**
    - Mindestens 5 sinnvolle Commits
    - Aussagekräftige Commit-Messages

### Nice-to-Haves (Optional)

- [ ] Fortschrittsanzeige beim Scrapen (`Seite 3/10 geladen...`)
- [ ] Zitate nach Stichwort im Text durchsuchen
- [ ] `time.sleep()` zwischen Requests (höfliches Scraping)
- [ ] Autor-Detailseiten scrapen (Geburtstag, Bio)
- [ ] Doppelte Zitate erkennen und filtern
- [ ] Ergebnisse sortieren (nach Autor, Anzahl Tags)

---

## Projektstruktur

```
quote-scraper/
├── main.py              # CLI-Menü und Programmstart
├── scraper.py           # Klasse QuoteScraper
├── storage.py           # Funktionen für CSV/JSON-Export
├── requirements.txt     # Abhängigkeiten (requests, beautifulsoup4)
└── output/              # Ordner für gespeicherte Dateien
    ├── quotes.csv
    └── quotes.json
```

---

## Technische Vorgaben

- **Erlaubte Themen:**
    - ✅ OOP: Klassen, Attribute, Methoden
    - ✅ Exceptions: `try/except`, `raise_for_status()`
    - ✅ File I/O: CSV und JSON schreiben
    - ✅ Module: `requests`, `bs4`, `csv`, `json`
    - ✅ Datenstrukturen: Listen, Dictionaries, List Comprehensions
    - ✅ Type Hints bei allen Funktionen und Methoden

---

## Beispielcode: Grundgerüst

### `scraper.py`

```python
import requests
from bs4 import BeautifulSoup


class QuoteScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.quotes: list[dict] = []

    def scrape_page(self, url: str) -> list[dict]:
        """Extrahiert alle Zitate von einer einzelnen Seite."""
        # TODO: Request senden, HTML parsen, Zitate extrahieren
        pass

    def scrape_all(self) -> list[dict]:
        """Scrapt alle Seiten über Pagination."""
        # TODO: Schleife über alle Seiten mit Next-Link
        pass

    def get_authors(self) -> list[str]:
        """Gibt eine sortierte Liste aller einzigartigen Autoren zurück."""
        return sorted(set(q["author"] for q in self.quotes))

    def filter_by_author(self, author: str) -> list[dict]:
        """Filtert Zitate nach Autor."""
        return [q for q in self.quotes if q["author"].lower() == author.lower()]

    def filter_by_tag(self, tag: str) -> list[dict]:
        """Filtert Zitate nach Tag."""
        return [q for q in self.quotes if tag.lower() in [t.lower() for t in q["tags"]]]
```

### `storage.py`

```python
import csv
import json


def save_to_csv(quotes: list[dict], filename: str) -> None:
    """Speichert Zitate als CSV-Datei."""
    # TODO: CSV mit Spalten text, author, tags schreiben
    pass


def save_to_json(quotes: list[dict], filename: str) -> None:
    """Speichert Zitate als JSON-Datei."""
    # TODO: JSON mit indent=2 und ensure_ascii=False schreiben
    pass
```

### `main.py`

```python
from scraper import QuoteScraper
from storage import save_to_csv, save_to_json


def main() -> None:
    scraper = QuoteScraper("https://quotes.toscrape.com")

    while True:
        print("\n=== Zitat-Scraper ===")
        print("1. Alle Zitate scrapen")
        print("2. Nach Autor filtern")
        print("3. Nach Tag filtern")
        print("4. Ergebnisse speichern")
        print("5. Statistik anzeigen")
        print("6. Beenden")

        try:
            choice = input("\nAuswahl: ").strip()
        except KeyboardInterrupt:
            print("\nProgramm beendet.")
            break

        # TODO: Menü-Logik implementieren


if __name__ == "__main__":
    main()
```

---

## Evaluation

| Kriterium | Punkte |
|-----------|--------|
| Scraper extrahiert alle 100 Zitate korrekt | ⭐⭐⭐ |
| Pagination funktioniert automatisch | ⭐⭐ |
| CSV- und JSON-Export funktioniert | ⭐⭐ |
| OOP sinnvoll eingesetzt (Klasse mit Methoden) | ⭐⭐ |
| Fehlerbehandlung vorhanden | ⭐ |
| CLI-Menü bedienbar | ⭐ |
| Type Hints bei allen Funktionen | ⭐ |
| Git-History mit sinnvollen Commits | ⭐ |
| Code-Qualität (lesbar, strukturiert) | ⭐ |
| Nice-to-Have Features | Bonus |

---

## Vorbereitende Aufgaben

Diese Aufgaben bereiten dich Schritt für Schritt auf das Projekt vor:

{{ task('tasks/projekt_webscraping/07_pagination.yaml') }}

{{ task('tasks/projekt_webscraping/08_daten_speichern.yaml') }}

---

## Tipps

- **Schrittweise vorgehen:** Erst eine Seite scrapen, dann Pagination hinzufügen, dann speichern
- **Testen mit `print()`:** Gib Zwischenergebnisse aus, um zu sehen, ob die Extraktion korrekt ist
- **Browser-DevTools nutzen:** ++f12++ im Browser, um die HTML-Struktur der Zielseite zu inspizieren
- **`time.sleep(1)`:** Baue eine Sekunde Pause zwischen Requests ein – das ist höflich gegenüber dem Server
- **Git-Commits:** Nach jedem funktionierenden Schritt committen, nicht erst am Ende!
