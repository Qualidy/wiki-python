# Variablen und Datentypen

{{ youtube_video("https://www.youtube.com/embed/4umrj_L6grQ?si=jTK_7DsrNdTpJirf") }}

In diesem Abschnitt lernen wir die Grundlagen von Variablen und verschiedenen Datentypen in Python kennen. Variablen
sind wie Behälter, in denen wir Daten speichern können, während Datentypen die Art der Daten bestimmen, die in diesen
Variablen gespeichert werden können.

## Bedeutung von Variablen in der Programmierung

[//]: # ([60min])
Variablen sind ein unverzichtbarer Bestandteil der meisten Programmiersprachen, einschließlich Python. Sie erfüllen
mehrere wichtige Funktionen:

#### 1. **Daten speichern**:
   Variablen dienen als Speicherorte im Arbeitsspeicher eines Computers, in denen Daten gespeichert werden können.
   Diese Daten können Zahlen, Texte, und andere möglichen anderen Objekte sein.

```python
sum = 10 + 13
print(sum)
```

#### 2. **Lesbarkeit und Wartbarkeit**:
   Variablen helfen, den Code verständlicher zu machen. Durch sinnvolle Namen wird der Zweck des Codes klarer, was die
   Wartung und Fehlerbehebung vereinfacht.

#### 3. **Berechnungen durchführen und Ergebnisse speichern**:
   Variablen ermöglichen die Durchführung von Berechnungen mit gespeicherten Werten. So können beispielsweise
   mathematische Operationen ausgeführt und das Ergebnis in einer anderen Variablen gespeichert werden.

```python
nominator = 3
denominator = 6
result = nominator / denominator
print(result)
```

#### 4. **Daten wiederverwenden** :
   Variablen werden eingesetzt, um Daten in verschiedenen Teilen eines Programms zu nutzen.

#### 5. **Speichern von Zuständen** :
   In komplexeren Anwendungen dienen Variablen dazu, den Zustand einer Anwendung zu speichern und zu verwalten.
   Beispiele hierfür sind der Login-Status eines Nutzers oder die Anzahl der Artikel in einem Warenkorb.

```python
name = "Hans"
print("Hallo " + name)
print("Ich heiße auch " + name)
name = "Klaus"
print("Hallo auch " + name)
```

Variablen sind somit essenziell für die Erstellung flexibler, effizienter und verständlicher Programme und bilden die
Grundlage für fast alle Operationen und Logiken in der Programmierung.

----

# Variablenbenennung

{{ youtube_video("https://www.youtube.com/embed/Vh9EhNoBbUg?si=00nEOu7edngNqrXx") }}

[//]: # ([75min])

Eine Variable in Python kann erstellt werden, indem man ihr einen Namen gibt und
ihr einen Wert zuweist. Dabei steht links immer der Variablenname und rechts der Wert, der in dieser gespeichert werden
soll:

**Beispiel:**

```python
meine_variable = 10
alter = 23
Geburtsjahr = 1940
willkommens_text = "Hey du!"

print(meine_variable)
print(alter)
print(Geburtsjahr)
print(willkommens_text)
```

## Namenskonventionen:

[//]: # ([20min])
- Variablennamen sollten klar und beschreibend sein. In Python verwenden wir oft Snake-Case,
  bei dem Wörter durch Unterstriche getrennt werden (z.B. `meine_variable`).
- Variablennamen dürften nicht mit einer Zahl anfangen und keine Sonderzeichen außer dem Unterstrich enthalten.

Kurze Variablennamen sind nur in absoluten Ausnahmefällen zu verwenden, z.B. als Laufvariable in einer Schleife. Es
kostet keine Ressourcen und kein Geld aussagekräftige Variablen zu nutzen.

Eine Variable `a` könnte alles sein, während die Variable `zinssatz` recht sicher ein Zinssatz darstellen wird.

## Besonderheit bei Pythons `=`

{{ youtube_video("https://www.youtube.com/embed/zNgZVTrWxng?si=BsjNS8CHHqBJ02KB") }}

In Python ist auch die folgende Syntax erlaubt, um mit weniger
Codezeilen mehrere Variablen zuzuordnen:

```python
a = b = c = 10  # a,b,c haben alle den Wert 10
d, e = 15, 20   # d = 15 und e = 20
```

----

# Datentypen

{{ youtube_video("https://www.youtube.com/embed/Z85rA3SxHls?si=t8TWYWv5EtwUZtnG") }}

[//]: # ([60min])
In Python gibt es verschiedene Datentypen, aber hier konzentrieren wir uns auf die grundlegendsten.

## Primitive Datentypen

### Integers (Ganzzahlen):

Integers repräsentieren ganze Zahlen, positiv oder negativ, ohne Dezimalstellen:

```python
alter = 30
anzahl_der_aepfel = -3
```

Möchte man andere Datentypen in Integers umwandeln, nutzt man die `int`-Funtkion, wie wir unten im Beispiel sehen
können:

```python
zahl_von_zeichenkette = int("20")
```

### Floats (Gleitkommazahlen):

Dezimalzahlen werden durch den Datentyp `float` dargestellt und sind im IEEE 754 Format codiert. Beim Umgang mit floats
kann es zu Ungenauigkeiten kommen, da sich nicht alle Dezimalzahlen perfekt darstellen lassen. Das sollte aber hier
für uns noch keine große Rolle spielen.

Beispiel:

```python
preis = 19.99
temperatur = -2.5
floaty = float(2)
```

### Booleans (Boolesche Werte):

Booleans repräsentieren nur zwei Werte: True (wahr) oder False (falsch).

Sie sind sehr nützlich in Bedingungen und Schleifen, da sie das zum Beispiel das Ergebnis von Vergleichen sind
(später mehr dazu).

Ein anderer praktischer Anwendungsfall ist die Nutzung als 'flag', ob zum Beispiel jemand Student ist oder nicht.

Beispiel:

```python
ist_student = True
ist_sonnig = False
```

Von Booleans werden wir um Laufe der Woche noch mehr hören und sie auch schon direkt in unserem eigenen Programm nutzen.

### Übungsaufgaben

[//]: # ([35min])

{{ task(file="tasks/python_grundlagen/variables_types/01_integer_addition.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/02_integer_subtraktion.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/03_float_division.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/04_multiplikation_von_integers.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/05_float_zu_integer.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/06_vergleich_von_integers.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/07_booleansches_and.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/08_booleansches_or.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/09_integer_in_boolean.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/10_modulo_operator.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/11_potenzierung_von_floats.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/12_vergleich_von_floats.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/13_integer_in_float.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/14_negation_eines_booleans.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/15_booleans_und_integers.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/16_diskussion_float_integer.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/17_diskussion_fliesskommazahlen.yaml") }}

## Die `type()`-Funktion

{{ youtube_video("https://www.youtube.com/embed/pEWPaCG4dGI?si=gFzVAMYYYHuBSDJQ") }}

Die `type()`-Funktion in Python sagt dir, was für eine Art
von Sache eine Variable ist. Sie verrät dir, ob es sich um eine Zahl, einen Text oder etwas
ganz anderes handelt.

**Ein Beispiel:**
Angenommen, du hast eine Zahl, sagen wir 42. Du möchtest wissen, welche Art von Zahl das ist. Du könntest die `type()`
-Funktion verwenden, indem du folgenden Code schreibst:

```python
nummer = 42
print(type(nummer))
```

Wenn du diesen Code ausführst, wird Python dir sagen, dass `nummer` vom Typ "int" ist, was für "integer" steht.
So verwendest du die `type()`-Funktion , um den Typ von Variablen in Python herauszufinden. Du gibst ihr etwas und sie
verrät dir, was es ist.

**Wofür man die `type()`-Funktion verwenden kann:**
Die Verwendung der `type()`-Funktion in Python kann sehr nützlich sein. Hier sind einige Anwendungsfälle:

* **Fehlervermeidung:** Wenn du sicherstellen möchtest, dass dein Code mit den richtigen Daten arbeitet, kannst
   du `type()` verwenden, um sicherzustellen, dass die erwarteten Datentypen vorliegen. Wenn du beispielsweise eine
   Funktion schreibst, die nur mit Ganzzahlen arbeitet, kannst du überprüfen, ob die eingegebene Variable wirklich eine
   Ganzzahl ist, bevor du weitermachst.

```python
def verdopple(zahl):
    if type(zahl) == int:
        return zahl * 2
    else:
        return "Ungültige Eingabe"
```

* **Debugging:** Wenn du einen Fehler in deinem Code findest und herausfinden möchtest, warum er auftritt, kann
   die `type()`-Funktion dir helfen. Du kannst sie verwenden, um die Datentypen von Variablen während der Ausführung
   deines Programms zu überprüfen und so eventuelle Inkonsistenzen zu erkennen.
* **Dynamisches Programmieren:** In Python können Variablen unterschiedliche Datentypen haben, da Python eine
   dynamische Typisierung unterstützt. Manchmal ist es hilfreich, den aktuellen Typ einer Variable während der Laufzeit
   zu überprüfen und den Programmfluss entsprechend anzupassen.

Die `type()`-Funktion ist also ein Werkzeug, mit dem du sicherstellen kannst, dass dein Code korrekt funktioniert und
den erwarteten Datentypen entspricht. Sie ist besonders nützlich, wenn du mit verschiedenen Datenstrukturen und -typen
in Python arbeitest.

## Strings, List, Tupel, Set, Dictionary

{{ youtube_video("https://www.youtube.com/embed/FaXcBl25hFQ?si=OOKZKs3NAauT4MAz") }}

### Strings (Zeichenketten):

[//]: # ([45min])

Strings werden verwendet, um Text zu speichern. In Python gibt es eine Vielzahl von Funktionen und Methoden, die es
erlauben Strings zu verarbeiten. Strings in Python sind Unicode, das heißt so ziemlich jedes Zeichen, was es gibt kann
gespeichert werden, auch Emojis zum Beipiel!

**Beispiel**:

```python
name = "Anna"
begruessung = 'Hallo Welt!'
zahl_als_text = "1234"
cool = "😎"

print(name)
print(begruessung)
print(zahl_als_text)
print(cool)
```

Strings sind für uns sehr wichtig. Der Datentyp ist sehr universell und typischerweise werden jegliche Eingaben und
Ausgaben eine Art String sein.

### Listen

[//]: # ([45min])

Listen in Python sind eine der vielseitigsten Datenstrukturen und werden verwendet, um eine geordnete Sammlung von
Elementen zu speichern.

Listen werden mit eckigen Klammern `[]`  oder der `list()`-Funktion erstellt. Die Elemente werden in eckigen Klammern
durch Kommata getrennt.

**Beispiel:**

```python
fruechte = ["Apfel", "Banane", "Kirsche"]
zahlen = [1, 2, 3, 4, 5, 4, 3, 2, 1]
gemischt = [3.14, "Hallo", True]

buchstaben = list("Hallo") # ["H", "a", "l", "l", "o"]
```

Listen sind sehr häufig verwendete Datenstrukturen. Deswegen ist dies hier nur ein kleiner Einstieg und wir lernen
später noch mehr zu Listen.

Wir können auf Listen-Elemente auch einfach zugreifen und neue Elemente hinzufügen:

```python
erster_buchstabe = buchstaben[0]

fruechte.append("Birne") # ["Apfel", "Banane", "Kirsche", "Birne"]
```

Beim Zugriff auf Listen fangen wir immer bei 0 an mit zählen.

### Tupel

Tupel in Python sind ähnlich wie Listen eine Datenstruktur zur Sammlung von Werten. Im Gegensatz zu Listen sind sie
unveränderlich, wenn sie einmal erstell wurden.

Sie werden mit runden Klammern `()` erstellt. Die Elemente werden durch Kommas getrennt.

**Beispiel**:

```python
koordinaten = (50.0, 20.1)
rgb_farbe = (256, 128, 0)
```

Ebenso wie Listen, sind Tupel wichtige Datenstrukturen. Auch hier lernen wir später noch mehr. Wir dürfen aber jetzt
schon verraten, dass wir Elemente eines Tupels genauso auslesen können, wie die Elemente einer Liste:

```python
rot_anteil = rgb_farbe[0]
```

Aber was passiert eigenltich, wenn wir folgendes machen:

```python
blau_anteil = rgb_farbe[3]
```

Wir bekommen einen Fehler! Und zwar folgenden:

```python
IndexError: tuple index out of range
```

Das sagt uns, dass wir "our of range" sind, also außerhalb der möglichen Elemente einen Zugriff durchführen wollen.

### Aufgaben

[//]: # (Zeit: 20min)

{{ task(file="tasks/python_grundlagen/variables_types/18_liste_erstellen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/19_tupel_zu_liste.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/20_liste_invertieren.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/21_tupel_aus_listen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/22_liste_von_tupeln.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/23_listenelemente_filtern.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/24_element_in_tupel_ueberpruefen.yaml") }}

### Sets

[//]: # ([45min])

Sets in Python sind eine Datenstruktur, die für die Speicherung einer ungeordneten Sammlung von einzigartigen Elementen
verwendet wird. Das heißt kein Element kann doppelt vorkommen.

Wir erstellen Sets mit geschweiften Klammern `{}` und den jeweiligen Elementen:

```python
einzigartige_zahlen = {1, 2, 3, 4, 5, 4, 3, 1}
print(einzigartige_zahlen)

buchstaben = {'a', "a", "A", 'aa'}
print(buchstaben)
```

### Dictionaries

[//]: # ([45min])

Mit Dictionaries können wir Schlüssel-Wert-Paare speichern. Dies ist die vielleicht wichtigste Datenstruktur in Python
und wird auch von der Sprache selbst in hohem Maße genutzt. Sehr viele Dinge in Python lassen sich im Grunde auf
Dictionaries zurückführen.

Wir erstellen Dictionaries mit geschweiften Klammern `{}` und `Schlüssel: Wert`- Paaren, die durch Komma getrennt sind:

```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict)

# Zugriff auf den Wert mit dem Schlüssel "Name"
name = mein_dict["Name"]
print(name)  # Gibt "Max" aus
```

# Aufgaben

[//]: # ([20min])

Wenn ihr bei einer Aufgabe nicht wisst, wie es geht oder euch nicht sicher seit, versucht zuerst bei einer Suchmaschine
eurer Wahl nach einem Lösungsweg zu suchen. Das Finden von Informationen ist ein wichtiger Skill als Software-Entwickler.

{{ task(file="tasks/python_grundlagen/variables_types/25_elemente_zu_set_hinzufuegen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/26_schluessel_wert_paare_dictionary.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/27_element_aus_set_entfernen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/28_werte_aus_dictionary_abrufen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/29_dictionary_werte_aendern.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/30_set_operationen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/31_schluessel_aus_dictionary_entfernen.yaml") }}

{{ task(file="tasks/python_grundlagen/variables_types/32_duplikate_aus_liste_entfernen.yaml") }}
