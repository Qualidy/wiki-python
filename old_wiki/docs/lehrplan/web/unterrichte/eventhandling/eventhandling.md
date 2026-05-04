# Eventhandler

[60 min]

Events sind Aktionen oder Vorkommnisse, die im Browser stattfinden und von JavaScript erkannt werden können. Diese können Benutzerinteraktionen wie Klicks, Mausbewegungen, Tastendrücke oder auch Systemereignisse wie das Laden einer Seite sein.

## Events

### `click`-Event

Wird ausgelöst, wenn der Benutzer auf ein Element klickt.

```javascript
document.getElementById("meinButton").onclick = function() {
    alert("Button geklickt!");
};
```

Oder per HTML Element und zugehörigem Attribut `onclick`.

```html
<button id="meinButton" onclick="handleClick()">Klick mich!</button>
```

```javascript
function handleClick() {
    alert("Button geklickt!");
}
```

### `hover`-Event

Wird ausgelöst, wenn der Mauszeiger über ein Element bewegt wird.

```javascript
document.getElementById("meinElement").onmouseover = function() {
    console.log("Maus ist über dem Element");
};
```

Oder per HTML Element und zugehörigem Attribut `onmouseover`.

```html
<div id="meinElement" onmouseover="handleMouseOver()">Fahre mit der Maus über mich!</div>
```

```javascript
function handleMouseOver() {
    console.log("Maus ist über dem Element");
}
```

## Event Listeners

Um über JavaScript beliebige Event Listener einzubauen, gibt es die `addEventListener` Methode. Hiermit können DOM-Element mit variablem Eventhandling verbunden werden.

Hinzufügen eines `click`-Listeners

```javascript
let button = document.getElementById("meinButton");
button.addEventListener("click", function() {
    console.log("Button wurde geklickt!");
});
```

Reaktion auf ein Tastatur `keydown`-Event:

```javascript
document.addEventListener("keydown", function(event) {
    console.log("Taste gedrückt: " + event.key);
});
```

## Event Propagation: Bubbling und Capturing

Event Propagation bezeichnet den Weg, den ein Event durch den DOM-Baum nimmt. Es gibt zwei Phasen: Bubbling und Capturing.

Bei komplexen Benutzeroberflächen mit verschachtelten Elementen ermöglicht Event Propagation z.B. dass in einem Menü das Klicken auf ein Untermenü-Element spezielle Aktionen auslösen, während ein Klick auf das Hauptmenü andere Aktionen ausführt.

**Bubbling**: Events "blubbern" von dem Element, das das Event auslöst, bis zum Root-Element des DOM.

```javascript
document.getElementById("kindElement").addEventListener("click", function() {
    console.log("Kind-Element geklickt!");
}, false); // False für Bubbling-Phase
```

**Capturing**: Events werden zuerst auf dem höchsten Level des DOM abgefangen, bevor sie zum auslösenden Element heruntergehen.

```javascript
document.getElementById("elternElement").addEventListener("click", function() {
    console.log("Eltern-Element geklickt!");
}, true); // True für Capturing-Phase
```

## DOM-Manipulation

Im vorherigen Kapitel haben wir bereits das DOM kennen gelernt und verstanden, dass es aus einer Baumstruktur besteht, die die Website aus Eltern- und Kindbeziehungen modelliert.

```css
        html
      /    \
    /        \
  head         body
    |         /  |  \
  title header section footer
            /     /  \     \
          h1     p   img    p
```

### Elementauswahl und -manipulation

**`getElementById`**: Greift auf ein Element basierend auf seiner ID zu.

```javascript
document.getElementById("meinElement").innerHTML = "Geänderter Text";
```

**``querySelector``**: Ermöglicht eine feinere Auswahl mit CSS-Selektoren.
  
```javascript
document.querySelector(".meineKlasse").style.color = "blau";
```

**`createElement`**: Erstellt dynamisch neue Elemente und fügt diese in den DOM-Baum ein.

```javascript
let neuerAbsatz = document.createElement("p");
neuerAbsatz.innerText = "Ein neuer Absatz";
document.body.appendChild(neuerAbsatz);
```

**`removeChild`**: Enfernt Elemente aus dem DOM.

```javascript
let zuEntfernendesElement = document.getElementById("zuEntfernen");

zuEntfernendesElement.parentNode.removeChild(zuEntfernendesElement);
```

## Aufgaben

