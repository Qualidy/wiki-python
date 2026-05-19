# Schleifen

[//]: # "[10min]"

In der Programmierung sind **Schleifen** ein grundlegendes Konzept, welches verwendet wird, um einen bestimmten Block
von Anweisungen wiederholt auszuführen. Man sagt auch, dass Schleifen über etwas iterieren. Dies kann zum Beispiel ein
Zahlenbereich sein oder auch eine Menge an Elementen in einer Liste.

In Python gibt es zwei Hauptarten von Schleifen:

**`for`-Schleife:** Die `for`-Schleife wird verwendet, um über eine Sequenz (z. B. eine Liste, ein Tupel oder eine
Zeichenkette) zu iterieren und den Codeblock für jedes Element in der Sequenz auszuführen.

**`while`-Schleife:** Die `while`-Schleife wird so lange ausgeführt, wie eine angegebene Bedingung wahr ist. Sie wird
verwendet, wenn die Anzahl der Schleifendurchläufe im Voraus nicht bekannt ist.

# Einführung in `for`-Schleifen

{{ youtube_video("https://www.youtube.com/embed/IZmCkNQb5v8?si=I4rS9cz-B1xrp0_6") }}

Hier ist ein einfaches Beispiel für eine `for`-Schleife in Python (drücke auf "Next >" um den Code schrittweise
durchzuführen):

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=fruechte%20%3D%20%5B%22Apfel%22,%20%22Banane%22,%20%22Kirsche%22%5D%0Afor%20frucht%20in%20fruechte%3A%0A%20%20%20%20print%28frucht%29%0Aprint%28%22fertig%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
for frucht in fruechte:
    print(frucht)
print("fertig")
```

Diese Schleife iteriert über die Liste `fruechte` und gibt jede Frucht nacheinander aus. Für jeden Durchlauf der
Schleife nimmt `frucht` ein anderes Element der Liste an und steht im Schleifenkörper zur Verfügung.

## Syntax einer `for`-Schleife

Die grundlegende Syntax einer `for`-Schleife in Python lautet:

```python
for element in sequenz:
# Anweisungen, die für jedes Element ausgeführt werden
```

- `element`: Eine Variable, die den aktuellen Wert aus der Sequenz repräsentiert.
- `sequenz`: Die Sequenz, über die iteriert wird (z. B. eine Liste, ein Tupel, eine Zeichenkette oder eine range, auf die wir gleich eingehen werden).

## Aufgaben

[//]: # "[35min]"

{{ task(file="tasks/python_grundlagen/loops/loops/01_zahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/02_stadtetrip.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/03_summierung.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/04_langster_name.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/05_quadratzahlen.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/06_verdreht.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/07_fakultat.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/08_thermometer_fur_amerikaner.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/09_vokale.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/10_haufigkeit.yaml") }}

# Iteration über feste Zahlenbereiche mit `range`

{{ youtube_video("https://www.youtube.com/embed/IQhjfZiCOro?si=47NPqX5Fn0SOri8G") }}

Möchte man über einen bestimmten Zahlenraum iterieren, so verwendet man in Python die `range`-Funktion. Es gibt drei
Möglichkeiten `range` aufzurufen:

| Anazahl Parameter | Aufruf                         | Bedeutung                                                                                                                | Beispiel          | Entsprechende Liste |
| ----------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------- | ------------------- |
| 1                 | `range(end)`                   | Die Range enthält die Integer von `0` bis _ausschließlich_ `end`.                                                        | `range(3)`        | `[0,1,2]`           |
| 2                 | `range(start, end)`            | Die Range enthält die Integer von `start` bis _ausschließlich_ `end`.                                                    | `range(12, 15)`   | `[12,13,14]`        |
| 3                 | `range(start, end, step_size)` | Die Range enthält die Integer von `start` bis _ausschließlich_ `end`. und geht dabei in Schritten der Größe `step_size`. | `range(3, 10, 2)` | `[3,5,7,9]`         |

{{ task(file="tasks/python_grundlagen/loops/loops/11_ranges_vorhersagen.yaml") }}

## Nutzen von Ranges

Ranges wirken auf den ersten Blick sehr ähnlich zu Listen. Schaut man sie sich genauer an, stellt man sogar fest,
dass sie sogar Indizierung und Slicing erlauben. Es gibt zwei wichtige Vorteile:

- Ranges können leicht instanziiert werden (wie würdest du eine Liste aller geraden Zahlen bis 1000 in Python sonst erstellen?),
- Ranges sparen Speicherplatz. Denn die Zahlen, die in der Range sind, werden nicht alle zunächst im Speicher hinlegt, sondern erst bei Bedarf bereitgestellt (indem sie jeweils berechnet werden).

Wir können Ranges so einfach für Schleifeniterationen über einen Integer-Zahlenraum nutzen:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=for%20i%20in%20range%285%29%3A%0A%20%20%20%20print%28i%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
for i in range(5):
    print(i)
```

# Einführung in While-Schleifen in Python

{{ youtube_video("https://www.youtube.com/embed/nqMMCr3juCE?si=RpI4n9QONgTR_Qz7") }}

[//]: # "[120min]"

While-Schleifen ermöglichen es einen Block von Anweisungen
wiederholt auszuführen, **solange eine bestimmte Bedingung erfüllt ist**.
Sie sind besonders nützlich, wenn die Anzahl der
Wiederholungen **nicht im Voraus bekannt** ist. Dies ist zum Beispiel bei einer wiederholten Eingabeaufforderung an den
Nutzer der Fall.

Hier ist ein einfaches Beispiel für eine `while`-Schleife in Python:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=zaehler%20%3D%200%0Awhile%20zaehler%20%3C%205%3A%0A%20%20%20%20print%28%22Schleife%20Nr.%22,%20zaehler%29%0A%20%20%20%20zaehler%20%2B%3D%201%0Aprint%28%22fertig%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
zaehler = 0
while zaehler < 5:
    print("Schleife Nr.", zaehler)
    zaehler += 1
print("fertig")
```

Hier sehen wir noch ein kompliziertes Beispiel, bei dem eine Zahl so lange von einer anderen Subtrahiert wird,
bis eine Zahl negativ wird. Welcher Rechenoperation wird mit diesem Code umgesetzt?

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=zaehler%20%3D%2018%0Aoriginal_zaehler%20%3D%20zaehler%0Anenner%20%3D%205%0Aanzahl%20%3D%200%0Awhile%20zaehler%20-%20nenner%20%3E%200%3A%0A%20%20%20%20zaehler%20%3D%20zaehler%20-%20nenner%0A%20%20%20%20anzahl%20%3D%20anzahl%20%2B%201%0Aprint%28f%22%7Bnenner%7D%20passt%20%7Banzahl%7D%20mal%20in%20den%20%7Boriginal_zaehler%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
zaehler = 18
original_zaehler = zaehler
nenner = 5
anzahl = 0
while zaehler - nenner > 0:
    zaehler = zaehler - nenner
    anzahl = anzahl + 1
print(f"{nenner} passt {anzahl} mal in den {original_zaehler}")
```

Natürlich können wir auch sehr einfach **Endlosschleifen** erzeugen in dem wir die Bedingung einfach immer auf `True`
lassen:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=while%20True%3A%0A%20%20%20%20eingabe%20%3D%20input%28%22Bitte%20gib%20etwas%20ein%3A%22%29%0A%20%20%20%20print%28f%22Deine%20Eingabe%20ist%3A%20%7Beingabe%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2212%22,%22asdfadsf%22%5D&textReferences=false)

```python
while True:
    eingabe = input("Bitte gib etwas ein:")
    print(f"Deine Eingabe ist: {eingabe}")
```

Wie wir die Endlosschleife doch verlassen können, lernen wir dann gleich.

## Aufgaben

[//]: # "[35min]"

{{ task(file="tasks/python_grundlagen/loops/loops/12_summe_von_1_bis_100.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/13_input_erfragen.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/14_fakultat_2.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/15_fast_endlose_schleife.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/16_fibonacci.yaml") }}

# Vorzeitiges Abbrechen einer Schleife

{{ youtube_video("https://www.youtube.com/embed/suZrbAoSmr0?si=hloioyGs7h7phUNw") }}

[//]: # "[60min]"

In vielen Fällen sucht man einfach einen Wert in einem Bereich oder ein bestimmtes Element in einer List. Sobald man
dieses gefunden hat, kann man die Schleife eigentlich abbrechen. Dafür nutzt man das Keyword `break`:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=for%20i%20in%20range%280,%2010%29%3A%0A%20%20%20%20print%28i%29%0A%20%20%20%20if%20i%20%3D%3D%205%3A%0A%20%20%20%20%20%20%20%20break%0Aprint%28%22Ende%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
for i in range(0, 10):
    print(i)
    if i == 5:
        break
print("Ende")
```

Sobald die Bedingung `i == 5` wahr wird, sorgt `break` dafür, dass wir die Schleifen verlassen. Damit sparen wir uns 5
weitere Durchläufe. Bei komplexen Problemstellungen kann man damit sehr viel Zeit sparen.

Auf der anderen Seite gibt es aber auch Fälle, in denen man nicht die ganze Schleife beenden will, sondern nur den
aktuellen Durchlauf. Dafür nutzt man das Keyword `continue`.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=for%20i%20in%20range%280,%2010%29%3A%0A%20%20%20%20if%203%20%3C%3D%20i%20%3C%3D%205%3A%0A%20%20%20%20%20%20%20%20continue%0A%20%20%20%20print%28i%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
for i in range(0, 10):
    if 3 <= i <= 5:
        continue
    print(i)
```

Wieso? Für jeder Zahl zwischen 0 und 10 wird überprüft, ob diese Zahl zwischen 3 und 5 liegt. Ist das der Fall, springt
der Code direkt an den Schleifenanfang (wegen des `continue`), statt die Zeile 4 auszuführen.
direkt zum nächsten Durchlauf. In allen anderen Fällen wird die Zahl auf der Konsole ausgegeben.

Sehr häufig wird break in Kombination mit while-Schleifen verwendet. Wieso? Weil es so einfach möglich ist,
Endlosschleifen zu erzeugen, die unter bestimmten Bedingungen abbrechen, die nicht im Schleifenkopf überprüft werden.

Zum Beispiel:

```python
while True:
    eingabe = input()
    if eingabe == "C":
        break

    print(f"Deine Eingabe in groß: {eingabe.upper()}")

print("Bye Bye")
```

Durch `while True:` läuft diese Schleife theoretisch endlos lange, weil die Bedingung immer wahr ist. Bei jedem
Schleifendurchlauf wird der Nutzer nach einer Eingabe gefragt. Sobald der Nutzer "C" eingibt, wird die Schleife durch
den Befehl `break` verlassen und das Programm kann normal weiterlaufen.

# Else-Zweig bei While- und For-Schleifen in Python

{{ youtube_video("https://www.youtube.com/embed/_HQlJUAIuh8?si=N0iBJYNgI4g8MVpT") }}

[//]: # "[30min]"

In Python können sowohl `while`- als auch `for`-Schleifen mit einem optionalen `else`-Zweig versehen werden. Dieser Teil
der Schleife wird ausgeführt, wenn die Schleife auf normale Weise beendet wird, d.h., **nicht durch ein `break`-Statement
unterbrochen wird**.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=summe%20%3D%200%0Afor%20number%20in%20%5B%2243%22,%20%221234%22,%20%2233.4%22,%20%2210%22%5D%3A%0A%20%20%20%20if%20not%20number.isdigit%28%29%3A%0A%20%20%20%20%20%20%20%20print%28f%22%7Bnumber%7D%20is%20no%20integer!%20Abort%22%29%0A%20%20%20%20%20%20%20%20break%0A%20%20%20%20summe%20%2B%3D%20int%28number%29%0Aelse%3A%0A%20%20%20%20print%28f%22Die%20Summe%20aller%20Zahlen%20ist%20%7Bsumme%7D.%22%29%0Aprint%28%22Ende%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
summe = 0
for number in ["43", "1234", "33.4", "10"]:
    if not number.isdigit():
        print(f"{number} is no integer! Abort")
        break
    summe += int(number)
else:
    print(f"Die Summe aller Zahlen ist {summe}.")
print("Ende")
```

# Verschachtelte Schleifen

{{ youtube_video("https://www.youtube.com/embed/eBdI_N7yK8A?si=rr9x0FQ3WyNqqyki") }}

Es ist auch möglich Schleifen in Schleifen zu verwenden. Dies sieht man tatsächlich sehr häufig, da es oft
verschachtelte Strukturen gibt, die durchlaufen werden sollen, z.B. Listen von Listen.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=list_of_lists%20%3D%20%5B%5B1,2,3%5D,%20%5B40,50,60%5D,%20%5B700,800,900%5D%5D%0A%0Asumme%20%3D%200%0A%0Afor%20sub_list%20in%20list_of_lists%3A%0A%20%20%20%20for%20element%20in%20sub_list%3A%0A%20%20%20%20%20%20%20%20summe%20%2B%3D%20element%0A%20%20%20%20print%28f%22Zwischenergebnis%3A%20%7Bsumme%7D%22%29%20%20%20%20%20%20%20%20%0Aprint%28f%22Endergebnis%3A%20%7Bsumme%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
list_of_lists = [[1,2,3], [40,50,60], [700,800,900]]

summe = 0

for sub_list in list_of_lists:
    for element in sub_list:
        summe += element
    print(f"Zwischenergebnis: {summe}")
print(f"Endergebnis: {summe}")
```

{{ task(file="tasks/python_grundlagen/loops/loops/17_produktsummen.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/18_summenprodukt.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/23_tannenbaum.yaml") }}

# Anspruchsvolle Aufgaben

[//]: # "[60min]"

{{ task(file="tasks/python_grundlagen/loops/loops/19_finden.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/20_benutzerdefinierte_passwortuberprufung.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/21_einfacher_zahlenraten.yaml") }}
{{ task(file="tasks/python_grundlagen/loops/loops/22_bestellung_in_einem_virtuellen_cafe.yaml") }}
