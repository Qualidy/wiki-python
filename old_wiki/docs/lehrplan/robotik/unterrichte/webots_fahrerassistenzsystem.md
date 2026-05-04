# Webots: Entwicklung eines einfachen Fahrerassistenzsystems

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/bhLvo51myvw?si=RLK4vGXS36rzHI0j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [10 min]

Die nächste Zielsetzung ist es ein kleines (sehr einfaches) Fahrerassistenzsystem für das Fahrrzeug in Webots in Python zu entwickeln.

Stellen Sie sich dazu folgende Situaton vor: vielleicht parken Sie auf Ihrem Grundstück jeweils ziemlich genau an der gleich Stelle. Jeden Morgen, wenn Sie von Ihrem Grundstück zur Arbeit fahren, durchlaufen Sie wahrscheinlich in etwa die gleiche Sequenz an Steuersignalen für Ihr Auto wenn Sie ausparken wollen. Langsam rückwärts fahren, Räder erst gerade ausstellen, dann um einen bestimmten Winkel drehen, vom Grundstück rückwärts auf die Straße fahren, Räder wieder gerade stellen, Vorwärtsgang einlegen, anfahren, etc.

Wir stellen uns jetzt vor, dass ein Benutzer für solche repetitiven Steuersequenzen sein Auto "programmieren" kann, indem er die Sequenz einmal vormacht, dabei aufzeichnet und dann mit nur einem Knopfdruck wieder abspielen kann.

Genau das wollen wir jetzt in Webots nachbauen: dazu werden wir einen neuen Controller in Python schreiben, der zwei Modi anbieten wird. Erstens die Aufnahme einer Steuersequenz und zweiten das "Abspielen" der vorher gespeicherten Steuersequenz.

Natürlich ist das nur bedingt realistisch. Für ein echtes Fahrerasistenzsystem brauchen wir auch Sensorik, die überprüft, ob ein Hindernis zum Beispiel plötzlich auftritt.

Solche Hindernisse können dynamischer Natur sein (eine Katze oder eine Person, die den Fahrweg kreuzt) oder statischer Natur sein (da steht noch ausnahmsweise heute eine Mülltonne im Weg, die nur Donnerstags Morgen für die Müllabfuhr rausgeräumt wird).

Wir konzentrieren uns hier der Einfachheit halber nur auf den Steueranteil, d.h. schreiben einen Controller, der Sequenzen aufnehmen und dann abspielen kann. Den Regelungsanteil, d.h. das Reagieren auf Objekte über Sensordaten blenden wir hier aus.

## Aufgaben [300 min]

### A1: Sequenzen aufnehmen können [120 min] 🌶️🌶️

Erweitern Sie jetzt den Tastatur-Controller (der es einem Benutzer erlaubt das Fahrzeug über die Tastatur zu steuern) so, dass die aufgenommenen Steuersignale an das Auto (den "Roboter") mit einer zeitlichen Information in einer Pandas Tabelle gespeichert werden, wenn der Benutzer die Aufnahme mit "r" (record start) startet und mit "r" (record stop" wieder beendet.

Die zeitliche Information / das Timing ist später sehr wichtig um die Sequenz auch zeitlich korrekt wieder zu geben!

Zum Beispiel könnte das Fahrmanöver "Rückwärts ausparken und langsames anfahren" sinngemäßg aus der folgenden Sequenz von Steuersignalen bestehen:

    Zeitpunkt 0: START DER AUFNAHME DER SEQUENZ
    Zeitpunkt 10: Geschwindigkeit auf -5 km/h
    Zeitpunkt 35: Lenkwinkel auf -0.2° setzen
    Zeitpunkt 70: Geschwindigkeit auf 0 km/h
    Zeitpunkt 75: Lenkwinkel auf 0.0° setzen
    Zeitpunkt 90: Geschwindigkeit auf +5 km/h
    Zeitpunkt 110: Geschwindigkeit auf +10 km/h
    Zeitpunkt 130: Geschwindigkeit auf +15 km/h
    Zeitpunkt 150: ENDE DER AUFNAHME DER SEQUENZ

Überlegen Sie sich dazu auch einen geeigneten Aufbau der Pandas-Tabelle.

Die erzeugte Pandas-Tabelle soll dann in einer Datei fahrsequenz1.csv gespeichert werden, sobald der Benutzer die Fahrsequenzaufnahme mit "r" beendet.

### A2: Sequenzen abspielen können [120 min] 🌶️🌶️🌶️

Das Ergebnis von Aufgabe 1 ist, dass der Benutzer nun ein Fahrzeug steuern kann und die Steuersequenz als Tabelle in einer Datei wie z.B. fahrsequenz1.csv speichern kann.

Wenn der Benutzer nun "p" drückt (wie "play"), soll diese Sequenztabelle aus der Datei wieder eingelesen werden und die Sequenz abgespielt werden.

Überlegen Sie sich hierzu, wie Sie das Timing der Steuerkommandos für das Fahrzeug, das in der Tabelle auch gespeichert ist möglichst einfach bei dem Wiederabspielen der Steuerkommandos berücksichtigen.

Ziel ist es hier, eine möglichst kompkakte, leicht verständliche und wartbare Lösung in Python zu programmieren!

### A3: Test des Fahrsequenz-Assistenten bei Einparkvorgang [60 min] 🌶️🌶️

Erstellen Sie jetzt ein Webot Welt, in der Sie neue andere Fahrzeuge aus Webots, mit denen wir bisher nicht gearbeitet haben, an den Straßenrand stellen. Lassen Sie dabei eine gute Parklücke Platz!

Stellen Sie "Ihr" Fahrzeug auf die Straße etwas vor die Parklücke.

Dann nehmen Sie den von Ihnen entwickelten Fahrsequenz-Assistenten und nehmen einen Ihrer erfolgreichen Einpark-Vorgänge auf.

Testen Sie dann den Einparkassistenten: kann der Assistent beim Wiederabspielen der Einparksequenz das Fahrzeug erfolgreich in die Parklücke einparken?

Finden Sie heraus wie Sie in Webots ein Video erstellen können und nehmen Sie den Test Ihres Einparkassistenten als Video auf!

[Lösungen](webots_fahrerassistenzsystem_loesungen.md)
