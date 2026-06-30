# Projekt: Web Scraping

## Lernziele

In diesem Projekt lernst du, wie du automatisiert Daten von Webseiten extrahieren kannst. Du wirst:

- HTTP-Requests mit der `requests`-Bibliothek senden
- HTML-Seiten mit `BeautifulSoup` parsen und navigieren
- CSS-Selektoren verwenden, um gezielt Elemente zu finden
- Einen vollständigen Scraper bauen, der über mehrere Seiten navigiert
- Extrahierte Daten in CSV und JSON speichern

---

## Kursthemen-Abdeckung

Dieses Projekt verbindet viele Themen aus dem Kurs:

| Kursthema | Anwendung im Projekt |
|-----------|---------------------|
| **OOP** | Klasse `QuoteScraper` mit Methoden |
| **Exceptions** | `requests.exceptions`, `try/except` bei Netzwerkfehlern |
| **File I/O** | Ergebnisse als CSV und JSON speichern |
| **Module & pip** | `requests`, `beautifulsoup4` installieren und nutzen |
| **Datenstrukturen** | Listen von Dictionaries für Zitate |
| **List Comprehensions** | Datenextraktion kompakt formulieren |

---

## Ziel-Webseite

Wir scrapen **[quotes.toscrape.com](https://quotes.toscrape.com)** – eine speziell für Scraping-Übungen erstellte Webseite mit Zitaten, Autoren und Tags.

!!! info "Warum diese Seite?"
    `quotes.toscrape.com` ist eine **Übungsseite**, die explizit zum Lernen von Web Scraping erstellt wurde. Im Gegensatz zu echten Webseiten darfst du diese Seite bedenkenlos scrapen. Bei echten Webseiten musst du immer die `robots.txt` und die Nutzungsbedingungen beachten!

---

## Setup

### 1. Virtuelle Umgebung (falls nicht vorhanden)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
.\venv\Scripts\Activate.ps1  # Windows
```

### 2. Bibliotheken installieren

```bash
pip install requests beautifulsoup4
```

### 3. Installation prüfen

```python
import requests
from bs4 import BeautifulSoup

print(f"requests version: {requests.__version__}")
print(f"BeautifulSoup importiert: ✅")
```

---

## Aufbau des Projekts

Das Projekt ist in vier aufeinander aufbauende Teile gegliedert:

1. **HTTP & Requests** – Webseiten herunterladen und Statuscodes verstehen
2. **HTML Parsing mit BeautifulSoup** – HTML-Struktur verstehen und navigieren
3. **CSS-Selektoren** – Elemente gezielt mit `.select()` finden
4. **Projektaufgabe** – Einen vollständigen Zitat-Scraper bauen

Jeder Teil enthält Erklärungen und praktische Aufgaben mit steigender Schwierigkeit.

---

## Ethik & Rechtliches

!!! warning "Verantwortungsvolles Scraping"
    - **Prüfe immer** die `robots.txt` einer Webseite (z.B. `https://example.com/robots.txt`)
    - **Respektiere** die Nutzungsbedingungen der Webseite
    - **Überlaste keine Server** – baue Pausen (`time.sleep()`) in deinen Scraper ein
    - **Personenbezogene Daten** unterliegen der DSGVO – scrape keine persönlichen Informationen
    - Für dieses Projekt nutzen wir `quotes.toscrape.com`, eine **explizite Übungsseite**
