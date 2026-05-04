# Exkurs: Images verwalten

[120 min]

Nachdem Sie ein Docker-Image erstellt haben, ist der nächste Schritt oft, dieses Image in einem Repository zu sichern.
Dies ermöglicht es Ihnen, das Image zu teilen, es auf verschiedenen Maschinen zu verwenden und eine Versionierung Ihrer
Container-Umgebungen zu haben.

## Warum Docker-Images in Repositories speichern?

**Versionierung und Wiederverwendbarkeit:**
Repositories ermöglichen es Ihnen, verschiedene Versionen eines Images zu
speichern und bei Bedarf darauf zurückzugreifen.

**Kollaboration:**
Durch das Hochladen von Images in ein Repository können Teams gemeinsam an Anwendungen arbeiten
und sicherstellen, dass jeder auf die gleiche Umgebung zugreift.

**Deployment:**
Images aus Repositories können leicht auf Produktions- oder Entwicklungsservern bereitgestellt
werden.

## Schritte zum Sichern eines Docker-Images in einem Repository

**Wählen eines Docker-Repositorys:**
Das bekannteste Docker-Repository ist Docker Hub, aber es gibt auch andere Optionen wie AWS Elastic Container
Registry (ECR), Google Container Registry (GCR) oder private Repositories.

**Taggen des Docker-Images:**
Bevor Sie ein Image in ein Repository hochladen, sollten Sie es taggen. Dies gibt dem Image einen Namen und
optional eine Version. Befehl zum Taggen eines Images:

```bash
docker tag hello-world-python yourusername/hello-world-python:version
```

Ersetzen Sie `yourusername` mit Ihrem Benutzernamen im Repository und `version` mit dem gewünschten Versions-Tag.

**Anmelden am Docker-Repository:**
Um Images hochzuladen, müssen Sie sich bei dem Repository anmelden.
Befehl zum Anmelden bei Docker Hub:

```bash
docker login
```

Folgen Sie den Anweisungen, um Ihre Anmeldeinformationen einzugeben.

**Hochladen (Push) des Images:**
Nachdem das Image getaggt und Sie angemeldet sind, können Sie es in das Repository hochladen.
Befehl zum Hochladen des Images:

```bash
docker push yourusername/hello-world-python:version
```

**Überprüfen des Images im Repository:**
Nach dem Hochladen können Sie sich in Ihrem Repository anmelden und überprüfen, ob das Image erfolgreich
hochgeladen wurde.

## Best Practices

- **Konsistente Tagging-Konventionen:** Verwenden Sie klare und konsistente Tags für Ihre Images, um die Verwaltung zu
  erleichtern.
- **Sicherheit:** Achten Sie darauf, keine sensiblen Daten in Ihren Images zu speichern, bevor Sie diese hochladen.
- **Regelmäßige Updates:** Halten Sie Ihre Images im Repository aktuell, um von Sicherheitsupdates und neuen Features zu
  profitieren.

### **Aufgabe: Erzeugung einer leeren Docker Umgebung. 🌶️️🌶️️.**

Löschen Sie sämtliche Container und Images.

### **Aufgabe: Mit Docker Hub arbeiten 🌶️️🌶️️.️**

Melden Sie sich im Repository an und ab. Laden Sie das Image mit pull.

## Erstellung eines privaten Docker-Repositories

Neben der Nutzung öffentlicher Repositories wie Docker Hub kann es für Teams und Organisationen sinnvoll sein, ein
privates Docker-Repository zu erstellen. Ein privates Repository bietet mehr Kontrolle über den Zugriff und die
Sicherheit Ihrer Docker-Images. Hier erfahren Sie, wie Sie ein privates Docker-Repository einrichten können.

### Vorteile eines privaten Repositories

- **Sicherheit:** Kontrollieren Sie, wer Zugriff auf Ihre Docker-Images hat.
- **Datenschutz:** Ideal für Images, die sensible oder proprietäre Informationen enthalten.
- **Anpassung:** Passen Sie das Repository an Ihre spezifischen Bedürfnisse und Workflows an.

### Optionen für private Docker-Repositories

- **Docker Hub Private Repositories:**
    - Docker Hub bietet die Möglichkeit, private Repositories zu erstellen, die nicht öffentlich zugänglich sind.
    - Einfach zu verwenden, aber es gibt Kosten für private Repositories auf Docker Hub.

- **Selbst gehostete Repositories:**
    - Sie können Ihr eigenes Docker-Registry auf einem Server hosten.
    - Docker bietet eine offizielle Registry-Software namens "Docker Registry", die Sie selbst hosten können.

### Exkurs: Schritte zur Einrichtung eines selbst gehosteten Docker-Repositories

#### Vorbereitung:

- Stellen Sie sicher, dass Sie einen Server haben, auf dem Sie die Registry hosten können.
- Installieren Sie Docker auf diesem Server.

#### Starten der Docker Registry:

- Führen Sie den folgenden Befehl aus, um eine Docker Registry als Container zu starten:

```bash
docker run -d -p 5000:5000 --restart=always --name registry myrepo:2
```

- Dies startet eine Docker Registry (
  mit [Port Mapping](kommunikation_zwischen_und_mit_docker_containern.md#netzwerkkommunikation-und-port-weiterleitung)),
  die auf dem Host Port 5000 lauscht und die Anfragen an ihren internen Pot 5000 weitergibt ( `-p` Option).
- Die registry hat in diesem Fall den Namen `myrepo` mit dem tag `2` (Tags haben oft die Bedeutung von Versionsnummern).
- Die registry läuft wie ein Container im `detached` Modus, also unabhängig von der Konsole( `-d` Option).
- Der Befehl `restart=always` sorgt dafür, dass der Container automatisch neu gestartet wird,
  wenn er aus irgendeinem Grund beendet wird. Dies schließt Fälle ein, in denen der Container aufgrund eines Fehlers
  oder durch manuelle Beendigung gestoppt wird.

#### Taggen und Pushen eines Images zur privaten Registry:

Taggen Sie Ihr lokales Image für die private Registry:

```bash
docker tag hello-world-python localhost:5000/hello-world-python
```

Pushen Sie das Image zur privaten Registry:

```bash
docker push localhost:5000/hello-world-python
```

#### Zugriff auf das private Repository:

Um auf Images aus der privaten Registry zuzugreifen, verwenden Sie den vollständigen Pfad in Ihren
Docker-Befehlen, z.B. `localhost:5000/hello-world-python`.

### Sicherheitsaspekte

**HTTPS:**
Es wird empfohlen, Ihre Registry mit HTTPS zu sichern, um die Übertragung von Images zu schützen.

**Authentifizierung:**
Authentifizierungsmechanismen sollten eingerichtet werden, um den Zugriff auf Ihre Registry zu kontrollieren. Dies
sprengt aber den Rahmen dieses Kurses.

### **Aufgabe: privates repository. 🌶️️🌶️️.**

Laden Sie ein Image aus deinem privaten Repository.

### **Aufgabe: privates repository. 🌶️️🌶️️.**

Finden Sie heraus, wie man alle Container und Images löscht.
