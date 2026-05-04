# Lösungen

## Responsive Card-Layout mit Flexbox
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Responsive Card-Layout</title>
    <style>
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .card {
            flex-basis: 30%;
            border: 1px solid #ddd;
            border-radius: 10px;
            margin: 10px;
            padding: 20px;
            text-align: center;
        }
        .card img {
            width: 100%;
            height: auto;
            border-radius: 10px;
        }
        @media (max-width: 600px) {
            .card {
                flex-basis: 80%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <img src="bild1.jpg" alt="Bild 1">
            <h2>Produkt 1</h2>
            <p>Beschreibung des Produkts 1.</p>
            <button>Mehr erfahren</button>
        </div>
        <div class="card">
            <img src="bild2.jpg" alt="Bild 2">
            <h2>Produkt 2</h2>
            <p>Beschreibung des Produkts 2.</p>
            <button>Mehr erfahren</button>
        </div>
    </div>
</body>
</html>
```


## Erstellung eines responsiven Menüs mit Bootstrap
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Responsives Menü mit Bootstrap</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Pricing</a>
                </li>
            </ul>
        </div>
    </nav>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
```


## Fortgeschrittenes Grid-Layout mit CSS Grid
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Fortgeschrittenes Grid-Layout</title>
    <style>
        .container {
            display: grid;
            grid-template-columns: 2fr 1fr;
            grid-template-rows: auto;
            grid-gap: 20px;
        }
        .main {
            grid-column: 1 / 2;
        }
        .sidebar {
            grid-column: 2 / 3;
        }
        .article {
            border: 1px solid #ddd;
            padding: 20px;
        }
        @media (max-width: 800px) {
            .container {
                grid-template-columns: 1fr;
            }
            .sidebar {
                grid-column: 1;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="main">
            <div class="article">Hauptartikel 1</div>
            <div class="article">Hauptartikel 2</div>
        </div>
        <div class="sidebar">Sidebar mit weiteren Informationen</div>
    </div>
</body>
</html>
```
