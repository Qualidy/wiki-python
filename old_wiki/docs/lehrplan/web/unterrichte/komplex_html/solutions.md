# Lösungen

## Kontaktformular mit Validierung
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Kontaktformular</title>
</head>
<body>
    <form action="/submit-form" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">E-Mail:</label>
        <input type="email" id="email" name="email" required><br>
        
        <label for="message">Nachricht:</label>
        <textarea id="message" name="message" required></textarea><br>
        
        <label for="subject">Betreff:</label>
        <select id="subject" name="subject">
            <option value="anfrage">Anfrage</option>
            <option value="feedback">Feedback</option>
            <option value="support">Support</option>
        </select><br>
        
        <input type="submit" value="Absenden">
    </form>
</body>
</html>
```

## Tabellarische Darstellung von Daten
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Produkttabelle</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Produktname</th>
            <th>Preis</th>
            <th>Kategorie</th>
            <th>Bewertung</th>
        </tr>
        <tr>
            <td>Produkt 1</td>
            <td>10€</td>
            <td>Kategorie A</td>
            <td>★★★★☆</td>
        </tr>
        <tr>
            <td>Produkt 2</td>
            <td>15€</td>
            <td>Kategorie B</td>
            <td>★★★☆☆</td>
        </tr>
    </table>
</body>
</html>
```

## Integration einer OpenStreetMap-Karte mit `<iframe>`
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Kartenintegration</title>
</head>
<body>
    <h1>Standort auf OpenStreetMap</h1>
    <iframe width="600" height="450" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
            src="https://www.openstreetmap.org/export/embed.html?bbox=7.668594360351562%2C51.29230316540803%2C7.755497932434082%2C51.35584341253237&amp;layer=mapnik&amp;marker=51.324073288970204%2C7.712046146392822"
            style="border: 1px solid black"></iframe>
    <br>
    <small><a href="https://www.openstreetmap.org/#map=6/51.324/7.712">Größere Karte anzeigen</a></small>
</body>
</html>
```