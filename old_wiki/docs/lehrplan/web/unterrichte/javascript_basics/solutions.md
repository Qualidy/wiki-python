# Lösungen

## Einfache Nachrichtenausgabe
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

## Einfache Berechnung und Ausgabe

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

## Interaktive Benutzerbegrüßung

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

## Einfaches Farbwechsel-Skript

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
