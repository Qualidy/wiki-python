# Exkurs: Monitoring von Cloud Applikationen

[30 min]

Monitoring von Cloud-Applikationen in Azure ist entscheidend für die Leistung, Sicherheit und Zuverlässigkeit Ihrer Anwendungen. Vor allem durch die Eingeschränken Möglichkeiten, loakal getestete Applikationen in der Cloud zu Debuggen, bedarf es zusätzlicher Techniken und Services.

## Azure Monitor

Der [Azure Monitor](https://azure.microsoft.com/de-de/products/monitor) bietet umfassende Lösungen für das Sammeln, Analysieren und Handeln basierend auf Telemetriedaten aus Ihrer Cloud- und On-Premises-Umgebung.

Features sind unter anderen das sammeln von Metriken und Protokollen, Anwendungseinsichten für Leistungsüberwachung und die Netzwerküberwachung und Diagnose.

### Azure Application Insights

Ein Feature von Azure Monitor, das speziell für die Überwachung der Leistung und Verfügbarkeit von Webanwendungen konzipiert ist.

- Automatische Erfassung von Leistungsanomalien.
- Detaillierte Analyse von Anfragen und Fehlerdiagnosen.
- Benutzer- und Sitzungsverfolgung.

## CI/CD mit Azure DevOps

Eine Suite von DevOps-Tools, die das Planen, Entwickeln, Testen und Bereitstellen von Software ermöglichen.

Unter anderem enthalten sind Boards für Planung, Repos für Code-Management, Pipelines für CI/CD und Testpläne und Artefakte.

## Debugging von Cloud-Applikationen

Debugging von Cloud-Applikationen in Azure erfordert ein umfassendes Verständnis und die Anwendung spezifischer Techniken, insbesondere wenn es um das Debuggen von Live-Anwendungen geht. **Remote-Debugging** ist dabei eine Schlüsseltechnik, die es Entwicklern ermöglicht, direkt in einer in der Cloud laufenden Anwendung zu debuggen.

Ein weiterer wesentlicher Aspekt beim Debugging von Cloud-Applikationen ist die **Log-Analyse**. Durch die Nutzung von Protokollen können Entwickler wichtige Informationen über das Verhalten ihrer Anwendung sammeln und analysieren. 

Azure bietet hierfür spezielle Dienste wie [Azure Log Analytics](https://azure.microsoft.com/de-de/products/monitor/) zum sammeln und analysieren von Protokollen aus verschiedenen Azure-Ressourcen. Zusätzlich gibt es den [Snapshot Debugger](https://learn.microsoft.com/en-us/azure/azure-monitor/snapshot-debugger/snapshot-debugger-data), welches den Zustand einer Anwendung im Moment einer Ausnahme erfasst und einsehbar macht.
