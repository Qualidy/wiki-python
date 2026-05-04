# Docker für Entwickler

## it works on my machine!
Beim Entwickeln von komplexen Applikationen benutzt ein Entwickler meist Bibliotheken und Dienste wie Datenbanken oder Webserver. Im Optimalfall kann man beim Ausliefern auf das Zielsystem einfach das fertige Programm kopieren und ausführen.
In der Praxis ist das allerdings meist etwas komplizierter.

Stellen wir uns für einen Moment vor, dass wir eine Web App programmieren. Diese App braucht neben dem Source Code welchen wir schreiben auch noch eine Datenbank. Für dieses Beispiel sagen wir mal MariaDB. Das ganze soll letzten Endes auf einen Server gepackt werden.

Nehmen wir mal an, dass dieser vom Auftraggeber bereitgestellt werden soll. Da der Kunde seinen Server natürlich nicht aktuell hält, (denn warum auch?) läuft auf dem Server des Kunden Debian Linux 8. Da Debian 8 schon in 2020 keinen Update support mehr hatte, sind Versionen von MariaDB insofern verfügbar so veraltet dass sie ggf. nicht mehr mit unserer App funktionieren. Da der Kunde seine auf dem Server bereits laufenden Dienste nicht auf eine neue Version von Debian migrieren möchte, ist ein Update des Systems auch nicht denkbar.

Hier ist also das Problem:
Wir können beim Ausliefern nicht garantieren dass die Umgebung in der die App laufen soll unseren Anforderungen entspricht.

Das ist nicht nur bei veralteten Systemen so. Oft passiert es dass eine App eine bestimmte Konfiguration benötigt. Den Kunden zu bitten seinen Server aufgrund unserer Wünsche umzukonfigurieren ist meist inakzeptabel.

Was wäre also, wenn wir dem Kunden einfach zusammen mit unserer App ein komplett konfiguriertes Betriebssystem ausliefern? Alles was der Kunde nun tun müsste, wäre dieses maßgeschneiderte System in einer Art virtuellen Umgebung laufen zu lassen.

Genau das ist die Idee hinter Docker. Wir lösen das Problem der unbekannten Umgebung indem wir unsere eigene schaffen.
Um diese besagte Umgebung zu schaffen, muss lediglich eine Textdatei erstellt werden, welche die Installationsanweisungen für unser System beinhaltet. Diese Datei ist meist nicht länger als 10 Zeilen. Wir können dann Docker beauftragen dieses beschriebene System für uns innerhalb einer virtuellen Umgebung auf unserem Computer zu installieren. Des weiteren können wir damit beschreiben wie dieses System unsere App startet.


Da ich das gesamte System durch eine einzige kleine Datei beschreiben kann, ist es mir ein leichtes dieses System auszuliefern. Ich muss ja nur die Textdatei versenden, welche der Kunde bei sich installieren lassen kann. Insofern der Kunde ein mit Docker kompatibles System hat (Linux Kernel 3.10) passiert der rest automatisch.

Docker erlaubt es uns also ein maßgeschneidertes und vor allem reproduzierbares System zu schaffen. Dies kann das Ausliefern von Applikationen erheblich erleichtern und ich als Entwickler muss weniger Kompromisse bei der Entwicklung meiner App eingehen. Kann aber trotzdem die Lauffähigkeit meiner App quasi garantieren.


## Setup

@V: bei der installation bitte rausfinden ob docker-desktop mit installiert wird. Das müsste höchstwarscheinlich verhindert werden, da das innerhalb vom VW-Kontext eine Lizenz bräuchte.
`Commercial use of Docker Desktop at a company of more than 250 employees OR more than $10 million in annual revenue requires a paid subscription (Pro, Team, or Business).`

https://docs.docker.com/desktop/install/mac-install/

alternativ:

`$ brew install docker`
`$ brew install docker-buildx`


## Beispiel 0_basic_container
Das erste mitgelieferte Beispiel

(In den Ordner wechseln)

`$ docker build -t hello-world .`

`$ docker image ls`
```
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    a0e201548b22   7 weeks ago   7.37MB
```

`$ docker run hello-world`

## Beispiel 1_example_server


`$ docker build -t web .`
`$ docker run -p 42069:80 web`

@V: Kurze Erklärung zu ports allgemein? den Port von innerhalb des Containers (80) auf außerhalb umleiten (42069).


Webbrowser auf unter http://localhost:42069/index.html

## COPY vs. ADD vs. bind mount

Beide Befehle kopieren den Inhalt der lokal verfügbaren Datei oder des Verzeichnisses in das Dateisystem innerhalb eines Docker-Images.

In der offiziellen Dokumentation von Docker wird darauf hingewiesen, dass Benutzer immer COPY anstelle von ADD wählen sollten.

Von ADD wird in allen Fällen abgeraten, außer wenn man eine lokale komprimierte Datei extrahieren möchte. Zum Kopieren von Remote-Dateien ist der Befehl „run“ in Kombination mit „wget“ oder „curl“ sicherer und effizienter.


## Mount points (Volumes)
https://docs.docker.com/storage/bind-mounts/


