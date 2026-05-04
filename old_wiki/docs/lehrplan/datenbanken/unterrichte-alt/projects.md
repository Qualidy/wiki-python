# Gruppenarbeit - Projekte

Nachdem wir gemeinsam die grundlegenden Sprachelemente von SQL in einem intensiven Lernprozess erarbeitet haben, stehen
wir nun an einem spannenden Wendepunkt unserer Ausbildung. Es ist an der Zeit, das bisher erworbene Wissen zu festigen
und durch praktische Anwendung zu vertiefen. In diesem nächsten Abschnitt unserer Ausbildung werden wir uns in Gruppen
aufteilen und uns auf Projekte konzentrieren, die uns helfen, unsere Fähigkeiten in der realen Welt anzuwenden und zu
erweitern.

Jede Gruppe wird die Möglichkeit haben, ein Projektthema auszuwählen, das sowohl herausfordernd als auch interessant
ist. Diese Projekte sollen als Plattform dienen, um das Gelernte in die Praxis umzusetzen, Problemlösungsfähigkeiten zu
entwickeln und kreativ mit Daten zu arbeiten. Alternativ können die Teilnehmer sich auch selbst einem der
vorgeschlagenen Themen zuordnen, je nach ihren Interessen und Zielen.

## Themenvorschläge für Projekte 🌶️🌶️🌶️

1. [**Kundendatenbank für ein Einzelhandelsunternehmen**](beispiel_projekt_kaufhaus.md): Entwickeln Sie eine Datenbank, die Kundeninformationen,
   Kaufhistorie und Produktbestände verwaltet. Dieses Projekt könnte auch Aspekte wie Kundenloyalitätsprogramme und
   Inventarmanagement umfassen.

2. **Buchungs- und Reservierungssystem für ein kleines Hotel**: Erstellen Sie eine Datenbank, die Reservierungen,
   Zimmerbelegungen und Gästeinformationen verwaltet. Das System könnte auch Funktionen für die Abrechnung und die
   Verwaltung von Dienstleistungen beinhalten.

3. **Veranstaltungsmanagement-System**: Entwickeln Sie eine Datenbank zur Verwaltung von Veranstaltungen, einschließlich
   Informationen zu Veranstaltungsorten, Teilnehmern und Zeitplänen. Dies könnte auch die Handhabung von Ticketverkäufen
   und Teilnehmerfeedback einschließen.

4. **Schulverwaltungssystem**: Erstellen Sie eine Datenbank, die Schülerdaten, Kursinformationen, Lehrpläne und Noten
   verwaltet. Dieses Projekt könnte auch Aspekte wie Anwesenheitsverfolgung und Lehrerzuweisungen beinhalten.

5. **Personalverwaltungssystem für kleine Unternehmen**: Entwickeln Sie eine Datenbank zur Verwaltung von
   Mitarbeiterdaten, Gehaltsabrechnungen, Urlaubsanträgen und Leistungsbeurteilungen.

Diese Projekte sind so konzipiert, dass sie sowohl herausfordernd als auch lehrreich sind, und bieten eine
ausgezeichnete Gelegenheit, die praktische Anwendung von SQL in verschiedenen realen Szenarien zu erleben. Wählen Sie
ein Thema, das Sie am meisten anspricht, und beginnen Sie, die Welt der Datenbanken zu erkunden und zu gestalten!

## Leitfaden für die Entwicklung von SQL-Projekten

Die Entwicklung eines Datenbankprojekts ist ein komplexer Prozess, der sowohl technische Fähigkeiten als auch Teamarbeit
erfordert. Hier ist ein Leitfaden, der Ihnen und Ihrer Gruppe helfen soll, ein erfolgreiches Projekt zu gestalten:

1. **Freie Diskussion innerhalb der Gruppe**: Beginnen Sie mit einer offenen Diskussionsrunde, um Ideen zu sammeln und
   die Ziele des Projekts zu definieren. Jedes Teammitglied sollte seine Gedanken und Perspektiven einbringen können.

2. **Entwicklung von UML-Diagrammen**: Visualisieren Sie die Struktur Ihrer Datenbank mit UML-Diagrammen. Dies umfasst
   die Erstellung von Entitäts-Beziehungs-Diagrammen, um die Beziehungen zwischen den verschiedenen Tabellen und
   Entitäten zu klären.

