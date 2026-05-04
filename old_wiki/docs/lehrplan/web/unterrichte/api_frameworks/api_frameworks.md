# Web API Frameworks

[120 min]

## Flask & Django

Flask und Django bieten zwei sehr unterschiedliche Ansätze für die Entwicklung von Webanwendungen und APIs in Python. Flask ist ideal für schnelle Entwicklung, kleine Projekte oder wenn eine hohe Flexibilität erforderlich ist. Django hingegen bietet ein umfassendes Ökosystem für größere und komplexere Anwendungen.

**Die Wahl zwischen Flask und Django hängt von den spezifischen Anforderungen des Projekts, der bevorzugten Arbeitsweise des Entwicklerteams und der Komplexität der zu entwickelnden Anwendung ab**.

## Flask: Das Mikro-Framework

### Konzept und Philosophie

Flask ist ein leichtgewichtiges und flexibles Mikro-Framework für Python, entworfen für kleine bis mittelgroße Anwendungen und einfache Web-Dienste.
Es legt großen Wert auf Einfachheit und Erweiterbarkeit und bietet die Freiheit, die meisten Aspekte der Anwendung nach Bedarf zu gestalten.

### Hauptmerkmale von Flask

**Minimalistischer Kern**: Flask kommt mit sehr wenig eingebauter Funktionalität. Dies ermöglicht eine hohe Anpassungsfähigkeit, erfordert aber auch, dass Entwickler viele Funktionen selbst implementieren oder Erweiterungen nutzen.

**Erweiterungen**: Eine breite Palette von Erweiterungen verfügbar, die nahtlos integriert werden können, um Funktionen wie Datenbankanbindung, Formularverarbeitung, Authentifizierung etc. hinzuzufügen.

**Einfache Routengestaltung**: Flask ermöglicht eine einfache und intuitive Routendeklaration mit Python-Dekoratoren.

### Einrichtung einer API mit Flask

**1. Installation**: Beginne mit der Installation von Flask mittels `pip install flask`.

**2. Anwendungserstellung**: Erstelle eine neue Python-Datei und importiere Flask.

**3. Route definieren**: Beachte, dass in Flask eine API oft als eine einfache Funktion beginnt, die über eine Annotation mit einem URL-Endpunkt verknüpft wird.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/') # Flask URL-Endpunkt Annotation
def hello_world():
    return 'Hallo Welt!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**4. Server starten**: Führe die Anwendung aus, um den lokalen Server zu starten.

### Aufgabe: Hello World Flask 🌶️️

Erstelle einen GET Endpunkt der den Text "Hallo Welt!" als Response zurückgibt in Flask.

<details>
<summary>Lösung</summary>

<pre><code>
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hallo Welt!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
</code></pre>
</details>

### Aufgabe: Dynamische URL-Parameter in Flask 🌶️🌶️

Erstelle eine Flask-Anwendung, die dynamische URL-Parameter verwendet. Der Endpunkt soll `/greet/<name>` sein und eine Begrüßung in der Form "Hallo, [name]!" zurückgeben, wobei `[name]` durch den Namen ersetzt wird, der als URL-Parameter übergeben wird.

<details>
<summary>Lösung</summary>

