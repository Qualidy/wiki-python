# Einführung in Git Teil 3

## Lernziele dieses Kapitels
    - Du hast verstanden, wie man gemeinsam an einem Projekt arbeitet.
    - Du hast eine ahnung davon, was schief gehen kann und kannst im Internet nach passenden Lösungen suchen.

# Inhaltsangabe

#### Teil 3
11. Git Branching
12. Fazit


## 11. Branches

Branches werden verwendet, um voneinander isolierte Features zu entwickeln. Wir nutzen andere Branches für die Entwicklung und führen sie nach Fertigstellung wieder mit der Master-Branch zusammen.

## 11.1 git branch – Branches verwalten
Um einen neuen Branch zu erstellen, geben wir einfach einen Namen an:

```console
$ git branch new-branch
```

Ein lokaler Branch ist für andere erst verfügbar, wenn wir ihn in das Remote-Repository veröffentlichen.

Wir können nun den neu erstellten Zweig sehen, indem wir alle Branches auflisten:

```console
$ git branch --list --all
* master
  new-branch
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```

Wenn wir einen lokalen Branch löschen möchten, führen wir Folgendes aus:

```console
$ git branch -d new-branch
```

## 11.2 git checkout – Aktuellen Branch ändern
Wenn wir den aktuellen Branch wechseln möchten, verwenden wir die Funktionen git checkout oder git switch:

```console
$ git switch new-branch
Switched to branch 'new-branch'
$ git checkout master
Switched to branch 'master'
```

Wir sind gerade mit beiden Befehlen vom Master zum New-Branch und dann wieder zurück zum Master gewechselt.

Obwohl beide ähnlich funktionieren, ermöglicht der Befehl git switch lediglich das Wechseln von Zweigen. Im Gegensatz dazu ist der Git-Checkout ein komplexerer Befehl, der es uns ermöglicht, zusätzlich Dateien zu verwalten, Branches zurückzusetzen oder Dateien auf bestimmte Versionen zurückzusetzen.

## 12. Fazit
In diesem Artikel haben wir alle Git-Grundlagen behandelt und die meisten gängigen Vorgänge besprochen, die jeder Entwickler bei der Arbeit mit Git kennen sollte. Durch praktische Beispiele haben wir gelernt, wie man mit diesem Versionskontrollsystem arbeitet.

Wir begannen mit der Installation und Konfiguration von Git und erstellten dann das erste Repository. Danach haben wir einige Änderungen vorgenommen und gelernt, wie man den Commit-Verlauf ändert. Abschließend haben wir die Änderungen durch die Synchronisierung beider Repositories veröffentlicht und gelernt, wie man mit Git-Branches arbeitet.


# Aufgaben:
[320min]


## 1. Branch erzeugen. 🌶️️
Auf dem Repository von gestern erzeuge einen eigenen Branch.
Mache hier eine Änderung, commite sie und veröffentliche sie.

## 1. Branches zusammenführen. 🌶️️
Führe deinen Branch mit dem master zusammen.
Erzeuge danach zwei neue Branches. Auf jedem Banch erstellst du eine neue Datei mit unterschiedlichen Namen. Commite und veröffentliche.
Führe beide Branches nacheinander zusammen.

## 2. Ein externes Repository klonen 🌶️️🌶️️
Mache die Aufgabe wie oben aber provuziere einen Konflikt.

## 3. Konflikt auflösen. 🌶️️🌶️️
Löse den Konflikt von oben auf einem Weg deiner Wahl auf.

## 4. Provuziere unterschiedliche Konflikte. 🌶️️🌶️️
Erstelle unterschiedliche Konflikte und löse sie jeweils mit einer anderen Methode auf.

## 5. Arbeitet gemeinsam. 🌶️️🌶️️
Einigt euch ein gemeinsames Projekt in einem Remote Repository zu erstellen. Dort sollen bestimmte Dateien enthalten sein.
Bildet Arbeitsgruppen und erstellt je einen Branch pro Arbeitsgruppe.
Erzeugt eigene Beiträge innerhalb der Branches. Commitet dann und löst Konflikte ggf auf. Veröffentlicht eure Commits.
Führt nach möglichkeit alles wieder im Master zusammen und veröffentlicht.