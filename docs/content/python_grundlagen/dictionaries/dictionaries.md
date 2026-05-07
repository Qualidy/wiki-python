# Dictionaries (Schlüssel-Wert-Paare):

{{ youtube_video("https://www.youtube.com/embed/X4zTZUsRaH4?si=yv0MYIVcgN6l1DJZ") }}

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
{{ youtube_video("https://www.youtube.com/embed/HBGqzO0NiVs?si=8ok12Sj93l6g_wlb") }}

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

{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/01_grundlegendes_dictionary.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/02_zugriff_auf_werte.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/03_hinzufugen_eines_eintrags.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/04_andern_eines_wertes.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/05_entfernen_eines_eintrags.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/06_durchlaufen_mit_schleifen.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/07_nur_schlussel_durchlaufen.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/08_nur_werte_durchlaufen.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/09_schlussel_existenz_prufen.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/10_nested_dictionary.yaml") }}
# Anspruchsvolle Aufgaben

[//]: # ([75min])

{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/11_wortzahler.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/12_telefonbuch.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/13_lagerbestandsverwaltung.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/14_verschachteltes_dictionary_analysieren.yaml") }}
{{ task(file="tasks/python_grundlagen/dictionaries/dictionaries/15_haufigster_buchstabe_in_einem_string_finden.yaml") }}
