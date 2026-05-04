# Arten von APIs
[45 min]

Beim durchschauen verschiedener APIs kann es sein, dass man unterschiedliche API-Arten findet. Je nach Anforderung an Einsatzszenario, Skalierbarkeit und Performance in der Entwicklung gibt es unter anderen diese 3 Arten.

## REST (Representational State Transfer)
REST basiert auf den Prinzipien des HTTP-Protokolls und ist für Einfachheit und Leistungsfähigkeit bekannt.
So genannten "RESTful" APIs verwenden standardisierte HTTP-Methoden (GET, POST, PUT, DELETE) und sind zustandslos, was bedeutet, dass jede Anfrage unabhängig ist. Das bedeutet auch, dass z.B. keine Nutzerinformationen gespeichert werden.

Im vorherigen Kapitel zu Datenbanken haben wir bereits das Konzept CRUD kennen gelernt. Die grundlegenden Operationen in CRUD (Erstellen, Lesen, Aktualisieren, Löschen) lassen sich auf die HTTP-Methoden abbilden, die in RESTful APIs verwendet werden
- **Read** entspricht **GET**.
- **Create** in CRUD entspricht **POST** in REST.
- **Update** entspricht **PUT** oder PATCH.
- **Delete** entspricht **DELETE**.

**Beispiel**
Eine neue Bestellung aufgeben:

```js
HTTP-Methode: GET
URI: /essen/{gericht}
``````

Wichtig zu verstehen ist, dass die Struktur der Antwort vom Server ist fest definiert ist. Diese könnte z.B. so aussehen:
```js
"order": {
    "id": "1",
    "name": "Bolognese",
    "kellner_id": "25123",
    "zubereitungszeit": "350"
}
```


## GraphQL

Entwickelt von Facebook, ist GraphQL eine Umgebung und Abfragesprache für APIs, die es Nutzern ermöglicht, genau zu spezifizieren, welche Daten sie benötigen.
Im Gegensatz zu REST, bei dem der Server die Struktur der Antwort bestimmt, ermöglicht GraphQL dem Nutzer, die Struktur der Anfrage zu definieren. Das führt zu effizienteren und flexibleren API-Aufrufen.

Hierbei existiert eine Schema Definition durch die bekannt wird, welche Informationen abrufbar sind.

```js
type Bestellung {
  id: ID
  kellner_id: ID
  essen: [Essen]
  zubereitungszeit: INT
}

type Essen {
  id: ID
  name: String
}
```

Eine Abfrage mit gleichem Ergebnis wie beim RESTful Beispiel wäre dann:

```js
query {
  bestellung(id: "1") {
    id
    kellner_id
    essen {
      name
    }
    zubereitungszeit
  }
}
```

Und zu folgender Antwort führen würde:

```js
{
  "bestellung": {
    "id": "1",
    "kellner_id": "25123",
    "essen": [
      {
        "name": "Bolognese",
      }
    ],
    "zubereitungszeit": "350"
  }
}
```

## WebSockets

WebSockets sind eine weitere Möglichkeit zwischen Nutzer (Client) und Server zu kommunizieren. Anders als bei REST und GraphQL bieten Websockets eine dauerhafte Verbindung und ermöglichen Echtzeitdatenübertragung. Deshalb sind sie ideal für Anwendungen, die kontinuierliche Datenupdates benötigen.
Beispiele hierfür sind Chat-Anwendungen oder Online-Spiele.
Im Gegensatz zu HTTP, das eine unidirektionale Verbindung darstellt, ermöglichen WebSockets eine bidirektionale Kommunikation, sodass Server und Client Daten gleichzeitig senden und empfangen können.

## Aufgaben

### Aufgabe: API-Typen identifizieren 🌶️
Kannst du basierend auf der Beschreibung erkennen, welcher API-Typ (REST, GraphQL, WebSockets) am besten für eine Anwendung geeignet ist, die Echtzeit-Updates für Aktienkurse benötigt?

<details><summary>Lösung</summary>
WebSockets sind die beste Wahl für eine solche Anwendung, da sie eine dauerhafte Verbindung für Echtzeitdatenübertragungen bieten.
</details>

### Aufgabe: API-Auswahl begründen 🌶️
Du entwickelst eine Anwendung, die Nutzerinformationen speichert und diese Informationen bei jeder Sitzung aktualisiert. Welchen API-Typ würdest du wählen, REST oder GraphQL, und warum?

<details><summary>Lösung</summary>
REST wäre hier eine gute Wahl, da es zustandslos ist und jede Anfrage unabhängig verarbeitet wird, was ideal für das regelmäßige Aktualisieren von Nutzerinformationen in getrennten Sitzungen ist.
</details>

### Aufgabe: Leistungsoptimierung 🌶️🌶️
Betrachte eine Anwendung, die eine große Menge an Detaildaten über Produkte in einem Online-Shop darstellt. Welcher API-Typ, REST oder GraphQL, würde eine bessere Leistung hinsichtlich der Übertragung nur der benötigten Daten bieten?

<details><summary>Lösung</summary>
GraphQL bietet eine bessere Leistung für diese Anforderung, da es den Nutzern ermöglicht, genau zu spezifizieren, welche Produktinformationen abgerufen werden sollen, wodurch unnötige Datenübertragungen vermieden werden.
</details>

### Aufgabe: Datenabfrage vergleichen 🌶️🌶️
Stell dir vor, du möchtest eine Liste aller Gerichte mit einer Zubereitungszeit von weniger als 20 Minuten abrufen. Welcher API-Typ würde das effizient ermöglichen, REST oder GraphQL? Warum?

<details><summary>Lösung</summary>
GraphQL wäre effizienter, da es Nutzern ermöglicht, genau anzugeben, welche Daten abgerufen werden sollen (hier Gerichte mit einer Zubereitungszeit von unter 20 Minuten), was zu einer Verringerung unnötiger Datenübertragungen führt.
</details>

### Aufgabe: Praxisanwendung 🌶️🌶️🌶️
Welcher API-Typ wäre am besten geeignet, um eine mobile App zu entwickeln, die es den Nutzern ermöglicht, ihre Bestellungen aufzugeben und den Status in Echtzeit zu verfolgen, während die Bestellung vorbereitet wird?

<details><summary>Lösung</summary>
Eine Kombination aus REST und WebSockets wäre ideal. REST könnte für das Aufgeben der Bestellung und das Abrufen des anfänglichen Status verwendet werden, während WebSockets für die kontinuierliche Echtzeitaktualisierung des Bestellstatus genutzt werden könnten.
</details>

### Aufgabe: Technologieentscheidung analysieren 🌶️🌶️🌶️
Ein Team entwickelt eine interaktive Spielanwendung, bei der Spieler in Echtzeit gegen einander antreten. Welcher API-Typ, REST, GraphQL oder WebSockets, ist am besten geeignet, und warum könnte eine Kombination dieser Technologien vorteilhaft sein?

<details><summary>Lösung</summary>
WebSockets sind am besten für interaktive Spiele geeignet, da sie eine bidirektionale Kommunikation in Echtzeit ermöglichen. Eine Kombination mit REST könnte jedoch für das Einrichten von Spielsitzungen und das Abrufen von Spielerprofilen nützlich sein, um die Start- und Endpunkte der Kommunikation effizient zu verwalten.
</details>