3. **Normalsprachliche Pseudo-Syntax**: Formulieren Sie die Anforderungen und Funktionen Ihrer Datenbank in einer
   einfachen, verständlichen Sprache. Dies hilft dabei, die technischen Aspekte des Projekts für alle Teammitglieder
   zugänglich zu machen.

4. **Festlegen von Begriffen der Domäne**: Definieren Sie die Schlüsselbegriffe und Konzepte Ihrer Anwendungsdomäne. Ein
   klares Verständnis der Fachterminologie ist entscheidend für die Entwicklung einer kohärenten und funktionalen
   Datenbank.

5. **Finden von Indizes, Constraints, Defaults, Datentypen**: Bestimmen Sie die geeigneten Datentypen für jede Spalte
   und identifizieren Sie, wo Indizes, Constraints (wie Primärschlüssel, Fremdschlüssel, Unique-Constraints) und
   Default-Werte benötigt werden, um die Integrität und Leistung Ihrer Datenbank zu optimieren.

6. **Schreiben von Scripts zur Erstellung der Datenbank als Batch**: Entwickeln Sie SQL-Skripte, die Ihre
   Datenbankstruktur definieren. Diese Skripte sollten alle notwendigen Befehle enthalten, um Tabellen zu erstellen,
   Beziehungen zu definieren und die Datenbank zu initialisieren.

7. **Füllen der Datenbank mit Daten als Script**: Erstellen Sie Skripte, um Ihre Datenbank mit initialen Daten zu
   füllen. Dies kann Testdaten oder reale Datensätze umfassen, die für die Entwicklung und das Testen der Datenbank
   erforderlich sind.

8. **Diskussion über die Fragen an die Datenbank**: Besprechen Sie, welche Arten von Abfragen die Datenbank beantworten
   soll. Dies beinhaltet das Verständnis der Benutzeranforderungen und wie die Datenbank diese Anforderungen erfüllen
   kann.

9. **Formulierung der Fragen in Normalsprache**: Übersetzen Sie die Anforderungen in normalsprachliche Formulierungen.
   Dies hilft dabei, die SQL-Abfragen zu definieren, die später implementiert werden müssen. Während dieses Prozesses
   werden Sie feststellen, dass ein wesentliches Stilmittel in der Datenbankentwicklung noch
   fehlt.
   Die Normalisierung der Daten muss für die sinnvolle Darstellung der Daten wieder umgekehrt werden. JOINs ermöglichen
   es, getrennte Daten, die durch den Normalisierungsprozess in verschiedene
   Tabellen aufgeteilt wurden, wieder zusammenzuführen. Sie sind entscheidend für die Durchführung komplexer Abfragen
   und
   die Gewinnung von Einsichten aus den relationalen Daten. Dieses Verständnis wird Ihnen helfen, effektivere und
   leistungsfähigere Datenbankabfragen zu entwickeln.

10. **Hilfestellung**: Stellen sie sich vor, dass ein Programm auf die Datenbank zugreift und Daten für Dialoge erhalten
    möchte oder Daten von den Dialogen empfangen soll. Diese Dialoge dienen zum einen der Darstellung der Daten, zum
    anderen enthalten sie meist Eingabefelder für
    neue Daten oder Optionen zur Darstellung der Daten.

    Beispiel:

    Ein Menüpunkt im Programm heißt "Personal". Die Erwartung des Benutzers wäre wahrscheinlich, dass nach dem Aufruf
    eine Liste der Angestellten zu sehen ist. Hier stellt man sich folgende Möglichkeiten vor:

    - neuen Mitarbeiter anlegen
    - bestehenden Mitarbeiter löschen
    - bestehenden Mitarbeiter bearbeiten
    - Liste nach Kriterien filtern oder sortieren
    
    **Erwartung:**

    - Der erste Punkt öffnet einen leeren Dialog mit Feldern für alle Daten zum neuen Angestellten.
    - Der zweite Punkt sendet direkt ein Kommando an die Datenbank.
    - Der dritte Punkt öffnet einen Dialog mit allen Daten zum Angestellten.
    - Der vierte Punkt lädt die Liste, mit den Kriterien bearbeitet, erneut vom Server.

Entwickeln sie daraus die entsprechenden SQL Kommandos.
