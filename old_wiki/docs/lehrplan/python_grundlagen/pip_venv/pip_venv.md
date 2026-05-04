# Module und Pakete

## Pip und Venv

### Verwaltung von Paketen mit `pip`

**Pip** ist das Standard-Paketverwaltungssystem für Python, das das Installieren, Aktualisieren und Verwalten von Python-Paketen ermöglicht. Wie bereits im Abschnitt [Pakete](../pakete/pakete.md) besprochen, können externe Pakete auf Plattformen wie [PyPi](https://pypi.org/) gefunden werden. 

In den meisten Fällen ist `pip` vorinstalliert und sofort einsatzbereit.

### Aufgabe: Erkunde `pip` 🌶️

1. **Überprüfung der Pip-Version**: Öffne ein Terminal und gib `pip --version` ein, um die installierte Pip-Version zu überprüfen.

2. **Auflistung installierter Pakete**: Mit dem Befehl `pip list` erhältst du eine Liste aller auf deinem System installierten Pakete.

3. **Suche nach Paketen**: Benutze `pip search PACKAGE_NAME`, um nach einem spezifischen Paket zu suchen. Ersetze `PACKAGE_NAME` mit dem Namen des gewünschten Pakets, wie z.B. `requests`.

4. **Paketinstallation**: Installiere ein Paket mit `pip install PACKAGE_NAME`, zum Beispiel `pip install requests`. Hinweis: In neueren Pip-Versionen (>3.10) könnte ein Fehler angezeigt werden, wenn versucht wird, ein Paket systemweit zu installieren.

<pre><code>
This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.

...
</code></pre>

### Nutzung von `venv` für virtuelle Umgebungen

Ein Virtual Environment (`venv`) ermöglicht die Installation von Python-Paketen in einer isolierten Umgebung. Dies verhindert Abhängigkeitskonflikte zwischen verschiedenen Projekten.

#### Warum sind `venv`s wichtig?

- **Isolierung**: Jedes Projekt kann mit seinen eigenen Abhängigkeiten arbeiten, ohne andere zu beeinflussen.
- **Konsistenz**: Stellt sicher, dass alle Projektmitglieder dieselben Paketversionen nutzen, was typische "Bei mir läuft's aber!"-Probleme vermeidet.
- **Einfache Verwaltung**: Ermöglicht das problemlose Aktualisieren oder Downgraden von Paketen ohne Beeinträchtigung des Gesamtsystems.

### Aufgabe: Erstelle und nutze eine virtuelle Umgebung 🌶️

1. **Virtual Environment erstellen**: Navigiere in deinem Terminal zum Projektverzeichnis und führe `python -m venv venv_name` aus, wobei `venv_name` der Name deiner virtuellen Umgebung ist. Dies erstellt eine neue Umgebung in deinem aktuellen Verzeichnis.

2. **Virtual Environment aktivieren**: Aktiviere die Umgebung mit dem Befehl `source {venv_name}/bin/activate`. Dieser Schritt ist notwendig, um die Umgebung in deiner aktuellen Terminal-Session zu nutzen.

   **Hinweis zu `source`**: Der Befehl `source` lädt Variablen oder Funktionen aus einer Datei in die aktuelle Session. Durch Aktivieren des Virtual Environments mittels des `activate`-Skripts werden die Umgebungsvariablen der Session temporär geändert.

3. **Überprüfen des leeren Environments**: Mit `pip list` kannst du alle in der virtuellen Umgebung installierten Pakete auflisten. Direkt nach der Erstellung sollte nur `pip` selbst aufgelistet sein.

<pre><code>
Package Version
------- -------
pip     24.0
</code></pre>

| Zum verlassen des Virtual Environment wird der Befehl `deactivate` genutzt.


### Installation von Paketen im Virtual Environment

Mit einem aktiven Virtual Environment kannst du Pakete isoliert installieren. Verwende `pip install package_name`, um ein Paket zu installieren, wobei `package_name` der Name des gewünschten Pakets ist.

### Aufgabe: Let it pip! 🌶️

1. Erstelle einen neuen Ordner für dein Projekt.
2. Erstelle und aktiviere ein Virtual Environment darin.
3. Installiere mehrere externe Pakete von PyPi, um mit deinem Projekt zu beginnen.