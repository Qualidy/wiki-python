# Dictionaries (Schlüssel-Wert-Paare):

<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/X4zTZUsRaH4?si=yv0MYIVcgN6l1DJZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>


Dictionaries sind ein Datentyp in Python, mit dem wir Schlüssel-Wert-Paar beschreiben können. 
Sie ermöglichen uns, Werte mithilfe von Schlüsseln zu speichern und abzurufen, ähnlich wie ein echtes Wörterbuch es 
erlaubt, die Bedeutung eines Wortes zu finden. Wir erinnern uns an Listen oder Tupels, bei denen wir auf die Elemente
durch ihre Position in der Sammlung, also deren Index, auf die Elemente zugreifen können. 

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=mein_dict%20%3D%20%7B%22Name%22%3A%20%22Max%22,%20%22Alter%22%3A%2025,%20%22Stadt%22%3A%20%22Berlin%22%7D%0Aprint%28mein_dict%29&cumulative=false&curInstr=2&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict)
```


## Eigenschaften von Dictionaries

[//]: # ([30min])

- **Schlüssel und Werte**: Jeder Eintrag in einem Dictionary besteht aus einem Schlüssel und einem zugehörigen Wert.

- **Einzigartige Schlüssel**: Jeder Schlüssel in einem Dictionary muss einzigartig sein. Sollen mehrere Elemente 
    in einem Schlüssel gespeichert werden, kann man natürlich auch eine Liste für diesen Schlüssel speichern.

- **Veränderbar**: Dictionaries sind veränderbar, was bedeutet, dass Einträge hinzugefügt, entfernt oder geändert
   werden können.

- **Ungeordnet**: Die Elemente in einem Dictionary sind nicht in einer bestimmten Reihenfolge gespeichert. Man greift 
    auf die Elemente über deren Schlüssel zu.

- **Dynamisch**: Die Größe eines Dictionaries kann sich während der Laufzeit des Programms ändern.

## Operationen mit Dictionaries
[75min]
### Erstellen und Initialisieren eines Dictionaries

Es gibt verschiedene Möglichkeiten ein Dictionary anzulegen:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=a%20%3D%20dict%28one%3D1,%20two%3D2,%20three%3D3%29%0Ab%20%3D%20%7B'one'%3A%201,%20'two'%3A%202,%20'three'%3A%203%7D%0Ac%20%3D%20dict%28%5B%28'two',%202%29,%20%28'one',%201%29,%20%28'three',%203%29%5D%29%0Ad%20%3D%20dict%28%7B'three'%3A%203,%20'one'%3A%201,%20'two'%3A%202%7D%29%0Ae%20%3D%20dict%28%7B'one'%3A%201,%20'three'%3A%203%7D,%20two%3D2%29%0A%0Aprint%28a%20%3D%3D%20b%20%3D%3D%20c%20%3D%3D%20d%20%3D%3D%20e%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict({'three': 3, 'one': 1, 'two': 2})
e = dict({'one': 1, 'three': 3}, two=2)

print(a == b == c == d == e)
```


### Zugriff auf Werte

Der Zugriff auf die Werte erfolgt über den entsprechenden Schlüssel in eckigen Klammern. Das sieht ähnlich aus wie bei
Listen, nur dass wir keinen Index verwenden, sondern den entsprechenden Schlüssel.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=mein_dict%20%3D%20%7B%22Name%22%3A%20%22Max%22,%20%22Alter%22%3A%2025,%20%22Stadt%22%3A%20%22Berlin%22%7D%0Aprint%28mein_dict%5B%22Name%22%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict["Name"])
```


Eine weitere Möglichkeit auf die Values eines Dictionaries zuzugreifen besteht in der Methode `get()`.
Das besondere: Wenn der Key nicht existiert, wird `None` zurückgegeben. Das ist in `if`-Bedingungen nützlich,
bei denen ich Code nur durchführen möchte, wenn der Schlüssel auch tatsächlich existiert. Denn `bool(None)` 
ist immer `False`.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=my_dict%20%3D%20dict%28one%3D1,%20two%3D2,%20three%3D3%29%0A%0Av1%20%3D%20my_dict.get%28%22one%22%29%0A%0Aif%20v1%3A%0A%20%20%20%20print%28f%22Found%20value%3A%20%7Bv1%7D%22%29%0Aelse%3A%0A%20%20%20%20print%28%22No%20Value%20found%22%29%0A%0Av2%20%3D%20my_dict.get%28%22four%22%29%0A%0Aif%20v2%3A%0A%20%20%20%20print%28f%22Found%20value%3A%20%7Bv2%7D%22%29%0Aelse%3A%0A%20%20%20%20print%28%22No%20Value%20found%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
my_dict = dict(one=1, two=2, three=3)

v1 = my_dict.get("one")

if v1:
    print(f"Found value: {v1}")
else:
    print("No Value found")

v2 = my_dict.get("four")

if v2:
    print(f"Found value: {v2}")
else:
    print("No Value found")
```


