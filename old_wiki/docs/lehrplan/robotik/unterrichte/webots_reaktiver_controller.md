# Reaktiver Robotercontroller

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/ruvbl1fUWTY?si=tHelXIDSdy59ItkV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


## Einführung [20 min]

Roboter sind komplexe Systeme, die durch verschiedene Kontrollarchitekturen gesteuert werden. Diese Architekturen ermöglichen es Robotern, Aufgaben autonom oder semi-autonom auszuführen. Die Auswahl der geeigneten Kontrollarchitektur ist entscheidend für die Effektivität und Effizienz eines Roboters in seiner spezifischen Anwendung.

## Grundlegende Klassifizierung der Roboterkontrollarchitekturen

### 1. Reaktive Architekturen

Reaktive Architekturen basieren auf dem Prinzip des direkten Reagierens auf Umweltstimuli, ohne dass ein internes Modell der Welt oder eine komplexe Verarbeitung erforderlich ist. Diese Architekturen sind schnell und robust gegenüber Veränderungen in der Umgebung.

Beispiel: Die subsumption Architektur, entwickelt von Rodney Brooks, ist ein bekanntes Beispiel für eine reaktive Architektur. Sie strukturiert das Verhalten des Roboters in Ebenen, wobei jede Ebene eine bestimmte Aufgabe kontrolliert.

### 2. Deliberative Architekturen

Deliberative Architekturen nutzen interne Modelle der Welt und führen komplexe Planungen durch, bevor sie handeln. Der Roboter "überlegt" was er macht, daher die Bezeichnung "deliberativ". Diese Architekturen sind geeignet für Aufgaben, die eine detaillierte Analyse und Langzeitplanung erfordern.

Beispiel: Die hierarchische Kontrollarchitektur, die oft in industriellen Robotersystemen verwendet wird, wo eine sequentielle Planung und präzise Kontrolle erforderlich sind.

### 3. Hybride Architekturen

Hybride Architekturen kombinieren Elemente aus reaktiven und deliberativen Ansätzen. Sie ermöglichen es Robotern, sowohl schnell auf Umweltänderungen zu reagieren als auch komplexe Planungen durchzuführen.

- Beispiel: Die ATLANTIS-Architektur, die sowohl reaktive als auch deliberative Komponenten integriert, um eine flexible und effiziente Steuerung zu erreichen.

## Kriterien zur Klassifizierung von Kontrollarchitekturen

Die Klassifizierung von Roboterkontrollarchitekturen kann anhand verschiedener Kriterien erfolgen:

- **Reaktionsschnelligkeit**: Wie schnell kann der Roboter auf Änderungen in seiner Umgebung reagieren?
- **Planungsfähigkeit**: Kann der Roboter komplexe Aufgaben planen und ausführen?
- **Lernfähigkeit**: Ist der Roboter in der Lage, aus Erfahrungen zu lernen und sein Verhalten anzupassen?
- **Flexibilität**: Wie gut kann der Roboter in verschiedenen Umgebungen und unter verschiedenen Bedingungen arbeiten?
- **Robustheit**: Wie widerstandsfähig ist der Roboter gegenüber Fehlern und unvorhergesehenen Ereignissen?

## Zukünftige Trends und Entwicklungen

Die Zukunft der Roboterkontrollarchitekturen liegt in der weiteren Integration von KI und maschinellem Lernen. Dies ermöglicht Robotern, autonomer zu agieren und komplexere Aufgaben in dynamischen Umgebungen zu bewältigen. Die Entwicklung hin zu adaptiveren und intelligenteren Systemen wird wahrscheinlich die Robotik revolutionieren und neue Anwendungsbereiche eröffnen.

Roboterkontrollarchitekturen sind ein entscheidender Aspekt in der Robotik. Die Wahl der richtigen Architektur hängt von den spezifischen Anforderungen und der Umgebung ab, in der der Roboter eingesetzt wird. Mit dem Fortschritt der Technologie werden diese Architekturen immer ausgefeilter und ermöglichen Robotern, eine immer größere Rolle in unserem Alltag und in der Industrie zu spielen.

## Zielsetzung für den nächsten Lernabschnitt

Eine deliberative Roboterkontrollarchitektur übersteigt unser zeitliches Budget in unserer Robotik-Woche. Daher schauen wir uns den konzeptionell einfacheren Ansatz an: wir wollen uns ein Beispiel einer reaktiven Roboterkontrollarchitektur anschauen und diesen auch in Python und Webots umsetzen!



## Aufgaben [210 min]

### A1: Einarbeitung in Braitenberg Vehikel [60 min] 🌶️🌶️

Braitenberg Vehikel sind ein historisch wichtiger Meilenstein in der Geschichte der Robotik. Für uns - so werden sie sehen - bieten sie eine tolle Möglichkeit einfache Roboterkontrollarchitekturen umzusetzen.

Führen Sie nun eine Internet-Recherche durch:
- Was sind Braitenberg Vehikel?
- Handelt es sich dabei um eine reaktive, deliberative oder hybride Roboterkontrollarchitektur?
- Welche Varianten von Braitenberg Vehikeln gibt es bzw. kann man unterscheiden?

### A2: Braitenberg Vehikel in Python/Webots programmieren [150 min] 🌶️🌶️

Sie sollen nun ein einfaches Braitenberg Vehikel in Webots mit Python umsetzen.

Nehmen Sie dazu den epuck-Roboter aus dem vorherigen Kapitel und die vorherige aufgebaute .wbt Welt, in der der epuck-Roboter noch zufällig umhergefahren ist.

Jetzt soll der epuck-Roboter auch auf seine Umwelt reagieren. Dazu sollen seine Abstandssensoren ausgelesen werden und die Werte sollen direkt bestimmen wie schnell die beiden Motoren links und rechts sich drehen.

Versuchen Sie zuerst herauszufinden, wie man die Abstandssensorwerte des epuck-Roboters in Python auslesen kann. Nutzen Sie dazu sowohl die Webots Dokumentation als auch Codebeispiele, die Sie im Internet hierzu suchen.

Wählen Sie dann zwei Absstandsensoren S1, S2, die jeweils nach vorne links bzw. vorne rechts im Winkel von ca. -45° und +45° ausgerichtet sind. Steuern Sie dann den Roboter dann sinngemäß in etwa so, dass S1 den linken Motor steuert und S2 den rechten Motor und zwar so, dass der Roboter vor Hindernissen ausweicht.

Experimentieren Sie hierzu im Robotersimulator und der vorher erstellten .wbt-Welt mit den vielen Hindernissen, bis der Roboter zufriedenstellend vor Hindernissen ausweicht.

Gehen Sie hierzu eventuell von dem Braitenberg-Vehikel zu einem Zustandsgesteuerten Controller über, der vom Prinzip her etwas Ähnliches macht wie das Braitenberg-Vehikel:

    Wenn links ein Hindernis, dann drehe nach rechts
    Wenn rechts ein Hindernis, dann drehe nach links
    Ansonsten fahre nach vorne

[Lösungen](webots_reaktiver_controller_loesungen.md)
