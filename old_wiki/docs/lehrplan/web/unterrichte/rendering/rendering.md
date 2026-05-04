# Rendering (Ausblick)

[45 min]

Je nach Projektanforderung und Umsetzung kann der Fokus des Renderings entweder auf den Server oder Clienten gelegt werden. Client-Side Rendering bietet eine bessere Benutzererfahrung und reduzierte Serverlast, während Server-Side Rendering Vorteile bei der Ladegeschwindigkeit und SEO bietet.

## Client-Side vs. Server-Side Rendering

### Client-Side Rendering

Die Inhalte der Webseite werden im Browser des Benutzers durch JavaScript generiert. Nur das Grundgerüst der Seite wird vom Server geladen. Client-Side Rendering wird häufig in Single Page Applications (SPAs) wie mit React oder Angular erstellten Anwendungen verwendet.

### Server-Side Rendering

Die gesamte Webseite inklusive aller Inhalte wird auf dem Server generiert und als fertige HTML-Seite an den Browser gesendet. Server-Side Rendering wird bei traditionellen Webanwendungen und Websites, die schnelles Laden und SEO-Optimierung benötigen, verwendet.

## Templates (Flask)

Im Kontext von Client-Side und Server-Side Rendering zeigt Flask, wie serverseitiges Rendering in der Praxis umgesetzt wird. Die dynamische Erzeugung von Inhalten auf dem Server kontrastiert mit dem client-seitigen Ansatz moderner SPA-Frameworks wie React oder Vue.

Flask verwendet [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) als Template-Engine, die es ermöglicht, HTML-Templates mit dynamischen Inhalten zu erstellen.

```python
# app.py - Flask-Server-Datei
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Max")

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html - Ein einfaches Jinja2-Template -->
<!DOCTYPE html>
<html>
<head>
    <title>Flask Template Beispiel</title>
</head>
<body>
    <h1>Hallo {{ name }}!</h1>
</body>
</html>
```
