# Normalisierung von Daten

Schauen wir uns noch einmal diese Tabelle genauer an:

| Einkäufer | Ware    | Stück |
|-----------|:--------|:------|   
| A         | Bananen | 4     |
| A         | Gurken  | 0     |
| A         | Milch   | 0     |
| B         | Bananen | 0     |
| B         | Gurken  | 2     |
| B         | Milch   | 0     |
| C         | Bananen | 0     |
| C         | Gurken  | 0     |
| C         | Milch   | 1     |

Es ist leicht zu erkennen, dass sich Texte wiederholen. A,B,C und Bananen, Gurken, Milch sind mehrfach vorhanden.
Verändern wir die Tabelle, sodass sie realistischer ist:

| Einkäufer  | Ware    | Stück |
|------------|:--------|:------|
| Anton      | Bananen | 4     |
| Anton      | Gurken  | 0     |
| Anton      | Milch   | 0     |
| Bertholt   | Bananen | 0     |
| Bertholt   | Gurken  | 2     |
| Bertholt   | Milch   | 0     |
| Christiane | Bananen | 0     |
| Christiane | Gurken  | 0     |
| Christiane | Milch   | 1     |

Es wird deutlich, dass diese Namen viel mehr Speicher verbrauchen, aber gleichzeitig wird die Absicht hinter der Tabelle
klarer. Allerdings muss man den Schreibfehler bei 'Bertolt' in drei Zeilen einzeln korrigieren (zu 'Bertold').

Stellen wir uns vor, die Bezeichnung von 'Milch' müsste geändert werden in 'Milch 3,5% Fett'. Wieder müssten drei
Zellen geändert werden.

Ziehen wir die Namen und Waren doch aus der Tabelle heraus und ersetzen sie durch Hinweise. Man nennt diese Hinweise
auch Zeiger oder Schlüssel (englisch: index oder key. Der englische Name für Zeigefinger ist "index finger").

Bleiben wir zunächst bei der Bezeichnung Index.

Tabelle Einkäufer:

| Index | Name       |
|-------|:-----------|
| 1     | Anton      |
| 2     | Bertolt    |
| 3     | Christiane |

Tabelle Waren:

| Index | Ware    |
|-------|:--------|
| 1     | Bananen |
| 2     | Gurken  |
| 3     | Milch   |

Tabelle Einkaufsliste:

| Einkäufer | Ware | Stück |
|-----------|:-----|:------|
| 1         | 1    | 4     |
| 1         | 2    | 0     |
| 1         | 3    | 0     |
| 2         | 1    | 0     |
| 2         | 2    | 2     |
| 2         | 3    | 0     |
| 3         | 1    | 0     |
| 3         | 2    | 0     |
| 3         | 3    | 1     |

Nach dieser Aufräumaktion ist keine Information mehr mehrfach vorhanden.
Diesen Vorgang des Aufräumens nennt man **Normalisieren**.

**Hinweis:** Es gibt insgesamt 6 Stufen der Normalisierung. Man spricht hier von Normalformen (NF). Die hier gezeigte
Normalisierung entspricht der Stufe 3NF. Wir gehen hier näher auf [Normalformen](normalization.md) ein. Dies ist aber
ein vertiefendes Thema und für den weiteren Verlauf des Kurses zunächst nicht notwendig.

Um den Bertold jetzt zu korrigieren, muss nur noch eine einzige Zelle geändert werden. Auch der Speicherbedarf ist
geringfügig kleiner geworden. Geringfügig daher, weil nun drei Tabellen zu verwalten sind. Ein echter Spareffekt stellt
sich aber schnell bei längeren Tabellen ein.

### Aufgabe: Normalisieren Sie folgende Tabelle so weit wie möglich. 🌶️🌶️

### Aufgabe: Schreiben Sie die SQL Befehle zur Erstellung der notwendigen neuen Tabellen 🌶️🌶️

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

<details>
<summary>
Lösung:
</summary>

<h3>Tabelle Berufe</h3>
<table>
    <tr>
        <th>Index</th>
        <th>Beruf</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Softwareentwickler</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Projektmanagerin</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Verkäuferin</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Lehrer</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Marketing Spezialistin</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Ingenieur</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Fußballspieler</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Juristin</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Koch</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Musikerin</td>
    </tr>
    <tr>
        <td>11</td>
        <td>IT-Berater</td>
    </tr>
    <tr>

        <td>12</td>
        <td>Biologin</td>
    </tr>
</table>

```sql
  CREATE TABLE Berufe
  (
      BerufeIndex INT,
      Beruf       TEXT
  );
```

