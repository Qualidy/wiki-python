# Begriffssammlung Robotik

# Einführung: Robotik  & Robotersimulatoren

| Begriff            | Kurzerklärung                                                                              | Link zur Referenz                                |
|--------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------|
| Robotik            | Interdisziplinäres Gebiet, das sich mit dem Bau und der Steuerung von Robotern beschäftigt | [Referenz](https://de.wikipedia.org/wiki/Robotik)|
| CoppeliaSim        | Robotersimulator | [Referenz](https://www.coppeliarobotics.com/)    |
| Gazebo             | Robotersimulator | [Referenz](https://gazebosim.org/home)           |
| Webots             | Robotersimulator | [Referenz](https://cyberbotics.com/)             |

# Einen Webots-Roboter aus Python heraus steuern

| Begriff            | Kurzerklärung | Link zur Referenz |
|--------------------|---------------|-------------------|
| `getDevice()`      | Funktion in Webots, um Zugriff auf einen Motor oder Sensor zu erhalten | [Referenz](https://cyberbotics.com/doc/reference/device?tab-language=python) |
| `setVelocity()`    | Funktion in Webots, um Geschwindigkeit eines Motors zu setzen | [Referenz](https://cyberbotics.com/doc/reference/motor) |
| Scene Tree         | Der Scene Tree in Webots repräsentiert die Hierarchie und Struktur der Objekte und Umgebungen in der aktuellen Simulation. | [Referenz](https://cyberbotics.com/doc/guide/the-scene-tree) |
| `.wbt` Datei       | Eine .wbt-Datei ist das Hauptdateiformat in Webots und enthält die Beschreibung der Simulationswelt, einschließlich der Umgebung, der Objekte und der Roboter. | [Referenz](https://cyberbotics.com/doc/reference/generalities) |
| Robot Controller   | Ein Robot Controller in Webots ist ein Skript oder Programm, das das Verhalten eines Roboters in der Simulation steuert. | [Referenz](https://cyberbotics.com/doc/guide/controller-programming) |
| Supervisor Node    | Der Supervisor Node ermöglicht erweiterte Kontrolle und Überwachung der Simulation, einschließlich der Möglichkeit, die Szene und die Eigenschaften der Objekte zu verändern. | [Referenz](https://cyberbotics.com/doc/reference/supervisor) |
| World Info Node    | Der World Info Node enthält globale Einstellungen für die Simulation wie die Schwerkraft, die Hintergrundfarbe und allgemeine Umgebungseinstellungen. | [Referenz](https://cyberbotics.com/doc/reference/worldinfo) |
| PROTO-Datei        | Eine PROTO-Datei in Webots definiert ein wiederverwendbares Modell oder Objekt, das in verschiedenen Simulationswelten verwendet werden kann. | [Referenz](https://cyberbotics.com/doc/reference/proto) |
| Physics Properties | Die Physics Properties definieren die physikalischen Eigenschaften von Objekten in der Simulation, wie Masse, Reibung und Elastizität. | [Referenz](https://cyberbotics.com/doc/reference/physics) |


# Reaktiver Robotercontroller

| Begriff            | Kurzerklärung | Link zur Referenz |
|--------------------|---------------|-------------------|
| Reaktive Roboterkontrollarchitekturen | Architekturen, die auf direktem Reagieren auf Umweltstimuli basieren, ohne interne Modelle oder komplexe Verarbeitung. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter#Verhaltensbasierte_Architektur_(Reaktive_Architektur)) |
| Deliberative Roboterkontrollarchitekturen | Architekturen, die interne Modelle nutzen und komplexe Planungen durchführen, bevor sie handeln. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter#Funktionsorientierte_Architektur_(Deliberative_Architektur)) |
| Hybride Roboterkontrollarchitekturen | Architekturen, die Elemente aus reaktiven und deliberativen Ansätzen kombinieren. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter#Hybride_Architekturen) |
| Subsumption Architektur | Eine reaktive Architektur, die das Verhalten eines Roboters in Ebenen strukturiert, jede für eine bestimmte Aufgabe. | [Referenz](https://en.wikipedia.org/wiki/Subsumption_architecture) |
| Hierarchische Kontrollarchitektur | Eine deliberative Architektur, oft in industriellen Robotersystemen verwendet, für sequentielle Planung und präzise Kontrolle. | [Referenz](https://en.wikipedia.org/wiki/Hierarchical_control_system) |
| Reaktionsschnelligkeit | Die Fähigkeit eines Roboters, schnell auf Änderungen in seiner Umgebung zu reagieren. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter) |
| Planungsfähigkeit | Die Fähigkeit eines Roboters, komplexe Aufgaben zu planen und auszuführen. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter) |
| Lernfähigkeit | Die Fähigkeit eines Roboters, aus Erfahrungen zu lernen und sein Verhalten anzupassen. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter) |
| Flexibilität | Die Fähigkeit eines Roboters, in verschiedenen Umgebungen und unter verschiedenen Bedingungen zu arbeiten. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter) |
| Robustheit | Die Widerstandsfähigkeit eines Roboters gegenüber Fehlern und unvorhergesehenen Ereignissen. | [Referenz](https://de.wikipedia.org/wiki/Autonomer_mobiler_Roboter) |
| Braitenberg Vehikel | Einfache, hypothetische Fahrzeuge mit Sensoren und Motoren, die auf direkte Reaktionen auf Umweltreize basieren. | [Referenz](https://de.wikipedia.org/wiki/Braitenberg-Vehikel) |


# Webots Fahrzeug aus Python heraus steuern

| Begriff              | Kurzerklärung                                                | Link zur Referenz |
|----------------------|--------------------------------------------------------------|-------------------|
| `setSteeringAngle()` | Funktion, um den Lenkwinkel eines Webots Fahrzeugs zu setzen | [Referenz](https://cyberbotics.com/doc/automobile/cpp-java-and-python-wrappers-of-the-automobile-libraries?tab-language=python)      |
| `setCruisingSpeed()` | Funktion, um die Geschwindigkeit eines Webots Fahrzeugs zu setzen | [Referenz](https://cyberbotics.com/doc/automobile/cpp-java-and-python-wrappers-of-the-automobile-libraries?tab-language=python)      |


# Fahrsequenz-Assistent in Python/Webots

| Begriff            | Kurzerklärung | Link zur Referenz |
|--------------------|---------------|-------------------|
| Fahrerassistenzsystem | Eine Funktionalität in modernen Fahrzeugen, die eine Teilaufgabe des Fahrens des Fahrzeuges übernimmt, um die Sicherheit oder den Fahrkomfort zu erhöhen | [Referenz](https://de.wikipedia.org/wiki/Fahrerassistenzsystem) |


# Roboternavigationsverhalten untersuchen

| Begriff            | Kurzerklärung | Link zur Referenz |
|--------------------|---------------|-------------------|
| Robotertrajektorie | Die "Robotertrajektorie" bezieht sich auf den Pfad oder die Bahn, die ein Roboter im Raum während einer Bewegung oder Aufgabenausführung verfolgt. | [Referenz](https://de.wikipedia.org/wiki/Trajektorie_(Physik)) |
