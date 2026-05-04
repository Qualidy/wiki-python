# HTML

[90 min]

Vor der Umsetzung der ersten eigene Website, wird eine Auflistung der wichtigsten HTML-`Tags` benötigt. Folgend die in den kommenden Aufgaben notwendigen Tags.

Meist wird die initale Website (Home) unter dem namen `index.html` gespeichert. Webserver liefern das HTML Dokument mit diesem Namen ohne weitere Konfiguration als Standard aus.

Es gibt sehr viele Tags die wir hier nicht alle behandeln werden. Für einen ausführlicheren Kurs zum Thema HTML, schaut euch [FreeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/) an.

## Tags

### `<!DOCTYPE>`

Gibt den Dokumenttyp und die HTML-Version an. Wichtig für den Browser, um die Seite korrekt zu rendern.

```html
<!DOCTYPE html>
```

### `<html>`

Das Wurzelelement, das das gesamte HTML-Dokument umschließt.

```html
<html lang="en">
</html>
```

### `<head>`

Enthält Metadaten, Links zu Stylesheets, Skripten und andere Informationen, die nicht direkt auf der Webseite angezeigt werden.

```html
<head>
  <title>Seitentitel</title>
</head>
```

### `<title>`

Definiert den Titel der Webseite, der im Browser-Tab angezeigt wird.

```html
<title>Meine Webseite</title>
```

### `<body>`

Der Hauptteil des Dokuments, enthält den sichtbaren Inhalt der Webseite.

```html
<body>
  <p>Willkommen auf meiner Seite!</p>
</body>
```

### `<h1>` bis `<h6>`

Überschriften-Tags, wobei `<h1>` die wichtigste Überschrift ist und `<h6>` die geringste Wichtigkeit hat.

```html
<h1>Hauptüberschrift</h1>
<h2>Unterüberschrift</h2>
```

### `<footer>`

Definiert den Fußbereich der Webseite.

```html
<footer>Kontakiere Mich: info@kontakt.de</footer>
```

### `<span>`

Ein Inline-Container, der verwendet wird, um Teile des Textes zu stylen oder auszurichten, ohne den Dokumentenfluss zu ändern.

```html
<p>Das ist ein <span class="highlight">wichtiger</span> Textabschnitt.</p>
```

### `<div>`

Ein div ist ein generischer Container für Fließinhalt, oft verwendet, um Layouts mit CSS zu gestalten.

```html
<div class="header">Kopfbereich der Seite</div>
```

### `<p>`

Definiert einen Textabsatz.

```html
<p>Das ist ein Absatz.</p>
```

### `<a>`

Definiert einen Hyperlink, also einen Link auf eine externe Website, Ressource, oder einen Anchor im gleichen Dokument.

```html
<a href="https://www.beispiel.de">Besuche meine Webseite</a>
```

### `<img>`

Bindet ein Bild ein.

```html
<img src="bild.jpg" alt="Beschreibung">
```

### `<ul>` und `<ol>`

`<ul>` (unordered list) für ungeordnete Listen und `<ol>` (ordered list) für geordnete Listen. Beide nutzen `<li>` (list item) als Listenelemente.

```html
<ul>
  <li>Listenelement 1</li>
  <li>Listenelement 2</li>
</ul>
<ol>
  <li>Erstes Element</li>
  <li>Zweites Element</li>
</ol>
```

### `<link>`

Wird hier verwendet, um z.B. das externe CSS-Stylesheet einzubinden.

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

### `<nav>`

Definiert einen Navigationsbereich.

```html
<nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Kontakt</a></li>
    </ul>
</nav>
```

## Aufgaben

[60 min]

### Grundgerüst einer HTML-Seite 🌶️️

Erstelle eine einfache HTML-Seite mit Basisstruktur.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Meine erste Webseite</title>
</head>
<body>
    <h1>Willkommen auf meiner Webseite!</h1>
    <p>Dies ist mein erster Absatz auf meiner eigenen Seite.</p>
</body>
</html>
```

</details>

### Einfache Navigation und Inhalte 🌶️️🌶️️

Erweitere die HTML-Seite um eine Navigationsleiste und mehr Inhalt.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Meine Webseite mit Navigation</title>
</head>
<body>
    <nav>
        <a href="#home">Home</a>
        <a href="#kontakt">Kontakt</a>
    </nav>
    <h1>Willkommen auf meiner Webseite!</h1>
    <p>Dies ist ein einführender Absatz.</p>
    <h2>Über uns</h2>
    <p>Hier ist ein wenig Information über uns.</p>
    <h3>Kontakt</h3>
    <p>Für weitere Informationen, kontaktieren Sie uns.</p>
    <img src="bild.jpg" alt="Beschreibender Text">
</body>
</html>
```
</details>

### Listen und Fußzeile 🌶️️🌶️️

Füge der Seite eine ungeordnete Liste und eine Fußzeile hinzu.

<details>
<summary>Lösung</summary>

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Webseite mit Liste und Fußzeile</title>
</head>
<body>
    <nav>
        <a href="#home">Home</a>
        <a href="#kontakt">Kontakt</a>
    </nav>
    <h1>Meine Webseite</h1>
    <ul>
        <li>Punkt 1</li>
        <li>Punkt 2</li>
        <li>Punkt 3</li>
    </ul>
    <footer>
        <p>Kontaktieren Sie uns unter: info@beispiel.de</p>
    </footer>
