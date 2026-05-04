# Deployment eines Docker Containers

Zwar können wir Docker Container lokal auf unserem Rechner ausführen, aber in der Praxis werden wir sie meistens auf einem Server oder in der Cloud ausführen. In diesem Abschnitt werden wir uns mit dem Deployment von Docker Containern auf verschiedenen Plattformen befassen.

## Deployment in Azure

Azure bietet mehrere Services für das Deployment von Docker Containern. 

Wir schauen und das Deployment über Azure Container Apps an. 

### Azure Container Apps

Für das Deployment suchen wir uns zunächst eine Beispielanwendung aus. Azure stellt in seinem Tutorial zu Container Apps die folgende Beispielanwendung zur Verfügung:

```bash
git clone https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart.git
```

Auf der Ebene des Ordners müssen wir nun eine Datei mit dem Namen `Dockerfile` erstellen. In dieser Datei definieren wir, wie unser Container gebaut werden soll. Hier ein Beispiel für eine Flask Anwendung:

```Dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "app:app"]
```

Um Ressourcen zu sparen, erstellen wir außerdem eine .dockerignore Datei, in der wir Dateien und Ordner definieren, die nicht in den Container kopiert werden sollen:

```bash
.git*
**/*.pyc
.venv/
```

Bevor wir den Container deployen, fügen wir als letztes noch gunicorn ein. Gunicorn ist ein Server, welcher Python Anwendungen ausführen kann. Der folgenden Inhalt wird in der Datei `gunicorn.conf.py` gespeichert:

```py
# Gunicorn configuration file
import multiprocessing

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

bind = "0.0.0.0:50505"

workers = (multiprocessing.cpu_count() * 2) + 1
threads = workers

timeout = 120
```

Nun können wir das Image erstellen:

```bash
docker build --tag flask-demo .
```

Denkt dran, dass dieser Schritt aufgrund der Netzwerkeinschränkungen bei Volkswagen problematisch sein kann.

Anschließend testen wir den Docker Container lokal:

```bash
docker run --detach --publish 5000:50505 flask-demo
```

Nun können wir die Anwendung unter `http://localhost:5000` aufrufen.

Um die Anwendung in Azure zu deployen, müssen wir uns zunächst in Azure anmelden:

```bash
az login
```

Anschließend erstellen wir eine neue eine Container App:

```bash
az containerapp up --resource-group <DEINE-RESSOURCE-GROUP> --name web-aca-app --ingress external --target-port 50505 --source .
```


Nach dem erfolgreichen erstellen wird uns die URL der Anwendung angezeigt. Diese können wir nun im Browser aufrufen.

Um die ressourcegruppe wieder zu löschen, können wir den folgenden Befehl verwenden:

```bash
az group delete --name <DEINE-RESSOURCE-GROUP>
```