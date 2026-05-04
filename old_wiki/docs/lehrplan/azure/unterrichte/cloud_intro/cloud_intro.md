# Web, APIs und die Cloud

[60 min]

## Web und APIs Fragen

[20 min]

1. Erkläre, was Flask ist und wozu man es normalerweise verwendet.
2. Was ist der Hauptunterschied zwischen einer GET- und einer POST-Anfrage?
3. Beschreibe, was eine API ist und warum sie in der Webentwicklung wichtig ist.
4. Was ist mit dem Begriff "Route" in Flask gemeint?
5. Welche HTTP-Methoden gibt es und was sind ihre Unterschiede?
6. Was ist SQLAlchemy und wie wird es in einem Flask-Projekt eingesetzt?
7. Erkläre, warum ein Datenmodell in der Webentwicklung wichtig ist.
8. Was verstehst man unter "Agile Entwicklung" und welche Prinzipien gibt es?
9. Was ist ein Use Case Diagram und wofür wird es verwendet?
10. Was ist Middleware in einer Webanwendung und wozu dient sie?
11. Beschreibe, was JSON ist und wie es in Web-APIs eingesetzt wird.
12. Welche Frameworks für Client-Side Rendering gibt es?

## Die Cloud

Bisher konnten wir Projekte nur lokal entwickeln und ausführen. Es gab keinen einfachen Weg, einen Link mit Bekannten zu teilen um Anwendungen gemeinsam zu nutzen. Das Deployment von Anwendungen spielt eine zentrale Rolle im Entwicklungszykluses.

### Warum die Cloud?

In der heutigen schnelllebigen digitalen Welt ist die Agilität in der Softwareentwicklung entscheidend. Die Cloud-Technologie hat sich als unverzichtbar für die Entwicklung von Web-Apps etabliert, indem sie Flexibilität, Skalierbarkeit und Effizienz bietet, die weit über die Möglichkeiten traditioneller lokaler Umgebungen hinausgehen.

### Wo ist die Cloud?

Wichtig zu verstehen ist, dass die "Cloud" sich nicht auf einen einzelnen physischen Ort bezieht, sondern auf ein Netzwerk von Datenzentren, die über das Internet verteilt sind und zusammenarbeiten, um verschiedene Dienste bereitzustellen.

Diese Datenzentren, die über den gesamten Globus verteilt sind, beinhalten zahlreiche Server und Hardwarekomponenten. Die geografische Verteilung dieser Datenzentren ermöglicht es, Daten und Anwendungen näher am Nutzer zu hosten, was schnellere Zugriffszeiten und verbesserten Datenschutz bietet. Ein wichtiger Aspekt der Cloud ist die Virtualisierung der Serverressourcen, wodurch mehrere Nutzer oder Unternehmen gleichzeitig auf die Hardware zugreifen können, ohne sich gegenseitig zu beeinflussen. Dank dieser Virtualisierung und der weitreichenden Verfügbarkeit des Internets können Nutzer von überall auf die Cloud-Dienste zugreifen, vorausgesetzt, sie haben eine Internetverbindung.

### Der Paradigmenwechsel von Lokal zu Cloud

Traditionelle lokale Umgebungen sind oft durch begrenzte Ressourcen, hohe Wartungskosten und mangelnde Skalierbarkeit gekennzeichnet. Das schränkt die Entwicklungsgeschwindigkeit und -flexibilität ein.

Externe Ressourcen (Cloud) ermöglichen es Entwicklern, sich so von den physischen Einschränkungen zu lösen und bieten gleichzeitg Zugriff auf eine breite Palette von Diensten, die nach Bedarf skaliert werden können. Zusätzlich sind weitere Faktoren wie die Kosteneffizienz Abdeckung wichtig.

### Skalierbarkeit und Flexibilität

- **Anpassungsfähige Ressourcen**: In der Cloud können Unternehmen die Rechenleistung und den Speicherplatz nahtlos anpassen, um Spitzenlasten oder unerwartete Benutzeranstiege zu bewältigen.

- Ein Online-Medienunternehmen kann z.B. seine **Serverkapazitäten automatisch erhöhen**, wenn die Anzahl der gleichzeitigen Nutzer während wichtiger Nachrichtenereignisse ansteigt, und diese später wieder reduzieren, um Kosten zu sparen.

### Kosteneffizienz

- **Pay-as-you-go-Modell**: Cloud-Dienste folgen oft einem Verbrauchsmodell, bei dem nur für die genutzten Ressourcen bezahlt wird. Das führt zu einer signifikanten Kostensenkung im Vergleich zum Vorhalten eigener Infrastruktur.

- Ein Startup kann **ohne hohe Anfangsinvestitionen** eine Web-App entwickeln, indem es Cloud-Dienste wie Amazon Web Services (AWS) oder Microsoft Azure nutzt.

### Globale Reichweite und Performance

