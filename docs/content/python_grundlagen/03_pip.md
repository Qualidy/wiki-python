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

## 1. Installation eines Pakets 🌶️️
   - Verwende den Befehl `pip install` und installiere das Paket "requests".

## 2. Aktualisierung eines Pakets 🌶️️
   - Aktualisiere das Paket "requests" auf die neueste verfügbare Version mit dem Befehl `pip install --upgrade`.

## 3. Deinstallation eines Pakets 🌶️️
   - Deinstalliere das Paket "requests" mit dem Befehl `pip uninstall`.

## 4. Anzeige installierter Pakete 🌶️️
   - Zeige alle installierten Pakete mit dem Befehl `pip list`.

## 5. Suche nach einem Paket 🌶️️
   - Suche nach dem Paket "numpy" mit dem Befehl `pip search numpy`.

## 6. Installation einer bestimmten Paketversion 🌶️️
   - Installiere eine spezifische Version des Pakets "requests" mit dem Befehl `pip install requests==2.25.1`.

## 7. Upgrade eines Pakets auf eine bestimmte Version 🌶️️
   - Upgrade das Paket "requests" auf eine bestimmte Version mit dem Befehl `pip install --upgrade requests==2.26.0`.
   