# Exkurs: Interaktion mit Docker-Containern

## 1. Starten und Stoppen von Containern

**Starten eines Containers:**

```bash
docker run -d --name mein-container hello-world-python
```

Das Image haben wir [hier](images_erstellen) erstellt.

Dieser Befehl startet einen Container namens `mein-container` im Hintergrund (`-d`, englisch "detached") basierend auf
dem `hello-world-python` Image. Hier sind einige wichtige Punkte zum **detached Modus**:

1. **Hintergrundausführung:** Der Container läuft im Hintergrund, d.h. Sie erhalten sofort die Kontrolle über die
   Kommandozeile zurück, nachdem der Container gestartet wurde.

2. **Keine Ausgabe im Terminal:** Im detached Modus sehen Sie keine Ausgabe des Containers in Ihrem Terminal. Der
   Container läuft still im Hintergrund, es sei denn, Sie greifen explizit auf seine Logs zu.

3. **Zugriff auf Logs:** Obwohl der Container im Hintergrund läuft und keine Ausgabe direkt im Terminal anzeigt, können
   Sie die Logs des Containers jederzeit mit dem Befehl `docker logs [CONTAINER_ID oder NAME]` oder über Docker
   Desktop einsehen, wie [hier](fehlersuche_mit_container_logs) beschrieben.

4. **Verwendung:** Der detached Modus wird häufig verwendet, wenn Sie einen Container als langlaufenden Dienst oder
   Prozess ausführen möchten, ohne dass dieser Ihre Terminal-Sitzung blockiert. Dies ist besonders nützlich in
   Produktionsumgebungen oder beim Ausführen von Anwendungen, die als Hintergrunddienste fungieren sollen.

**Stoppen eines Containers:**

```bash
docker stop mein-container
```

Dieser Befehl stoppt den Container `mein-container`.

## 2. Zugriff auf laufende Container

**Interaktiver Modus:**
Mit dem folgenden Befehl werden Sie in die Bash-Shell des Containers versetzt, wo Sie Befehle ausführen und
mit dem Container interagieren können, als ob Sie direkt in ihm arbeiten würden.

```bash
docker exec -it mein-container bash
```

Mit diesem Befehl starten Sie eine interaktive Bash-Shell im Container `mein-container`.
Der Befehl `docker exec -it ...` wird verwendet, um in einem bereits laufenden Docker-Container interaktive Befehle
auszuführen. Dieser Befehl ist besonders nützlich, wenn Sie eine interaktive Shell innerhalb des Containers starten
möchten, um verschiedene Aufgaben auszuführen, wie z.B. das Überprüfen von Konfigurationen, das Ändern von Dateien
oder das Ausführen von Diensten innerhalb des Containers. Hier ist, was die einzelnen Optionen und Argumente bedeuten:

- `docker exec`: Dieser Befehl führt einen neuen Befehl in einem laufenden Container aus.
- `mein-container` ist der Name oder die ID Ihres laufenden Containers.
- `bash` ist der Befehl, den Sie im Container ausführen möchten, in diesem Fall das Starten einer Bash-Shell.
- `-i` (oder `--interactive`): Hält den STDIN offen, auch wenn er nicht an das Terminal angeschlossen ist. Dies
  ermöglicht die interaktive Eingabe in den Container.
- `-t` (oder `--tty`): Weist Docker an, ein Pseudo-TTY zuzuweisen, das heißt, es simuliert ein Terminal, ähnlich wie
  wenn Sie eine Shell-Sitzung in einem normalen Terminal verwenden. Dies ermöglicht eine formatierte Ausgabe und die
  Möglichkeit, interaktive Anwendungen zu nutzen.

Zusammen ermöglichen `-it` die Interaktivität mit dem Container, was bedeutet, dass Sie Befehle eingeben und die
Ausgaben so sehen können, als ob Sie direkt in einer Terminal-Sitzung auf dem Container arbeiten würden.

Wenn Sie fertig sind, können Sie `exit` eingeben, um die Shell zu verlassen und zum Host-Terminal zurückzukehren.

### Zusammenfassung

Der Befehl `docker exec -it` ist ein mächtiges Werkzeug in der Docker-Toolbox, das es Ihnen ermöglicht, interaktiv mit
Ihren laufenden Containern zu arbeiten. Es ist besonders nützlich für die Fehlerbehebung, schnelle Änderungen oder
einfach nur, um den Zustand und die Konfiguration von Diensten innerhalb des Containers zu überprüfen.

## 3. Datenmanagement und -austausch

Die folgenden Kommandos beziehen sich auf die Arbeit mit einem Container.

**Kopieren von Dateien:**

```bash
docker cp host_datei.txt mein-container:/container_datei.txt
```

Kopiert `host_datei.txt` vom Host-System in den Container `mein-container`.
**Persistente Daten mit Volumes:**

```bash
docker run -d --name mein-container -v mein-volume:/app hello-world-python
```

In diesem Befehl:

- `-d` ist der Schalter für den oben beschriebenen detached mode.
- `--name mein-container` gibt dem container seinen Namen.
- `-v mein-volume:/app` sagt Docker, dass es das Volume `mein-volume` an den Pfad `/app` im Container binden soll.
  Ein Volume ist ein dedizierter Speicherraum für den Container. Er wird hier automatisch ertellt.
  Näheres zu Volumes findet sich [hier](wo_und_wie_docker_container_daten_speichern.md).
- `hello-world-python` ist das Image, aus dem der Container erstellt wird.

## 4. Überwachung und Management

**Container-Status überprüfen:**

```bash
docker ps
```

Zeigt alle laufenden Container an.

**Ressourcennutzung überwachen:**

```bash
docker stats
```

Zeigt Echtzeitinformationen zur Ressourcennutzung aller Container.

## 5. Container-Updates und -Änderungen

**Container aktualisieren:**

```bash
# Stoppen des alten Containers
docker stop mein-container
# Entfernen des alten Containers
docker rm mein-container
# Starten eines neuen Containers mit dem aktualisierten Image
docker run -d --name mein-container hello-world-python:neue-version
```

Wenn ein Image erstellt wird, sollte ein Tag (hier 'neue-version') als Versionsbezeichnung hintere einem Doppelpunkt
angegeben werden. So können Tags wie `:latest` dafür sorgen, dass immer das aktuellste Image verwendet wird.

### Aufgabe: Information 🌶️🌶️

1. Nutzen Sie die Kommandozeile, um sich die laufenden Container aufzulisten.
2. Suchen Sie den Kommandozeilenbefehl über `docker --help`, um sich die vorhandenen Images aufzulisten.

### Aufgabe: Interaktion mit Docker-Containern 🌶️🌶️

Üben sie die Interaktion mit Containern. Trainieren sie beide grundlegenden Arten der Interaktion: CLI und Desktop.

- Starten und Stoppen sie beliebige Container.
- Löschen sie Container.
- Öffnen sie die Bash auf dem Container und lassen sie sich die Verzeichnisstruktur anzeigen.
- Speichern sie eine Datei im Container.
- Wählen sie einen für sie interessantes Image auf Docker Hub und starten sie einen Container damit.
- Schauen sie sich die Arbeit des Containers an, indem sie ihn in Docker Desktop anklicken und sich Logs und andere
  Reiter im folgenden Dialog ansehen.