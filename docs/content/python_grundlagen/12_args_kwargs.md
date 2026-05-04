# Args & Kwargs in Python 🌶️️🌶️️
[60min]

In Python gibt es zwei wichtige Konzepte im Zusammenhang mit Funktionen, nämlich `*args` und `**kwargs`. Diese ermöglichen es, Funktionen flexibler zu gestalten und mit variabler Anzahl von Argumenten umzugehen.

## Args (`*args`):

`*args` ermöglicht es einer Funktion, eine variable Anzahl von nicht-schlüsselwortbasierten Argumenten zu akzeptieren. Das bedeutet, dass die Anzahl der Argumente nicht im Voraus festgelegt ist.

```python
def funktionsname(arg1, *args):
    # Funktionscode
    pass
```

Beispiel:

```python
def addiere_zahlen(zahl1, *zahlen):
    ergebnis = zahl1
    for zahl in zahlen:
        ergebnis += zahl
    return ergebnis

summe = addiere_zahlen(1, 2, 3, 4, 5)
print(summe)  # Ausgabe: 15
```

## Kwargs (`**kwargs`):

`**kwargs` ermöglicht es einer Funktion, eine variable Anzahl von schlüsselwortbasierten Argumenten (Key-Value-Paaren) zu akzeptieren.

```python
def funktionsname(arg1, **kwargs):
    # Funktionscode
    pass
```

Beispiel:

```python
def drucke_infos(name, **infos):
    print(f"Name: {name}")
    for key, value in infos.items():
        print(f"{key}: {value}")

drucke_infos("Max", alter=23, stadt="Wolfsburg", beruf="Softwareentwickler")
```

# Aufgaben:
[240min]

## 1. `*args` Verwendung 🌶️️

Schreibe eine Funktion, die eine beliebige Anzahl von Zahlen akzeptiert und ihre Summe zurückgibt. Verwende dabei `*args`.

## 2. `**kwargs` Verwendung 🌶️️

Implementiere eine Funktion, die verschiedene Informationen (Name, Alter, Geschlecht) als schlüsselwortbasierte Argumente annimmt und ausdruckt. Verwende dabei `**kwargs`.

## 3. Kombination aus beidem 🌶️️🌶️️

Erstelle eine Funktion, die sowohl `*args` als auch `**kwargs` verwendet. Die Funktion sollte die Summe der Zahlen aus `*args` berechnen und zusätzlich alle Informationen aus `**kwargs` ausdrucken.

## 4. Personalinformationen verarbeiten 🌶️️🌶️️🌶️️

Schreibe eine Funktion namens `verarbeite_personalinformationen`, die personenbezogene Informationen entgegennimmt. Die Funktion sollte folgende Anforderungen erfüllen:

- Akzeptiere den Namen als Pflichtargument (`name`).
- Akzeptiere die E-Mail-Adresse, die Telefonnummer und das Geburtsdatum als optionale Argumente (`email`, `telefon`, `geburtsdatum`) mit Standardwerten `None`.
- Verarbeite die erhaltenen Informationen und gib einen formatierten Text aus, der alle Informationen enthält.

Beispielaufruf:

```python
verarbeite_personalinformationen("Max Mustermann", email="max@example.com", telefon="123456789", geburtsdatum="01.01.1990")
```

Erwartete Ausgabe:

```
Name: Max Mustermann
E-Mail: max@example.com
Telefon: 123456789
Geburtsdatum: 01.01.1990
```

Hinweise:
- Verwende `**kwargs` für die optionalen Argumente.
- Beachte die sinnvolle Verwendung von Standardwerten für die optionalen Argumente.
- Nutze die Funktion, um einen formatierten Text auszugeben, der alle erhaltenen Informationen enthält.
