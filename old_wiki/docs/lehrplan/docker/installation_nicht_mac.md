# Installation von Docker auf nicht Mac OS Systemen

## Windows

- Docker wird auf Windows über Docker Desktop installiert.
- Docker Desktop für Windows setzt auf Hyper-V und WSL 2 (Windows Subsystem für Linux) auf.
- Es bietet eine integrierte Umgebung mit einer Benutzeroberfläche und ermöglicht das Ausführen sowohl von Linux- als
  auch von Windows-Containern.

## Linux

- Docker auf Linux wird als Docker Engine bezeichnet.
- Die Installation erfolgt meist über die Paketverwaltung des jeweiligen Linux-Systems (z.B. apt für Ubuntu, yum für
  CentOS).
- Docker Engine auf Linux bietet eine eher traditionelle, CLI-basierte Erfahrung und ist eng mit dem Linux-Kernel und
  seinen Funktionen verknüpft.

### **Hinweis für Docker unter Linux**

#### Warum `sudo` benötigt wird:

Auf Linux-Systemen läuft der Docker-Daemon typischerweise mit Root-Privilegien, da er direkten Zugriff auf viele
Low-Level-Funktionen des Betriebssystems benötigt. Wenn ein Benutzer Docker-Befehle ausführt, interagiert er mit diesem
Daemon. Standardmäßig erfordert der Zugriff auf den Docker-Daemon Root-Berechtigungen, daher wird oft `sudo` vor
Docker-Befehlen verwendet, um diese Berechtigungen zu gewähren.

#### Umgehen der Notwendigkeit von `sudo`:

Die ständige Verwendung von `sudo` für Docker-Befehle kann umständlich sein und birgt Sicherheitsrisiken, wenn `sudo` zu
freizügig verwendet wird. Um dies zu umgehen, kann man den Benutzer zur Docker-Gruppe hinzufügen. Hier sind die
Schritte:

1. **Docker-Gruppe erstellen (falls noch nicht vorhanden):**
   ```bash
   sudo groupadd docker
   ```

2. **Aktuellen Benutzer zur Docker-Gruppe hinzufügen:**
   ```bash
   sudo usermod -aG docker $USER
   ```
   Ersetzen Sie `$USER` mit Ihrem Benutzernamen.

3. **Neustart oder Ab-/Anmeldung:**
   Damit die Änderungen wirksam werden, sollten Sie sich ab- und wieder anmelden oder den Computer neu starten.

4. **Überprüfen:**
   Führen Sie einen Docker-Befehl ohne `sudo` aus, z.B.:
   ```bash
   docker run hello-world
   ```
   Wenn keine Fehlermeldung bezüglich der Berechtigungen erscheint, war die Änderung erfolgreich.

#### Sicherheitshinweis:

Das Hinzufügen eines Benutzers zur Docker-Gruppe gewährt diesem Benutzer effektiv Root-Zugriff, da er nun Befehle mit
Docker ausführen kann, die Root-Berechtigungen erfordern. Dies sollte nur bei vertrauenswürdigen Benutzern und in
sicheren Umgebungen angewendet werden.

### **Docker Konfiguration**

#### `daemon.json` Datei in Docker auf Linux

Die `daemon.json` Datei in Docker ist eine Konfigurationsdatei für den Docker-Daemon auf **Linux-Systemen**. Sie
ermöglicht
es Benutzern, die Standardkonfiguration des Daemons anzupassen.

**Wo befindet sich die Datei?**

- Die `daemon.json` Datei befindet sich üblicherweise unter `/etc/docker/daemon.json`. Falls sie nicht existiert, kann
  sie manuell erstellt werden.

**Was kann konfiguriert werden?**

- In dieser Datei können verschiedene Einstellungen vorgenommen werden, wie z.B. die Konfiguration des Logging, die
  Festlegung von Speicherlimits, die Definition von Registry-Mirrors, die Konfiguration von Netzwerkeinstellungen und
  vieles mehr.

**Beispiel:**
Ein einfaches Beispiel für eine `daemon.json` Datei könnte so aussehen:

```json
{
  "debug": true,
  "log-level": "info",
  "storage-driver": "overlay2"
}
```

Dieses Beispiel aktiviert den Debug-Modus, setzt das Log-Level auf "info" und definiert "overlay2" als den
Storage-Driver.

**Änderungen anwenden:**

- Nachdem Änderungen an der `daemon.json` Datei vorgenommen wurden, muss der Docker-Daemon neu gestartet werden, damit
  die Änderungen wirksam werden:
  ```bash
  sudo systemctl restart docker
  ```
#### Zusammenfassung

- Die `daemon.json` Datei auf Linux und die Einstellungen in Docker Desktop auf Windows und Mac bieten flexible
  Möglichkeiten, die Docker-Umgebung an spezifische Bedürfnisse anzupassen.
- Während `daemon.json` eine manuelle Bearbeitung der Konfigurationsdatei erfordert, bietet Docker Desktop eine
  benutzerfreundliche Schnittstelle für die Konfiguration.
- Es ist wichtig, die Auswirkungen von Änderungen an der Konfiguration zu verstehen, insbesondere in Bezug auf
  Systemressourcen und Netzwerksicherheit.
- Anpassung von Speicher, Netzwerk und anderen Ressourceneinstellungen.

### Starten und Stoppen der Docker Engine auf Linux

#### Starten der Docker Engine

- **Systemd (die meisten modernen Distributionen):**
  ```bash
  sudo systemctl start docker
  ```
- **Ältere Systeme mit init.d:**
  ```bash
  sudo /etc/init.d/docker start
  ```

#### Stoppen der Docker Engine

- **Systemd:**
  ```bash
  sudo systemctl stop docker
  ```
- **Init.d:**
  ```bash
  sudo /etc/init.d/docker stop
  ```

