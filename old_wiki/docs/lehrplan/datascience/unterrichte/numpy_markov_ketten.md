# Exkurs: Pandemie Simulation
## Markov-Ketten 

### Lernziele für heute

* Verstehen was eine Markov-Kette ist
* Verstehen welche Systeme man durch Markov-Ketten beschreiben kann
* Mit Hilfe von einer Markov-Kette die Entwicklung von einer Epedemie simulieren
* Die Simulation evaluieren

### Markov-Ketten

Markov-Ketten sind ein Werkzeug mit dem man zufallsbasierte Vorgänge modellieren kann. Eine Markov-Kette besteht aus einer Menge an Zuständen, in denen das modellierte Sytsem sich zu unterschiedlichen Zeiten befinden kann, und Übergangswahrscheinlichkeiten für alle Paare von Zuständen aus dieser Menge. Markov-Ketten eignen sich gut um Systeme zu beschreiben, deren Veränderung nur von ihrem derzeitigen Zustand und nicht ihrer Vergangenheit abhängt.

<b>Beispiel:</b>
<p align="center">
    <img src="markov_files/Markov-Chain_example.svg">
</p>
Die Zustandsmenge für unser Beispiel ist:

$$
\{Z_1, Z_2, Z_3\}
$$

## Übergangswahrscheinlichkeiten

Die Übergangswahrscheinlichkeiten sind in der folgenden Matrix dargestellt:

