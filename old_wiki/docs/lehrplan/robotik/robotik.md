# Robotik Skript Übersicht

Dieses Skript bietet eine Einführung in das Thema Robotik & Python durch einen State-of-the-Art Roboter Simulator namens "Webot" (der übrigens ein Industrie-Standard ist).

Der Kurs ist in mehrere Schlüsselthemen gegliedert, die eine umfassende Einführung in die Robotik bieten:

## Einführung: Robotik & Robotersimulatoren

Wir beginnen mit einer Einführung in die Robotik und eine kurzen Überblick über den Roboter-Simulator Webots.

## Einen Webots-Roboter aus Python heraus steuern

Sie lernen einen einfachen Roboter ("epuck") aus Python heraus in Webots zu steuern. Der Roboter wird sich erstmal zufällig bewegen und anstoßen. Damit ist aber der Anfang einer ersten Steuerung geschafft!

## Reaktiver Robotercontroller
   
Hier beschäftigen wir uns mit der Theorie der Roboterkontrollarchitekturen. Was gibt es da überhaupt für Ansätze? Dann entwickeln wir einen eigenen reaktiven Robotercontroller. Dieser Robotercontroller wird dafür sorgen, dass der Roboter nicht mehr irgendwo anstößt. Dazu lesen wir Abstandssensorwerte aus und berechnen daraus geeignete Motorkommandos für die Motoren eine zweirädrigen Roboters.

## Webots Fahrzeug aus Python heraus steuern

Webots bietet auch Fahrzeuge! Damit schließt sich der Kreis und Sie können am Ende Ihres Python Lernpfades auch ein Fahrzeug aus Python heraus steuern. Die erste Steuerung wird manuell sein. Sie lernen Tastatureingaben vom Benutzer auszulesen und damit den Lenkwinkel und die Geschwindigkeit eines Autos in Webots zu steuern.

## Fahrsequenz-Assistent in Python/Webots

Dieser Skriptabschnitt wird Ihnen besonders Spaß machen! Hier bauen Sie ein erstes eigenes Fahrerassistenzsystem! Dieses einfache Fahrerassistenzsystem soll kurze immer wieder kehrende Steuerungen des Fahrzeuges übernehmen. Dazu schreiben Sie zuerst einen "Recorder", bei dem der Benutzer eine Sequenz von Steuersignalen vormacht. Diese werden zusammen mit dem genauen zeitlichen Timing aufgezeichnet. Im "Play"-Modus dieses einfachen Fahrsequenz-Fahrerassistenzsystems kann dann eine vorher aufgezeichnete Fahrsequenz (wie beispielsweise das Einparken in eine Parklücke) abgespielt werden.

![Hier schon mal ein kleiner Teaser](http://www.juergenbrauer.org/demos/city_einparken_luecke.mp4) wohin wir gegen Ende der Robotik-Woche kommen wollen.


## Roboternavigationsverhalten untersuchen

Zum Abschluss untersuchen wir das Navigationsverhalten von Robotern. Dazu lernen wir den GPS-Sensors eines Roboters auszulesen und die vom Roboter besuchten (x,y,z)-Koordinaten in der Welt in einer Pandas-Tabelle zu speichern. Abschließend nutzen Sie Ihre Fähigkeiten, die Sie in der Pandas/Matplotlib-Woche aufgebaut haben, um die Aufenthaltsorte des Roboters in der Welt zu visualisieren. Das erlaubt es uns einfach "zu sehen", wohin ein gegebener Python-Roboter-Controllercode den Roboter in die Welt führt und  - noch wichtiger - wohin der Controller in der Welt vielleicht nicht geführt hat.
