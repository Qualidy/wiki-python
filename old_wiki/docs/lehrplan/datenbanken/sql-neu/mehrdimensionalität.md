


## verschiedenartige Tabellen

Tabellen können in mehreren Dimensionen dargestellt werden.



### Eine eindimensionale Tabelle ist eine Liste:

| Ware    |
|:--------|
| Bananen |
| Gurken  |
| Milch   |

### Zweidimensionale Tabellen

Eine zweidimensionale Tabelle hat mehrere Spalten und ist die übliche Vorstellung, die wir auch von Excel her kennen.
Die Anzahl der Spalten ist durch das jeweilige Datenbankprogramm begrenzt. Es ist natürlich leicht verständlich, dass man die
Spaltenanzahl nicht zu groß wählt, um die Übersichtlichkeit nicht zu verlieren. Auch für die Anzahl der Zeilen gelten
Regeln. Da diese aber durchaus im Bereich von Millionen oder sogar Milliarden liegen, wollen wir das hier nicht
weiter vertiefen. Im Zweifel hilft die Dokumentation zum Datenbankprogramm.

| Ware    | Stück |
|:--------|:------|
| Bananen | 4     |
| Gurken  | 2     |
| Milch   | 1     |

### Drei- und mehrdimensionale Tabellen

Solche Tabellen kennen wir vielleicht aus der höheren Mathematik oder aus anderen
Programmiersprachen mit mehrdimensionalen Arrays. Auch Excel kann so etwas verarbeiten. Nehmen wir das Beispiel der
Einkaufstabelle und erweitern sie durch das Hinzufügen einer Spalte wie folgt, damit eine dreidimensionale Tabelle
entsteht:

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

Wieso ist diese Tabelle jetzt plötzlich dreidimensional? Sieht doch genauso aus wie die anderen.

### Aufgabe: Versuchen Sie eine Erklärung 🌶️🌶️🌶️

<details>
<summary>
Lösung:
</summary>
<ul>
<li>Die Unterscheidung liegt in der folgenden Möglichkeit der Veränderung:</li>
<li>Man könnte diese Tabelle in drei gleichartige Tabellen teilen und aufeinander stapeln. 
Nehmen wir Excel wieder als Beispiel. Hier würde man drei gleichartige Tabellenblätter erstellen und 
diesen die Namen A, B und C zuordnen.
</li>
<li>Die Waren wiederholen sich im Rythmus der Einkäufer. Daher die Gleichartigkeit der Tabellen.</li>
<li>Man hätte dann in der x-Achse die Stückzahl, in der y-Achse die Warenart, und in der z-Achse den Einkäufer. 
Also drei Dimensionen.</li>
<li>Für Menschen sind Informationen in mehrdimensionalen Strukturen schwer vorstellbar 
und nur über Hilfskonstrukte darstellbar. Daher verbleiben wir bei der zweidimensionalen Darstellung.</li>
</ul>
</details>