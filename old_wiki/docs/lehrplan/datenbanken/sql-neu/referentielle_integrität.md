# Referentielle Integrität

Die Einführung der Normalisierung und der Zeiger hilft Platz und Aufwand bei Korrekturen zu sparen.
Sie hat aber auch Nachteile:

- Es sind jetzt mehr Tabellen zu verwalten.
- Wenn ich später die Daten wie im Original wieder haben will, muss ich sie wieder zusammenbauen.
- Wenn ich einen Zeiger habe, der auf eine falsche Zeile in einer Tabelle (Datensatz) zeigt, ist meine Datenbank wertlos
  geworden.
- Wenn ein Zeiger auf einen Datensatz zeigt, der nicht mehr existiert, ist er verwaist.
- Was passiert, wenn es einen Zeiger zweimal gibt?

Alle diese Probleme werden unter dem Begriff **Referentielle Integrität** zusammengefasst. Die Zeiger bezeichnet man
auch als Referenz und die Datensätze, auf die sie zeigen werden durch sie referenziert. Das Einhalten der Zusammenhänge
nennt man Integrität.

### Eindeutigkeit und Duplikate bei Zeigern

**In der Tabelle, in der die Spalte Index definiert ist und deren Werte in einer anderen Tabelle referenziert werden,
müssen die Werte eindeutig sein! Es darf keine Duplikate geben.**

Beispiel mit Fehlern:

| Name             | Strasse        | Ort | Email                 | Geburtstag | Beruf |
|------------------|----------------|-----|-----------------------|------------|-------|
| Max Mustermann   | Musterstraße 1 | 1   | max@muster.de         | 01.01.1980 | 1     |
| Erika Mustermann | Musterstraße 1 | 1   | erika@example.com     | 02.02.1985 | 2     |
| Anna Schmidt     | Hauptstraße 3  | 2   | anna.schmidt@mail.com | 03.03.1990 | 3     |
| Peter Pan        | Nebenweg 4     | 3   | peter@pan.de          | 04.04.1995 | 4     |
| Julia Klein      | Kurzgasse 5    | 4   | julia.k@web.de        | 05.05.2000 | 5     |
| Lars Groß        | Langstraße 6   | 6   | lars.gross@email.com  | 06.06.1975 | 6     |

| Index | Beruf                  |
|-------|------------------------|
| 1     | Softwareentwickler     |
| 2     | Projektmanagerin       |
| 3     | Verkäuferin            |
| 6     | Lehrer                 |
| 5     | Marketing Spezialistin |
| 6     | Ingenieur              |
| 7     | Fußballspieler         |

Frage: Welchen Beruf hat Lars Groß?

Erklären Sie, wie, auf welchem Weg genau, wird diese Frage beantwortet?

Antwort:

- Lars Groß in der ersten Tabelle suchen und dann rechts den Index auf Beruf lesen → 6.
- In der zweiten Tabelle die 6 suchen und erkennen, das zwei Datensätze infrage kommen.
- Da eine Entscheidung nicht getroffen werden kann, wird dies als Fehler gemeldet.

Mal angenommen, die Datensätze der zweiten Tabelle wurden zeitlich in der Reihenfolge von oben nach unten eingegeben,
dann hätten beim Ingenieur die Alarmglocken läuten müssen.

An dieser Stelle helfen uns nun Sprachelemente von SQL, um diese Eindeutigkeit und die Alarmglocken zu garantieren.
ABer zunächst müssen wir noch zwei Begriffe deutlich erklären:

**Index und Schlüssel**

Wir haben den Begriff Index in der Verwendung als Zeiger auf andere Tabellen kennengelernt. Es hat sich aber
herausgestellt, dass es eine weitere Bedeutung gibt und daher muss ein zweiter Begriff her, um das zu trennen:
Schlüssel.

Diese beiden Begriffe sind untrennbar mit der referentiellen Integrität verbunden. Daher gehen wir in den nächsten Kapiteln
näher darauf ein.
