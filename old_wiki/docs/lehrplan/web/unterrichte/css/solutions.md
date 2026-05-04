# Lösungen

## Grundlegendes CSS-Styling
```css
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 10px 0;
}

footer {
    background-color: #f4f4f4;
    text-align: center;
    padding: 10px 0;
}
```

## Navigationsleiste stylen
```css
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

nav ul li {
    float: left;
}

nav ul li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

nav ul li a:hover {
    background-color: #111;
}
```

## Bildergalerie für Automodelle stylen
```css
.gallery {
    display: flex;
    justify-content: space-around;
    padding: 20px;
}

.gallery img {
    width: 30%;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
}
```

## Responsive Design
```css
@media screen and (max-width: 600px) {
    nav ul, .gallery {
        flex-direction: column;
    }

    .gallery img {
        width: 100%;
    }
}
```