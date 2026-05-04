# Lösungen

## Toggle-Schalter
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

## Dynamische Liste
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

## Tastatur-Event-Handler
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

## Bildergalerie mit Hover-Effekt
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

## Komplex-Aufgabe: Drag-and-Drop-Interface
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
