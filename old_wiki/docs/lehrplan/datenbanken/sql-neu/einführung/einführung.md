# Einführung in SQL

<details>
<summary>
Video 🎦
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/xp9chk334_E?si=lMsI26xaMCagaKeo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

## Was ist eine Datenbank?

Eine Datenbank ist eine Zusammenfassung von Daten und Datenbankelementen (siehe unten). Diese Sammlung kann
z.B. eine große Datei sein. Im einfachsten Fall ein Excel-Sheet. In der modernen Welt verbergen sich hinter jedem Service oder Tool, das wir verwenden, eine Vielzahl an Datenbanken.

Von Sozialen-Netzwerken über Flugreservierungssysteme und eure Anstellung bei VW, überall braucht es Datenbanken um Informationen strukturiert zu speichern und wieder auszulesen.

## Was sind Datenbankelemente?

Datenbankelemente sind die Bestandteile einer Datenbank, die Daten speichern, verarbeiten und darstellen.
Hierzu gehören:

- [Tabellen](../tabellen/tabellen.md) in diesen werden die Daten gespeichert.
- [Indizes](../indizes/indizes.md) sind Strukturen, die das Auffinden von Daten beschleunigen.
- [Schlüssel](../tabellen3/tabellen3.md) Schlüssel sind Bedingungen, die Tabellen sinnhaft miteinander verbinden.
- [Funktionen und Prozeduren](../exkurs_sql_scripte/exkurs_sql_scripte.md) sind Programme, die Daten verarbeiten.
- Views zeigen Teile und Zusammenfassungen von Tabellen an.
- Trigger sind Programme, die ereignisgesteuert ausgeführt werden (z.B. neuer Kunde in der Datenbank -> Email auf Gültigkeit prüfen).

Auf Funktionen und Prozeduren werden wir nicht eingehen, da Sqlite hier nur eine eingeschränkte Funktionalität besitzt.
Sichten und Trigger sind Bestandteil eines weiterführenden Kurses und werden daher in diesem Kurs nicht betrachtet.

Nehmen wir uns ein einfaches Beispiel für eine Tabelle in einer Datenbank. Stell dir vor, du hast ein Programm geschrieben,
das auf Kundendaten zugreift. Diese Kundendaten liegen nun in einer Datenbank mit einer Tabelle namens `Kunden`. Diese sieht z.B. wie die folgende aus:

| Name             | Adresse                           | Email                  | Geburtstag | Beruf                  |
|------------------|-----------------------------------|------------------------|------------|------------------------|
| Max Mustermann   | Musterstraße 1, 12345 Musterstadt | max@muster.de          | 01.01.1980 | Softwareentwickler     |
| Erika Mustermann | Musterstraße 1, 12345 Musterstadt | erika@example.com      | 02.02.1985 | Projektmanagerin       |
| Anna Schmidt     | Hauptstraße 3, 34567 Hauptstadt   | anna.schmidt@mail.com  | 03.03.1990 | Verkäuferin            |
| Peter Pan        | Nebenweg 4, 45678 Bergstadt       | peter@pan.de           | 04.04.1995 | Lehrer                 |
| Julia Klein      | Kurzgasse 5, 56789 Kurzstadt      | julia.k@web.de         | 05.05.2000 | Marketing Spezialistin |
| Lars Groß        | Langstraße 6, 67890 Langstadt     | lars.gross@email.com   | 06.06.1975 | Ingenieur              |
| Svenja Klein     | Ringstraße 7, 78901 Ringstadt     | svenja.klein@web.de    | 07.07.1980 | Projektmanagerin       |
| Timo Werner      | Parkallee 8, 67890 Langstadt      | timo@werner.de         | 08.08.1985 | Fußballspieler         |
| Mia Sommer       | Sommerweg 9, 90123 Sommerstadt    | mia.sommer@gmail.com   | 09.09.1990 | Juristin               |
| Noah Fischer     | Fischerstraße 10, 67890 Langstadt | noah.fischer@mail.com  | 10.10.1995 | Koch                   |
| Luisa Horn       | Hornweg 11, 12345 Hornstadt       | luisa@horn.de          | 11.11.2000 | Musikerin              |
| Felix Baum       | Baumallee 12, 23456 Baumstadt     | felix.baum@example.com | 12.12.1975 | Ingenieur              |
| Emma Walz        | Walzgasse 13, 34567 Walzstadt     | emma@walz.de           | 13.13.1980 | Verkäuferin            |
| Jonas Berg       | Bergstraße 14, 45678 Bergstadt    | jonas.berg@web.de      | 14.14.1985 | IT-Berater             |
| Sophia Fluss     | Flussufer 15, 56789 Flussstadt    | sophia.fluss@email.com | 15.15.1990 | Biologin               |