### Hinzufügen und Ändern von Einträgen

Werte können hinzugefügt werden, in dem wir einem Element, einen Schlüssel hinzufügen und diesem einen Wert zuweisen.
Existiert der Schlüssel bereits wird der vorhandene Wert einfach überschrieben.

Als Schlüssel können dabei nur Objekte genutzt werden, die hashable sind (also z.B. Zahlen, Strings, Tupel)

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=mein_dict%20%3D%20%7B%22Name%22%3A%20%22Max%22,%20%22Alter%22%3A%2025,%20%22Stadt%22%3A%20%22Berlin%22%7D%0A%23%20Hinzuf%C3%BCgen%20eines%20neuen%20Eintrags%0Amein_dict%5B%22Beruf%22%5D%20%3D%20%22Ingenieur%22%0A%0A%23%20%C3%84ndern%20eines%20vorhandenen%20Eintrags%0Amein_dict%5B%22Alter%22%5D%20%3D%2026&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
# Hinzufügen eines neuen Eintrags
mein_dict["Beruf"] = "Ingenieur"

# Ändern eines vorhandenen Eintrags
mein_dict["Alter"] = 26
```


### Entfernen von Einträgen

Das Entfernen von Einträgen sieht leider nicht wie typischer Python-Code aus. Man greift auf das Element, welches man 
löschen will wie gewohnt zu und löscht das Element mit einem vorangestellten `del`.

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=mein_dict%20%3D%20%7B%22Name%22%3A%20%22Max%22,%20%22Alter%22%3A%2025,%20%22Stadt%22%3A%20%22Berlin%22%7D%0A%0Adel%20mein_dict%5B%22Stadt%22%5D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

del mein_dict["Stadt"]
```



### Durchlaufen eines Dictionaries
<details>
<summary>
🎦 Video
</summary>
<iframe width="560" height="315" src="https://www.youtube.com/embed/HBGqzO0NiVs?si=8ok12Sj93l6g_wlb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</details>

Um die Keys **und** Values eines Dictionaries zu durchlaufen, muss die Methode `items()` verwendet werden.
Hier erhalten wir dann zwei Werte in unserer `for`-Schleife auf ein Mal:

