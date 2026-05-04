# MongoDB: 
[10 min]

MongoDB ist eine dokumentenorientierte NoSQL-Datenbank, die auf hohe Flexibilität und Skalierbarkeit ausgelegt ist. Im Gegensatz zu relationalen Datenbanken speichert MongoDB Daten in einem flexiblen, JSON-ähnlichen Format, das als BSON (Binary JSON) bekannt ist. Wie auch andere Dokumentenbasierte Datenbanken ist MongoDB frei von Schemaanforderungen. Trotzdem gelten für MonoDB die ACID Eigenschaften (Atomicity, Consistency, Isolation, Durability). MongoDB eignet sich besonders gut für Anwendungsfälle mit unstrukturierten oder stark variierenden Daten, darunter Content-Management-Systeme, Echtzeitanwendungen und Big-Data-Anwendungen.


## BSON
[5 min]

BSON (Binary JSON) ist ein Binärformat, das zur Serialisierung von JSON-ähnlichen Dokumenten verwendet wird. Es wurde speziell für die Verwendung mit MongoDB entwickelt und ermöglicht die effiziente Speicherung und Übertragung von Daten in MongoDB-Dokumenten. BSON unterstützt im Gegensatz zu JSON nicht nur Text, sondern auch andere Datentypen wie Datum/Uhrzeit, Binärdaten und reguläre Ausdrücke. Die binäre Repräsentation macht BSON effizienter für die Speicherung und Übertragung von Daten. BSON-Dokumente können auch komprimiert werden, um die Effizienz weiter zu verbessern. Die Verarbeitung der Binärdateien ist sowohl auf Server- als auch auf Clientseite möglich.


## Installation und Hosting
[20 min]

MongoDB kann auf verschiedene Arten bereitgestellt und verwendet werden. Hier sind einige Möglichkeiten, MongoDB-Server zu verwenden:

**Lokale Installation:** MongoDB kann direkt auf einem lokalen Rechner installiert und ausgeführt werden. Diese Option ist besonders nützlich, wenn lokal entwickelt wird oder wenn es sich um kleinere Projekte handelt.

**Cloud-Dienste:** Mehrere Cloud-Anbieter bieten MongoDB als verwalteten Dienst an. Einige bekannte Optionen sind:

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas): Ein Cloud-Dienst von MongoDB, der eine vollständig verwaltete Datenbank in der Cloud bereitstellt.
- [Amazon DocumentDB](https://aws.amazon.com/documentdb/): Ein von Amazon Web Services (AWS) verwalteter Dienst, der MongoDB-kompatibel ist.
- [Azure Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/): Ein von Microsoft Azure bereitgestellter Dienst, der mehrere Datenbankmodelle unterstützt.

**Docker:** MongoDB kann in einem Docker-Container ausgeführt werden. Dies ermöglicht eine flexible Bereitstellung und Skalierung, besonders wenn Docker bereits in der Infrastruktur verwendet wird.

```bash
# Beispiel Docker-Befehl für MongoDB
docker run --name mein-mongodb -p 27017:27017 -d mongo
```


**Lokale Entwicklungsumgebungen:** Einige Entwicklungsumgebungen bieten GUIs für die Verbindung zu lokalen oder entfernten MongoDB-Servern. Beispiele sind [MongoDB Compass](https://www.mongodb.com/products/compass) oder [Robo 3T](https://robomongo.org/).

**Plattformübergreifende Installationsmanager:** Installationsmanager wie [Homebrew](https://brew.sh/) für macOS oder [Chocolatey](https://chocolatey.org/) für Windows ermöglichen eine einfache Installation von MongoDB.

**Mongo Compass (Zusatz):** Um mit unser Datenbank zu intergaiereun und diese zu inspizieren, können wir auch die MongoDB Compass GUI verwenden. Diese kann [hier](https://www.mongodb.com/products/compass) heruntergeladen werden. Mit dieser GUI können wir uns mit der Datenbank verbinden und die Datenbankstruktur und -inhalte anzeigen.

_Wir werden MongoDB zunächst über einen Docker Container ausführen._

### Aufgabe: MongoDB mit Docker laden 🌶🌶
[20 min]

Erstelle ein Docker-Compose File, das einen MongoDB Container startet. Achte darauf, dass die Datenbank auch nach einem Neustart des Containers erhalten bleibt.
Recherchiere dazu im Internet.

[Link zur Lösung](../lösungen/aufgabe1.md)

## Exkurs: MongoDB Shell
[10 min]

Die MongoDB Shell ist in dem Docker Container standardmäßg vorhanden. Möchten wir also aus dem Container heraus mit der Datenbank interagieren, können wir die MongoDB Shell verwenden. Dafür müssen wir uns zunächst mit dem Container verbinden. Dies können wir über den Befehl `docker exec` erreichen.

```bash
docker exec -it mongo mongosh
```

Alternativ können wir auch über Homebrew die MongoDB Shell installieren und uns dann mit der Datenbank verbinden. Die Installation erfolgt durch den Befehlt `brew install mongosh`. Anschließend können wir uns mit der Datenbank verbinden, indem wir den Befehl `mongosh` ausführen und uns mit dem ausgewählen Port verbinden.

```bash
mongosh --port 27017
```


Nach dem Ausführen dieses Befehls sollte die MongoDB-Shell geöffnet werden. Nun könnenw wir über die Konsole mit der Datenbank direkt interagieren.

Über den Befehl `show databases` können wir uns alle bestehenden Datenbanken anzeigen lassen. Um eine neue Datenbank zu erstellen, können wir den Befehl `use <database_name>` verwenden. Zunächst ist diese Datenbank leer und wir daher über `show databases` auch nicht angezeit. Sobald wir jedoch eine Collection in dieser Datenbank erstellen, wird diese auch angezeigt. Collections sind in MongoDB das Äquivalent zu Tabellen in relationalen Datenbanken. Collections können über den Befehl `db.createCollection(<collection_name>)` erstellt werden. Wenn wir nun erneut `show databases` ausführen, sollte unsere neue Datenbank angezeigt werden. Um die aktuelle Datenbank zu wechseln, können wir den Befehl `use <database_name>` erneut verwenden. 

**Hinweis**: Wenn wir keine Collection explizit erstellen, sondern lediglich ein Dokument in eine Collection einfügen, wird diese Collection automatisch erstellt.

Über den Befehl `show collections` können wir uns alle Collections anzeigen lassen, die in der aktuellen Datenbank vorhanden sind. Im nächsten Kapitel werden wir uns ausführlicher mit den CRUD Operationen beschäftigen. Das Schließen der MongoDB Shell erfolgt über den Befehl `exit`.


### Aufgabe: Collection erstellen und User einfügen 🌶
[10 min]

Erstelle eine Collection mit dem Namen `users` und füge ein Dokument mit dem Namen `John Doe` ein. Lass die alle Collections anzeigen.

[Link zur Lösung](../lösungen/aufgabe2.md)