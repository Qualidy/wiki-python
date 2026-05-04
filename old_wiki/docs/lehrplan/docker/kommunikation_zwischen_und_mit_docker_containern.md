# Kommunikation zwischen und mit Docker Containern

In diesem Kapitel setzen wir und mit der Kommunikation von Docker Containern untereinander und mit der Außenwelt
auseinander.

Docker-Container kommunizieren mit ihrer Umgebung über mehrere Techniken, um Isolation zu gewährleisten und gleichzeitig
notwendige Interaktionen zu ermöglichen.

Docker-Container kommunizieren im Allgemeinen über Netzwerke (TCP/IP) untereinander und mit der Außenwelt.

Um die Dockercontainer voneinander Unterscheiden zu können, müssen sie mit einer Nummer versehen werden.
Diese Nummer bezeichnet man in der Netzwerktechnik als **Port**. Man kann es sich bildlich vorstellen, wie eine
Hausnummer bei der Post.

**Kommunikation zwischen den Container**:
Werden mehrere Container gleichzeitig betrieben und sollen sie miteinander
kommunizieren können, so müssen sie die Ports der jeweils anderen Container genau kennen.

**Kommunikation von Containern mit dem Hostsystem**:
Um jetzt einen Container mit der Außenwelt (dem Hostsystem) zu verbinden, muss ein Port veröffentlicht werden

```mermaid
graph LR
    subgraph CN[Container Netzwerk]
        subgraph C1["Container 1"]
            C1Port([Port 5050]) <--> C1A[Anwendung 1]
        end

        subgraph C2["Container 2"]
            C2Port([Port 5060]) <--> C2A[Anwendung 2]
        end

        subgraph C3["Container 3"]
            C3Port([Port 5070]) <--> C3A[Anwendung 3]
        end
    end

    C1Port <-..-> C2Port <-..-> C3Port <-..-> C1Port
    HPort([Host Port<br/>Port 8000]) <-. Portmapping .-> C1Port
```

Starte Container 1 mit dem Portmapping von 8000 zu 5050.

```bash
docker run -d -p 8000:5050 container_1
```

Container 2 und 3 werden mit den folgenden Befehlen gestartet:

```bash
docker run -d container_2
docker run -d container_3
```

Und was ist nun mit den Ports `5060` und `5070` von den Anwendungen 2 und 3?
Diese müssen nicht im Dockerfile oder so angelegt werden, sondern werden in den Anwendungen selbst definiert
und hinterlegt.

D.h. bei Anwendung 1 gibt es Code, der wie folgt aussehen könnte, um sich selbst auf Port 5050 ansprechbar zu machen:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
```

Andererseits gibt es in Anwendung 1 dann auch Code, um mit anderen Anwendungen zu kommunizieren,
hier die Definition für die Datenbank:

```python
# Configure the SQLAlchemy part of the app instance
username = 'sa'
password = 'Sql12345'
host = 'sql-server'  # or the IP address of your SQL Server
port = '1433'  # default SQL Server port
database = 'Zeiterfassung'
driver = 'ODBC Driver 18 for SQL Server'

SQLALCHEMY_DATABASE_URI \
    = f'mssql+pyodbc://{username}:{password}@{host}:{port}/{database}?driver={driver}&TrustServerCertificate=yes'

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to suppress a warning
```

Ähnliche Codes wären dann auch in Anwendung 2 und 3 vorhanden.

### Exkurs: Netzwerktypen in Docker

Docker bietet verschiedene Netzwerktypen an, um die Kommunikation zu realisieren.

| Netzwerktyp | Erklärung                                                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bridge`    | Standardnetzwerktyp für Docker-Container. Jeder Container in diesem Netzwerk erhält eine eigene IP-Adresse, was die interne Kommunikation ermöglicht. |
| `host`      | Container teilen sich den Netzwerk-Stack des Hosts. Nützlich für Dienste, die auf dem Host-Netzwerk sichtbar sein müssen.                             |
| `overlay`   | Ermöglicht die Netzwerkkommunikation zwischen Containern auf verschiedenen Docker-Hosts, typisch in Docker-Swarm-Umgebungen.                          |

### Beispiel

Wir werden mit `docker compose` ein Werkzeug kennenlernen, mit dem mehrere Container gestartet werden können.
Dort werden wir dann auch ein ausführliches Beispiel für die Kommunikation von Docker Containern und der Außenwelt
betrachten.

### Vom Nutzer definierte Netzwerke

In dem obigen Beispiel haben wir von Docker automatisch ein Netzwerk anlegen lassen. Wir können jedoch auch
zunächst ein eigenes Netzwerk anlegen und dann Container zu diesem hinzufügen:

**Erstellen eines Netzwerks:**

```bash
docker network create mein-netzwerk
```

Erstellt ein benutzerdefiniertes Netzwerk namens `mein-netzwerk`.

**Starten von Containern in diesem Netzwerk:**

```bash
docker run -d --name mein-container --network mein-netzwerk hello-world-python
```

Startet einen Container im `mein-netzwerk`. Container innerhalb desselben Netzwerks können miteinander kommunizieren,
während sie von anderen Netzwerken isoliert sind.

### Mehrere Netzwerke

Wir können nun auch mehrere Netzwerke definieren und Container so in verschiedenen Netzwerken separieren.

```mermaid
graph LR
    subgraph Docker System
        subgraph Netzwerk_A [Netzwerk A]
            A[Container A1] <--> PA([Port 5001]) <-.-> PB([Port 5002]) <--> B[Container A2]
        end
        subgraph Netzwerk_B [Netzwerk B]
            C[Container B1] <--> PC([Port 5001]) <-.-> PD([Port 5002]) <--> D[Container B2]
        end
    end

    Netzwerk_A -. Keine direkte Kommunikation .-x Netzwerk_B
```

Durch die Verwendung von benutzerdefinierten Netzwerken können Sie sicherstellen, dass nur die gewünschten Container
miteinander kommunizieren können, während andere Container oder Netzwerke isoliert bleiben. Dies ist besonders wichtig
für die Sicherheit, das Netzwerkmanagement und die Architektur von Microservices.

## Exkurs: Nginx

nginx ist ein Programm, dass als Webserver fungiert. Ein anderer, viel umfangreicherer Webserver ist z. B. Apache.

Ein Webserver nimmt zum Beispiel HTTP-Anfragen entgegen und leitet sie an geeignete Empfänger weiter. Damit er auch
weiß, was er tut, muss er konfiguriert werden.

```mermaid
graph TD

subgraph Docker System
subgraph CN["Container NGINX"]
Conf[[<b>NGINX Config:</b><br/><span style="color:#f54242">app_security = 5000</span><br/> app_rechnung = 6000<br/> app_datenbank = 7000]]
end
PN([Port 80]) <--> CN
PA([Port 5000]) <--> CA["Container<br/>app_security"]
PB([Port 6000]) <--> CB["Container<br/>app_rechnung"]
PC([Port 7000]) <--> CC["Container<br/>app_datenbank"]

end

CN <-->|Weiterleitung|PA


HPort([öffentlicher Host Port<br/>Port 80]) <-->|Portmapping|PN

Client <-->|localhost/app_security|HPort

style CN fill: #ECECFF, stroke: #9370DB
style Conf fill: #e8dcbc , stroke: #f7be20

```
