# Kapitel: Verwendung von pip
[120min]

Pip ist das Paketverwaltungstool für Python, das verwendet wird, um Python-Pakete zu installieren, zu aktualisieren und zu entfernen. In diesem Kapitel werden wir die grundlegende Verwendung von Pip sowie das Setzen eines Proxys mit Authentifizierung besprechen.

Ein Paketverwaltungstool ist eine Software, die die einfache Installation, Aktualisierung und Deinstallation von Softwarepaketen erleichtert, indem sie automatisch Abhängigkeiten auflöst und Versionskontrolle ermöglicht. In Python ist "pip" das gängige Paketverwaltungstool, das die Verwaltung von Bibliotheken und Modulen erleichtert.

## 1. Installation von pip

Bevor wir pip verwenden können, müssen wir sicherstellen, dass es installiert ist. Normalerweise ist Pip bereits in den neueren Python-Versionen enthalten. Falls nicht, kann es mit dem folgenden Befehl installiert werden:

- `python -m ensurepip --default-pip`

Alternativ kann auch der direkte Download-Link verwendet werden:

- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
- `python get-pip.py`

Nach der Installation können wir pip mit dem Befehl `pip` aufrufen.

## 2. Grundlegende Pip-Befehle

### 2.1. Pakete installieren

Um ein Paket zu installieren, verwenden wir den Befehl:

- `pip install Paketname`

Beispiel:

- `pip install requests`

Requests ist eine Python-Bibliothek, die es ermöglicht, HTTP-Anfragen einfach zu senden und die entsprechenden Antworten zu verarbeiten.

### 2.2. Pakete aktualisieren

Wenn eine neue Version eines Pakets verfügbar ist, können wir es aktualisieren:

- `pip install --upgrade Paketname`

Beispiel:

- `pip install --upgrade requests`

### 2.3. Installierte Pakete anzeigen

Um alle installierten Pakete anzuzeigen, verwenden wir:

- `pip list`

## 3. Verwendung eines Proxys mit Authentifizierung

Manchmal ist es notwendig, Pip in Umgebungen mit einem Proxy-Server zu verwenden, der eine Authentifizierung erfordert. Im Umfeld von Volkswagen ist dies in der Regel notwendig.

### 3.1. Setzen des Proxys

- `pip install --proxy=http://proxy-server:proxy-port Paketname`

### 3.2. Setzen des Proxys mit Authentifizierung

- `pip install --proxy=http://Benutzername:Passwort@proxy-server:proxy-port Paketname`

Ersetze `Benutzername`, `Passwort`, `proxy-server` und `proxy-port` durch die entsprechenden Informationen des Proxys.

Beispiel:

- `pip install --proxy=http://myuser:mypassword@proxy.example.com:8080 requests`

Durch diese Befehle wird Pip angewiesen, den angegebenen Proxy zu verwenden, wenn es auf das Internet zugreift, und falls erforderlich, wird auch die Authentifizierung durchgeführt.

# Aufgaben
[60min]

{{ task(file="tasks/python_grundlagen/03_pip/01_installation_eines_pakets.yaml") }}
{{ task(file="tasks/python_grundlagen/03_pip/02_aktualisierung_eines_pakets.yaml") }}
{{ task(file="tasks/python_grundlagen/03_pip/03_deinstallation_eines_pakets.yaml") }}
{{ task(file="tasks/python_grundlagen/03_pip/04_anzeige_installierter_pakete.yaml") }}
{{ task(file="tasks/python_grundlagen/03_pip/05_suche_nach_einem_paket.yaml") }}
{{ task(file="tasks/python_grundlagen/03_pip/06_installation_einer_bestimmten_paketversion.yaml") }}
{{ task(file="tasks/python_grundlagen/03_pip/07_upgrade_eines_pakets_auf_eine_bestimmte_version.yaml") }}
