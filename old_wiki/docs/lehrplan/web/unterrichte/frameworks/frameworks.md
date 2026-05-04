# Einbindung von JavaScript Frameworks und Libraries

[30 min]

Die Nutzung von externen JavaScript-Bibliotheken und Frameworks ist ein wesentlicher Bestandteil der modernen Webentwicklung. Sie bieten eine Reihe von Funktionen und Werkzeugen, um die Entwicklung effizienter zu gestalten.

## Einbindung in HTML

JavaScript-Bibliotheken können direkt in HTML-Dokumente eingebunden werden, in der Regel durch das Hinzufügen eines `<script>`-Tags, das auf die Bibliotheksdatei verweist. Nachdem die Bibliothek eingebunden ist, können ihre Funktionen und Objekte im JavaScript-Code verwendet werden.

### 1. Beispiel für jQuery

Hier wird [jQuery](https://jquery.com/) verwendet, um bei einem Klick auf ein Paragraph-Element (`<p>`) dieses auszublenden.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Meine Webseite</title>
    <!-- Einbindung der externen Library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <script>
        // jQuery Code kann hier verwendet werden
        $(document).ready(function() {
            // Fügt Event Listener zu allen <p>-Elementen hinzu.
            $("p").click(function() {
                // Verbirgt das aktuell geklickte Element.
                $(this).hide();
            });
        });
    </script>
</body>
</html>
```

### 2: Beispiel für Moment.js

Moment.js ist eine Library zur Datums- und Zeitmanipulation und -formatierung.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Moment.js Beispiel</title>
    <!-- Einbindung der externen Library -->
    <script src="https://cdn.jsdelivr.net/npm/moment@2.29.1/min/moment.min.js"></script>
</head>
<body>
    <script>
        // Formatierung des aktuellen Datums
        console.log(moment().format('YYYY-MM-DD'));
    </script>
</body>
</html>
```

## Statische vs. Dynamische Webseiten

### Statische Webseiten

Statische Webseiten sind aus einer festen Anzahl vorab erstellter Dateien aufgebaut, die auf einem Webserver gespeichert sind. Diese Dateien, HTML, CSS und JavaScript, werden vom Webbrowser des Benutzers ausgeführt. Statische Webseiten ändern sich nur, wenn ein Entwickler die Quelldateien modifiziert und sie erscheinen jedem Benutzer gleich. Sie sind einfach zu erstellen und zu warten, schneller aufgrund minimaler Backend-Verarbeitung und leichter zu cachen, haben aber Nachteile in Bezug auf Skalierbarkeit, Personalisierung und eingeschränkte Funktionalität für bestimmte Website-Typen, wie E-Commerce-Seiten.
Wir werden uns vor allem auf diese Art der Website konzentrieren.

### Dynamische Webseiten 
Dynamische Webseiten hingegen präsentieren unterschiedlichen Besuchern verschiedene Informationen, basierend auf Faktoren wie Standort, lokaler Zeit, Einstellungen und Benutzerverhalten. Sie verwenden serverseitige Skriptsprachen wie PHP, Python, Ruby oder serverseitiges JavaScript (NodeJS), um Seiten "on-the-fly" zu erstellen, wenn ein Benutzer eine Seite anfordert. Dynamische Webseiten bieten personalisierte Inhalte und sind flexibler, aber auch komplexer im Aufbau und in der Wartung. Sie können langsamer sein, da sie mehr Backend-Verarbeitung erfordern
