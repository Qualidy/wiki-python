# Begriffssammlung Python Grundlagen

# Intro

| Begriff | Kurzerklärung                                        | Link zur Referenz                              |
|---------|------------------------------------------------------|------------------------------------------------|
| Python  | Programmiersprache unserer Wahl                      | [Referenz](https://www.python.org)             |
| PyCharm | Umfassende Python IDE von Jetbrains                  | [Referenz](https://www.jetbrains.com/pycharm/) |
| VSCode  | Universal-IDE mit mächtigen Python-Plugins           | [Referenz](https://code.visualstudio.com/)     |
| Jupyter | Entwicklungsumgebung für interaktives Programmiereun | [Referenz](https://jupyter.org/)               |

# Variablen Datentypen


| Begriff    | Kurzerklärung                                      | Link zur Referenz                                                                                       |
|------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Variable   | Name, mit dem man Werte wiederholt nutzen kann     | [Referenz](https://docs.python.org/3/faq/programming.html)                                              |
| Integer    | Datentyp für Ganzzahlen                            | [Referenz](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)             |
| Float      | Datentyp für Fließkommazahlne                      | [Referenz](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)             |
| Boolean    | Datentyp für Wahrheitswerte (`True`/`False`)       | [Referenz](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)                           |
| String     | Datentyp für Zeichenketten                         | [Referenz](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)                      |
| List       | Veränderliche Kollektion verschiedener Elemente    | [Referenz](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)             |
| Tupel      | Unveränderliche Kollektion verschiedener Elementen | [Referenz](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)             |
| Set        | Menge einzigartiger Elemente                       | [Referenz](https://docs.python.org/3.12/tutorial/datastructures.html?highlight=set#sets)                |
| Dictionary | Schlüssel-Wert-Paare                               | [Referenz](https://docs.python.org/3.12/tutorial/datastructures.html?highlight=dictionary#dictionaries) |

# Input Output

| Begriff  | Kurzerklärung                                                         | Link zur Referenz                                                                                   |
|----------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `print`  | Funktion um Variablen als Text auf der Konsole auszugeben             | [Referenz](https://docs.python.org/3/library/functions.html?highlight=print#print)                  |
| `input`  | Funktion, um Nutzereingaben von der Konsole zu lesen                  | [Referenz](https://docs.python.org/3/library/functions.html?highlight=input#input)                  |
| f-String | Möglichkeit, Strings zu formatieren                                   | [Referenz](https://docs.python.org/3/tutorial/inputoutput.html?highlight=f%20strings#tut-f-strings) |
| `int()`  | Funktion, um Strings, die nur Zahlen enthalten in Integer umzuwandlen | [Referenz](https://docs.python.org/3/library/functions.html?highlight=int#int)                      |


# Mathematische Operationen

| Begriff     | Kurzerklärung                       | Link zur Referenz                                                                       |
|-------------|-------------------------------------|-----------------------------------------------------------------------------------------|
| `+`         | Addition von zwei Variablen         | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `-`         | Subtraktion von zwei Variablen      | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `*`         | Multiplikation von zwei Variablen   | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `/`         | Divison von zwei Variablen          | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `//`        | Ganzzahldivision von zwei Variablen | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `%`         | Module von zwei Variablen           | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `**`        | Potenzieren                         | [Referenz](https://docs.python.org/3/library/operator.html)                             |
| `math.sqrt` | Ziehen der Quadratwurzel            | [Referenz](https://docs.python.org/3/library/math.html?highlight=math%20sqrt#math.sqrt) |
| `math.exp`  | Exponentailfunktion                 | [Referenz](https://docs.python.org/3/library/math.html?highlight=math%20sqrt#math.exp)  |
| `math.log`  | Logartihmus zur angegeben Basis     | [Referenz](https://docs.python.org/3/library/math.html?highlight=math%20sqrt#math.log)  |



# Verzweigungen

| Begriff      | Kurzerklärung                          | Link zur Referenz                                                                            |
|--------------|----------------------------------------|----------------------------------------------------------------------------------------------|
| `if`, `else` | Verzweigungen aufgrund von Bedingungen | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=else#if-statements) |

# Debugging

| Begriff       | Kurzerklärung                                                                                                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Breakpoint    | Zeile im Code, bis zu der dieser vom Debugger ausgeführt wird. Diese Zeile wartet noch auf die Ausführung.                                                                          |
| Continue      | Führt den Code weiter aus bis zum nächsten Breakpoint oder zum Programmende.                                                                                                        |
| Step Over     | Führe die aktuelle Codezeile aus und gehe zur nächsten Codezeile, die ausgeführt werden soll.                                                                                       |
| Step Into     | Wenn in der akutellen Zeile eine Funktion ausgeführt werden soll, wird in diese hineingesprungen, sodass die Ausführung der Funktion schritt für Schritt nachvollzogen werden kann. |
| Step Out      | Wenn derzeit eine Funktion ausgeführt wird, wird die Ausführung so lange automatisch weitergeführt, bis die Funktionsausführung beendet ist und dann wieder unterbrochen.           |
| Restart       | Beendet die Ausführung der Applikation und startet den Debugmodus erneut.                                                                                                           |
| Stop          | Beendet die Ausführung der Applikation.                                                                                                                                             |
| Debug Console | Erlaubt die Ausführung von Befehlen, während das Programm im Debugmodus pausiert. Funktionen können hier ausgeführt und Variablen gelesen und manipuliert werden.                   |

# Listen

| Begriff                      |                                                                                                                                                                       | Link zur Referenz                                                                          |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `list`                       | Datentyp in Python zur Sammlung mehrerer Daten. Listen sind mutable (veränderbar).                                                                                    | [Referenz](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)           |
| Mutability                   | Einträge des Objekts können im Nachhinein verändert werden.                                                                                                           | [Referenz](https://docs.python.org/3/glossary.html#term-mutable)                           |
| Immutablity                  | Einträge des Objekts können nicht mehr verändert werden.                                                                                                              | [Referenz](https://docs.python.org/3/glossary.html#term-immutable)                         |
| Slicing                      | Wähle mit der Notation `sequence[i:j:s]` einen Teil einer Liste/Tupel/String aus. Nämlich den Teil vom Index `i` (inklusive) bis `j` (exklusive) in Schrittgrößen `s` | [Referenz](https://docs.python.org/3/reference/datamodel.html?highlight=slicing#sequences) |
| `mylist.append(x)`           | Fügt ein Element am Ende der Liste hinzu                                                                                                                              | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.extend([x, y, ...])` | Erweitert die Liste um die Elemente in der angegebenen Liste                                                                                                          | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.insert(i, x)`        | Fügt an Position `i` das Element `x` ein                                                                                                                              | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.remove(x)`           | Entfernt das erste Vorkommen von `x` aus der Liste                                                                                                                    | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.pop(i)`              | Entfernt und gibt das Element an der Position `i` zurück                                                                                                              | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.clear()`             | Entfernt alle Elemente aus der Liste                                                                                                                                  | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.index(x)`            | Gibt den Index des ersten Vorkommens von `x` zurück                                                                                                                   | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.count(x)`            | Zählt, wie oft `x` in der Liste vorkommt                                                                                                                              | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.sort()`              | Sortiert die Elemente der Liste                                                                                                                                       | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `mylist.reverse()`           | Kehrt die Reihenfolge der Elemente in der Liste um                                                                                                                    | [Referenz](https://docs.python.org/3/tutorial/datastructures.html)                         |
| `in`                         | Schlüsselwort, um zu überprüfen, ob ein Element in einer Liste ist.                                                                                                   | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)                |
| `list1 + list2`              | Konkatination zweier Listen zu einem großen Liste                                                                                                                     | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)                |
| `list1 * zahl`               | Vervielfältigung eines Liste                                                                                                                                          | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)                |


# Tupel

| Begriff           | Kurzerklärung                                                                               | Link zur Referenz                                                                       |
|-------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Tupel             | Unveränderlicher Datentypen zur Sammlung von Daten                                          | [Referenz](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) |
| `tuple`           | Konstruktor der Klasse `tuple`, mit dem eine Liste uws. in ein Tupel übersetzt werden kann. | [Referenz](https://docs.python.org/3/library/stdtypes.html#tuple)                       |
| `len(tupel)`      | Gibt die Anzahl der Elemente im Tupel zurück.                                               | [Referenz](https://docs.python.org/3/library/functions.html#len)                        |
| `max(tupel)`      | Gibt das größte Element im Tupel zurück.                                                    | [Referenz](https://docs.python.org/3/library/functions.html#max)                        |
| `min(tupel)`      | Gibt das kleinste Element im Tupel zurück.                                                  | [Referenz](https://docs.python.org/3/library/functions.html#min)                        |
| `sum(tupel)`      | Berechnet die Summe der Elemente im Tupel.                                                  | [Referenz](https://docs.python.org/3/library/functions.html#sum)                        |
| `tupel.index()`   | Sucht nach einem Element und gibt dessen Index zurück.                                      | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| `tupel.count()`   | Zählt, wie oft ein Element im Tupel vorkommt.                                               | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| `tuple1 + tuple2` | Konkatination zweier Tupel zu einem großen Tupel                                            | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| `tuple1 * zahl`   | Vervielfältigung eines Tupels                                                               | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| `in`              | Schlüsselwort, um zu überprüfen, ob ein Element in einem Tupel ist.                         | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |


# Strings


| Funktion                    | Kurzbeschreibung                                                                                                               | Beispiel                                                                   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `str`                       | Primitiver Datentyp zum Speichern von Zeichenketten in Python.                                                                 | [Referenz](https://docs.python.org/3/library/stdtypes.html#textseq)        |
| Escape Zeichen              | Zeichen, wie `\n` für Absätze oder `\t` für Tabs.                                                                              | [Referenz](https://de.wikipedia.org/wiki/Escape_(Steuerzeichen))           |
| Unicode                     | Der Unicode-Standard legt frest, wie Schrift elektronisch gespeichert wird.                                                    | [Referenz](https://de.wikipedia.org/wiki/Unicode)                          |
| `len(string)`               | Gibt die Länge des Strings zurück.                                                                                             | [Referenz](https://docs.python.org/3/library/functions.html#len)           |
| `string.upper()`            | Konvertiert den String in Großbuchstaben.                                                                                      | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.upper)      |
| `string.lower()`            | Konvertiert den String in Kleinbuchstaben.                                                                                     | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.lower)      |
| `string.strip()`            | Entfernt Leerzeichen am Anfang und Ende des Strings.                                                                           | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.strip)      |
| `string.replace(old, new)`  | Ersetzt Teilzeichenketten im String.                                                                                           | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.replace)    |
| `string.split(delimiter)`   | Teilt den String in Teile anhand eines Trennzeichen.                                                                           | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.split)      |
| `string.find(substring)`    | Sucht nach einer Teilzeichenkette und gibt den Index des ersten Vorkommens zurück. Wenn nicht gefunden, wird -1 zurückgegeben. | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.find)       |
| `string.startswith(prefix)` | Überprüft, ob der String mit einem bestimmten Präfix beginnt.                                                                  | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.startswith) |
| `string.endswith(suffix)`   | Überprüft, ob der String mit einem bestimmten Suffix endet.                                                                    | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.endswith)   |
| `string.count(substring)`   | Zählt die Anzahl der Vorkommnisse einer Teilzeichenkette im String.                                                            | [Referenz](https://docs.python.org/3/library/stdtypes.html#str.count)      |
| `str1 + str2`               | Konkatination zweier Strings zu einem großen String                                                                            | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| `str1 * zahl`               | Vervielfältigung eines String                                                                                                  | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| `in`                        | Schlüsselwort, um zu überprüfen, ob ein String in einem anderen enthalten ist.                                                 | [Referenz](https://docs.python.org/3/library/stdtypes.html#typesseq-common)             |
| f-String                    | Strings, die sich besonders leicht formatieren lassen.                                                                         | [PEP 498](https://peps.python.org/pep-0498/)                                                                           |


# Schleifen

| Begriff           | Kurzbeschreibung                                                                                                             | Link zur Referenz                                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `for ... in ...:` | Schlüsselwort, um Schleife zu definieren, die eine Sequenz durchläuft.                                                       | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements)                                          |
| `range`           | Erstellt eine Rangeobjekt, dass ein Integerintervall umfasst.                                                                | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#the-range-function)                                      |
| `break`           | Bricht die komplette Durchführung einer Schleife ab.                                                                         | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#break-and-continue-statements-and-else-clauses-on-loops) |
| `continue`        | Bricht den aktuellen Schleifendurchlauf ab und geht an den an den Schleifenkopf                                              | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#break-and-continue-statements-and-else-clauses-on-loops) |
| `else`            | Kann nach Schleifen verwendet werden um Code nach der Schleifenausführung durchzuführen, wenn kein `break` ausgeführt wurde. | [Referenz](https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#break-and-continue-statements-and-else-clauses-on-loops) |
| `while ...:`      | Schlüsselwort, um Schleifen zu definieren, die von einer Bedingung abhäng.                                                   | [Referenz](https://docs.python.org/3/reference/compound_stmts.html?highlight=while#the-while-statement)                                |


# Sets

| Begriff                                              |                                                                                                                        | Link zur Referenz                                               |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `set`                                                | Ungeordnete Sammlung von Hashables, bei denen jedes Element höchstens ein mal auftaucht.                               | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `frozenset`                                          | Ungeordnete Sammlung von Hashables, bei denen jedes Element höchstens ein mal auftaucht, die immutable ist (wie Tupel) | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `a in set1`                                          | Prüfe, ob ein Element in einem Set ist.                                                                                | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.add(x)`                                        | Fügt das Element `x` zum Set hinzu.                                                                                    | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.remove(x)`                                     | Entfernt das Element `x` aus dem Set. Wirft einen Fehler, falls `x` nicht vorhanden ist.                               | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.discard(x)`                                    | Entfernt das Element `x` aus dem Set. Kein Fehler, wenn `x` nicht vorhanden ist.                                       | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.pop()`                                         | Entfernt und gibt ein zufälliges Element aus dem Set zurück.                                                           | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.clear()`                                       | Entfernt alle Elemente aus dem Set.                                                                                    | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.union(set2)` oder `set1 ǀ set2`                | Gibt ein Set zurück, dass die Summe der Elemente von `set1` und `set2` enthält                                         | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |                                                                                                     | Gibt ein neues Set zurück, das die Vereinigung von `set1` und `set2` ist.                              | `set3 = set1.union(set2)`                |
| `set1.intersection(set2)` oder `set1 & set2`         | Gibt ein neues Set zurück, das die Schnittmenge von `set1` und `set2` ist.                                             | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.difference(set2)` oder `set1 - set2`           | Gibt ein neues Set zurück, das die Elemente von `set1` enthält, die nicht in `set2` sind.                              | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |
| `set1.symmetric_difference(set2)` oder `set1 ^ set2` | Gibt ein neues Set zurück, das Elemente enthält, die in `set1` oder `set2`, aber nicht in beiden sind.                 | [Referenz](https://docs.python.org/3/library/stdtypes.html#set) |


# Dictionaries

| Begriff              | Kurzerklörung                                                                                                                    | Link zur Referenz                                                              |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `dictionary`         | Ein Datencontainer mit dem man Werte und schlüssel miteinander assoziieren kann.                                                 | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| Schlüssel            | Value über den im Dictionary ein Wert referenziert wird.                                                                         | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| Wert                 | Für ein Schlüssel gespeicherter Value                                                                                            | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| Schlüssel-Wert-Paare | Paar auch Schlüssel und Wert (Key-Value-Pair)                                                                                    | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `my_dict[key]`       | Greif auf den Wert mit dem Key `key` zu. Existiert dieser nicht wird er beim Schreiben erstellt. Beim Lesen gibt es einen Fehler | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `get(key)`           | Gibt den Wert für den angegebenen Schlüssel zurück. Gibt `None` zurück, wenn der Schlüssel nicht existiert.                      | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `keys()`             | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel des Dictionaries enthält.                                               | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `values()`           | Gibt ein neues Ansichtsobjekt zurück, das alle Werte des Dictionaries enthält.                                                   | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `items()`            | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel-Wert-Paare des Dictionaries als Tupel enthält.                          | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `update(dict2)`      | Aktualisiert das Dictionary mit Schlüssel-Wert-Paaren aus einem anderen Dictionary oder iterierbaren Schlüssel-Wert-Paaren.      | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `pop(key)`           | Entfernt den Eintrag mit dem angegebenen Schlüssel und gibt dessen Wert zurück.                                                  | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `popitem()`          | Entfernt und gibt ein zufälliges Schlüssel-Wert-Paar als Tupel zurück.                                                           | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `clear()`            | Entfernt alle Elemente aus dem Dictionary.                                                                                       | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |
| `copy()`             | Erstellt eine flache Kopie des Dictionaries.                                                                                     | [Referenz](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) |


# Funktionen

| Begriff                             | Kurzerklörung                                                                                                                           | Link zur Referenz                                                        |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Funktion                            | Ein gekapselter Codeteil, der von anderer Stelle aus aufgerufen werden kann.                                                            | [Referenz](https://docs.python.org/3/glossary.html#term-function)        |
| `def`                               | Kennzeichnet die Definition einer Funktion oder Methode in Pythoncode.                                                                  | [Referenz](https://docs.python.org/3/glossary.html#term-function)        |
| Parameter                           | Platzhalter Werte welche an Funktionne übergeben werden.                                                                                | [Referenz](https://docs.python.org/3/glossary.html#term-parameter)       |
| Argument                            | Name für die Werte, die für die Parameter eingesetzt werden.                                                                            | [Referenz](https://docs.python.org/3/glossary.html#term-argument)        |
| `return`                            | Optionales Keyword, das einzeigt, dass der nachfolgende Code in der Zeile die Rückgabe der Funktion ist.                                | [Referenz](https://docs.python.org/3/reference/simple_stmts.html#return) |
| Callstack                           | Der Liste von Funktionenaufrufen, die aufeinander basieren.                                                                             |                                                                          |
| Funktionen als First Class Citizens | Funktionen werden als Objekte behandelt und können dementsprechend als Argumente an Funktionen übergeben werden.                        | [Referenz](https://de.wikipedia.org/wiki/First-Class-Funktion)           |
| `id`                                | Gibt die Id eines Objektes zurück.                                                                                                      | [Referenz](https://docs.python.org/3/library/functions.html#id)          |

# Booleans

| Begriff           | Kurzerklörung                                                                          | Link zur Referenz                                                                        |
|-------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `and`             | Funktion, die primär für Booleans angewandt wird und dem logichsen "und" entspricht.   | [Referenz](https://docs.python.org/3/reference/expressions.html#boolean-operations)      |
| `or`              | Funktion, die primär für Booleans angewandt wird und dem logichsen "oder" entspricht.  | [Referenz](https://docs.python.org/3/reference/expressions.html#boolean-operations)      |
| `not`             | Funktion, die primär für Booleans angewandt wird und dem logichsen "nicht" entspricht. | [Referenz](https://docs.python.org/3/reference/expressions.html#boolean-operations)      |
| Ternärer Operator | Kurzschreibweise um, eine Variable unter einer Bedingung verschieden zuzuordnen.       | [Referenz](https://docs.python.org/3/reference/expressions.html#conditional-expressions) |


# Type Hints

| Begriff          | Kurzerklärung                                               | Link zur Referenz                                                                     |
|------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Type Hint        | Optionaler Typhinweis einer Variable oder Funktionrückgabe. | [PEP 484](https://peps.python.org/pep-0484/)                                          |
| `typing`         | Modul, um Typehinweise durchzuführen.                       | [Python Dokumentation](https://docs.python.org/3/library/typing.html#module-typing)   |
| `Sequence`       | Zusammenfassender Typ aus dem Typingmodul.                  | [Python Dokumentation](https://docs.python.org/3/library/typing.html#typing.Sequence) |
| `Optional`       | Zeigt an, dass der Typ auch None sein kann.                 | [Python Dokumentation](https://docs.python.org/3/library/typing.html#typing.Optional) |
| `Union` oder `ǀ` | Vereinigt mehrere mögliche Typen.                           | [Python Dokumentation](https://docs.python.org/3/library/typing.html#typing.Union)    |
| `Any`            | Typ, der beliebigen Typ beschreibt.                         | [Python Dokumentation](https://docs.python.org/3/library/typing.html#typing.Any)      |

# Bytecode

| Begriff                   | Kurzerklärung                                                                                                                                  | Link zur Referenz                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Bytecode                  | Eine übersetzte Repräsentation eines Programmes, welches für einen Pythoninterpreter verständlich ist.                                         | [Referenz](https://docs.python.org/3/glossary.html#term-bytecode)  |
| Maschinencode             | Code welcher für Prozessoren verständlich, aber für Menschen unverständlich ist.                                                               | [Referenz](https://en.wikipedia.org/wiki/Machine_code)             |
| `dis` Module              | Programmmodule welche das rück-übersetzen von Bytecode zu für Menschen lesbaren Text ermöglicht.                                               | [Referenz](https://docs.python.org/3/library/dis.html#)            |
| Kompilieren               | Übersetzen in Programmcode in eine für den Computer verständliche Repräsentation.                                                              | [Referenz](https://de.wikipedia.org/wiki/Compiler)                 |
| Interpretieren            | Übersetzt wie der Compiler Programmcode in eine für den Computer verständliche Repräsentation, jedoch wird nicht alles im vorhinein übersetzt. | [Referenz](https://de.wikipedia.org/wiki/Interpreter)              |


# List Comprehension

| Begriff            | Kurzerklärung                                                                                                                                    | Link zur Referenz                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| List Comprehension | Sammelbegriff für die Anwendung von Funktionen auf Listen, Sets, uws., welche in anderen Programmiersprachen mit Schleifen gelöst werden müssen. | [Referenz](https://docs.python.org/3/glossary.html#term-list-comprehension) |
| `generator`        | Funktion, die über `next` neue Elemente liefert.                                                                                                 | [Referenz](https://docs.python.org/3/glossary.html#term-generator)          |

# zip

| Begriff     | Kurzerklärung                                                  | Link zur Referenz                                                                              |
|-------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| `zip`       | Methode zur Elementweisen Bildung von Paaren zweier Iterables. | [Referenz](https://docs.python.org/3/library/functions.html?highlight=zip#zip)                 |
| `enumarate` | Methode die Index un Element in eines Iterables zurückgibt.    | [Referenz](https://docs.python.org/3/library/functions.html#enumerate)                 |

# Try Except

| Begriff         | Kurzerklärung                                                     | Link zur Referenz                                                                       |
|-----------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `BaseException` | Basisklasse, um Ausnahmen im Programmcode darzustellen.           | [Referenz](https://docs.python.org/3/library/exceptions.html)                           |
| `try`           | Einleitung des Blocks in dem eine Exception geworfen werden kann. | [Referenz](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)   |
| `except`        | Behandlung einer Ausnahme.                                        | [Referenz](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)   |
| `finally`       | Abschluss, der immer ausgeführt wird.                             | [Referenz](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)   |
| `raise`         | Werfen einer Exception                                            | [Referenz](https://docs.python.org/3/reference/compound_stmts.html#the-raise-statement) |
| `else`          | optionaler Block, falls keine Exception auftrat                   | [Referenz](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)   |
| `class`         | Schlüsselwort, um Klasse und Exceptions zu definieren             | [Referenz](https://docs.python.org/3/reference/classes.html)                            |

# Docstring

| Begriff   | Kurzerklärung                                                                                  | Link zur Referenz                                                  |
|-----------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Docstring | Mehrzeiliger String z.B. unter einem Funktionskopf, der die Nutzung der Funktion dokumentiert. | [Referenz](https://docs.python.org/3/glossary.html#term-docstring) |

# Klassen definieren und instanziieren

| Begriff           | Kurzerklärung                                                                          | Link zur Referenz                                                                   |
|-------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Klasse            | Eine Blaupause für Instanzen, also vom Nutzer definierte Objekte.                      | [Referenz](https://docs.python.org/3/glossary.html#term-class)                      |
| `class`           | Schlüsselwort, mit dem eine Klasse in Python definiert wird.                           | [Referenz](https://docs.python.org/3/tutorial/classes.html#class-definition-syntax) |
| instanziieren     | Fachbegriff, der ausdrückt, dass ein Objekt einer bestimmten Klasse erzeugt wird.      | [Referenz](https://docs.python.org/3/tutorial/classes.html#class-objects)           |
| `is` und `is not` | Funktion, um herauszufinden, ob in zwei Variablen die _selbe_ Instanz gespeichert ist. | [Referenz](https://docs.python.org/3/reference/expressions.html#is)                 |

# Attribute

| Begriff         | Kurzerklärung                                                               | Link zur Referenz                                                                        |
|-----------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Attribut        | Eigenschaft einer Instanz.                                                  | [Referenz](https://docs.python.org/3/reference/datamodel.html#id3)                       |
| Klassenattribut | Eigenschaft einer Klasse, die von jeder Instanz aus aufgerufen werden kann. | [Referenz](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables) |
| `x.__dict__`    | Auflistung der Attribute einer Instanz.                                     | [Referenz](https://docs.python.org/3/reference/datamodel.html#id3)                       |

# Methoden

| Begriff    | Kurzerklärung                                                   | Link zur Referenz                                                              |
|------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------|
| Methode    | Funktion in einer Klasse                                        | [Referenz](https://docs.python.org/3/glossary.html#term-method)                |
| `self`     | Erste Parameter in einer Methode, der die Instanz referenziert. | [Referenz](https://docs.python.org/3/glossary.html#term-method)                |
| `__init__` | Methode, die eine neu erstelle Instanz inizialisiert.           | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__init__) |
| `__new__`  | Funktion, die eine neu erstelle Instanz inizialisiert.          | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__new__)  |


# Unittests

| Begriff    | Kurzerklärung                                                                                                    | Link zur Referenz                                                                      |
|------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `unittest` | Ein integriertes Testframework-Modul in Python                                                                   | [Referenz](https://docs.python.org/3/library/unittest.html)                            |

[Liste mit Methoden der Klasse Testcase](../lehrplan/python_grundlagen/oop/unittests/unittests.md#methoden-der-klasse-testcase)

# Vererbung

| Begriff   | Kurzerklärung                                                                                                                                                | Link zur Referenz                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Vererbung | Das Konzept, bei dem eine Klasse (Unterklasse) von einer anderen Klasse (Basisklasse) erbt, um deren Attribute und Methoden zu nutzen und/oder zu erweitern. | [Referenz](https://docs.python.org/3/tutorial/classes.html#inheritance) |
| super()   | Ein Funktionsaufruf, der in einer abgeleiteten Klasse verwendet wird, um auf Methoden oder Attribute der Basisklasse zuzugreifen.                            | [Referenz](https://docs.python.org/3/library/functions.html#super)      |


# Magic Methods
| Begriff        | Kurzerklärung                                                                                                                                                                                        | Link zur Referenz                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `__str__`      | Diese magische Methode wird aufgerufen, wenn die `str`-Funktion auf ein Objekt angewendet wird. Sie ermöglicht die Definition einer benutzerfreundlichen Zeichenfolge, die das Objekt repräsentiert. | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__str__)      |
| `__add__`      | Diese magische Methode wird aufgerufen, wenn das `+`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Addition von zwei Objekten der Klasse.                                | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__add__)      |
| `__len__`      | Diese magische Methode wird aufgerufen, wenn die `len`-Funktion auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Anzahl von Elementen in einem Objekt.                              | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__len__)      |
| `__sub__`      | Diese magische Methode wird aufgerufen, wenn das `-`-Zeichen auf ein Objekt angewendet wird. Sie ermöglicht die Definition der Subtraktion von zwei Objekten der Klasse.                             | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__sub__)      |
| `__eq__`       | Diese magische Methode wird aufgerufen, um die Gleichheit von zwei Objekten zu überprüfen.                                                                                                           | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__eq__)       |
| `__ne__`       | Diese magische Methode wird aufgerufen, um die Ungleichheit von zwei Objekten zu überprüfen.                                                                                                         | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__ne__)       |
| `__lt__`       | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt kleiner als ein anderes ist.                                                                                                 | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__lt__)       |
| `__le__`       | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt kleiner oder gleich einem anderen ist.                                                                                       | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__le__)       |
| `__gt__`       | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt größer als ein anderes ist.                                                                                                  | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__gt__)       |
| `__ge__`       | Diese magische Methode wird aufgerufen, um festzustellen, ob ein Objekt größer oder gleich einem anderen ist.                                                                                        | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__ge__)       |
| `__getitem__`  | Diese magische Methode wird aufgerufen, um den Zugriff auf ein Element mittels Index zu ermöglichen.                                                                                                 | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__getitem__)  |
| `__setitem__`  | Diese magische Methode wird aufgerufen, um das Setzen eines Elements mittels Index zu ermöglichen.                                                                                                   | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__setitem__)  |
| `__contains__` | Diese magische Methode wird aufgerufen, um zu prüfen, ob ein Objekt ein bestimmtes Element enthält.                                                                                                  | [Referenz](https://docs.python.org/3/reference/datamodel.html#object.__contains__) |

# Class staticmethod

| Begriff        | Kurzerklärung                                                       | Link zur Referenz                                                         |
|----------------|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| `staticmethod` | ist ein Dekorator für die Definition statischer Methoden in Python. | [Referenz](https://docs.python.org/3/library/functions.html#staticmethod) |
| `classmethod`  | ist ein Dekorator für die Definition von Klassenmethoden in Python. | [Referenz](https://docs.python.org/3/library/functions.html#classmethod)  |

# Getter Setter

| Begriff                   | Kurzerklärung                                                                                                                                                                                                                                                       | Link zur Referenz                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Getter und Setter         | Getter und Setter sind Methoden, die den Lese- und Schreibzugriff auf Attribute ermöglichen. Der Getter liest den Wert eines Attributs, während der Setter den Wert setzt.                                                                                          | [Referenz](https://docs.python.org/3/library/functions.html#property)           |
| `@property`               | `@property` ist ein Dekorator in Python, der es ermöglicht, eine Methode wie ein Attribut zu behandeln. Es wird verwendet, um den Zugriff auf Attribute zu steuern.                                                                                                 | [Referenz](https://docs.python.org/3/library/functions.html#property)           |
| `@setter`                 | `@setter` ist ein spezifischer Dekorator, der mit `@property` verwendet wird, um die Setzung eines Attributs zu steuern. Es wird verwendet, um die Zuweisung eines Werts über den Setter zu ermöglichen.                                                            | [Referenz](https://docs.python.org/3/library/functions.html#property)           |
| Getter                    | Ein Getter ist eine Methode, die den Wert eines privaten Attributs zurückgibt. Es ermöglicht den Lesezugriff auf das Attribut von außerhalb der Klasse. Der Getter wird normalerweise mit `@property` implementiert.                                                | [Referenz](https://de.wikipedia.org/wiki/Zugriffsfunktion)                      |
| Setter                    | Ein Setter ist eine Methode, die den Wert eines privaten Attributs setzt. Es ermöglicht den Schreibzugriff auf das Attribut von außerhalb der Klasse. Der Setter wird normalerweise mit `@setter` implementiert.                                                    | [Referenz](https://de.wikipedia.org/wiki/Zugriffsfunktion)                      |

[//]: # (| Einzelnes Unterstrich     | Ein einzelnes Unterstrichzeichen vor einem Attribut &#40;z. B. `_attribut`&#41; signalisiert, dass es als schwach "internen" oder "privaten" Verweis betrachtet werden sollte. Es ist jedoch nur eine Konvention und hat keine eigentliche Auswirkung auf die Sichtbarkeit. | [Referenz]&#40;https://www.python.org/dev/peps/pep-0008/#single-leading-underscore&#41; |)
[//]: # (| Sichtbarkeit &#40;Visibility&#41; | Sichtbarkeit bezieht sich auf die Zugriffsberechtigungen von Attributen und Methoden. In Python gibt es keine strikte Privatsphäre, sondern nur Konventionen, die durch Namenskonventionen und Name Mangling erreicht werden.                                       | [Referenz]&#40;https://de.wikipedia.org/wiki/Sichtbarkeit_&#40;Programmierung&#41;&#41;         |)

# Dateioperationen

| Begriff        | Kurzerklärung                                                        | Link zur Referenz                                                                |
|----------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `open`         | Eine Funktion  um eine Datei zu öffnen                               | [Referenz](https://docs.python.org/3/library/functions.html?highlight=open#open) |
| absolute Pfade | Der vollständige Speicherort einer Datei                             | [Referenz](https://www.codingrooms.com/blog/file-paths)                          |
| relative Pfade | Der Speicherort einer Datei  in relation zum aktuellen Arbeitsordner | [Referenz](https://www.codingrooms.com/blog/file-paths)                          |
| r-Präfix       | Ein String in welchem Escape-Zeichen deaktiviert sind                | [Referenz](https://docs.python.org/3/reference/lexical_analysis.html)            |

# args kwargs

| Begriff  | Kurzerklärung                                                                                                | Link zur Referenz                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `args`   | Erlaubt den Umgang mit einer variablen Anzahl von **nicht**-schlüsselwortbasierten Argumenten in Funktionen. | [Referenz](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) |
| `kwargs` | Ermöglicht den Umgang mit einer variablen Anzahl von schlüsselwortbasierten Argumenten in Funktionen.        | [Referenz](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) |

# Module

| Begriff                      | Kurzerklärung                                                                                                       | Link zur Referenz                                                                      |
|------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Modul                        | Eine .py Datei. Diese kann in anderen Pythondatein eingebunden werden, um die implementierten Funktionen zu nutzen. | [Referenz](https://docs.python.org/3/tutorial/modules.html)                            |
| `import`                     | Importiert ein Modul oder Teile davon in ein Python-Skript.                                                         | [Referenz](https://docs.python.org/3/reference/simple_stmts.html#import)               |
| `from`                       | Importiert spezifische Teile aus einem Modul oder Paket.                                                            | [Referenz](https://docs.python.org/3/reference/simple_stmts.html#from)                 |
| `as`                         | Ermöglicht das Festlegen von Aliasen für Module oder importierte Teile.                                             | [Referenz](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement) |
| `random`                     | Ein Modul mit vielen Funktionen um Pseudozufallszahlen zu erzeugen.                                                 | [Referenz](https://docs.python.org/3/library/random.html)                              |
| `if __name__ == "__main__":` | Zeigt Code an, der Nur ausgeführt wird, wenn diese Pythondatei ausgeführt wird.                                     | [Referenz](https://docs.python.org/3/library/__main__.html#module-__main__)            |

# Pakete

| Begriff                      | Kurzerklärung                                                                                                       | Link zur Referenz                                                                      |
|------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Paket                        | Eine Sammlung von Modulen in einem Verzeichnis, das einem Namespace entspricht. Pakete strukturieren den Python-Code. | [Referenz](https://docs.python.org/3/tutorial/modules.html#packages)                            |
| `__init__.py`                | Eine Datei, die angibt, dass ein Verzeichnis als Python-Paket behandelt werden sollte. Sie kann Initialisierungscode für das Paket enthalten.                               | [Referenz](https://docs.python.org/3/reference/import.html#regular-packages)           |
| `site-packages`              | Ein Verzeichnis, in dem Drittanbieter-Pakete installiert werden. Es ist Teil des Python-Suchpfads, auf den `import` zugreift. | [Referenz](https://docs.python.org/3/tutorial/modules.html#the-module-search-path) |
| `PyPI`                       | Die Python Package Index ist ein Repository von Software für die Programmiersprache Python. Nutzer können Pakete hochladen und installieren. | [Referenz](https://pypi.org/) |

# Pip und Venv

| Begriff                       | Kurzerklärung                                                                                                       | Link zur Referenz                                                                      |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `pip`                        | Das Paketinstallationsprogramm für Python. Es ermöglicht das Installieren, Aktualisieren und Entfernen von Paketen. | [Referenz](https://pip.pypa.io/en/stable/cli/pip_install/) |
| `virtualenv`                 | Ein Werkzeug zum Erstellen isolierter Python-Umgebungen. Jede Umgebung kann eigene Paketversionen haben, unabhängig von anderen Umgebungen. | [Referenz](https://virtualenv.pypa.io/en/latest/) |
| `requirements.txt`           | Eine Datei, die die Paketabhängigkeiten für ein Python-Projekt auflistet. Es wird oft verwendet, um eine konsistente Umgebung für Projekte zu gewährleisten. | [Referenz](https://pip.pypa.io/en/stable/reference/requirements-file-format/) |
| `pip --version`               | Ein Befehl im Terminal, um die installierte Version von pip zu überprüfen.                                           | [Referenz](https://pip.pypa.io/en/stable/reference/pip_version/) |
| `pip list`                    | Listet alle auf dem System installierten Python-Pakete auf.                                                         | [Referenz](https://pip.pypa.io/en/stable/reference/pip_list/) |
| `pip search PACKAGE_NAME`     | Sucht nach einem spezifischen Paket auf PyPI, ersetzt `PACKAGE_NAME` mit dem Namen des gesuchten Pakets. Hinweis: Diese Funktion wurde in neueren Versionen von pip entfernt. | [Referenz](https://pip.pypa.io/en/stable/news/) |
| `pip install PACKAGE_NAME`    | Installiert ein Python-Paket, wobei `PACKAGE_NAME` der Name des gewünschten Pakets ist.                              | [Referenz](https://pip.pypa.io/en/stable/reference/pip_install/) |
| `venv`                        | Ein Modul zur Erstellung isolierter Python-Umgebungen, um Abhängigkeitskonflikte zwischen Projekten zu vermeiden.    | [Referenz](https://docs.python.org/3/library/venv.html) |
| `python -m venv venv_name`    | Erstellt eine neue virtuelle Umgebung mit dem Namen `venv_name`.                                                     | [Referenz](https://docs.python.org/3/library/venv.html) |
| `source {venv_name}/bin/activate` | Aktiviert die virtuelle Umgebung `venv_name`, sodass deren Pakete und Skripte im aktuellen Terminal verwendet werden können. | [Referenz](https://docs.python.org/3/library/venv.html) |
| `deactivate`                  | Deaktiviert die aktuelle virtuelle Umgebung und kehrt zur globalen Python-Umgebung zurück.                           | [Referenz](https://docs.python.org/3/library/venv.html) |


[//]: # (# Under Construction 👷‍♂️👷‍♀️)

[//]: # (# pip)

[//]: # ()
[//]: # (| Begriff     | Kurzerklärung                                                                                                | Link zur Referenz                                                             |)

[//]: # (|-------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|)

[//]: # (| `pip`       | Ein Programm zum Verwalten von Softwarepaketen. Diese können fertige Python Programme und Bibliotheken sein. | [Referenz]&#40;https://pip.pypa.io/en/stable/&#41;                                    |)

[//]: # (| `install`   | Der installierungs-Unterbefehl für pip um Pakete auf dem System zu installieren.                             | [Referenz]&#40;https://pip.pypa.io/en/stable/cli/pip_install/&#41;                    |)

[//]: # (| `upgrade`   | Der aktualisierungs-Unterbefehl für pip um Pakete auf dem System zu aktualisieren.                           | [Referenz]&#40;https://pip.pypa.io/en/stable/cli/pip_install/#upgrading-packages&#41; |)

[//]: # (| `uninstall` | Das Gegenteil von install.                                                                                   | [Referenz]&#40;https://pip.pypa.io/en/stable/cli/pip_uninstall/&#41;                  |)

[//]: # (| `list`      | Betrachten und auflisten von lokal installierten Paketen.                                                    | [Referenz]&#40;https://pip.pypa.io/en/stable/cli/pip_list/&#41;                       |)

[//]: # (| `search`    | Suchen von verfügbaren Paketen.                                                                              | [Referenz]&#40;https://pip.pypa.io/en/stable/cli/pip_search/&#41;                     |)

[//]: # ()
[//]: # (# OOP Intro)

[//]: # ()
[//]: # (| Begriff        | Kurzerklärung                                                                                                                                              | Link zur Referenz                                                         |)

[//]: # (|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|)

[//]: # (| Klassen        | Ein Bauplan für Objekte, der Attribute &#40;Variablen&#41; und Methoden &#40;Funktionen&#41; definiert. In Python wird eine Klasse mit dem Schlüsselwort `class` erstellt. | [Referenz]&#40;https://de.wikipedia.org/wiki/Klasse_&#40;Objektorientierung&#41;&#41;     |)

[//]: # (| Objekte        | Eine Instanz einer Klasse. Mit dem Befehl `objekt = Klasse&#40;&#41;` wird eine Instanz der Klasse erstellt.                                                       | [Referenz]&#40;https://de.wikipedia.org/wiki/Objekt_&#40;Programmierung&#41;&#41;         |)

[//]: # (| Vererbung      | Die Übertragung von Eigenschaften von Objekten durch eine relationale Beziehung.                                                                           | [Referenz]&#40;https://de.wikipedia.org/wiki/Vererbung_&#40;Programmierung&#41;&#41;      |)

[//]: # (| Polymorphismus | Die Fähigkeit eines Objektes unterschiedlichen Klassen zu entsprechen.                                                                                     | [Referenz]&#40;https://de.wikipedia.org/wiki/Polymorphie_&#40;Programmierung&#41;&#41;    |)

[//]: # (| Kapselung      | Daten werden in einer Struktur zusammengefasst. Der Zugriff auf diese Daten erfolgt durch Prozeduren.                                                      | [Referenz]&#40;https://de.wikipedia.org/wiki/Datenkapselung_&#40;Programmierung&#41;&#41; |)

[//]: # ()
[//]: # (# OOP Python)

[//]: # ()
[//]: # (| Begriff          | Kurzerklärung                                                                                                                                                                                     | Link zur Referenz                                                            |)

[//]: # (|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|)

[//]: # (| Instanz          | Ein konkretes Vorkommen eines Objekts. Wenn du ein Objekt von einer Klasse erstellst, erstellst du eine Instanz dieser Klasse.                                                                    | [Referenz]&#40;https://de.wikipedia.org/wiki/Objekt_&#40;Programmierung&#41;&#41;            |)

[//]: # (| Attribut         | Eine Variable, die zur Darstellung von Eigenschaften oder Merkmalen eines Objekts verwendet wird. In Python können Attribute in der `__init__`-Methode der Klasse initialisiert werden.           | [Referenz]&#40;https://de.wikipedia.org/wiki/Attribut_&#40;Programmierung&#41;&#41;          |)

[//]: # (| Methode          | Eine Funktion, die zu einer Klasse gehört und auf Objekten dieser Klasse aufgerufen wird. Methoden werden innerhalb der Klasse definiert und können auf Objekten dieser Klasse aufgerufen werden. | [Referenz]&#40;https://de.wikipedia.org/wiki/Methode_&#40;Programmierung&#41;&#41;           |)

[//]: # (| `class`          | Ein Konventionsschlüsselwort in Python, das als erstes Argument in den Methoden einer Klasse verwendet wird und auf die Instanz der Klasse verweist.                                              | [Referenz]&#40;https://docs.python.org/3/tutorial/classes.html&#41;                  |)

[//]: # (| `self`           | Das Schlüsselwort in Python, um eine Klasse zu definieren.                                                                                                                                        | [Referenz]&#40;https://docs.python.org/3/tutorial/classes.html#instance-objects&#41; |)

[//]: # (| `Instanzmethode` | Eine Methode, die auf Instanzen einer Klasse angewendet wird und automatisch das `self`-Argument enthält.                                                                                         | [Referenz]&#40;https://docs.python.org/3/tutorial/classes.html#instance-methods&#41; |)

[//]: # ()



[//]: # (# pep)

[//]: # ()
[//]: # (| Begriff      | Kurzerklärung                                                                      | Link zur Referenz                                     |)

[//]: # (|--------------|------------------------------------------------------------------------------------|-------------------------------------------------------|)

[//]: # (| PEP 8        | Der Python Style Guide über Python Code                                            | [Referenz]&#40;https://www.python.org/dev/peps/pep-0008/&#41; |)

[//]: # (| PEP 20       | Der Python Style Guide über allgemeine Regeln zu Python                            | [Referenz]&#40;https://www.python.org/dev/peps/pep-0020/&#41; |)

[//]: # (| PEP 257      | Der Python Style Guide über Docstring Conventions                                  | [Referenz]&#40;https://www.python.org/dev/peps/pep-0257/&#41; |)

[//]: # (| Konventionen | Regeln welche meist die Art und Weise der Formatierung von Dokumenten beschreiben. | [Referenz]&#40;https://de.wikipedia.org/wiki/Styleguide&#41;  |)

[//]: # (| Style Guide  | Eine Ansammlung von Konventionen als Dokument.                                     | [Referenz]&#40;https://de.wikipedia.org/wiki/Styleguide&#41;  |)

[//]: # (| Docstrings   | Eine Zeichenkette in einem Modul welche als Dokumentation dient.                   | [Referenz]&#40;https://peps.python.org/pep-0257/&#41;         |)

[//]: # (# Design Patterns)

[//]: # ()
[//]: # (| Begriff            | Kurzerklärung                                                                                                                                      | Link zur Referenz                                                     |)

[//]: # (|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|)

[//]: # (| Design Pattern     | Eine abstrakte Regel zur Strukturierung von Code in eine bestimmtes Muster.                                                                        | [Referenz]&#40;https://de.wikipedia.org/wiki/Entwurfsmuster&#41;              |)

[//]: # (| Creational Pattern | Diese Muster befassen sich mit der Instanziierung von Objekten. Beispiele sind das Singleton-Muster und das Factory-Muster.                        | [Referenz]&#40;https://de.wikipedia.org/wiki/Erzeugungsmuster&#41;            |)

[//]: # (| Structural Pattern | Diese Muster beschäftigen sich mit der Zusammensetzung von Klassen und Objekten. Beispiele sind das Adapter-Muster und das Decorator-Muster.       | [Referenz]&#40;https://de.wikipedia.org/wiki/Strukturmuster&#41;              |)

[//]: # (| Behavioral Pattern | Diese Muster definieren den Austausch von Informationen zwischen Objekten und Klassen. Beispiele sind das Observer-Muster und das Strategy-Muster. | [Referenz]&#40;https://de.wikipedia.org/wiki/Verhaltensmuster_&#40;Software&#41;&#41; |)

[//]: # ()

[//]: # (# Strategy)

[//]: # ()
[//]: # (| Begriff          | Kurzerklärung                                                                                                                                                                                                 | Link zur Referenz                                                     |)

[//]: # (|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|)

[//]: # (| Verhaltensmuster | Ein Verhaltensmuster definiert, wie Objekte zusammenarbeiten, um bestimmte Verhaltensweisen zu realisieren. Es legt fest, wie Klassen und Objekte miteinander interagieren.                                   | [Referenz]&#40;https://de.wikipedia.org/wiki/Verhaltensmuster_&#40;Software&#41;&#41; |)

[//]: # (| Algorithmus      | Ein Algorithmus ist eine Schritt-für-Schritt-Anleitung zur Lösung eines bestimmten Problems oder zur Durchführung einer Aufgabe. Im Kontext des Strategy Patterns sind verschiedene Algorithmen austauschbar. | [Referenz]&#40;https://de.wikipedia.org/wiki/Algorithmus&#41;                 |)

[//]: # ()
[//]: # (# Factory Method)

[//]: # ()
[//]: # (| Begriff          | Kurzerklärung                                                                                                                                                                                                                                                                       | Link zur Referenz                                                                                  |)

[//]: # (|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|)

[//]: # (| Erzeugungsmuster | Erzeugungsmuster befassen sich mit der Art und Weise, wie Objekte erstellt werden. Sie kapseln den Instanziierungsprozess und stellen sicher, dass die Art der Erstellung eines Objekts flexibel bleibt.                                                                            | [Referenz]&#40;https://de.wikipedia.org/wiki/Erzeugungsmuster&#41;                                         |)

[//]: # (| Schnittstelle    | Eine Schnittstelle definiert, welche Methoden eine Klasse implementieren muss, ohne die genaue Implementierung vorzuschreiben. Im Kontext des Factory Method Patterns kann eine Schnittstelle die abstrakte Methode darstellen, die von den konkreten Produkten implementiert wird. | [Referenz]&#40;https://de.wikipedia.org/wiki/Schnittstelle_&#40;Objektorientierung&#41;&#41;                       |)

[//]: # (| Instantiierung   | Instantiierung bezieht sich auf den Prozess, bei dem eine Klasse ein Objekt erstellt. Im Zusammenhang mit Erzeugungsmustern wie dem Factory Method Pattern wird die Instantiierung in abgeleitete Klassen ausgelagert.                                                              | [Referenz]&#40;https://de.wikipedia.org/wiki/Objekt_&#40;Programmierung&#41;#Objektorientierte_Programmierung&#41; |)

[//]: # ()
[//]: # (# Adapter)

[//]: # ()
[//]: # (| Begriff        | Kurzerklärung                                                                                                                                                                                             | Link zur Referenz                                                                                  |)

[//]: # (|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|)

[//]: # (| Kompatibilität | Im Kontext von Design Patterns bezieht sich Kompatibilität darauf, wie gut verschiedene Klassen oder Komponenten miteinander arbeiten können, insbesondere wenn ihre Schnittstellen unterschiedlich sind. | [Referenz]&#40;https://de.wikipedia.org/wiki/Objekt_&#40;Programmierung&#41;#Objektorientierte_Programmierung&#41; |)

[//]: # (| Zusammenarbeit | Zusammenarbeit beschreibt die Interaktion und Koordination von verschiedenen Klassen oder Komponenten, um ein gemeinsames Ziel zu erreichen.                                                              | [Referenz]&#40;https://de.wikipedia.org/wiki/Objekt_&#40;Programmierung&#41;#Objektorientierte_Programmierung&#41; |)

[//]: # ()
[//]: # ()
[//]: # (# OOP vs Funktional)

[//]: # ()
[//]: # (| Begriff            | Kurzerklärung                                                                            | Link zur Referenz                                                                      |)

[//]: # (|--------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|)

[//]: # (| Unveränderlichkeit | Betont die Verwendung von unveränderlichen Daten.                                        | [Referenz]&#40;https://docs.python.org/3/library/functools.html#immutable-functional-data&#41; |)

[//]: # (| Höhere Ordnung     | Funktionen, die andere Funktionen als Argumente akzeptieren oder Funktionen zurückgeben. | [Referenz]&#40;https://docs.python.org/3/howto/functional.html#higher-order-functions&#41;     |)

[//]: # (| Rekursion          | Die Technik, bei der eine Funktion sich selbst aufruft.                                  | [Referenz]&#40;https://docs.python.org/3/tutorial/controlflow.html#defining-functions&#41;     |)

[//]: # (| Lambda-Funktionen  | Anonyme Funktionen, erstellt mit dem `lambda`-Schlüsselwort.                             | [Referenz]&#40;https://docs.python.org/3/reference/expressions.html#lambda&#41;                |)

[//]: # (| `in`              | Schlüsselwort, um zu überprüfen, ob ein Element in eine Tupel ist.                          | `1 in &#40;3,2,1&#41; # True`                                                                   |)