[60 min]

### Toggle-Schalter 🌶️️

Erstelle einen Button, der bei jedem Klick die Farbe eines Div-Elements zwischen Rot und Grün wechselt.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Toggle Schalter</title>
</head>
<body>
    <div id="farbDiv" style="width: 100px; height: 100px; background-color: red;"></div>
    <button id="toggleButton">Farbe ändern</button>

    <script>
        let toggleButton = document.getElementById("toggleButton");
        let farbDiv = document.getElementById("farbDiv");
        let istRot = true;

        toggleButton.addEventListener("click", function() {
            if (istRot) {
                farbDiv.style.backgroundColor = "green";
            } else {
                farbDiv.style.backgroundColor = "red";
            }
            istRot = !istRot;
        });
    </script>
</body>
</html>
```

</details>

### Dynamische Liste 🌶️️🌶️️

Erstelle ein Formular, das es Benutzern ermöglicht, Elemente zu einer Liste hinzuzufügen.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dynamische Liste</title>
</head>
<body>
    <input id="listInput" type="text">
    <button id="addButton">Hinzufügen</button>
    <ul id="liste"></ul>

    <script>
        let addButton = document.getElementById("addButton");
        let listInput = document.getElementById("listInput");
        let liste = document.getElementById("liste");

        addButton.addEventListener("click", function() {
            let li = document.createElement("li");
            li.innerText = listInput.value;
            liste.appendChild(li);
            listInput.value = ""; // Feld leeren
        });
    </script>
</body>
</html>
```

</details>

### Tastatur-Event-Handler 🌶️️🌶️️

Erstelle eine Anwendung, die auf Tastendrücke reagiert und eine Aktion ausführt.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Tastatur-Event-Handler</title>
</head>
<body>
    <p id="status">Drücke eine Taste!</p>

    <script>
        document.addEventListener("keydown", function(event) {
            let status = document.getElementById("status");
            status.innerText = "Gedrückte Taste: " + event.key;
        });
    </script>
</body>
</html>
```

</details>

### Bildergalerie mit Hover-Effekt 🌶️️🌶️️🌶️️

Erstelle eine Bildergalerie, bei der das Überfahren eines Bildes mit der Maus Informationen zum Bild anzeigt.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bildergalerie mit Hover-Effekt</title>
</head>
<body>
    <div>
        <img src="bild1.jpg" alt="Bild 1" onmouseover="showInfo('info1')" onmouseout="hideInfo('info1')">
        <p id="info1" style="display:none;">Informationen über Bild 1</p>
        <!-- Weitere Bilder und Beschreibungen -->
    </div>

    <script>
        function showInfo(infoId) {
            document.getElementById(infoId).style.display = "block";
        }

        function hideInfo(infoId) {
            document.getElementById(infoId).style.display = "none";
        }
    </script>
</body>
</html>
```

</details>

## Anspruchsvolle Aufgaben

[45 min]

### Drag-and-Drop-Interface 🌶️️🌶️️🌶️️🌶️️🌶️️

Implementiere eine Drag-and-Drop-Funktionalität, bei der Elemente auf der Seite verschoben werden können.

- Erstelle mehrere draggable Elemente und einen Drop-Bereich.
- Verwende `drag`- und `drop`-Events, um die Elemente innerhalb des Drop-Bereichs zu bewegen.

<details>

<summary>Lösung</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Drag-and-Drop-Interface</title>
    <style>
        #dropBereich {
            width: 300px;
            height: 300px;
            border: 2px dashed #aaa;
        }
        .draggable {
            width: 50px;
            height: 50px;
            background-color: blue;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div id="dropBereich"></div>
    <div class="draggable" draggable="true"></div>
    <div class="draggable" draggable="true"></div>

    <script>
        let draggables = document.querySelectorAll('.draggable');
        let dropBereich = document.getElementById('dropBereich');

        draggables.forEach(draggable => {
            draggable.addEventListener('dragstart', function(event) {
                event.dataTransfer.setData('text/plain', event.target.id);
            });
        });

        dropBereich.addEventListener('dragover', function(event) {
            event.preventDefault();
        });

        dropBereich.addEventListener('drop', function(event) {
            event.preventDefault();
            let data = event.dataTransfer.getData('text');
            let draggableElement = document.getElementById(data);
            dropBereich.appendChild(draggableElement);
        });
    </script>
</body>
</html>
```

</details>
