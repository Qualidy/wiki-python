# Schlussbemerkungen

## Sprachvielfalt in Datenbanksystemen

Standards existieren zwar in der Datenbankwelt, jedoch tendieren führende Unternehmen wie Microsoft, SAP oder Oracle
dazu, eigene sprachliche Varianten in ihre Produkte zu integrieren. Diese Abweichungen vom Standard erschweren die
übergreifende Zusammenarbeit erheblich.

Die Sprachdefinition des Standards umfasst allein für den DML-Teil über 1500 Seiten, doch eine vollständige
Implementierung ist bislang ausgeblieben.

## Serverseitige vs. Clientseitige Verarbeitung

Die Fähigkeiten von Datenbanken gehen weit über das bisher Besprochene hinaus. Themen wie Stored Procedures, Table
Functions, Scalar Functions oder Trigger wurden noch nicht behandelt.

Dies könnte teilweise auf einen Trend zurückzuführen sein, der sich in den letzten Jahren entwickelt hat. SQL und seine
Programmierbarkeit entstanden in einer Zeit, in der Netzwerkverkehr teuer und langsam war, was eine Minimierung des
Datentransfers erforderlich machte.

Mit der gestiegenen Leistungsfähigkeit des Internets und moderner PCs wird dieser Ansatz jedoch zunehmend in den
Hintergrund gedrängt, und es werden mehr Daten über das Netzwerk übertragen. Datenbanken drohen zu reinen Datenspeichern
zu werden, während die gesamte Verarbeitung auf den Client-Seiten stattfindet. Dabei wird oft übersehen, wie sehr dies
das Netzwerk belastet, insbesondere wenn komplette Tabelleninhalte anstatt nur der Ergebnisse zum Client übertragen
werden.

Dieser Trend spiegelt sich auch in der zwar älteren, aber immer noch relevanten Programmiersprache PHP wider, die
ursprünglich für das Serverseitige Rendering von HTML/CSS konzipiert war, um die Seitengrößen gering zu halten. Heute
werden jedoch umfangreiche Datenmengen, einschließlich Bilder, Audio, Grafiken und Videos, über das Netzwerk übertragen.

Im beruflichen Alltag, fernab von privaten Anwendungen, spielen jedoch wirtschaftliche Überlegungen eine entscheidende
Rolle. Dialoge und Prozesse müssen effizient und zielgerichtet gestaltet sein, damit Mitarbeiter ihre Aufgaben schnell
und korrekt erledigen können. Mit Millionen von Datensätzen in Datenbanken ist es unerlässlich, Daten serverseitig zu
verarbeiten und nur die notwendigen Informationen zurückzusenden. Dies ist insbesondere bei Geoinformationssystemen von
Bedeutung, um die Downloadzeiten zu minimieren.

## Duale Programmiersprachen

Die Anzahl der Programmiersprachen, die sowohl client- als auch serverseitig einsetzbar sind, hat zugenommen.

Dies entfernt die Entwickler jedoch von den optimierten und effizienten Möglichkeiten, die Datenbanksysteme bieten.
Anstatt das Rad neu zu erfinden, sollten die Vorteile der integrierten Funktionalitäten genutzt werden, um effiziente
Lösungen zu erzielen.

## Fazit

Datenbanken sind weit mehr als bloße Tabellenspeicher. Ihr Potenzial sollte genutzt werden, wenn es angebracht ist. Es
ist nicht immer möglich oder ratsam, aber es sollte stets in Betracht gezogen werden.

[zurück](../datenbanken.md)