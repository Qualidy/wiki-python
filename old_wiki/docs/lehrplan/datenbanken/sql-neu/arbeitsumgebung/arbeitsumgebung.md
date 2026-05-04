# Arbeitsumgebung

## Einleitung

Wir verwenden in diesem Skript die [PyCharm IDE](https://plugins.jetbrains.com/plugin/1800-database-navigator) von JetBrains.
Wenn du mit VSCode arbeitest, dann lade das Plugin [Sqlite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) herunter. Die Arbeitsschritte lassen sich
analog durchführen.

Da wir uns nicht der Programmierung von Datenbank mit Python beschäftigen, sondern
Datenbanken in ihrer **rohen** Form kennenlernen möchten, werden wir die Einrichtung und Bedienung auch
über CLI (Commandline Interface) erledigen und üben.

```mermaid
graph TD
    subgraph Pycharm
        DBN
    end

    subgraph VSCode
        PluginVSCode(["Plugin<br>Sqlite"])
    end

    DBN(["Plugin<br>Database Navigator"])-- 
    " greift zu auf " --> SQLite3["Datenbankprogramm<br>SQLite3"] -- " greift zu auf " --> DB[(" Datenbank<br>myDatabase.db")]

PluginVSCode -- " greift zu auf " --> SQLite3

Konsole -- " greift zu auf " --> SQLite3

style SQLite3 fill: #f5f5, stroke: #a33
style Konsole fill: #ffffde, stroke: #aaaa33
```

## Arbeitsumgebung in PyCharm einrichten - Überblick

Folgende Schritte sind dazu zu unternehmen:

- PyCharm starten.
- Neues Projekt "Datenbank_Einführung" anlegen.
- Plugin "Database Navigator" installieren und in der IDE mithilfe des Datenbank-Symbols öffnen.
- Kommandozeile öffnen.

So soll es aussehen:

![img_23.png](img_23.png)

## Arbeiten mit dem Databank Navigator in Pycharm

Über das grüne Plus-Zeichen in diesen Dialog legt man eine neue Datenbank an oder stellt eine neue Verbindung zu einer
bestehenden Datenbank her.

![img_1.png](./img_1.png)

SQLite erstellt für jede Datenbank eine eigene Datei. In dieser Datei liegen die Daten.

🍀 **Anmerkung:** SQLite kann effizient und zuverlässig kleine bis mittelgroße Datenmengen, bis zu maximal 100 GB, verarbeiten. Während es technisch möglich ist, Dateien bis zu 140 TeraByte zu verwalten, empfiehlt es sich bei extrem großen Datenmengen, auf leistungsfähigere Datenbankprogramme zurückzugreifen.

Um eine Datenbank anzulegen, muss die Datei im Block **Database Files** angepasst werden.
Dazu klickt man in das ... Menü der Zeile in der "sqlite.db" steht und wählt Pfad und Dateinamen aus. Gibt es die Datei
noch nicht, so wählt man nur das Verzeichnis aus und hängt den Namen per Tastatureingabe an.

Es sollte auch der Datenbankname im Feld **Name** angepasst werden.

mit Klick auf "ok" sind wir hier:

![img_24.png](img_24.png)

Mittels **Doppelklick** auf die Datenbankverbindung öffnet sich ein Editorfenster, dass es uns ermöglicht, Befehle an die
Datenbank zu senden.

![img_25.png](img_25.png)

Geben wir nun ein paar Befehle ein, um die Funktionsweise zu zeigen:

```sql
CREATE TABLE test (
  einkaeufer,
  ware,
  stueck
);
```

```sql
INSERT INTO test VALUES ('Mario', 'Bananen', 5);
```

```sql
SELECT * FROM test;
```

Wir starten die Ausführung jeden Kommandos mit dem grünen Pfeil links daneben. Die Frage beantworten wir mit dem
Standard:

![img_28.png](img_28.png)

Die Anzeige in der DB Execution Console im unteren Teil des Fensters zeigt uns den Erfolg des Vorgangs.

![img_27.png](img_27.png)

Ein Klick auf Settings öffnet erneut den Konfigurationsdialog. Nachdem man die betreffende Datenbank ausgewählt hat,
genügt der Klick auf das rote Minus-Zeichen, um die **Datenbankverbindung** zu löschen.

![](./img_4.png)

Die Datenbank selbst bleibt im Verzeichnis bestehen. Der Übung halber löschen wir sie wieder.

![img_29.png](img_29.png)

## Arbeitsumgebung in VS-Code einrichten

Folgende Schritte sind dazu zu unternehmen:

- VS-Code starten.

![img_7.png](img_7.png)

- Plugin "Sqlite" installieren

![img_8.png](img_8.png)

- Füge einen Ordner zum Arbeitsbereich. Klicke dazu auf 'Open Folder' und navigiere zu einem Verzeichnis deiner Wahl. Erstelle dort einen Ordner mit dem Namen 'Datenbank_Einführung'.

![img_9.png](img_9.png)

- über das Symbol für 'neue Datei' erstellen Sie eine Datei namens 'test.db'.

![img_10.png](img_10.png)

- und über diese Auswahl definieren wir die Datei als Datenbank.

![img_11.png](img_11.png)

- Um jetzt Anfragen (Queries) an die Datenbank schicken zu können benötigen wir eine SQL Query. Gib ihr den Namen `test.sql`.

![img_11_a.png](./img_11_a.png)

- Geben wir nun ein paar Befehle ein, um die Funktionsweise zu zeigen:

```sql
CREATE TABLE test (
  einkaeufer TEXT,
  ware TEXT,
  stueck INTEGER
);
```

```sql
INSERT INTO test (einkaeufer, ware, stueck) VALUES ('Mario', 'Bananen', 5);
```

```sql
SELECT * FROM test;
```

![img_12.png](img_12.png)

- und die dazu gehörende Ausführung

![img_13.png](img_13.png)

- zeigen einen ersten Erfolg:

![img_14.png](img_14.png)

- die Datenbank löschen wir wieder mit 'delete'.

![img_15.png](img_15.png)

## Arbeiten mit dem Kommandozeilen-Tool

### Kommandozeilen-Tool = Command Line Interface = CLI

Eine frische Konsole mit dem Befehl zum Wechseln in ein anderes Verzeichnis

![img_16.png](img_16.png)

Hier erstellen wir ein neues Verzeichnis und wechseln hinein

![img_17.png](img_17.png)

Der Befehle 'sqlite3' sollte uns Zugang zum Datenbankprogramm gewähren.

![img_18.png](img_18.png)

Wie im Text angegeben öffnen oder, falls die Datenbank nicht existiert, erstellen wir die Datenbank 'test.db'.

![img_19.png](img_19.png)

Im nächsten Schritt führen wir die gleichen Befehle aus wie vorher.

![img_20.png](img_20.png)

Da wir keine grafische Oberfläche haben, brauchen wir Werkzeuge, die uns helfen, den Überblick zu behalten.
Zum Beispiel können wir den Befehl `.help` nutzen , um herauszufinden, wie man die Liste der Tabellen aufruft.

![img_21.png](img_21.png)

Das probieren wir gleich noch einmal aus und löschen danach unsere Arbeit wieder.

![img_22.png](img_22.png)

### **Aufgabe: Kommandozeile bedienen 🌶️️**

[10min] Probiere `.help` selbst aus. Suche den Befehl zum Verlassen der Konsole.

Verlasse die Konsole. Das ist nicht unbedingt notwendig, aber es ist gut, den Befehl zu kennen um zur "normalen" Betriebssystem Konsole zurückzukommen.  

Rufe die SQLite Konsole erneut auf und öffne dabei eine neue Datenbank mit einem Namen deiner Wahl.

<details>
<summary>Lösung</summary>

**Lösung 1:**

Der zu verwendende Befehl lautet .quit oder (was nicht angegeben ist) CTRL-D.

<img src="img_6.png">

**Lösung 2:**

<img src="img_7.png">

</details>

### **Aufgabe: Täglich grüßt das Murmeltier 🌶️️**
[15min] 

Ziel dieser Aufgabe ist es, eine einfache Datenbank zu erstellen, die Mitarbeiterdaten speichert. Verwende dafür entweder PyCharm oder VSCode, je nachdem, was du bevorzugst.

- Erstelle eine neue Datenbank namens `mitarbeiter.db`.
- Erstelle eine Tabelle mitarbeiter mit den Spalten id, name, position, und gehalt.
- Füge zwei Einträge in die Tabelle ein:
  - (1, 'Anna Meier', 'Softwareentwicklerin', 5000)
  - (2, 'Max Schulz', 'Projektmanager', 5500)
- Verwende ein SELECT-Statement, um alle Einträge aus der Tabelle mitarbeiter abzurufen.
- Lösche die Datenbank `mitarbeiter.db` über den Editor, sobald du die Aufgabe abgeschlossen hast.

<details>
<summary>Lösung</summary>

<pre><code>
CREATE TABLE mitarbeiter (
  id,
  name,
  position,
  gehalt
);

INSERT INTO mitarbeiter VALUES (1, 'Anna Meier', 'Softwareentwicklerin', 5000);
INSERT INTO mitarbeiter VALUES (2, 'Max Schulz', 'Projektmanager', 5500);

SELECT * FROM mitarbeiter;
</code></pre>
</details>

# Zusammenfassung

Wir haben dargestellt, wie man mittels des Datenbank-Navigators, des Sqlite-Plugins oder des CLI, Datenbankdateien
erstellt
oder eine Verbindung dazu herstellt. Über den Editor im Navigator oder Plugin können nun genauso wie im CLI Kommandos an
die
Datenbank senden und die Ergebnisse von Abfragen anzeigen.

⚠️ **WICHTIG!**
Dateinamen bei SQLite folgen keiner bestimmten Konvention. So kann auch eine
Datenbank ohne Endung angelegt werden.
Es ist also wichtig hier einer eigenen Norm zu folgen.

**Vorschlag:**
SQLite Dateinamen immer auf `.db` enden lassen. Das hilft anderen Programierer(n):innen oder Programmen anzuzeigen, dass es sich um eine Datenbankdatei handelt.

Es ist dabei einleuchtend, dass der Navigator wesentlich komfortabler ist als die CLI. Man sollte die CLI aber nicht
unterschätzen. Bei kleinen Aufgaben und Wartungsarbeiten ist man mit dem CLI deutlich schneller als mit einer
**großen** Lösung.
