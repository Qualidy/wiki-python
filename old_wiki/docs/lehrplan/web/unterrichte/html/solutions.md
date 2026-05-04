# Lösungen

## Grundgerüst einer HTML-Seite
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

## Einfache Navigation und Inhalte
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

## Listen und Fußzeile
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

## Externes Styling und Komplexer Inhalt
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

## Komplex-Aufgabe: Grundstruktur der Automobil-Website
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

## Komplex-Aufgabe: Navigationsleiste
```html
<nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">Modelle</a></li>
        <li><a href="#">Kontakt</a></li>
    </ul>
</nav>
```

## Bildergalerie für Automodelle
```html
  <div class="gallery">
        <a title="Thomas doerfer, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:VW_Touareg_III_Elegance.jpg"><img width="512" alt="VW Touareg III Elegance" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/VW_Touareg_III_Elegance.jpg/512px-VW_Touareg_III_Elegance.jpg"></a>
        <a title="© M 93 / Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg"><img width="512" alt="VW Arteon R-Line – f 20052021" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg/512px-VW_Arteon_R-Line_%E2%80%93_f_20052021.jpg"></a>
        <a title="Spurzem - Lothar Spurzem, CC BY-SA 2.0 DE &lt;https://creativecommons.org/licenses/by-sa/2.0/de/deed.en&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:VW_Standard,_Bj._1950_(2009-05-01_Sp).jpg"><img width="512" alt="VW Standard, Bj. 1950 (2009-05-01 Sp)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/VW_Standard%2C_Bj._1950_%282009-05-01_Sp%29.jpg/512px-VW_Standard%2C_Bj._1950_%282009-05-01_Sp%29.jpg"></a>
    </div>
  ```
