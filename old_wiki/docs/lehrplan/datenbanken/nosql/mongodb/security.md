# Exkurs: Sicherheit in MongoDB
[20 min]

Da unsere Datenbanken häufig über das Internet erreichbar sind und teilweise sensible Daten beinhalten, ist es wichtig, dass wir uns mit dem Thema Sicherheit auseinandersetzen. In diesem Abschnitt werden wir uns mit den Sicherheitsfunktionen von MongoDB beschäftigen und einige Sicherheitsmaßnahmen kennenlernen, die wir ergreifen können, um unsere Datenbanken zu schützen.

Ein Teil der im Folgenden vorgestellten Maßnahme ändert die Konfigurationsdatei `mongod.conf`. Diese Datei befindet sich in der Regel im Verzeichnis `/etc/mongod.conf`. Die Konfigurationsdatei enthält die Konfigurationsoptionen für den MongoDB-Server und kann bei einer lokalen installation auch über die Kommandozeile angepasst werden. Dazu können wir den Befehl `mongod` verwenden. Die Konfigurationsoptionen können wir über die Option `--config` angeben. Da wir uns für die Verwednung von MongoDB über Docker entschieden haben, müssten wir die Datei in dem Container anpassen. Glücklicherweis habe wir beretis in dem Docker Abschnitt gelernt, wie wir Bind Mounts verwenden können, um Dateien aus dem Hostsystem in den Container zu mounten. Wir können also die Konfigurationsdatei in dem Hostsystem anpassen und dann über ein Bind Mount in den Container mounten. In diesem Schritt werden wir auch gleich eine Verknüpfung zu den Logging Dateien herstellen. Unser verwendetes Docker-Compose File könnte dann wie folgt aussehen:

```yaml
name: mongo-db
networks:
  mongodb_network:
    name: mongodb_network_localhost

services:
  mongodb:
    image: mongodb/mongodb-enterprise-server:latest
    env_file:
      - .env
    volumes:
      - ./mongod.conf:/etc/mongod.conf
      - ./mongodb-logs:/var/log/mongodb
      - my_volume:/data/db
    ports:
      - ${MONGODB_PORT}:${MONGODB_PORT} # HOST_PORT : CONTAINER_PORT
    networks:
      - mongodb_network
    #environment:
    #  - MONGO_INITDB_ROOT_USERNAME=value
    #  - MONGO_INITDB_ROOT_PASSWORD=pass12345
    command:
        - '-f'
        - '/etc/mongod.conf'
volumes:
  my_volume:
    name: my_local_volume_mdb
```

Zusätzlich sollten wir einen Ordner `mongodb-logs` erstellen, in dem die Log Dateien gespeichert werden können. Dieser Ordner wird dann ebenfalls in den Container gemountet. In der .env Datei können wir dann die Konfigurationsoptionen für den MongoDB Server angeben. 

```yaml
# Settings for mongodb
MONGODB_INITDB_ROOT_USERNAME=root
MONGODB_INITDB_ROOT_PASSWORD=pass12345
MONGODB_PORT=27017
MONGODB_HOST=localhost
MONGODB_NAME=fakultaet73
```

## Authentifizierung
[10 min]

Über eine authentifizierung können wir bereits eine erste, effektive Sicherheitsmaßnahme ergreifen. Durch die Implementierung von robusten Authentifizierungsmaßnahmen können wir sicherstellen, dass nur autorisierte Benutzer auf die Datenbank zugreifen und Aktionen durchführen können. Dies kann durch das anpassen der datei mongod.conf erreicht werden.

```yaml
# Konfigurationsdatei (mongod.conf)
security:
    authorization: enabled
```


Zusätzlich können wir die Berechtigungen von Benutzern einschränken. Das Anlegen von neuen Benutzern beispielsweise ist eine Admin Funktion uns sollte möglichwerweise nicht für jeden Nutzer möglich sein. Einen neuen Benutzer mit der Rolle `readWrite` können wir wie folgt anlegen:

```bash
// Beispiel für die Rollenvergabe
use admin
db.createUser({
  user: "deinBenutzername",
  pwd: "deinPasswort",
  roles: ["readWrite"]
})
```

Wir können sowohl vordefinierte Rollen verwenden, als auch eigene Rollen definieren. 

```bash
use admin
db.createRole({
  role: "deineBenutzerdefinierteRolle",
  privileges: [
    { resource: { db: "deineDatenbank", collection: "" }, actions: ["find", "insert", "update"] }
  ],
  roles: []
})
```

Die Rollen können wir dann den Benutzern zuweisen.

```bash
use admin
db.updateUser("deinBenutzername", {
  roles: [
    { role: "deineBenutzerdefinierteRolle", db: "deineDatenbank" }
  ]
})
```

## Verschlüsselung
[5 min]

Um die Daten in der Datenbank zu verschlüsseln, können wir TLS/SSL verwenden. Dies ist eine Möglichkeit, die Daten sowohl im Ruhezustand als auch während der Übertragung zu verschlüsseln. In cloud Umgebungen wird die Verschlüsselung häufig bereits über die cloud Anbieter realisiert. 


## Auditing und Logging
[10 min]

Die Überwachung von Aktivitäten in der Datenbank ist eine weitere wichtige Sicherheitsmaßnahme. MongoDB bietet die Möglichkeit, die Überwachungsfunktionen zu aktivieren, um Aktivitäten zu protokollieren. Dies kann über die Konfigurationsdatei `mongod.conf` erreicht werden.

```yaml
# Konfigurationsdatei (mongod.conf)
auditLog:
  destination: file
  path: /var/log/mongodb/audit.log
```


Neben den aufgeführen Methoden gibt es noch weitere Sicherheitsmaßnahmen, die wir ergreifen können. Dazu gehören unter anderem die Begrenzung von Berechtigungen, der Schutz vor Injection-Angriffen, die Begrenzung von Netzwerkzugriffen und die regelmäßige Aktualisierung der Datenbank. Auch das Verwenden sicherer Passwörter und das regelmäßige Ändern von Passwörtern erhöht die Sicherheit.