### Aufgabe: Ein erster Blick 🌶
Wie heißen die Ingenieure? Wie gehst du dabei vor, diese Frage zu beantworten?

## Was ist SQL?

Wir brauchen eine Möglichkeit, wie der Computer mit der Datenbank kommunizieren kann, um z.B. die Frage der letzten
Aufgabe zu beantworten. Hier kommt **SQL** ins Spiel. SQL ist eine Sprache, um mit Datenbanken zu kommunizieren.
SQL steht für **S**tructured **Q**uery **L**anguage, auf Deutsch "strukturierte Abfragesprache".

Die Frage, wie die Ingenieure heißen, würde man z.B. mit der folgenden SQL-Abrage lösen:

```sql
SELECT name FROM Kunden WHERE Beruf LIKE "Ingenieur";
```
Wenn du diesen Satz mal laut vorließt und übersetzt, wirst du feststellen, dass er recht sprechend unsere Anfrage beschreibt.

Wir erhalten dann als Antwort:

| Name             |
|------------------|
| Lars Groß        |
| Felix Baum       |

Wir können uns natürlich jegliche Informationen, z.B. Name und Email, aus unserer Datebank für die jeweiligen Einträge zurückgeben lassen.

```sql
SELECT name, email FROM Kunden WHERE Beruf LIKE "Ingenieur";
```

Was zu folgende Ergebnisse führen würde:

| Name       | Email                |
|------------|----------------------|
| Lars Groß  | lars.gross@email.com |
| Felix Baum | felix.baum@example.com |

Die SQL-Sprache stellt alle Befehle für die Verwaltung des Datenbankprogramms, von Datenbankelementen und den Umgang mit
den Daten zur Verfügung.

Wir werden in den folgenden Kapiteln lernen, mithilfe von SQL:

* Datenbanken zu erstellen
* Tabellen zu erstellen
* Daten in Tabellen zu speichern (**C**reate)
* Daten aus Tabellen auszulesen (**R**ead)
* Daten in Tabellen zu ändern (**U**pdate)
* Daten in Tabellen zu lösen (**D**elete)

## Was ist ein Datenbankprogramm?

Um mit einer Datenbank zu kommunizieren bzw. diese zu verwalten, benötigen wir ein **Datenbankprogramm**.

Ein Datenbankprogramm ist eine Software, mit der die Sammlungen von Datenbankelemente verwaltet werden können.

Es gibt viele verschiedene Datenbankprogramme, deren SQL-Sprachen sich leicht unterscheiden, was man auch Dialekte nennt.
Z.B. gibt es:

- [mySQL](https://www.mysql.com/)
- [Oracle](https://www.oracle.com/database/)
- [postGreSQL](https://www.postgresql.org/)
- [Elasticsearch](https://www.elastic.co/de/)
- [MongoDB (No-SQL)](https://www.mongodb.com/de-de)

Wir werden uns mit **[SQLite3](https://www.sqlite.org/)**, da es Bestandteil von Python ist, befassen.

Datenbankprogramme werden oft abgekürzt als **DBMS** (**D**aten**b**ank**m**anagment**s**ystem).
Häufig werden die Datenbankprogramme selbst auch als Datenbanken bezeichnet. Doch von dieser Doppelverwendung des
Begriffes lassen wir uns nun nicht mehr verwirren 😉

## Die Klassen der SQL Sprachelemente

Um die Vielfalt der Sprachelemente besser überblicken zu können, unterscheidet man verschiedene Klassen von Befehlen, unter anderen:

- **DDL (Data Definition Language)**: Befehle, die Datenstrukturen in der Datenbank definieren, verwalten und
  modifizieren.
- **DML (Data Manipulation Language)**: Befehle, die sich mit in der Datenbank gespeicherten Daten befassen.
- **DQL (Data Query Language)**: Befehle, die Daten abrufen.
- **DCL (Data Control Language)**: Befehle, die Berechtigungen und Zugriffsrechte verwalten.