@V Problemstellung: wenn man den Website-Inhalt ändern möchte, dann muss man den container neu bauen.
@V Lösung: mount points benutzen welche einen Ordner aus dem Host einbinden.

`$ docker build -t web .`
`$ docker run -p 42069:80 -v ./meine_website:/usr/share/nginx/html:ro web`


## Attached vs Detached

`$ docker run ...`
vs. 
`$ docker run -d ...`


### Attached
sinnvoll für:
 - den command output direkt sehen
 - debugging des containers
 - man einen container laufen lässt der eine aufgabe erfüllen und sich dann beenden soll (zb. einen containerisierten compiler)


### Detached
sinnvoll für:
 - einen funktionieren container 

### Detached Container beenden
`$ docker ps`
`$ docker kill [container name von ps]`


## Container naming und run vs. start

`$ docker run ...`
`$ docker start my_container ...`

bei start sind container per default detachted.
also für start gilt:

`$ docker start -a my_container ...`
wobei -a (--attach) für `Attach STDOUT/STDERR and forward signals` steht.






## Aufgabe: Websiteinhalt zur laufzeit ändern
1. Entferne die COPY Zeile
2. starte den container mit
`$ docker build -t web .`
`$ docker run -d -p 42069:80 -v ./meine_website:/usr/share/nginx/html:ro web`
3. Geh auf http://localhost:42069/index.html
4. Verändere die html datei der website
5. lade die seite neu und beobachte dass sich diese ohne das rebuilden des containers geändert hat.


@V: ausformulieren :^)


## Debugging eines containers zur laufzeit

1. an einen container mit der shell anhängen:

`docker ps`
```
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                     NAMES
c8eb29d66c2a   web       "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:42069->80/tcp, :::42069->80/tcp   strange_visvesvaraya
```
`docker exec -it strange_visvesvaraya bash`

2. zB gemounteten Ordner inspizieren unter /usr/share/nginx/html
3. prüfen ob die gewünschten Dateien wirklich da liegen




## Container orchestration mit docker-compose
Voraussetzung:
`$ brew install docker-compose`

@V: dieser Teil lehnt sich stark an: https://docs.docker.com/compose/gettingstarted/ Da das default beispiel auch einfach eine python web-app ist.

Einer der wichtigen Aspekte von Docker ist, dass mehre Container für ein Gesamtsystem benutzt werden können. Dies erlaubt einem:
1. vorgefertigte Images plug&play-mäßig zusammenzufügen
2. Stabilität zu garantieren, da ein container dessen Hauptprozess abstürzt einfach automatisch neu gestartet werden kann.
3. Einzelne Services einfacher austauschbar zu machen
4. sharding oder load balancing zu betreiben

@V: einzelne Aspekte müsste man hier wieder erklären, ähnlich wie in 'it works on my machine'


### compose like its Beethoven!
`docker-compose` ist ein tool welches zur Orchestrierung von Containern dient. Orchestrierung im Container-Kontext ist ein Ausdruck, welcher das (hoffentlich) harmonische Zusammenspiel von einzelnen Containern beschreibt. Wir können also nicht nur einen einzelnen, sondern mehrere Container dazu nutzen unsere App zu betreiben. Dies bringt die oben genannten Vorteile mit sich, benötigt allerdings einen 

docker compose build
docker compose up
docker compose rm


### Networking innerhalb vom container-netzwerk

@V: wie man an dem example code sieht, werden die namen der instanzen in compose.yaml zu hostnames innerhalb des netzwerkes. Sprich, die python anwendung kann einfach auf 'db' als host connecten. Stichwort: DNS


### Aufgabe: Development Setup vs. Deployment Setup

Erstelle eine zweite version der compose.yaml. Diese soll dir ermöglichen zur laufzeit die app.py zu modifizieren ohne das Cluster zu stoppen und wieder zu starten.

@V: hier fehlen die vorbeispiele damit die TN 1&1 zusammenführen können: Volumes in compose.yaml; flask hot reloading;
@V: ersteres ist schon für die db-instanz gegeben; zweiteres ist zu finden unter: https://stackoverflow.com/questions/16344756/auto-reloading-python-flask-app-upon-code-changes


Dafür müssen angepasst werden:
1. Volumes des Flask containers
2. Environment Variablen Flask containers


## Kubernetes als Orchestrations-Tool
@V: Ich nehm mal an, dass das too much ist, vor allem für eine Woche Unterricht. Falls du ne Woche 2 machen willst, kannste folgende Themen noch anreißen:
@V: Kubernetes ist quasi der dicke Bruder von `docker compose`. Kubernetes bring praktisch den Vorteil mit, dass die Orchestration einfacher über mehrere PHYSICHE server verteilt werden kann und man das ganze mit Hilfe einer API steuern kann.

### Übertragung des Clusters auf Kubernetes mit `kompose convert`
Cluster welche schon mit `docker compose` erstellt wurden können in Kubernetes mehr oder minder importiert werden.

@V: https://github.com/kubernetes/kompose
@V: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/


## Interfacing mit Kubernetes durch Python
@V: https://github.com/kubernetes-client/python
@V: Die Orchestration selber kann man durch Kubernetes weiter automatisieren. Kubernetes 

