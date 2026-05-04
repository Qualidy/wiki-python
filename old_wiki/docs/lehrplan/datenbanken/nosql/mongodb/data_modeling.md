# Exkurs: Datenmodellierung und Design Patterns
[30 min]

## Schema Design Patterns in MongoDB:

In MongoDB bezieht sich der Begriff "Schema Design Patterns" auf bewährte Methoden und Ansätze für das Entwerfen von Dokumentstrukturen. Im Gegensatz zu traditionellen relationalen Datenbanken gibt es in MongoDB kein festes Schema, und die Daten werden in der Regel in BSON-Dokumenten (Binary JSON) gespeichert. Schema Design Patterns bieten Richtlinien und bewährte Praktiken für die Strukturierung von MongoDB-Dokumenten, um die Leistung, Skalierbarkeit und Flexibilität der Datenbank zu optimieren. Im folgenden sind einige wichtige Schema Design Patterns aufgezählt:

### Präkalkulierte Muster (Precomputed Patterns):
Das Precomputed Pattern in MongoDB beinhaltet die vorausschauende Berechnung und Speicherung von Daten direkt im Dokument, um wiederholte Berechnungen während Abfragen zu vermeiden. Diese Methode zielt darauf ab, die Leistung zu steigern, indem Ergebnisse im Voraus ermittelt und in der Datenbank gespeichert werden. Statt Berechnungen jedes Mal durchzuführen, wenn die Daten abgefragt werden, werden die vorab berechneten Werte gespeichert, was zu schnelleren Antwortzeiten und geringerer Belastung der Datenbank führt. Dies ist besonders nützlich in Szenarien, in denen bestimmte Berechnungen teuer sind und sich selten ändern.

### Baumstrukturen (Tree Structures):

Das Schema Design Pattern für Baumstrukturen in MongoDB umfasst zwei Ansätze: materialisierte Pfade und Elternreferenzen.

- **Materialisierte Pfade:**
  Bei diesem Ansatz werden materialisierte Pfade verwendet, um die Baumstruktur abzubilden. Das bedeutet, dass jeder Knoten im Baum einen Pfad zu seinem eigenen Speicherort enthält. Dieser Pfad kann beispielsweise als Zeichenkette dargestellt werden, die die Hierarchie bis zum Wurzelknoten repräsentiert. Die Verwendung materialisierter Pfade erleichtert das Navigieren und Abfragen von Hierarchien in der Baumstruktur.

- **Elternreferenzen:**
  Im Falle von Elternreferenzen enthält jeder Knoten eine explizite Referenz auf seinen Elternknoten. Diese Referenz ermöglicht eine effiziente Navigation von einem Knoten zu seinem Elternteil. Dieser Ansatz erleichtert insbesondere das Traversieren von Eltern zu Kindern oder umgekehrt, was in bestimmten Anwendungsfällen vorteilhaft sein kann. Es ist wichtig zu beachten, dass dieser Ansatz zusätzlichen Speicherplatz für die Verwaltung der Referenzen benötigt, aber er bietet klare Beziehungen innerhalb der Baumstruktur.

### Polymorphe Muster (Polymorphic Patterns):
Polymorphe Muster beziehen sich auf die Verwendung von Schlüsseln zur Typisierung von Dokumenten. Dieses Schema Design Pattern ermöglicht die Kennzeichnung und Unterscheidung verschiedener Dokumenttypen innerhalb einer Sammlung. Bei diesem Ansatz werden spezielle Schlüssel in jedem Dokument verwendet, um den Typ des jeweiligen Dokuments anzugeben. Dieser Schlüssel dient als Markierung oder Kennzeichnung, die auf den spezifischen Typ des enthaltenen Inhalts hinweist. Durch die Nutzung dieses polymorphen Musters können verschiedene Arten von Informationen innerhalb derselben Sammlung effizient verwaltet werden. Es ermöglicht eine flexible Struktur, da unterschiedliche Dokumente innerhalb einer Sammlung unterschiedliche Felder und Strukturen haben können, abhängig von ihrem Typ.