[💻 Link zum Onlinecompiler](https://pythontutor.com/render.html#code=mein_dict%20%3D%20%7B%22Name%22%3A%20%22Max%22,%20%22Alter%22%3A%2025,%20%22Stadt%22%3A%20%22Berlin%22%7D%0A%0Afor%20key,%20value%20in%20mein_dict.items%28%29%3A%0A%20%20%20%20print%28key,%20value%29%0A%0Aprint%28%22fertig%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

for key, value in mein_dict.items():
    print(key, value)

print("fertig")
```


## Häufige Funktionen und Methoden für Dictionaries in Python

Hier haben wir eine Auswahl einiger Methoden auf Dictionaries.
[Hier ist die gesamte Liste.](https://docs.python.org/3/library/stdtypes.html#dict)

| Funktion        | Beschreibung                                                                                                                     | Beispiel                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| `my_dict[key]`  | Greif auf den Wert mit dem Key `key` zu. Existiert dieser nicht wird er beim Schreiben erstellt. Beim Lesen gibt es einen Fehler | `dict["Key"] = Value`               |
| `get(key)`      | Gibt den Wert für den angegebenen Schlüssel zurück. Gibt `None` zurück, wenn der Schlüssel nicht existiert.                      | `wert = dict.get('schluessel')`     |
| `keys()`        | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel des Dictionaries enthält.                                               | `schluessel = dict.keys()`          |
| `values()`      | Gibt ein neues Ansichtsobjekt zurück, das alle Werte des Dictionaries enthält.                                                   | `werte = dict.values()`             |
| `items()`       | Gibt ein neues Ansichtsobjekt zurück, das alle Schlüssel-Wert-Paare des Dictionaries als Tupel enthält.                          | `paare = dict.items()`              |
| `update(dict2)` | Aktualisiert das Dictionary mit Schlüssel-Wert-Paaren aus einem anderen Dictionary oder iterierbaren Schlüssel-Wert-Paaren.      | `dict.update(dict2)`                |
| `pop(key)`      | Entfernt den Eintrag mit dem angegebenen Schlüssel und gibt dessen Wert zurück.                                                  | `wert = dict.pop('schluessel')`     |
| `popitem()`     | Entfernt und gibt ein zufälliges Schlüssel-Wert-Paar als Tupel zurück.                                                           | `schluessel, wert = dict.popitem()` |
| `clear()`       | Entfernt alle Elemente aus dem Dictionary.                                                                                       | `dict.clear()`                      |
| `copy()`        | Erstellt eine flache Kopie des Dictionaries.                                                                                     | `neues_dict = dict.copy()`          |

## Anwendungsbeispiele

Dictionaries sind nützlich für die Speicherung und Manipulation von Schlüssel-Wert-Paaren und bieten schnellen
Zugriff sowie flexible Datenstrukturen.

- **Datenorganisation**: Dictionaries sind ideal für die Speicherung und Organisation komplexer Daten, wie z.B.
  Benutzerinformationen oder Konfigurationseinstellungen.
- **Schneller Zugriff**: Aufgrund ihrer internen Struktur bieten Dictionaries einen schnellen Zugriff auf ihre Elemente.

# Aufgaben

[//]: # ([35min])

### 1. **Grundlegendes Dictionary**: 🌶️️
Erstelle ein Dictionary mit drei Schlüssel-Wert-Paaren und gib es aus.
### 2. **Zugriff auf Werte**: 🌶️️
Greife auf einen Wert in einem Dictionary zu und gib ihn aus.
### 3. **Hinzufügen eines Eintrags**: 🌶️️
Füge einem bestehenden Dictionary einen neuen Schlüssel-Wert-Eintrag hinzu.
### 4. **Ändern eines Wertes**: 🌶️️
Ändere den Wert eines bestehenden Eintrags in einem Dictionary.
### 5. **Entfernen eines Eintrags**: 🌶️️🌶️️
Entferne einen Eintrag aus einem Dictionary.
### 6. **Durchlaufen mit Schleifen**: 🌶️️🌶️️
Durchlaufe ein Dictionary und gib alle Schlüssel und deren zugehörige Werte aus.
### 7. **Nur Schlüssel durchlaufen**: 🌶️️🌶️️
Durchlaufe ein Dictionary und gib nur die Schlüssel aus.
### 8. **Nur Werte durchlaufen**: 🌶️️🌶️️
Durchlaufe ein Dictionary und gib nur die Werte aus.
### 9. **Schlüssel-Existenz prüfen**: 🌶️️🌶️️🌶️️
Überprüfe, ob ein bestimmter Schlüssel in einem Dictionary existiert.
### 10. **Nested Dictionary**: 🌶️️🌶️️🌶️️
Erstelle ein verschachteltes Dictionary (ein Dictionary innerhalb eines anderen Dictionaries)
    und greife auf ein Element des inneren Dictionaries zu.

[Lösungen](solution.md#lösungen)

# Anspruchsvolle Aufgaben

[//]: # ([75min])

### Aufgabe 1: Wortzähler 🌶️️🌶️️

Schreibe ein Programm, das einen Text (String) entgegennimmt und ein Dictionary zurückgibt, das die Häufigkeit jedes
Wortes im Text zählt. Wörter sollen unabhängig von Groß- und Kleinschreibung gezählt werden. Verwende `input()` zur
Eingabe des Textes.

### Aufgabe 2: Telefonbuch 🌶️️🌶️️

Erstelle ein einfaches Telefonbuch-Programm, das es dem Benutzer ermöglicht, Namen und Telefonnummern hinzuzufügen, zu
suchen, zu ändern und zu löschen. Verwende ein Dictionary zur Speicherung der Daten. Das Programm soll fortlaufend
laufen, bis der Benutzer sich entscheidet, es zu beenden. Achte darauf, dass es nicht bei Fehleingaben abstürzt.

```python
telefonbuch = {}

while True:
    aktion = input("Wähle eine Aktion: anzeigen, hinzufügen, suchen, ändern, löschen, beenden: ")

    if aktion == "beenden":
        ...
    elif aktion == "hinzufügen":
        ...
    elif aktion == "suchen":
        ...
    elif aktion == "ändern":
        ...
    elif aktion == "löschen":
        ...
    elif aktion == "anzeigen":
        ...
    else:
        ...
```

### Aufgabe 3: Lagerbestandsverwaltung 🌶️️🌶️️🌶️️

Implementiere ein Lagerbestandsverwaltungssystem. Erstelle ein Dictionary, das Produkte und ihre Mengen enthält. Das
Programm soll es dem Benutzer ermöglichen, neue Produkte hinzuzufügen, vorhandene zu aktualisieren und Produkte zu
löschen. Zusätzlich soll das Programm eine Übersicht über alle Produkte und Mengen anzeigen können.

### Aufgabe 4: Verschachteltes Dictionary analysieren 🌶️️🌶️️🌶️️

Gegeben sei ein verschachteltes Dictionary, das Daten von Studenten und ihren Noten in verschiedenen Fächern enthält (
z.B. `studenten = {"Anna": {"Mathe": 1, "Englisch": 2}, "Max": {"Mathe": 3, "Englisch": 2}}`). Schreibe ein Programm,
das für jeden Studenten den Durchschnitt seiner Noten berechnet und diesen ausgibt. Nutze Schleifen, um durch das
Dictionary zu iterieren.

### 5. Häufigster Buchstabe in einem String finden: 🌶️️🌶️️
Schreibe einen Python-Code, um den häufigsten Buchstaben in einem String zu finden.

[Lösungen](solution.md#anspruchsvolle-aufgaben)