$$
P = \begin{pmatrix}
P(Z_1'|Z_1) & P(Z_2'|Z_1) & 0 \\
0 & 0 & P(Z_3'|Z_2) \\
0 & 0 & P(Z_3'|Z_3)
\end{pmatrix}
$$

Zwei wichtige Adjektive die man kennen muss um Markov-Ketten zu verstehen sind "diskret" und "abzählbar". Diskret und abzählbar haben beide die gleiche Bedeutung und beschreiben Mengen. Eine diskrete Menge hat entweder endlich viele Elemente, oder man kann ihre Elemente abzählen, so dass man nach beliebig vielen Schritten (auch unendlich) allen Elementen eine Nummer zugeteilt hat. Zwei diskrete Mengen wären Beispielweise: {b, c, a, d}, oder {1, 2, 3, 4, ...}. Ein Beispiel für eine nicht-diskrete Menge wären die Reellen Zahlen, also alle Zahlen mit beliebig (auch unendlich) vielen Nachkommastellen. Auch wenn das kein formal richtiger Beweis ist, kann man sich als Intuition, warum sie nicht diskret sind, vorstellen, dass es zwischen zwei beliebigen Reellen Zahlen immer unendlich viele andere Reelle Zahlen gibt. Das Gegenteil von diskret heißt kontinuierlich.

Die Menge der Zustände einer Markov-Kette muss diskret sein. Außerdem soll heute die Menge an Zeitpunkten, an denen unser System seinen Zusand wechseln kann, auch diskret sein.


### Aufgabe 1: Was heißt diskret?

Diskutieren Sie mit ihrem Sitznachbar, ob folgende Mengen diskret sind:

1. Die Menge der Sekunden in einer Minute
2. Die Menge der Zeitpunkte in einer Minute
3. Die Menge der Städte in Europa
4. Die Menge der Orte (im Sinne von Platz) auf der Erde
5. Die Menge an Wörtern, die man aus dem deutschen Alphabet bilden kann

### Aufgabe 2: Was lässt sich mit Markov-Ketten modellieren?

Untersuchen Sie zusammen mit Ihrem Sitznachbar die folgenden Systeme darauf, ob sie sich gut durch eine Markov-Kette beschreiben lassen. Insbesondere sollen Sie betrachten, ob der Zustandsraum und die Zeitpunkte zu denen das System seinen Zustand wechselt diskret sind, so wie ob die Übergangswahrscheinlichkeit zwischen Zuständen nur vom derzeitigen, oder auch von vergangenen Zuständen abhängt.

1. Ein System das kontinuierlich den Ort eines durch die Luft fliegenden Balls angibt
2. Ein System das jede Sekunde den Ort eines durch die Luft fliegenden Balls angibt
3. Ein System das jede Sekunde die abgerundete Distanz in Metern die ein Ball zurücklegt der durch Luft fliegt angibt
4. Ein System das jede Sekunde die abgerundete Distanz und Geschwindigkeit in Metern pro Sekunde die ein Ball zurücklegt der durch Vakuum fliegt angibt

## Epidemiemodellierung

Wir wollen eine Epidemie mit Hilfe von einer Markov-Kette modellieren, also die Entwicklung der Gesunden, Infizierten, Verstorbenen und Genesenen Personen vorhersagen. Eine Vereinfachung die wir treffen ist, dass Genesene nicht wieder "gesund" werden, bzw. nicht ein zweites Mal krank werden können. Als Beispiel verwenden wir die Corona Epedemie in Deutschland, da es hierzu relativ aktuelle Statistiken gibt. Die Daten die wir verwenden wollen stammen von der Johns Hopkins University und sind in folgendem [Git Repository](https://github.com/confusedlama/COVID-19) im Ordner "data" hinterlegt.

Die Daten sind wie folgt aufgebaut:

| date    | healthy | infected | recovered | infected_cumulated | deceased | 
| -------- | ------- | ----------|----------|---------|-----------|
| 1/23/20  | 82 500 000   | 0 | 0 | 0 | 0 |

* "<b> date </b>" ist das Datum zu dem die restlichen Daten der Reihe gehören. *str(Datetime)*

* "<b> healthy </b>" ist die Anzahl der Personen, die sich noch nicht mit Corona angesteckt haben. *int*

* "<b> infected </b>" ist die Anzahl der Personen die momentan mit dem Virus infiziert sind. *int*

* "<b> recovered </b>" ist die Anzahl der Personen die infiziert waren und dann genesen sind. *int*

* "<b> deceased </b>" ist die Anzahl der Personen die als an Corona verstorben gemeldet wurden nachdem sie infiziert waren. *int*

* "<b> infected_cumulated </b>" ist die Anzahl der Personen die insgesamt mit Corona infiziert waren. *int*

### Aufgabe 3: Ein erster Blick in die Daten.

* Beginnen Sie damit das Git Repository zu clonen, und erstellen Sie ein neues Jupyter Notebook, in dem Sie arbeiten können.
* Laden Sie die .csv datei von Deutschland als DataFrame
* Visualisieren Sie sich den DataFrame (das können Sie auch bei den folgenden Aufgaben zwischendurch immer mal machen)

```python
# Code Beispiel für die Visualisierung eines DataFrames in einem Jupyter Notebook
df.plot()

# Code Beispiel für das Speichern einer Visualisierung eines DataFrames in einer Python Datei
figure = df.plot().get_figure()
figure.savefig("pfad_zum_ort_wo_sie_gespeichert_werden_soll")
```

### Aufgabe 4: Wie sieht unsere Zustandsmenge aus?
Wir wollen für jeden Tag wissen wie viele Menschen noch gesund, momentan infiziert, oder bis jetzt genesen und gestorben sind.

* Überlegen Sie mit Ihrem Sitznachbarn, ob die Zustände in der Zustandsmenge der Markov-Kette der Verteilung der Gesamtbevölkerung über die unterschiedlichen Kategorien (gesund, infiziert, ...), oder den Zuständen in denen eine einzelne Person sich befinden kann entsprechen sollten.
* Schreiben Sie die Zustandsmenge Ihrer Markov-Kette auf. Ist sie diskret?
* In welchen zeitlichen Abständen sind die einzelnen Datenpunkte in Ihrem DataFrame aufgenommen, bzw. wird die Entwicklung der Fallzahlen zu diskreten Zeitpunkten betrachtet?
* Die Übergangswahrscheinlichkeiten zu den anderen Zuständen der Zustandsmenge sollten nur vom aktuellen Zustand abhängen. Schätzen Sie wovon die Zahlen des nächsten Tages jeweils abhängen. (nur ganz grob die Trends)
* Zeichnet ein Diagram Eurer Markov-Kette mit ihren Zuständen und Pfeilen zwischen den Zuständen falls die Übergangswahrscheinlichkeit größer als 0 ist.

### Aufgabe 5: Was sind unsere Übergangswahrscheinlichkeiten?
Wir vermerken die Übergangswahrscheinlichkeiten in einer Matrix P:

Übergangswahrscheinlichkeiten:

$$
\begin{array}{|c|c|c|c|c|}
\hline
P & H & I & R & D \\
\hline
H' & P(H'|H) & P(H'|I) & P(H'|R) & P(H'|D) \\
\hline
I' & P(I'|H) & P(I'|I) & P(I'|R) & P(I'|D) \\
\hline
R' & P(R'|H) & P(R'|I) & P(R'|R) & P(R'|D) \\
\hline
D' & P(D'|H) & P(D'|I) & P(D'|R) & P(D'|D) \\
\hline
\end{array}
$$

Sie sollen nun die Übergangswahrscheinlichkeiten zwischen ihren Zuständen berechnen. Die echten Wahrscheinlichkeiten zu berechnen ist relativ schwer. Beispielsweise wäre die Wahrscheinlichkeit, dass ein gesunder Mensch infiziert wird abhängig von der Wahrscheinlichkeit, dass ein gesunder Mensch einen infizierten Menschen trifft und der Wahrscheinlichkeit, dass ein infizierter Mensch einen gesunden Menschen ansteckt, wenn sie sich treffen. Diese Wahrscheinlichkeiten können wir nicht berechnen, da wir keine Daten dazu haben, wie sich die Bevölkerung bewegt, bzw. wie ansteckend infizierte Personen sind. Stattdessen müssen wir eine Heuristik finden, also eine Wahrscheinlichkeit die die echte Übergangswahrscheinlichkeit abschätzt. Eine sinnvolle Heuristik stellen wir jetzt vor:

Aus den Daten von der JHU die wir gestellt haben betrachten wir alle Paare von Tagen die aufeinanderfolgen, wie zum Beispiel 12-01-2021 und 13-01-2021. Tag1 nennen wir immer jeweils den ersten Tag aus den Paaren und Tag2 den darauf folgenden. Wir markieren die Daten die zu Tag2 gehören mit einem Strich:

Tag1: gesund, infiziert, genesen, verstorben
Tag2: gesund', infiziert', genesen', verstorben'

Jetzt wollen wir für zwei Zustände A, B' jeweils über alle Paare von Tagen den mittleren Anteil der Menschen aus A finden der am nächsten Tag in B' ist.

<b>Beispiel:</b>
A = gesund, B' = infiziert'
c = np.array mit jeweils der Anzahl der Menschen in gesund bei Tag1
d = np.array mit jeweils der Anzahl der Menschen die an Tag1 in gesund waren aber bei Tag2 in infiziert' sind
P(B'|A) = mean( d / c )

* Tips
    * Durch 0 teilen ist nicht zulässig
    * Die ausgehenden Wahrscheinlichkeiten an einem Zustand müssen insgesamt 1 sein
* Berechnen Sie die Übergangswahrscheinlichkeiten für alle Übergänge die in Ihrer Markov-Kette nicht 0 sein sollen.



### Aufgabe 6: Wie macht man einen Simulationsschritt?
Als nächstes wollen wir mit Hilfe von P unsere Simulation implementieren. Unser Ziel ist es die Anzahl der Gesunden, Infizierten, Genesenen und Verstorbenen nach n Tagen für bestimmte Start Werte vorher zu sagen. Um die neuen Werte für den jeweils nächsten Tag zu berechnen führt man folgende Rechnung durch:

Für die Vektoren

$$
\overrightarrow{a} = \begin{bmatrix} \text{|gesund|} \\ \text{|infiziert|} \\ \text{|genesen|} \\ \text{|verstorben|} \end{bmatrix}
$$

und

$$
\overrightarrow{b} = \begin{bmatrix} \text{|gesund'|} \\ \text{|infiziert'|} \\ \text{|genesen'|} \\ \text{|verstorben'|} \end{bmatrix}
$$

gilt:

$$
P \cdot \overrightarrow{a} = \overrightarrow{b}
$$


Wenn man also die Vorhersage für n = 10 haben möchte, muss man 10 mal diese Rechnung durchführen.

* Schreiben Sie die Matrixmultiplikation aus und versuchen Sie nach zu vollziehen warum man so die Vorhersage für den nächsten Tag berechnen kann.

* Implementieren Sie den Simulationsschritt (np.matmul kann helfen)

* Nutzen Sie Ihre Markov-Kette um die Entwicklung der Gesunden, Infizierten, Genesenen und Verstorbenen zu berechnen. Wählen Sie als Start- und Enddatum Tage aus, die in ihrem DataFrame sind, kürzen sie den DataFrame so, dass sich in ihm nur noch die Tage aus dem Interval in dem sie Vorhersagen treffen befinden und speichern Sie ihre Vorhersagen als neue Spalten. Visualisieren sie den DataFrame.

* Am Ende wollen wir die kumulierte Anzahl der Infektionen wissen, also die gesamte Anzahl der Infektionen. Wir sagen aber nur die Anzahl der momentan Infizierten vorher, das heißt, eine Person die an einem Tag infiziert ist, kann auch am nächsten Tag noch im Zustand infiziert sein, so dass man sie für jeden Tag wieder neu zählen würde, wenn man die Erkrankten für alle Tage aufsummiert. Wie können wir aus den Infizierten Zahlen der einzelnen Tage trotzdem die gesamte Anzahl der Infizierten berechnen, oder annähern.

* Berechnen Sie die kumulierte Anzahl der Infizierten

### Aufgabe 7: Evaluation
Wir sind nun in der Lage mit Hilfe einer Markov-Kette die Entwicklung einer Pandemie vorherzusagen, wissen aber nicht wie gut unsere Vorhersage ist. Das wollen wir nun herausfinden. Dafür verwenden wir eine verbreitete Methode, die genutzt wird um Modelle zu evaluieren, die auf Daten basierend Vorhersagen treffen.
Die Methode heißt k-fache Kreuzvalidierung, wird aber meistens mit ihrem englischen Namen k-fold cross validation genannt. Bei der Evaluation von datenbasierten Modellen gibt es ein grundlegendes Problem: Daten, die man zum erstellen der Modelle genutzt hat, eignen sich wenig um diese zu evaluieren. Dies liegt daran, dass Daten oft über einen begrenzten Zeitraum, in zu geringen Mengen, und/oder in einem nicht repräsentativen Verhältnis aufgenommen werden. Dies führt dazu, dass Modelle deutlich bessere Vorhersagen für Daten machen, mit denen sie trainiert wurden, als auf Daten die nicht im Training verwendet wurden.
K-fache Kreuzvalidierung funktioniert nach dem folgenden Prinzip:

1. Teile die verfügbaren Daten in k möglichst gleich große Teile (k ist eine natürliche Zahl, also k ist in {1, 2, 3, 4, 5, ...})
2. Für jeden Teil i der Daten: Trainiere das Modell mit allen Daten die nicht in i sind, und berechne mit Hilfe von i den Fehler.
3. Berechne den Durchschnitt aller Fehler die in 2. berechnet wurden.

Das Modell ist in unserem Fall die Markov-Kette, und das Trainieren ist das Berechnen der Übergangswahrscheinlichkeiten. Mit Fehler bezeichnet man meistens den Abstand der vorhergesagten Wertes zum gemessenen Wert. Das wäre bei uns z.B. für die Infizierten: abs(Infizierte - vorhergesehene Infizierte)
Wobei abs als Funktion den absoluten Wert einer Zahl, also die Zahl ohne Vorzeichen angibt (abs(1) = 1, abs(-1) = 1, abs(-50) = 50).

* Führen Sie 5-fache Kreuzvalidierung mit den gegebenen Datensatz durch, und geben Sie den durchschnittlichen Fehler für die Gesunden, die aktuellen Infizierten, die kumulierten Infizierten, die Genesenen und die Verstorbenen nach
    
    * (len(DataFrame)/5) * 1/10
    * (len(DataFrame)/5) * 1/5
    * (len(DataFrame)/5) * 1/2
    * (len(DataFrame)/5)

    Tagen an.

### Aufgabe 8 (Bonus): Herumspielen mit dem Modell
Hier sollen noch ein paar Fallbeispiele bearbeitet werden, um zu verdeutlichen, wie ein Modell wie das, was Sie heute entwickelt haben, in der Realität Anwendung finden könnte.

* Es sollen für 4 Medikamente entschieden werden, welches am effektivsten die Anzahl der Verstorbenen innerhalb der nächsten 3 Monate reduziert. Wir können davon ausgehen, dass alle in Deutschland dieses Medikament verabreicht bekommen. Benutzen sie 6/18/20 als Start und finden sie das richtige Medikament.
    1. Ein Medikament was die Chance sich anzustecken um 20% reduziert, aber die Chance zu sterben um 5% erhöht.
    2. Ein Medikament was die Chance sich anzustecken um 15% reduziert, aber die Chance zu sterben um 3% erhöht.
    3. Ein Medikament was die Chance sich anzustecken um 5% reduziert.
    4. Ein Medikament was die Chance sich anzustecken um 5% erhöht, aber die Chance zu sterben um 2% verringert.

* Es soll evaluiert werden wie effektiv Quarantäne als Maßnahme ist. Wir können davon ausgehen, dass die Einführung einer Quarantäne die Chance sich anzustecken um 80% verringern. Um wie viel Prozent würde sich die Anzahl der momentan Infizierten an den folgenden Zeitpunkten verringern:
    1. Eine Woche
    2. Zwei Wochen
    3. Ein Monat
    4. Drei Monate