### Caching Patterns:
Caching Pattern bezeichnen die gezielte Speicherung wiederholter Daten direkt in den Dokumenten, um die Notwendigkeit wiederholter Abfragen zu minimieren. Hierbei wird eine Strategie verfolgt, bei der häufig abgerufene oder benötigte Daten in einem Dokument zwischengespeichert werden, um den Zugriff und die Abfrageleistung zu optimieren. Anstatt Daten bei jeder Anfrage erneut abzurufen oder zu berechnen, werden sie im Voraus berechnet und in den entsprechenden Dokumenten zwischengespeichert. Dies ermöglicht eine schnelle Datenabfrage und trägt zur Reduzierung der Gesamtbelastung der Datenbank bei. Durch die gezielte Anwendung von Caching Patterns können Anwendungen reibungsloser und schneller auf wiederholte Datenanfragen reagieren, wodurch die allgemeine Leistungsfähigkeit der MongoDB-Datenbank gesteigert wird.

### Zeitreihenmuster (Time Series Patterns):
Das Zeitreihenmuster bezieht sich auf bewährte Methoden und Ansätze für die effiziente Modellierung und Verwaltung von Zeitreihendaten. Zeitreihendaten sind Informationen, die in zeitlicher Reihenfolge angeordnet sind, wie zum Beispiel Messwerte, Leistungsdaten oder Ereignisse, die im Laufe der Zeit erfasst werden. Innerhalb dieses Musters gibt es verschiedene Techniken, die darauf abzielen, die Leistung, Speichereffizienz und Abfragegeschwindigkeit von Zeitreihendaten zu optimieren. Ein Schlüsselelement dieses Musters ist die sogenannte "Rollende Sammlung". Das Konzept der rollenden Sammlungen besteht darin, für einen begrenzten Zeitraum Sammlungen von Zeitreihendaten zu erstellen. Anstatt alle historischen Daten in einer einzigen Sammlung zu aggregieren, werden periodisch neue Sammlungen erstellt, um die Daten nach Zeitabschnitten zu gruppieren. Dadurch wird nicht nur die Datenbankstruktur optimiert, sondern es erleichtert auch das effiziente Management und die Archivierung alter Daten. Dieses Muster trägt dazu bei, die Leistung bei der Abfrage von Zeitreihendaten zu verbessern, da Anfragen auf diejenigen Sammlungen beschränkt sind, die den relevanten Zeitraum abdecken.

### Bucket Patterns:
Das Bucket-Pattern bezieht sich auf bewährte Methoden zur Strukturierung und Organisation von Daten durch Gruppierung in sogenannten "Buckets" oder Behältern. Es wird oft angewendet, um die Effizienz von Abfragen und Analysen zu steigern, insbesondere wenn große Mengen von Daten verarbeitet werden. Innerhalb dieses Musters erfolgt die Gruppierung von Daten in klar definierten Buckets, wodurch die Verarbeitung und Analyse erleichtert wird. Dies ermöglicht eine gezielte und effiziente Abfrage von Daten, da sie bereits nach relevanten Kriterien vorsortiert sind. Die Anwendung von Bucket-Patterns kann dazu beitragen, die Leistung und Skalierbarkeit von MongoDB-Datenbanken zu verbessern.

### Outlier Patterns:
Das Outlier-Pattern bezieht sich auf bewährte Methoden zur Handhabung von Ausreißern oder ungewöhnlichen Datenpunkten in einer Datenbank. Ein Ausreißer ist ein Datenpunkt, der sich signifikant von der Mehrheit der Daten unterscheidet und potenziell zu verzerrten Analyseergebnissen führen kann. Innerhalb des Outlier-Patterns werden solche Ausreißer in separate Dokumente ausgelagert. Dies ermöglicht eine gezielte Verarbeitung und Analyse von Ausreißern, ohne die Leistung der gesamten Datenbank zu beeinträchtigen.

Durch die Auslagerung von Ausreißern in separate Dokumente können spezifische Maßnahmen ergriffen werden, um mit diesen Daten umzugehen, beispielsweise durch eine detaillierte Analyse, manuelle Überprüfung oder gezielte Bereinigung. Dieses Muster hilft, die Integrität der Gesamtdatenbank zu wahren, da Ausreißer keinen unverhältnismäßigen Einfluss auf Abfragen oder Analysen haben. Es trägt somit zur Verbesserung der Leistung und Konsistenz von MongoDB-Datenbanken bei.

