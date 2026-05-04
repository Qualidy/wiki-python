# Exkurs: Planen von Cloud Apps

[60 min]

Cloud-native ist ein Ansatz zur Entwicklung und Ausführung von Anwendungen, der die Vorteile der Cloud-Computing-Delivery-Modelle voll ausschöpft. Cloud-native Anwendungen sind so konzipiert, dass sie in einer elastischen und automatisierten Cloud-Umgebung laufen, wodurch sie robust, skalierbar und agil sind.

## Microservices

Eine architektonische Methode, bei der eine Anwendung als Sammlung kleiner Dienste entwickelt wird, die unabhängig voneinander implementiert, bereitgestellt und skaliert werden können.

Speziell auch die **Serverlose** Architektur spiel eine große Bedeutung im Bezug auf Microservices. Hierbei müssen sich die Entwickler nicht um die Serververwaltung kümmern. Stattdessen werden Ressourcen auf Anfrage bereitgestellt und verwaltet.

```python
import json

def lambda_handler(event, context):
    # Verarbeitungslogik hier
    return {
        'statusCode': 200,
        'body': json.dumps('Datei verarbeitet!')
    }
```

## Container

Leichtgewichtige, verpackte Softwareeinheiten, die alle erforderlichen Code- und Abhängigkeiten enthalten, um konsistente, effiziente und schnelle Bereitstellungen zu ermöglichen.

Über Container können schnell einzelne Services konfiguriert und deployed werden. Hierbei ist die Reproduzierbarkeit elementar. Aus diesem Grund werden Anforderungen und Anweisungen über z.B. ein `Dockerfile` definiert.

```bash
FROM python:3.12
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
```

## Orchestrierung

Automatisiertes Management von Container-Workloads und Services, um ihre Verfügbarkeit zu gewährleisten.

Auch bei der Orchestrierung ist die Automatisierung des Deployments, Managements und der Skalierung von Containern im Fokus. Hierbei werden so genannte `Manifest`-Dateien verwendet.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        image: webapp:latest
        ports:
        - containerPort: 80
```

## Cloud-native Entwicklungswerkzeuge

Gerade für die Enwticklung in der Cloud haben sich neue Werkzeuge als elementar herausgestellt um die wachsende Komplexität handhaben zu können.

- **Helm:** Ein Paketmanager für Kubernetes, der das Verwalten von Kubernetes-Anwendungen erleichtert.
- **Terraform:** Ein Infrastructure-as-Code-Tool für das Erstellen, Ändern und Versionieren von Infrastruktur sicher und effizient.
- **Ansible:** Ein Automatisierungstool für Konfigurationsmanagement und Anwendungsdeployment.

## Cloud Security

Bei der Planung von Cloud Applikationen muss besonderes Augenmerk auf die Sicherheit gelegt werden.

### Sicherheitsprinzipien in der Cloud

- **Least Privilege:** Beschränkung der Zugriffsrechte auf das Notwendigste.

- **Defense in Depth:** Mehrschichtige Sicherheitsmaßnahmen.

- **Data Encryption:** Verschlüsselung von Daten in Ruhe und während der Übertragung.

- **Container-Sicherheit:** Sicherstellen, dass Container-Images frei von Schwachstellen sind.

### Identitäts- und Zugriffsmanagement

- **IAM (Identity and Access Management):** Verwaltung von Nutzeridentitäten und Zugriffsberechtigungen.

- **Authentifizierung und Autorisierung:** Einsatz von Protokollen wie OAuth 2.0 und OpenID Connect.