- **Verteilte Datenzentren**: Cloud-Anbieter betreiben Netzwerke von Datenzentren auf der ganzen Welt. Das ermöglicht es, Anwendungen in geografischer Nähe zu den Endnutzern zu hosten, was die Latenz verringert.

- Ein E-Learning-Plattform kann ihre Dienste weltweit **mit minimaler Verzögerung bereitstellen**, indem sie die Cloud-Infrastruktur nutzt, um Inhalte in verschiedenen Regionen zu replizieren.

### Beschleunigte Entwicklung und Bereitstellung

- **Agile Entwicklung**: Cloud-Dienste unterstützen agile Entwicklungspraktiken, indem sie Continuous Integration/Continuous Deployment (CI/CD) Pipelines und DevOps-Tools anbieten.

- Viele moderne Softwareentwicklungsunternehmen verwenden Cloud-Entwicklungstools, um den **Code mehrmals täglich zu aktualisieren und automatisch in die Produktion zu überführen**.

### Sicherheit und Compliance

- **Erweiterte Sicherheitsfunktionen**: Cloud-Plattformen bieten fortschrittliche Sicherheitsfunktionen, die den Schutz von Web-Apps gewährleisten, von der Verschlüsselung bis hin zu Identitäts- und Zugriffsmanagement.

- Finanzdienstleister können die Cloud z.B. nutzen, um die strengen **Compliance-Anforderungen automatisiert zu testen und erfüllen**.

## Sensibilisierung in der Cloud-Nutzung

Die Nutzung von Cloud-Diensten erfordert aber ein Verständnis verschiedener Aspekte, um eine effiziente, sichere und kosteneffektive Nutzung zu ermöglichen.

### Datenschutz und Compliance

Ein Gesundheitsdienstleister speichert Patientendaten in einer Cloud-Umgebung, die nicht HIPAA-konform ist. Dies könnte zu einer Datenschutzverletzung führen, die nicht nur die Privatsphäre der Patienten gefährdet, sondern auch zu erheblichen Bußgeldern und Reputationsverlust für das Unternehmen führt.

### Sichtbarkeit

Ein Unternehmen überwacht seine Cloud-Ressourcen nicht angemessen. Ein plötzlicher Anstieg des Datenverkehrs, der durch einen DDoS-Angriff verursacht wird, bleibt unbemerkt. Dies führt zu erheblichen Ausfallzeiten und potenziellen Einnahmeverlusten.

### Zugriff & Freigaben

Ein Unternehmen setzt keine strikten Zugriffskontrollen um. Ein Mitarbeiter mit zu weitreichenden Berechtigungen versehentlich wichtige Daten löscht oder ein externer Angreifer erhält Zugriff auf sensible Informationen. Dies könnte zu Datenverlusten und schwerwiegenden Sicherheitsverletzungen führen.

### Kosten

Ein Unternehmen hat seine Cloud-Ressourcen nicht richtig konfiguriert und überwacht die Ausgaben nicht. Über einen Monat hinweg summieren sich ungenutzte oder überdimensionierte Instanzen zu enorm hohen Rechnungen, die die finanziellen Ressourcen des Unternehmens belasten.

### Sicherheit und Angriffsfläche

Ein Unternehmen implementiert keine ausreichenden Sicherheitsmaßnahmen in seiner Cloud-Umgebung. Hacker nutzen eine Sicherheitslücke aus, um in das Netzwerk einzudringen und sensible Daten zu stehlen oder Ransomware zu installieren, was zu erheblichen finanziellen und rechtlichen Konsequenzen führt.

## Schlüsseltechnologien und -komponenten

Auch wenn nicht im Fokus dieses Blocks, ist es wichtig im Kontext der Cloud verschiedene Begriffe gehört zu haben und ein ordnen zu können.

### Containerisierung

(Docker) Container sind leichtgewichtige, eigenständige Pakete, die Code, Laufzeitumgebung, Systemtools, Bibliotheken und Einstellungen enthalten. Sie bieten eine konsistente Umgebung für die Anwendung, unabhängig von der Infrastruktur.

### Orchestrierung und Management

Kubernetes ist eine führende Orchestrierungsplattform, die das Deployment, die Skalierung und das Management von Container-Anwendungen automatisiert.

#### Grundkonzepte von Kubernetes

- **Pods:** Die kleinste Einheit, die in Kubernetes erstellt und verwaltet wird.
- **Services:** Abstraktion, die einen logischen Satz von Pods definiert und eine Politik zur Zugriffssteuerung darauf anwendet.
  
## Verständnisfragen zur Cloud

**1. Warum ist die Cloud-Technologie für die moderne Softwareentwicklung unverzichtbar geworden?**

<details>
<summary>Antwort</summary>

Die Cloud-Technologie bietet Flexibilität, Skalierbarkeit und Effizienz, die weit über die Möglichkeiten traditioneller lokaler Umgebungen hinausgehen. Sie ermöglicht agilere Entwicklungsprozesse und schnellere Bereitstellung von Anwendungen.
</details>
<br />

