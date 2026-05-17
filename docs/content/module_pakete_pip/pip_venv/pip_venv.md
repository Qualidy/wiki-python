# Module und Pakete

## Pip und Venv

### Verwaltung von Paketen mit `pip`

**Pip** ist das Standard-Paketverwaltungssystem für Python, das das Installieren, Aktualisieren und Verwalten von Python-Paketen ermöglicht. Wie bereits im Abschnitt [Pakete](../pakete/pakete.md) besprochen, können externe Pakete auf Plattformen wie [PyPi](https://pypi.org/) gefunden werden. 

In den meisten Fällen ist `pip` vorinstalliert und sofort einsatzbereit.

{{ task(file="tasks/python_grundlagen/pip_venv/pip_venv/01_erkunde_pip.yaml") }}
### Nutzung von `venv` für virtuelle Umgebungen

Ein Virtual Environment (`venv`) ermöglicht die Installation von Python-Paketen in einer isolierten Umgebung. Dies verhindert Abhängigkeitskonflikte zwischen verschiedenen Projekten.

#### Warum sind `venv`s wichtig?

- **Isolierung**: Jedes Projekt kann mit seinen eigenen Abhängigkeiten arbeiten, ohne andere zu beeinflussen.
- **Konsistenz**: Stellt sicher, dass alle Projektmitglieder dieselben Paketversionen nutzen, was typische "Bei mir läuft's aber!"-Probleme vermeidet.
- **Einfache Verwaltung**: Ermöglicht das problemlose Aktualisieren oder Downgraden von Paketen ohne Beeinträchtigung des Gesamtsystems.

{{ task(file="tasks/python_grundlagen/pip_venv/pip_venv/02_erstelle_und_nutze_eine_virtuelle_umgebung.yaml") }}
### Installation von Paketen im Virtual Environment

Mit einem aktiven Virtual Environment kannst du Pakete isoliert installieren. Verwende `pip install package_name`, um ein Paket zu installieren, wobei `package_name` der Name des gewünschten Pakets ist.

{{ task(file="tasks/python_grundlagen/pip_venv/pip_venv/03_let_it_pip.yaml") }}
