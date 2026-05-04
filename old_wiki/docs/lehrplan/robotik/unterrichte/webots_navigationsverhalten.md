# Exkurs: Roboternavigationsverhalten untersuchen

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/NZksdNfPjfA?si=csr_AxQHSI_7ZN0Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [5 min]

Wir haben bereits ein Navigationsverhalten für einen Roboter implementiert: ein Braitenberg-Vehikel zur Hindernissvermeidung.

Aber wie gut funktioniert dieser Controller, um den Roboter durch die Welt zu navigieren? Schafft der Roboter es zum Beispiel mit diesem Controller in alle Bereiche einer gegebenen Welt zu kommen, um diese vollständig zu "explorieren" (zu "erkunden")?

Dazu müssten wir wissen, wo der Roboter bereits gewesen ist. Dies können wir in Webots einfach bewerkstelligen, indem wir den Roboter mit einem GPS Sensor ausstatten oder einen bestehenden Roboter nehmen, der bereits über einen GPS Sensor verfügt. Der GPS Sensor kann in Webots übrigens auch so eingestellt werden, dass er perfekte (x,y,z)-(Welt-)Koordinaten liefert. Dies wollen wir im Folgenden ausnutzen.

Überblick über das Bevorstehende: Sie sollen ...

- eine Webots .wbt Demowelt kopieren, der bereits einen Roboter enthält, der über einen GPS Sensor verfügt
- einen bestehenden C-Controller zur Steuerung des Robots in Python umschreiben (keine Sorge! Sie müssen kein C können!)
- lernen, wie man in Webots die GPS Sensorinformationen auslesen kann
- die ausgelesenen GPS-Sensordaten in einer Pandas Tabelle speichern
- die gespeicherten GPS-Sensordaten wieder einlesen und auf geeignete Weise mit Matplotlib und Seaborn visualisieren

## Aufgaben [165 min]

### A1: Demo nachvollziehen und Kopie einer Webots Welt anlegen [15 min] 🌶️

Wir wollen es uns einfach machen: wir nehmen eines der bestehenden Demos aus Webots als Grundlage für das Folgende. Öffnen Sie dazu in Webots unter

    "Help --> Webots Guided Tour ..."

bei 

    "Devices Tour"
    
das Demo

    gps.wbt

Es enthält einen einfachen "selbst gebauten" Roboter "myRobot".

Das Demo wird allerdings nur mit einem C-Controller geliefert. Schauen Sie sich erstmal das Demo an. Über den Tastendruck "G" (das 3D Window muss den Eingabefokus haben, d.h. bitte zuerst einmal in das 3D Window klicken!) wird Ihnen die GPS- bzw. Weltkoordinate (x,y,z) des Roboters angezeigt.

Erstellen Sie jetzt ein neues Projektverzeichnis und kopieren Sie die gps.wbt Datei hier rein!

### A2: C-Controller in Python umschreiben [45 min] 🌶️🌶️ 

Sie haben ja bereits einmal für den epuck-Roboter einen Python-Controller geschrieben. Der "myBot" ist aus dem vorherigen Demo hat allerdings etwas andere Distanzsensorbezeichnungen.

Finden Sie durch "Blick auf den C Code" heraus welche es sind und erstellen Sie analog einen neuen Python-Controller für diese Welt und diesen Roboter "myBot", so dass die Hindernissvermeidung aus dem C-Demo genauso in Python abläuft!

### A3: GPS-Koordinaten in Python auslesen und als Pandas Tabelle wegschreiben [45 min] 🌶️🌶️🌶

Ergänzen Sie nun Ihren Webots Python Controllercode so, dass sie ...

- Zugriff auf den GPS Sensor erhalten
- den GPS Sensor aktivieren ("enable")
- in jedem Simulationsschleifendurchlauf auch die GPS Koordinaten über den GPS Sensor auslesen
- die GPS Koordinaten in einer Liste sammeln
- aus der Liste  der GPS Koordinaten regelmäßig eine Pandas-Tabelle erzeugen
- die Pandas-Tabelle regelmäßig in einer Datei namens "koordinaten.csv" speichern

### A4: Analyse der vom Roboter besuchten Koordinaten [60 min] 🌶️🌶️

Wir haben jetzt eine tolle Datengrundlage (für Data Science!): in "koordinaten.csv" stehen alle Koordinaten drin, die der Roboter besucht hat. Vor lauter Zahlen sehen wir aber nichts. Es "schreit hier regelrecht" nach einer Visualisierung der vom Roboter besuchten Koordinaten / Stellen in der Welt.

Genau das sollen Sie jetzt tun!

Überlegen Sie sich mit Ihrem Vorwissen zu Matplotlib und Seaborn welche Visualisierungsmöglichkeiten wir für die Koordinaten haben, welche sinnvoll sind und setzen Sie mindestens zwei Visualisierungsmöglichkeiten in Python mit Matplotlib / Pandas um!

[Lösungen](webots_navigationsverhalten_loesungen.md)