<h3>Tabelle Orte</h3>
<table>
    <tr>
        <th>Index</th>
        <th>Stadt</th>
    </tr>
    <tr>
        <td>1</td>
        <td>12345 Musterstadt</td>
    </tr>
    <tr>
        <td>2</td>
        <td>34567 Hauptstadt</td>
    </tr>
    <tr>
        <td>3</td>
        <td>45678 Bergstadt</td>
    </tr>
    <tr>
        <td>4</td>
        <td>56789 Kurzstadt</td>
    </tr>
    <tr>
        <td>5</td>
        <td>67890 Langstadt</td>
    </tr>
    <tr>
        <td>6</td>
        <td>78901 Ringstadt</td>
    </tr>
    <tr>
        <td>7</td>
        <td>12345 Hornstadt</td>
    </tr>
</table>

```sql
  CREATE TABLE Orte
  (
      OrteIndex INT,
      Stadt     TEXT
  )
```

<h3>Tabelle Personen</h3>
<table>
    <tr>
        <th>Name</th>
        <th>Strasse</th>
        <th>Ort</th>
        <th>Email</th>
        <th>Geburtstag</th>
        <th>Beruf</th>
    </tr>
    <tr>
        <td>Max Mustermann</td>
        <td>Musterstraße 1</td>
        <td>1</td>
        <td>max@muster.de</td>
        <td>01.01.1980</td>
        <td>1</td>
    </tr>
    <tr>
        <td>Erika Mustermann</td>
        <td>Musterstraße 1</td>
        <td>1</td>
        <td>erika@example.com</td>
        <td>02.02.1985</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Anna Schmidt</td>
        <td>Hauptstraße 3</td>
        <td>2</td>
        <td>anna.schmidt@mail.com</td>
        <td>03.03.1990</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Peter Pan</td>
        <td>Nebenweg 4</td>
        <td>3</td>
        <td>peter@pan.de</td>
        <td>04.04.1995</td>
        <td>4</td>
    </tr>
    <tr>
        <td>Julia Klein</td>
        <td>Kurzgasse 5</td>
        <td>4</td>
        <td>julia.k@web.de</td>
        <td>05.05.2000</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Lars Groß</td>
        <td>Langstraße 6</td>
        <td>5</td>
        <td>lars.gross@email.com</td>
        <td>06.06.1975</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Svenja Klein</td>
        <td>Ringstraße 7</td>
        <td>6</td>
        <td>svenja.klein@web.de</td>
        <td>07.07.1980</td>
        <td>2</td>
    </tr>
    <tr>
        <td>Timo Werner</td>
        <td>Parkallee 8</td>
        <td>7</td>
        <td>timo@werner.de</td>
        <td>08.08.1985</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Mia Sommer</td>
        <td>Sommerweg 9</td>
        <td>8</td>
        <td>mia.sommer@gmail.com</td>
        <td>09.09.1990</td>
        <td>8</td>
    </tr>
    <tr>
        <td>Noah Fischer</td>
        <td>Fischerstraße 10</td>
        <td>5</td>
        <td>noah.fischer@mail.com</td>
        <td>10.10.1995</td>
        <td>9</td>
    </tr>
    <tr>
        <td>Luisa Horn</td>
        <td>Hornweg 11</td>
        <td>9</td>
        <td>luisa@horn.de</td>
        <td>11.11.2000</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Felix Baum</td>
        <td>Baumallee 12</td>
        <td>10</td>
        <td>felix.baum@example.com</td>
        <td>12.12.1975</td>
        <td>6</td>
    </tr>
    <tr>
        <td>Emma Walz</td>
        <td>Walzgasse 13</td>
        <td>2</td>
        <td>emma@walz.de</td>
        <td>13.13.1980</td>
        <td>3</td>
    </tr>
    <tr>
        <td>Jonas Berg</td>
        <td>Bergstraße 14</td>
        <td>3</td>
        <td>jonas.berg@web.de</td>
        <td>14.14.1985</td>
        <td>11</td>
    </tr>
    <tr>
        <td>Sophia Fluss</td>
        <td>Flussufer 15</td>
        <td>11</td>
        <td>sophia.fluss@email.com</td>
        <td>15.15.1990</td>
        <td>12</td>
    </tr>
</table>

```sql
  CREATE TABLE Personen
  (
      Name       TEXT,
      Strasse    TEXT,
      Ort        INT,
      Email      TEXT,
      Geburtstag DATE,
      Beruf      INT
  )
```

</details>