## Data Modeling Patterns in MongoDB:

Neben den Schema Design Patterns gibt es auch Data Modeling Patterns, die sich auf die Strukturierung und Organisation von Daten in MongoDB beziehen. Data Modeling Patterns in MongoDB beziehen sich auf bewährte Methoden für das Modellieren von Daten in einer MongoDB-Datenbank. Im Gegensatz zu relationalen Datenbanken, die Tabellen und Beziehungen verwenden, setzt MongoDB auf flexible, JSON-ähnliche Dokumente, die in BSON (Binary JSON) gespeichert werden. Wir werden in diesem Kurs die Einbettung von Datenmodellen und Verweise (References) genauer betrachten.

### Einbettung von Datenmodellen:
Die "Einbettung von Datenmodellen" meint das Speichern von Dokumenten in anderen DOkumenten. Dies ermöglicht die Strukturierung von Informationen, indem verschiedene Daten in einem einzigen Dokument kombiniert werden. Im Kontext der Data Modeling Patterns betrachten wir zwei Aspekte der Einbettung von Datenmodellen:

**Mehrfache Einbettung (Nested Documents):** 
Dies bezieht sich darauf, dass ein Dokument andere Dokumente als Teil seiner Struktur enthält. Zum Beispiel könnte ein Dokument Informationen zu einem Benutzer enthalten, und innerhalb dieses Benutzerdokuments könnten weitere eingebettete Dokumente Informationen zu den von diesem Benutzer erstellten Postings oder Kommentaren enthalten.
**Arrays:**
Die Verwendung von Arrays ermöglicht es, mehrere Werte oder Dokumente für ein bestimmtes Feld in einem Dokument zu speichern. Dies ist besonders nützlich, wenn eine Entität mehrere Attribute desselben Typs hat. Zum Beispiel könnte ein Dokument eines Autors ein Array von Büchern enthalten, die der Autor geschrieben hat.
Die Einbettung von Datenmodellen bietet den Vorteil, dass zusammengehörige Informationen gemeinsam abgerufen werden können, was die Leistung verbessern kann. Sie eignet sich besonders gut für Anwendungen, bei denen Daten oft gemeinsam verwendet oder aktualisiert werden. Allerdings sollte die Entscheidung für oder gegen die Einbettung von Datenmodellen von den spezifischen Anforderungen und Nutzungsmustern der Anwendung abhängen.

### Verweise (References):
Die Verwendung von "Verweisen" (References) beschreibt, wie Beziehungen zwischen Dokumenten hergestellt werden, indem man auf Dokumente in anderen Sammlungen verweist. Hierbei werden zwei Hauptaspekte betrachtet:

**Manuelle Verweise:**
Dies bezieht sich darauf, dass ein Dokument in einer Sammlung auf ein anderes Dokument in einer separaten Sammlung verweist. Zum Beispiel könnte ein Dokument über einen bestimmten Artikel in einer "Artikel"-Sammlung auf das zugehörige Benutzerdokument in einer "Benutzer"-Sammlung verweisen, um Informationen über den Autor des Artikels zu erhalten.

**DBRefs (Database References):**
MongoDB unterstützt spezielle Strukturen namens DBRefs, die als Referenzen auf Dokumente in anderen Sammlungen dienen. Eine DBRef enthält normalerweise drei Schlüssel: `$ref` (Sammlungsname), `$id` (ID des referenzierten Dokuments) und optional `$db` (Datenbankname). Dies erleichtert das Arbeiten mit Referenzen, da alle notwendigen Informationen in einem speziellen Format bereitgestellt werden.


### Aufgabe: 🌶🌶🌶🌶
[240 min] + [120 min Präsentation]
Teilt euch in Gruppen auf und bearbeitet jeweils ein Design Pattern. Erstellt eine Präsentation inklusive Live-Coding, in der ihr das Schema Design Pattern vorstellt und anhand eines Beispiels erklärt. Die Präsentation sollte einen Umfang von ca. 5 - 10 Minuten haben.