**2. Was versteht man unter dem Begriff "Cloud" und wo befindet sie sich?**

<details>
<summary>Antwort</summary>

Die "Cloud" bezieht sich auf ein Netzwerk von Datenzentren, die über das Internet verteilt sind und verschiedene Dienste bereitstellen. Diese Datenzentren sind weltweit verteilt und ermöglichen es, Daten und Anwendungen näher am Nutzer zu hosten.
</details>
<br />

**3. Welche Vorteile bietet die geografische Verteilung von Datenzentren in der Cloud?**

<details>
<summary>Antwort</summary>

Die geografische Verteilung ermöglicht schnellere Zugriffszeiten, verbesserte Datenschutzmaßnahmen und die Möglichkeit, Dienste näher an den Endnutzern zu hosten, was die Latenz verringert.
</details>
<br />

**4. Was bedeutet die Virtualisierung der Serverressourcen in der Cloud und welche Vorteile bietet sie?**

<details>
<summary>Antwort</summary>

Virtualisierung ermöglicht es mehreren Nutzern oder Unternehmen, gleichzeitig auf die Hardware zuzugreifen, ohne sich gegenseitig zu beeinflussen. Dies führt zu einer effizienteren Ressourcennutzung und Kosteneinsparungen.
</details>
<br />

**5. Wie unterscheiden sich traditionelle lokale Umgebungen von Cloud-basierten Umgebungen in Bezug auf Ressourcen und Skalierbarkeit?**

<details>
<summary>Antwort</summary>

Traditionelle lokale Umgebungen sind oft durch begrenzte Ressourcen, hohe Wartungskosten und mangelnde Skalierbarkeit gekennzeichnet. Cloud-Umgebungen bieten hingegen flexible und skalierbare Ressourcen, die nach Bedarf angepasst werden können.
</details>
<br />

**6. Erkläre das Pay-as-you-go-Modell der Cloud-Dienste und seine Kosteneffizienz.**

<details>
<summary>Antwort</summary>

Das Pay-as-you-go-Modell bedeutet, dass nur für die tatsächlich genutzten Ressourcen bezahlt wird. Dies führt zu signifikanten Kosteneinsparungen im Vergleich zum Vorhalten eigener Infrastruktur.
</details>
<br />

**7. Welche Rolle spielt die Cloud bei der Unterstützung agiler Entwicklungspraktiken und der CI/CD-Pipelines?**

<details>
<summary>Antwort</summary>

Cloud-Dienste unterstützen agile Entwicklungspraktiken, indem sie Continuous Integration/Continuous Deployment (CI/CD) Pipelines und DevOps-Tools bereitstellen, die eine schnellere und effizientere Entwicklung und Bereitstellung von Anwendungen ermöglichen.
</details>
<br />

**8. Welche erweiterten Sicherheitsfunktionen bieten Cloud-Plattformen und warum sind sie wichtig?**

<details>
<summary>Antwort</summary>

Cloud-Plattformen bieten fortschrittliche Sicherheitsfunktionen wie Verschlüsselung, Identitäts- und Zugriffsmanagement, die den Schutz von Web-Apps gewährleisten. Diese Funktionen sind wichtig, um Datenverluste und Sicherheitsverletzungen zu verhindern.
</details>
<br />

**9. Welche Herausforderungen und Risiken sind mit der Nutzung von Cloud-Diensten verbunden, insbesondere in Bezug auf Datenschutz und Compliance?**

<details>
<summary>Antwort</summary>

Herausforderungen und Risiken umfassen Datenschutzverletzungen, unzureichende Zugriffskontrollen, hohe Kosten durch falsche Konfiguration und Sicherheitslücken. Unternehmen müssen diese Aspekte verstehen und entsprechende Maßnahmen ergreifen, um sicher und kosteneffizient zu arbeiten.
</details>
<br />

## Weiterführende Materialien

- **Microsoft Azure Fundamentals**: Microsoft bietet eine dreiteilige Serie, die grundlegende Cloud-Konzepte vermittelt - [Microsoft Azure Fundamentals](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/).
- **AWS Cloud Essentials**: AWS bietet eine Einführung in die grundlegenden Konzepte des Cloud-Computings und der AWS-Cloud - [AWS Cloud Essentials](https://aws.amazon.com).
- **CCSP 2022: Cloud Computing Concepts & Reference Architectures von Skillsoft**: Umfassende Einführung in die grundlegenden Definitionen, Merkmale und Bausteine des Cloud-Computings - [NICCS](https://niccs.cisa.gov).
- **Grundlagen des Cloud-Computings von Lucidchart**: Einführung in die verschiedenen Cloud-Modelle wie private, öffentliche und hybride Clouds. - [Lucidchart](https://www.lucidchart.com).