</body>
</html>
```

</details>

### Layout mit Divs 🌶️️🌶️️🌶️️

Strukturiere die Seite mit `<div>`-Elementen.

<details>
<summary>Lösung</summary>

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Webseite mit Liste und Fußzeile</title>
</head>
<body>
    <nav>
        <a href="#home">Home</a>
        <a href="#kontakt">Kontakt</a>
    </nav>
    <h1>Meine Webseite</h1>
    <ul>
        <li>Punkt 1</li>
        <li>Punkt 2</li>
        <li>Punkt 3</li>
    </ul>
    <footer>
        <p>Kontaktieren Sie uns unter: info@beispiel.de</p>
    </footer>
</body>
</html>
```

</details>

### Externes Styling und Komplexer Inhalt 🌶️️🌶️️🌶️️

Erweitere die Seite um ein externes Stylesheet und komplexeren Inhalt wie ein Bild.

<details>
<summary>Lösung</summary>

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Komplexe Webseite</title>
</head>
<body>
    <div class="header">
        <nav>
            <a href="#home">Home</a>
            <a href="#kontakt">Kontakt</a>
        </nav>
    </div>
    <div class="main-content">
        <h1>Interessanter Artikel</h1>
        <p><span class="highlight">Dieser Artikel</span> behandelt mehrere interessante Themen.</p>
        <img src="bild.jpg" alt="Beschreibender Text">
        <p>Mehr Information zum Thema finden Sie auf <a href="https://www.beispiel.de">unserer Webseite</a>.</p>
    </div>
    <div class="footer">
        <footer>
            <p>Kontaktieren Sie uns unter: info@beispiel.de</p>
        </footer>
    </div>
</body>
</html>

```

</details>

## Anspruchsvolle Aufgaben

[60 min]

### Grundstruktur einer Automobil-Website 🌶️️🌶️️

Erstelle das Grundgerüst einer HTML-Seite für ein Automobilunternehmen. Diese Seite soll als Basis für die weiteren Schritte dienen und die grundlegenden Elemente wie Header, Hauptinhalt und Footer enthalten.
Anforderungen:

- Füge einen Header (`<header>`) mit dem Namen des Unternehmens ein.
- Im Hauptteil (`<body>`) soll ein Absatz (`<p>`) mit einer kurzen Beschreibung des Unternehmens stehen.
- Der Footer (`<footer>`) soll Kontaktinformationen wie eine E-Mail-Adresse enthalten.

<details>
<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mein Autohersteller</title>
</head>
<body>
    <header>
        <h1>Mein Autohersteller</h1>
    </header>
    <p>Willkommen bei Mein Autohersteller, dem Ort für innovative Fahrzeuge.</p>
    <footer>
        Kontakt: info@meinautohersteller.de
    </footer>
</body>
</html>
```

</details>

### Navigationsleiste 🌶️️🌶️️

Erweitere die Website um eine Navigationsleiste, die eine verbesserte Benutzerführung ermöglicht. Diese Leiste soll Links zu verschiedenen Abschnitten der Webseite enthalten.
Anforderungen:

- Füge im Header eine Navigationsleiste (`<nav>` mit `<ul>` und `<li>`) hinzu.
- Erstelle Links zu fiktiven Seiten wie "Home", "Modelle" und "Kontakt".

<details>
<summary>Lösung</summary>

```html
<nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Modelle</a></li>
        <li><a href="#">Kontakt</a></li>
    </ul>
</nav>
```

</details>

### Bildergalerie für Automodelle 🌶️️🌶️️🌶️️

Erstelle eine Bildergalerie, die verschiedene Modelle des Autoherstellers präsentiert. Ziel ist es, visuellen Content ansprechend zu integrieren.

- Füge unterhalb der Unternehmensbeschreibung eine Bildergalerie ein.
- Nutze `<img>`-Tags für mindestens drei verschiedene Automodelle.

> Nutze Lizenzfreie Bilder wie z.B. von diesem [VW Arteon R-Line](https://commons.wikimedia.org/wiki/File:VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg).

<details>
<summary>Lösung</summary>

```html
<div class="gallery">
<a title="Thomas doerfer, CC BY-SA 4.0" href="https://commons.wikimedia.org/wiki/File:VW_Touareg_III_Elegance.jpg"><img width="512" alt="VW Touareg III Elegance" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/VW_Touareg_III_Elegance.jpg/512px-VW_Touareg_III_Elegance.jpg"></a>
<a title="M 93" href="https://commons.wikimedia.org/wiki/File:VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg"><img width="512" alt="VW Arteon R-Line – f 20052021" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg/512px-VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg"></a>
<a title="Spurzem" href="https://commons.wikimedia.org/wiki/File:VW_Standard,_Bj._1950_(2009-05-01_Sp).jpg"><img width="512" alt="VW Standard, Bj. 1950 (2009-05-01 Sp)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/VW_Standard%2C_Bj._1950_%282009-05-01_Sp%29.jpg/512px-VW_Standard%2C_Bj._1950_%282009-05-01_Sp%29.jpg"></a>
</div>
```
</details>
