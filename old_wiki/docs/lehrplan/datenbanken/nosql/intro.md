# NoSQL Intro und Motivation
[20 min]

NoSQL steht für "Not only SQL" und bezeichnet eine Vielzahl von Datenbankmanagementsystemen, die sich von traditionellen relationalen Datenbanken unterscheiden. Der Begriff "NoSQL" bedeutet nicht zwangsläufig "kein SQL", sondern betont, dass diese Systeme zusätzlich zu SQL-basierten Datenbanken existieren. NoSQL Datenbanken sind in der Regel nicht relational und verzichten auf starre Schemata. Dadurch sind sie flexibler und können besser mit sich ändernden Anforderungen umgehen.

NoSQL Datenbanken können allgemein in folgende Kategorien eingeteilt werden:

- Dokumentenorientierte Datenbanken
- Graphdatenbanken
- Spaltenorientierte Datenbanken
- Schlüssel-Wert-Datenbanken

Die genauere Betrachtung dieser Kategorien wird im nächsten Abschnitt vorgenommen. Hier werden wir stattdessen auf die grundlegenden Unterschiede zwischen NoSQL und SQL eingehen.

## Unterschiede zu SQL-Datenbanken

Neben dem bereits Angesprochenen Unterschied des fehlenden Schemas und den vielfältigen Strukturen gibt es noch weitere Unterschiede zwischen NoSQL- und SQL-Datenbanken. Diese sind im folgenden aufgeführt und erklärt:

### Skalierbarkeit

NoSQL Datenbanken lassen sich in der Regel leichter horizontal skalieren als SQL Datenbanken. Horizontale Skalierung heist, dass man weitere gleichartige Hardware zu einem bestehendem System hinzufügt. Bei vertikaler Skalierung wird die Hardware eines Systems durch leistungsstärkere ersetzt. Dies liegt daran, dass NoSQL Datenbanken meistens auf die Primary-Secondary-Architektur setzen. Die Primary-Secondary-Architektur ist eine Datenbankarchitektur, die darauf abzielt, Redundanz und hohe Verfügbarkeit zu gewährleisten. In dieser Architektur gibt es eine primäre (Primary) Datenbankinstanz und mehrere sekundäre (Secondary) Datenbankinstanzen. Die primäre Instanz ist die Hauptdatenbank, die für Lese- und Schreibzugriffe verantwortlich ist. Die sekundären Instanzen replizieren Daten von der primären Instanz, um eine Kopie der Datenbank bereitzustellen. Dadurch kann die Last auf mehrere Server verteilt werden. Wenn die primäre Instanz ausfällt, kann eine der sekundären Instanzen zur primären Instanz werden, um die Verfügbarkeit zu gewährleisten.

Bei SQL Datenbaken ist diese horizontale Skalierung aufgrund der bestehenden Relationen nicht so einfach möglich. Es gibt zwar verschiedene Ansätze, wie SQL Datenbanken horizontal skaliert werden können, jedoch gehen diese häufig mit einer höheren Komplexität und einer geringeren Performance einher. Daher werden SQL Datenbanken in der Regel eher vertikal skaliert. Dies bedeutet, dass die Hardware, auf der die Datenbank läuft, aufgerüstet wird um die Leistungsfähigkeit zu erhöhen. Dies ist in Cloud Umgebungen wie AWS oder Azure einfach möglich, geht jedoch tendenziell mit höheren Kosten, als bei eine horziontalen Skalierung von NoSQL Datenbanken einher.

### ACID Eigenschaften

Im Gegensatz zu SQL Datenbaken müssen NoSQL Datenbanken nicht unbedingt die ACID Eigenschaften (Atomicity, Consistency, Isolation, Durability) erfüllen. Hier noch einmal die ACID Eigenschaften zur Erinnerung:

- Atomicity (Atomarität): Eine Transaktion wird entweder vollständig ausgeführt oder gar nicht. Es gibt keine Zwischenzustände.
- Consistency (Konsistenz): Die Datenbank befindet sich immer in einem konsistenten Zustand. Dies bedeutet, dass die Datenbank nach einer Transaktion in einen gültigen Zustand übergeht.
- Isolation (Isolation): Transaktionen werden unabhängig voneinander ausgeführt. Dies bedeutet, dass eine Transaktion nicht von einer anderen Transaktion beeinflusst werden kann.
- Durability (Dauerhaftigkeit): Nachdem eine Transaktion abgeschlossen wurde, bleiben die Daten dauerhaft in der Datenbank gespeichert.

Es gibt auch NoSQL Datenbanken, die diese Eigenschaften erfüllen. Beispiele hierfür sind MongoDB und Couchbase. Andere NoSQL Datenbanken, wie zum Beispiel Redis, verzichten auf die ACID Eigenschaften, um eine höhere Performance zu erreichen. Letztendlich sollte vor der Verwendung einer NoSQL Datenbank geprüft werden, ob die ACID Eigenschaften für die Anwendung relevant sind oder nicht und ob die Datenbank diese Eigenschaften erfüllt.