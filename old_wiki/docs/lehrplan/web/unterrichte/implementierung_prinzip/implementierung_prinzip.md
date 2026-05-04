# Implementierung

[60 min]

Die Implementierung einer API kann eine komplexe Aufgabe sein und umfasst folgende Schritte. Speziell bei der Entwicklung von APIs kann ein Test-Driven Developmentansatz unerwünschte Probleme vermeiden und zusätzlichen Aufwand durch den Fokus auf die Planung verhindern.

## 1. Planung

### Funktionsanforderungen

#### Anforderungsdokument

Die Erstellung eines umfassenden Anforderungsdokuments ist der erste Schritt in der Planungsphase. Es spezifiziert die funktionalen und nicht-funktionalen Anforderungen der API. Dazu gehört die Definition der zu unterstützenden Operationen, Sicherheitsanforderungen, Datenmodelle und Integrationen mit externen Diensten oder Datenbanken. Gerade für Projekte mit mehreren Teammitgliedern liegt der Erfolg in der Schaffung einer klaren und strukturierten Grundlage für die Entwicklung, die sicherstellt, dass alle Teammitglieder ein gemeinsames Verständnis der Ziele und Anforderungen haben.

#### API Architektur Prinzipien

Auch die Wahl einer Architektur hängt von den spezifischen Anforderungen und dem Kontext ab. REST ist eine gängige Wahl für Web-APIs. Die Verwendung von JSON als Datenformat ist weit verbreitet, leichtgewichtig und einfach zu integrieren, was z.B. besonders wichtig für die Leistung und Skalierbarkeit der API ist.

### Auswahl der Technologie

Die Auswahl des richtigen Frameworks und der Technologien erfolgt stets auf Basis der Anforderungen. Die meisten Frameworks unterstützen Grundlegende Funktionalitäten. Bei kleineren Projekten ist die Wahl der TEchnologie also deutlich weniger kritisch. API Frameworks wie Flask oder Django bieten eine robuste Basis für die Entwicklung von APIs in Python. Beide haben eingebaute Tools für Routing, Fehlerbehandlung und mehr.

## 2. Umsetzung

### Testen

Wie bereits in Wochen 4-5 erwähnt, sind Tests entscheidend, um die Zuverlässigkeit und Sicherheit der API zu gewährleisten. Dabei unterscheidet man zwischen verschiedenen Stufen.

**Unit-Tests** konzentrieren sich auf die kleinsten Teile der Anwendung, wie einzelne Funktionen oder Klassen, und stellen sicher, dass diese wie erwartet funktionieren.

**Integrationstests** prüfen das Zusammenspiel zwischen verschiedenen Komponenten der API, um sicherzustellen, dass sie zusammen korrekt funktionieren. Im heutigen Tagesprojekt werden wir uns vor allem auf diese Art der Tests mit Postman fokussieren. 

**End-to-End-Tests** hingegen simulieren reale Benutzerszenarien und prüfen die gesamte Anwendung in einer Umgebung, die der Produktionsumgebung ähnlich ist.

### Implementierung

Die Implementierung der API und der dafür nötigen Funktionalität nimmt of nur einen kleinen Teil der Entwicklung von Backend-Anwendungen in Anspruch. Im Falle, dass alle Anforderungen sowie die Tests bereits vordefiniert sind (TDD-Ansatz), ist die Entwicklung der Funktionen vergleichsweise unkompliziert.

## 3. Dokumentation

Auch wenn das Dokumentieren die am meisten vernachlässigte Aufgabe bei der Projekterstellung ist, ist sie doch unerlässlich für die Benutzerfreundlichkeit und Wartbarkeit der API. Sie sollte klar, vollständig sein und bei Änderungen konstant aktualisiert werden. Eine gute Dokumentation ermöglicht es Entwicklern, die API effizient zu nutzen und zu verstehen, und reduziert den Aufwand für Support und Fehlerbehebung.

Zu den Best Practices gehören unter anderem:

**Klarheit, Vollständigkeit und Konsistenz**: Die Dokumentation sollte umfassend sein, alle wichtigen Aspekte wie Endpoints, Parameter, Datenformate und Fehlercodes abdecken. Sie muss klar und präzise formuliert sein, um Missverständnisse zu vermeiden.

**Zielgruppenorientierung und Zugänglichkeit**: Die Dokumentation muss auf die Bedürfnisse der Zielgruppe, insbesondere Entwickler, zugeschnitten sein, einschließlich technischer Details und praktischer Beispiele.
Sie sollte leicht zugänglich, benutzerfreundlich und suchfreundlich gestaltet sein, um eine effiziente Nutzung zu ermöglichen.

**Interaktive Elemente und Versionierung**: Moderne API-Dokumentation sollte interaktive Beispiele enthalten, die das Testen der API direkt aus der Dokumentation heraus ermöglichen.
Eine klare Dokumentation der Versionsgeschichte hilft Benutzern, Änderungen und deren Auswirkungen auf ihre Anwendungen zu verstehen.

## 4. Deployment (Ausblick)

Der letze Schritt der Projektentwicklung ist die Veröffentlichung und Bereitstellung der API für die interne oder externe Nutzung. Jede (API)-Anwendung läuft auf einer Infrastruktur, heutzutage in den meisten Fällen einem virtuellen Cloud-Server.

### Cloud

Die Bereitstellung der Applikation über die Cloud bietet Skalierbarkeit, Zuverlässigkeit und oft Kosteneffizienz. Azure, welches in der kommenden Woche behandelt wird, ist eine beliebte Wahl mit einer breiten Palette von Diensten und Tools, die die Bereitstellung und das Management von APIs erleichtern. Im Kontext einer Cloudumgebung stoßen wir vermehrt auch auf den Begriff Docker-Container.

### Docker

Die Verwendung von Containern wie [Docker](https://www.docker.com/) für das Deployment bietet zahlreiche Vorteile, wie Portabilität, Konsistenz und Isolation. Docker erleichtert das Deployment und das Management von Anwendungen und ihrer Abhängigkeiten, was besonders in komplexen oder skalierenden Umgebungen nützlich ist.
