# Interaktivität mit JavaScript

[60 min]

JavaScript ist das zentrale Werkzeug in der modernen Webentwicklung. Es untersützt dynamische und interaktive Elemente auf Webseiten und wird von allen modernen Browsern unterstützt. Somit ist es universell für die Entwicklung einsetzbar und erleichtert zudem die Entwicklung durch zahlreiche Frameworks und Bibliotheken.

## Basics

Die wichtigsten Grundlagen von JavaScript zu verstehen, ist essentiell für jede Art von Webentwicklung. Folgend die 10 relevantesten Kernkonzepte von JavaScript mit einem kurzen Vergleich zu Python.

### `Variablen`

Wie in Python sind Variablen grundlegende Bausteine in JavaScript. Sie ermöglichen es, Daten zu speichern und auf sie zu verweisen.

> [Typescript](https://www.typescriptlang.org/) ermöglicht es, auch in JavaScript mit Types zu arbeiten.

#### Javascript

```javascript
let name = "Max";
const alter = 30;
var beruf = "Entwickler";
```

#### Python

```python
name = "Max"
alter = 30
beruf = "Entwickler
```

### `Datentypen`

JavaScript ist eine dynamisch typisierte Sprache, die verschiedene Datentypen wie Strings, Zahlen, Booleans, Arrays, Objekte und mehr unterstützt. Es unterscheidet nur zwischen Konstanten und sich verändernden Variablen.

#### Javascript

```javascript
const name = "Anna"; // Konstanter String
var alter = 25; // Variable Zahl
let hobbies = ["Lesen", "Programmieren"]; // Variabler Array
```

#### Python

```python
name = "Anna" # Variabler String
alter = 25 #Variable Zahl
hobbies = ["Lesen", "Programmieren"] # Variabler Array
```

### `Operatoren`

Operatoren ermöglichen es, einfache bis komplexe mathematische, vergleichende und logische Operationen durchzuführen.

#### Javascript

```javascript
let summe = 10 + 5;
let istGleich = (summe === 15);
let istWahr = (true && false); 
```

#### Python

```python
summe = 10 + 5
istGleich = (summe == 15)
istWahr = (true and false); 
```

### `Kontrollstrukturen`

Kontrollstrukturen wie if-else-Anweisungen und Schleifen steuern den Fluss eines Programms.

#### Javascript

```javascript
if (alter > 18) {
    console.log("Volljährig");
} else {
    console.log("Minderjährig");
}

for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

#### Python

```python
if alter > 18: 
  print("Volljährig")
else:
  print("Minderjährig")

for (i in range(5)):
  print(i)
```

## `Funktionen`

Funktionen sind auch in JavaScript wiederverwendbare Codeblöcke, die eine spezifische Aufgabe ausführen.

#### Javascript

```javascript
function grueße(name) {
    return `Hallo ${name}!`;
}

let gruß = grueße("Anna"); // "Hallo Anna!"
```

#### Python

```python
def grueße(name): 
  return "Hallo " + name

gruß = grueße("Anna") # "Hallo Anna!"
```

### `Arrays und Objekte`

Arrays und Objekte ermöglichen es, Sammlungen von Daten zu speichern und zu verwalten.

#### Javascript

```javascript
let farben = ["Rot", "Grün", "Blau"];
farben.push("Gelb");

let person = {
    name: "Max",
    alter: 30,
    beruf: "Entwickler"
};
person.hobby = "Musik";
```

#### Python

```python
farben = ["Rot", "Grün", "Blau"]
farben.append("Gelb")

person = {
    "name": "Max",
    "alter": 30,
    "beruf": "Entwickler"
}
person["hobby"] = "Musik"
```

### `Fehlerbehandlung`

Auch das Abfangen von Fehlern und Exceptions über `try...catch` is sehr ähnlich.

#### Javascript

```javascript
try { 
    // Code, der einen Fehler werfen könnte 
} catch (error) { 
    console.error(error); 
}
```

#### Python

```python
try:
    # Potenziell fehlerhafter Code
except Exception as error:
    print(error)
```

## Aufgaben
[60 min]

### Einfache Nachrichtenausgabe 🌶️️

Schreibe ein JavaScript-Programm, das mit `console.log()` eine Willkommensnachricht in der Konsole ausgibt.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Einfache Nachrichtenausgabe</title>
</head>
<body>
    <script>
        let willkommensNachricht = "Willkommen zur JavaScript-Welt!";
        console.log(willkommensNachricht);
    </script>
</body>
</html>
```

</details>

### Einfache Berechnung und Ausgabe 🌶️️

Schreibe ein JavaScript-Programm, das zwei Zahlen addiert und das Ergebnis in der Konsole ausgibt.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Einfache Berechnung und Ausgabe</title>
</head>
<body>
    <script>
        let zahl1 = 5;
        let zahl2 = 10;
        let summe = zahl1 + zahl2;
        console.log("Die Summe ist: " + summe);
    </script>
</body>
</html>
```

</details>

### Interaktive Benutzerbegrüßung 🌶️️🌶️️

Schreibe ein JavaScript-Programm, das den Benutzernamen abfragt und eine personalisierte Begrüßungsnachricht ausgibt.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Interaktive Benutzerbegrüßung</title>
</head>
<body>
    <script>
        function grueßen(name) {
            return `Hallo ${name}, willkommen zur JavaScript-Welt!`;
        }

        let benutzername = prompt("Bitte geben Sie Ihren Namen ein:");
        alert(grueßen(benutzername));
    </script>
</body>
</html>
```

</details>

### Einfaches Farbwechsel-Skript 🌶️️🌶️️

Erstelle ein JavaScript-Programm, das die Farbe eines `<div>`-HTML-Elements ändert.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Einfacher Farbwechsel</title>
</head>
<body>
    <div id="farbwechselDiv" style="width:100px; height:100px; background-color:blue;"></div>
    <button onclick="farbeAendern()">Farbe ändern</button>

    <script>
        function farbeAendern() {
            document.getElementById("farbwechselDiv").style.backgroundColor = "red";
        }
    </script>
</body>
</html>
```

</details>
