## Gültigkeitsbereich von Variablen - Scopes

[//]: # ([60min])
Der Begriff "Scope" bezieht sich in der Programmierung auf den Bereich eines Programms, in dem eine Variable zugänglich
ist. In Python gibt es zwei wichtige Scopes: global und lokal. Um den Scope von Variablen in und
außerhalb von Funktionen zu erläutern, betrachten wir ein konkretes Beispiel:

### Beispiel zur Erläuterung des Scopes

#### Globale Variable

Eine Variable, die außerhalb einer Funktion definiert wird, ist global. Das bedeutet, sie ist überall im Code
zugänglich. Bisher haben wir alle Variablen global definiert, da wir Funktionen noch nicht kannten.

```python
globale_variable = "Ich bin global!"


def meine_funktion():
    print(globale_variable)  # Zugriff auf die globale Variable ist möglich


meine_funktion()  # Gibt "Ich bin global!" aus
print(globale_variable)  # Gibt ebenfalls "Ich bin global!" aus
```

In diesem Beispiel ist `globale_variable` außerhalb der Funktion `meine_funktion` definiert und kann sowohl innerhalb
als auch außerhalb der Funktion verwendet werden.

**Anmerkung**:
Obwohl dieses Vorgehen möglich ist, sollten wir das möglichst nicht verwenden. Natürlich gibt es Ausnahmen in denen das
eine sinnvolle Vorgehensweise ist. Globale Variablen sollten allerdings so selten wie möglich und nur mit gutem Grund
angewendet werden. Sinnvollerweise übergibt man die notwendigen Variablen als Argumente an die Funktion.

#### Lokale Variable

Eine innerhalb einer Funktion definierte Variable ist lokal und nur innerhalb dieser Funktion gültig.

```python
def eine_andere_funktion():
    lokale_variable = "Ich bin lokal!"
    print(lokale_variable)  # Gültig innerhalb dieser Funktion


eine_andere_funktion()  # Gibt "Ich bin lokal!" aus
# print(lokale_variable)  # Fehler: lokale_variable ist außerhalb ihrer Funktion nicht definiert
```

In diesem Beispiel ist `lokale_variable` nur innerhalb der `eine_andere_funktion` gültig. Ein Versuch, auf sie außerhalb
ihrer Funktion zuzugreifen, führt zu einem Fehler.

## Shadowing

[//]: # ([60min])
Wenn eine lokale Variable denselben Namen wie eine globale Variable hat, wird die globale Variable innerhalb der
Funktion "verdeckt" oder "überschattet":

```python
variable = "Ich bin global!"


def schatten_funktion():
    variable = "Ich bin lokal!"
    print(variable)  # Gibt die lokale Variable aus


schatten_funktion()  # Gibt "Ich bin lokal!" aus
print(variable)  # Gibt die globale Variable aus, also "Ich bin global!"
```

In diesem Beispiel gibt es sowohl eine globale als auch eine lokale Variable namens `variable`. Innerhalb der
Funktion `schatten_funktion` bezieht sich `variable` auf die lokale Instanz.

**Anmerkung**: Auch hier gilt, dass man das möglichst vermeiden sollte. Moderne Python-IDEs geben auch eine Warnung aus,
wenn dies getan wird.

### Zusammenfassung - Scopes

- **Globale Variablen**: Außerhalb von Funktionen definiert; im gesamten Code gültig.
- **Lokale Variablen**: Innerhalb von Funktionen definiert; nur in ihrer eigenen Funktion gültig.
- **Schattenbildung**: Lokale Variablen können den gleichen Namen wie globale Variablen haben, aber sie sind separate
  Instanzen.

Das Verständnis des Scopes von Variablen ist entscheidend, um zu verstehen, wie Informationen und Daten in einem
Programm gespeichert und zugänglich gemacht werden. Es hilft auch dabei, Fehler zu vermeiden, die durch unbeabsichtigte
Überschneidungen von Variablennamen entstehen können.

## Übungsaufgaben zum Thema Scopes in Python
[60min]
### 1. **Globale Variable**: 🌶️️
Definiere eine globale Variable und gib sie innerhalb einer Funktion aus.
### 2. **Lokale Variable**: 🌶️️
Definiere eine lokale Variable innerhalb einer Funktion und gib sie innerhalb dieser Funktion
   aus.
### 3. **Globale und lokale Variable mit demselben Namen**: 🌶️️
Definiere eine globale und eine lokale Variable mit demselben
   Namen und gib beide innerhalb der Funktion aus.
### 4. **Änderung einer globalen Variable**: 🌶️️
Versuche, eine globale Variable innerhalb einer
   Funktion zu ändern, ohne das `global`-Keyword zu verwenden.
### 5. **Verwenden des `global`-Keywords**: 🌶️️
Ändere eine globale Variable innerhalb einer Funktion mit Hilfe des `global`
   -Keywords.
### 6. **Nested Functions Scope**: 🌶️️
Definiere eine verschachtelte Funktion und greife auf eine Variable aus der umgebenden
   Funktion zu.
### 7. **Lokale Variable in einer Schleife**: 🌶️️
Definiere eine lokale Variable innerhalb einer for-Schleife in einer Funktion
   und gib sie aus.
### 8. **Funktionsargument Scope**: 🌶️️
Übergebe eine Variable als Argument an eine Funktion und ändere sie innerhalb der
   Funktion.
### 9. **Rückgabewerte und Scope**: 🌶️️
Gib einen Wert aus einer Funktion zurück und weise ihn einer globalen Variable zu.

[Lösungen](solutions.md#scopes)