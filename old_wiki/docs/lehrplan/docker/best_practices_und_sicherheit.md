# Exkurs: Best Practices und Sicherheit in Docker

In diesem Kapitel konzentrieren wir uns auf Best Practices und Sicherheitsaspekte beim Umgang mit Docker. Diese
Richtlinien sind entscheidend, um die Integrität und Sicherheit Ihrer Docker-Container und -Images zu gewährleisten und
gleichzeitig eine effiziente und wartbare Umgebung zu schaffen.

## Best Practices in Docker

**Verwendung offizieller Images:** Bevorzugen Sie offizielle Docker-Images oder solche von vertrauenswürdigen Quellen, um Sicherheitsrisiken zu
minimieren.

**Minimale Images:**
Verwenden Sie minimale Basis-Images
wie [python:3.12.0-slim]( dockerfile_und_docker_compose#beispiel-eines-dockerfiles ), um die Angriffsfläche
zu reduzieren. Je weniger
im Image enthalten
ist, desto geringer ist das Risiko.

**Image-Größe Reduzieren:**
Entfernen Sie unnötige Dateien und Abhängigkeiten, um die Image-Größe zu reduzieren. Dies verbessert die Startzeit
und Effizienz.

**Effizientes Layering:**
Organisieren Sie Anweisungen im Dockerfile effizient, um die Anzahl der Schichten zu reduzieren und Caching zu
optimieren.

**Dockerfile Sicherheit:**
Vermeiden Sie das Einbetten sensibler Daten wie Passwörter im Dockerfile. Nutzen Sie stattdessen
Umgebungsvariablen oder Secrets.

## Sicherheitsaspekte in Docker

**Container Isolation:**
Stellen Sie sicher, dass Container voneinander isoliert sind und nur auf benötigte Ressourcen Zugriff haben.

**Netzwerksicherheit:**
Konfigurieren Sie Netzwerke sorgfältig, um unerwünschten Datenverkehr zu verhindern. Verwenden Sie Firewall-Regeln
und Netzwerksegmentierung.

**Volume- und Datenmanagement:**
Verwenden Sie Volumes für persistente Daten und achten Sie darauf, dass sensible Daten sicher gespeichert werden.

**Regelmäßige Updates:**
Halten Sie Ihre Docker-Engine und Container-Images aktuell, um von Sicherheitspatches und Updates zu profitieren.

**Nicht als Root laufen:**
Vermeiden Sie es, Anwendungen innerhalb von Containern als Root-Benutzer auszuführen, um das Risiko von
Privilegieneskalation zu minimieren.


## Praktisches Beispiel

Um die Sicherheit zu erhöhen, ist es gängige Praxis, Benutzer anzulegen.
Das folgende Dockerfile Beispiel nutzt Linux Befehle, um im Container einen Benutzer anzulegen. Dies sichert den
Container ab, da der normale und standardmäßig aktive root-Zugang damit geschlossen ist.

`python:3.12-slim` ist dabei ein einfaches Linux image ohne weiter Funktionalität.

Der `adduser` Befehl ist ein für alpine Linux gültiger Befehl, um Benutzer anzulegen. Das kann von Distribution zu
Distribution anders sein. Hier gilt die Dokumentation des betreffenden Systems.

Der `user` Befehl legt den akzeptierten Benutzer für das System fest.

**Dockerfile für ein minimales Image:**

```Dockerfile
FROM python:3.12.0-slim
RUN adduser -S meinapp
USER meinapp
COPY . /app
WORKDIR /app
CMD ["./meineapp"]
```