```python
from flask import Flask
app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f'Hallo, {name}!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

</details>

### Aufgabe: JSON-Antworten in Flask 🌶️🌶️🌶️

Implementiere einen Flask-Endpunkt, der eine JSON-Antwort zurückgibt. Der Endpunkt `/data` soll ein JSON-Objekt zurückgeben, das Informationen über drei fiktive Bücher enthält (z.B. Titel, Autor und Veröffentlichungsjahr). Nutze die `jsonify`-Funktion von Flask, um die JSON-Antwort korrekt zu formatieren.

<details>
<summary>Lösung</summary>

<pre><code>
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/data')
def data():
    books = [
        {'title': 'Buch Eins', 'author': 'Autor A', 'year': 2001},
        {'title': 'Buch Zwei', 'author': 'Autor B', 'year': 2002},
        {'title': 'Buch Drei', 'author': 'Autor C', 'year': 2003}
    ]
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
</code></pre>
</details>

### Aufgabe: Einfache ToDo-Liste mit Flask 🌶️🌶️🌶️🌶️

Erstelle eine Flask-Anwendung, die es einem Benutzer ermöglicht, eine einfache ToDo-Liste zu verwalten. Die Anwendung soll die folgenden Funktionen unterstützen:

- **Anzeigen der aktuellen ToDo-Liste**: Ein GET-Endpunkt (`/todos`), der eine Liste der aktuellen ToDo-Aufgaben zurückgibt. Anfangs kann die Liste leer sein.

- **Hinzufügen von Aufgaben**: Ein GET-Endpunkt (`/todos/add/<todo>`), der es dem Benutzer ermöglicht, eine neue Aufgabe hinzuzufügen. Die Aufgabe soll als einfacher Text übergeben werden.

- **Löschen von Aufgaben**: Ein GET-Endpunkt (`/todos/delete/<task_id>`), der es dem Benutzer ermöglicht, eine Aufgabe anhand ihrer eindeutigen ID zu löschen.

<details>
<summary>Lösung</summary>

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

@app.route('/todos')
def get_todos():
    global todos
    return jsonify(todos)

@app.route('/todos/add/<todo>')
def add_todo(todo):
    global todos
    todos.append(todo)
    return jsonify({"message": "Task added successfully"})

@app.route('/todos/delete/<task_id>')
def delete_todo(task_id):
    global todos
    todos = [todo for todo in todos if todo.get('id') != task_id]
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

</details>

## Exkurs: Django: Das "Batterien-inbegriffen"-Framework

### Konzept und Philosophie

Django ist ein leistungsstarkes und voll ausgestattetes Web-Framework für größere Anwendungen und Plattformen.
Sein Ansatz „Batterien inbegriffen“ bedeutet, dass es mit vielen integrierten Funktionen für die gängigsten Entwicklungsaufgaben kommt.

### Hauptmerkmale von Django

**Vollständige Entwicklungsumgebung**: Es bietet eine robuste Basis für Datenbankmodelle, Benutzerverwaltung, Sicherheitsmechanismen und mehr.

**ORM (Object-Relational Mapping)**: Eines der Kernmerkmale von Django ist sein ORM-System, das eine Abstraktionsschicht über die Datenbank bietet und SQL-Abfragen durch Python-Code ersetzt.

**Admin-Oberfläche**: Eine eingebaute Admin-Oberfläche ermöglicht einfache Verwaltung von Datenmodellen und Benutzerkonten.

### Einrichtung einer API mit Django

Im direkten Vergleich wird der Unterschied von Flask und Django klar, denn es erfordert ein wenig mehr Setup als Flask, bietet aber von Anfang an mehr Funktionalität.

**1. Installation und Projektstart**: Installiere Django und starten ein neues Projekt mit `django-admin startproject myproject`.

**2. Anwendung erstellen**: Erstelle eine neue Anwendung mit `python manage.py startapp myapp`.

**3. Views und URLs definieren**: Django verwendet keine Annotations sondern ein Muster von Views und URLs um Anfragen zu verarbeiten.

- In `views.py`, erstelle eine Funktion, die eine HTTP-Antwort zurückgibt.
- In `urls.py`, definiere eine URL-Route, die der View-Funktion entspricht.

```python
# views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hallo Welt!')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
]
```

**4. Server starten**: Führe `python manage.py runserver 8000` aus, um den Server zu starten.

### Aufgabe: Hello World Django 🌶️️

Erstelle eine einfache Django-Anwendung, die einen GET-Endpunkt bietet. Dieser Endpunkt soll bei einem Zugriff eine Textantwort "Hallo Welt!" zurückgeben. Dazu musst du eine View-Funktion in Django erstellen und diese mit einer URL in urls.py verbinden.

<details>
<summary>Lösung</summary>

<pre><code>
# views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hallo Welt!')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
]
</code></pre>
</details>

### Aufgabe: Dynamische URL-Parameter in Django 🌶️🌶️

Implementiere in Django einen Endpunkt, der dynamische URL-Parameter verarbeitet. Der Endpunkt `/greet/<name>` soll eine personalisierte Begrüßung in Form von "Hallo, [name]!" zurückgeben, wobei [name] der Name ist, der als Parameter in der URL übergeben wird. Du musst eine entsprechende View-Funktion erstellen und die URL in urls.py korrekt konfigurieren.

<details>
<summary>Lösung</summary>

<pre><code>
# views.py
from django.http import HttpResponse

def greet(request, name):
    return HttpResponse(f'Hallo, {name}!')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('greet/<str:name>/', views.greet),
]
</code></pre>
</details>

### Aufgabe: JSON-Antworten in Django 🌶️🌶️🌶️

Erstelle einen Django-Endpunkt, der eine JSON-Antwort liefert. Der Endpunkt /data soll ein JSON-Objekt zurückgeben, das Informationen über drei fiktive Bücher enthält (z.B. Titel, Autor und Veröffentlichungsjahr). Verwende die JsonResponse-Funktion von Django, um das JSON-Objekt korrekt zu formatieren und zurückzugeben.

<details>
<summary>Lösung</summary>

<pre><code>
# views.py
from django.http import JsonResponse

def data(request):
    books = [
        {'title': 'Buch Eins', 'author': 'Autor A', 'year': 2001},
        {'title': 'Buch Zwei', 'author': 'Autor B', 'year': 2002},
        {'title': 'Buch Drei', 'author': 'Autor C', 'year': 2003}
    ]
    return JsonResponse(books, safe=False)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data),
]
</code></pre>
</details>

## Lokaler HTTP Server

Ein lokaler HTTP(S) Server ermöglicht es, Webanwendungen und APIs auf einem lokalen Rechner zu entwickeln und zu testen. Sowohl Flask als auch Django bieten eingebaute Entwicklungsserver, die für Testzwecke und während der Entwicklung verwendet werden können. Diese Server sind jedoch nicht für den produktiven Einsatz gedacht, da sie nicht für hohe Lasten oder Sicherheitsanforderungen optimiert sind.

Für Produktionsumgebungen sollten auf jeden Fall robustere Serverlösungen wie [Apache](https://httpd.apache.org/) verwendet und [HTTPS](https://www.cloudflare.com/de-de/learning/ssl/what-is-https/) konfiguriert werden.

## Exkurs: Ports und ihre Bedeutung

Ports sind ein zentraler Bestandteil des Internetprotokolls (IP) und spielen eine entscheidende Rolle bei der Kommunikation zwischen verschiedenen Computern über das Netzwerk.

### Was sind Ports?

Ein Port ist eine **numerische Kennung, die einem bestimmten Prozess oder Dienst auf einem Hostcomputer zugewiesen ist**. Diese Nummer ermöglicht es dem Betriebssystem, eingehende Netzwerkanforderungen an die richtige Anwendung weiterzuleiten. Ports werden durch eine 16-Bit-Zahl dargestellt, was bedeutet, dass es theoretisch bis zu 65.535 Ports gibt (0 bis 65535). Einige davon sind für spezielle Zwecke reserviert.

- **Standardports**: Einige Ports haben Standardzuweisungen für bestimmte Dienste. Zum Beispiel wird HTTP normalerweise über Port 80 und HTTPS über Port 443 übertragen.

- **Benutzerdefinierte Ports**: Für benutzerdefinierte Anwendungen oder Dienste können Entwickler Ports jenseits der bekannten Standardports verwenden, solange diese nicht von anderen Diensten belegt sind.

### Wie funktionieren Ports?

Wenn ein Computer eine Netzwerkanforderung sendet, wie z.B. das Abrufen einer Webseite oder das Senden einer E-Mail, fügt das Betriebssystem des Senders dem Paket eine Ziel-IP-Adresse und einen Zielport hinzu. Beim Empfänger überprüft das Betriebssystem den Zielport und leitet die Anfrage an die entsprechende Anwendung weiter, die auf diesem Port wartet.

Ports ermöglichen die gleichzeitige Verwendung verschiedener Netzwerkdienste auf einem einzigen Computer. Zum Beispiel kann ein Webserver auf Port 80 lauschen, während ein E-Mail-Server auf Port 25 wartet. Ohne Ports wäre es schwierig, verschiedene Arten von Netzwerkdiensten auf einem Hostcomputer zu betreiben.

#### Portnutzung in Webentwicklung

In der Webentwicklung werden Ports verwendet, um Webserver und Webanwendungen zu identifizieren und zu erreichen. Bei lokalen Entwicklungsservern wie Flask und Django können Entwickler den Port konfigurieren, auf dem die Anwendung ausgeführt wird. Dies ermöglicht es mehreren Entwicklern, verschiedene Anwendungen gleichzeitig auf demselben Host zu entwickeln, ohne dass sie sich gegenseitig beeinflussen.

Ports spielen auch eine wichtige Rolle bei der Konfiguration von Firewalls. Administratoren können den Datenverkehr basierend auf den verwendeten Ports steuern, um die Sicherheit des Netzwerks zu gewährleisten.
