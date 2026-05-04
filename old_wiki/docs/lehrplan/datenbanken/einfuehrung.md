# Einführung in SQLAlchemy

<img alt="ORM" src="images/orm.png" width="600">

## Überblick über SQLAlchemy

[10 min]

SQLAlchemy ist eine Bibliothek zum Interagieren mit SQL-Datenbanken. Sie bietet zwei Hauptfunktionalitäten: ein ORM (Object-Relational Mapping) und eine SQL-Expression Language.

1. **ORM (Object-Relational Mapping)**: SQLAlchemy's ORM erlaubt es, Datenbanktabellen als Python-Klassen zu definieren und die dazugehörigen Zeilen als Instanzen dieser Klassen. Dies bedeutet, dass wir mit der Datenbank interagieren können, als würden wir mit normalen Python-Objekten arbeiten. Das ORM kümmert sich um die Umwandlung zwischen den Python-Objekten und den Datenbankdaten, was den Code lesbarer und wartbarer macht.

2. **SQL-Expression Language**: Für Fälle, in denen mehr Kontrolle oder eine direktere Interaktion mit der Datenbank erforderlich ist, bietet SQLAlchemy eine SQL-Expression Language. Diese ermöglicht es, SQL-Anweisungen in Python zu schreiben und auszuführen, wobei die Syntax und die Sicherheitsfunktionen von SQLAlchemy genutzt werden. Dies kann besonders nützlich sein, wenn komplexe Abfragen oder spezifische Datenbankoperationen erforderlich sind, die über die Möglichkeiten des ORMs hinausgehen.

Durch die Verwendung von SQLAlchemy in Ihren Projekten können wir eine höhere Ebene der Abstraktion und Flexibilität erreichen, was den Umgang mit relationalen Datenbanken erheblich vereinfacht. SQLAlchemy bietet damit die Möglichkeit, Datenbanken in Python-Anwendungen zu verwenden, ohne dass wir uns mit den Details der Datenbankinteraktionen befassen müssen.

## Vergleich von SQLAlchemy mit anderen Datenbank-Toolkits

[15 min]

Der Vergleich von SQLAlchemy mit anderen Datenbank-Toolkits gibt einen guten Überblick über die verschiedenen Ansätze und Funktionen, die in der Welt der Datenbankinteraktion zur Verfügung stehen. Hier sind einige gängige Toolkits und wie sie sich von SQLAlchemy unterscheiden:

1. **Django ORM**:
    - **Einsatzbereich**: Django ORM ist Teil des Django Web Frameworks und wird hauptsächlich für Webanwendungen verwendet. SQLAlchemy ist unabhängig von einem spezifischen Framework und kann in einer breiteren Palette von Anwendungen eingesetzt werden.
    - **Designphilosophie**: Django ORM zielt darauf ab, eng mit anderen Teilen des Django-Frameworks zu integrieren und bietet eine enge Kopplung zwischen Modellen und Datenbankstrukturen. SQLAlchemy hingegen legt Wert auf Flexibilität und erlaubt eine feinere Kontrolle über die Datenbankinteraktionen.
    - **Lernkurve**: Django ORM kann für Einsteiger in die Welt der Webentwicklung einfacher zu erlernen sein, da es mit vielen Standardeinstellungen und Konventionen kommt. SQLAlchemy hat eine etwas steilere Lernkurve aufgrund seiner umfassenden Funktionen und Konfigurationsoptionen.

2. **Active Record (Ruby on Rails)**:
    - **Sprache**: Active Record ist ein Teil von Ruby on Rails und für Ruby geschrieben. SQLAlchemy ist für Python.
    - **Paradigma**: Active Record folgt dem gleichnamigen Muster, bei dem jedes Modell eng mit der Datenbank verbunden ist. SQLAlchemy bietet durch sein Data Mapper Pattern mehr Trennung zwischen Objektmodellen und Datenbanktabellen.
    - **Flexibilität**: SQLAlchemy bietet mehr Flexibilität und eignet sich besser für komplexe Abfragen und Datenbankoperationen, während Active Record für seine Einfachheit und schnelle Entwicklung bekannt ist.

3. **Entity Framework (C#/.NET)**:
    - **Plattform**: Entity Framework ist für .NET-Plattformen und somit für C# und andere .NET-Sprachen. SQLAlchemy ist Python-spezifisch.
    - **Integration**: Entity Framework ist eng in das .NET-Ökosystem integriert und bietet Funktionen wie LINQ (Language Integrated Query), was die Abfragebildung vereinfacht. SQLAlchemy ist eigenständig und nicht an eine bestimmte Plattform oder Sprache gebunden.

4. **PeeWee**:
    - **Komplexität und Größe**: PeeWee ist ein kleineres, leichteres ORM-Toolkit für Python und zielt darauf ab, einfach und leichtgewichtig zu sein. SQLAlchemy ist umfangreicher und bietet mehr Funktionen und Flexibilität.
    - **Geeignet für**: PeeWee eignet sich gut für kleinere Anwendungen und Skripte, während SQLAlchemy besser für größere, komplexere Projekte geeignet ist.

5. **Hibernate (Java)**:
    - **Sprache**: Hibernate ist ein ORM-Toolkit für Java, während SQLAlchemy für Python ist.
    - **Funktionen**: Beide bieten ähnliche Funktionen wie Caching, Lazy Loading und eine reichhaltige Abfragesprache, aber Hibernate ist speziell auf Java-Anwendungen ausgerichtet.

Jedes dieser Toolkits hat seine Stärken in bestimmten Bereichen und Szenarien. SQLAlchemy zeichnet sich durch seine Flexibilität und seine Fähigkeit aus, sowohl mit einfachen als auch mit sehr komplexen Datenbankoperationen gut umzugehen. Es ist ideal für Python-Entwickler, die eine umfassende Kontrolle über ihre Datenbankinteraktionen benötigen.

## Installation

[30 min]

Die Installation und grundlegende Konfiguration von SQLAlchemy in einem Python-Projekt besteht aus einigen einfachen Schritten. Hier ist ein Leitfaden, um Sie durch den Prozess zu führen:

1. **Vorbereitung der Umgebung**: Es ist empfehlenswert, SQLAlchemy innerhalb einer virtuellen Umgebung zu installieren, um Konflikte mit anderen Bibliotheken zu vermeiden. Eine virtuelle Umgebung kömmem wir mit `python -m venv venv` erstellen und aktivieren.

2. **Installieren von SQLAlchemy**: Führe den folgenden Befehl aus, um SQLAlchemy zu installieren:

```bash
pip install sqlalchemy
```

### Grundlegende Konfiguration

Nach der Installation können wir SQLAlchemy in unserem Projekt einrichten:

```python
from sqlalchemy import create_engine, MetaData
```

**Erstellen einer Datenbank-Engine**: SQLAlchemy verwendet das Konzept einer "Engine", um eine Verbindung zur Datenbank herzustellen. Die Engine ermöglicht es, eine Verbindung zur Datenbank herzustellen. Sie spezifiziert die Art der Datenbank, den Verbindungspfad und andere Parameter. Zusätzlich verwaltet die Engine oftmals einen Verbindungspool, der die Wiederverwendung von Datenbankverbindungen erleichtert, um die Leistung zu verbessern. Hier ist ein Beispiel, wie man eine Engine für eine SQLite-Datenbank erstellt:

```python
engine = create_engine('sqlite:///example.db')
```

Ersetze `sqlite:///example.db` durch den entsprechenden Verbindungsstring für Ihre Datenbank. Zum Beispiel für eine PostgreSQL-Datenbank könnte es `postgresql://user:password@localhost/mydatabase` sein.

## Herstellen einer Verbindung zu verschiedenen Datenbanktypen

[30 min]

Das Herstellen einer Verbindung zu verschiedenen Datenbanktypen mit SQLAlchemy erfolgt durch die Erstellung einer Engine, die den entsprechenden Verbindungsstring für die jeweilige Datenbank verwendet. Hier sind Beispiele, wie wir Verbindungen zu einigen gängigen Datenbanktypen wie SQLite, PostgreSQL und MySQL herstellen können:

### SQLite

<img alt="ORM" src="images/SQLite.png" width="300">

SQLite ist eine leichte, dateibasierte Datenbank, die ideal für Entwicklung, Testen oder kleine Anwendungen ist. Sie benötigt keine separate Serverinstallation.

```python
from sqlalchemy import create_engine

# Für eine SQLite-Datenbank, die in einer Datei gespeichert wird
engine = create_engine('sqlite:///mydatabase.db')

# Für eine SQLite In-Memory-Datenbank
engine = create_engine('sqlite:///:memory:')
```

### PostgreSQL

<img alt="ORM" src="images/Postgresql.png" width="300">

PostgreSQL ist eine leistungsstarke, Open-Source objektrelationale Datenbank. Wir müssen den Benutzernamen, das Passwort, den Host (z. B. `localhost`) und den Datenbanknamen angeben.

```python
engine = create_engine('postgresql://username:password@localhost/mydatabase')
```

Ersetze `username`, `password` und `mydatabase` mit deinen PostgreSQL-Anmeldeinformationen und dem Datenbanknamen.

### MySQL/MariaDB

<img alt="ORM" src="images/mysql.png" width="300">

MySQL und MariaDB sind weit verbreitete Open-Source relationale Datenbankmanagementsysteme. Der Verbindungsstring ist dem von PostgreSQL sehr ähnlich.

```python
engine = create_engine('mysql+pymysql://username:password@localhost/mydatabase')
```

Ersetze auch hier `username`, `password` und `mydatabase` mit deinen eigenen Anmeldeinformationen.

### Hinweise

- Stell sicher, dass alle erforderlichen Abhängigkeiten für die jeweilige Datenbank installiert haben. Zum Beispiel benötigen wir für PostgreSQL den `psycopg2`-Treiber (`pip install psycopg2`) und für MySQL/MariaDB den `pymysql`-Treiber (`pip install pymysql`).
- Sicherheitsaspekt: Speicher niemals Benutzernamen und Passwörter direkt im Code. Verwende stattdessen sichere Methoden zur Speicherung von Anmeldeinformationen, wie Umgebungsvariablen oder spezielle Konfigurationsdateien (z. B. durch die Verwendung von `.env` Dateien). 

## Erste Schritte mit dem ORM
[30 min]

### Einführung in das ORM-Konzept

**Object-Relational Mapping (ORM)** ist ein Programmieransatz, der verwendet wird, um Daten zwischen inkompatiblen Typsystemen in objektorientierten Programmiersprachen zu konvertieren. In Python ermöglicht SQLAlchemy's ORM es Entwicklern, mit Datenbanken zu arbeiten, als ob sie mit gewöhnlichen Python-Objekten interagieren würden. Dieser Ansatz bietet mehrere Vorteile:

- **Abstraktion**: ORM verbirgt die Komplexität von SQL-Anweisungen hinter einfachen Python-Klassen und -Objekten.
- **Wartbarkeit**: Der Code ist übersichtlicher und leichter zu warten.
- **Portabilität**: Der Code ist in der Regel datenbankunabhängig, was den Wechsel zwischen verschiedenen Datenbanksystemen erleichtert.

### Definition von Modellen und Tabellen

In SQLAlchemy werden Tabellen durch Klassen dargestellt, die von `declarative_base()` abgeleitet werden. Jede Klasse repräsentiert eine Tabelle in der Datenbank, und jede Instanz der Klasse entspricht einer Zeile in dieser Tabelle.

### 1. **Definieren des Basismodells**:


```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```

### 2. **Erstellen eines Modells**:
   Modelle werden durch Klassen definiert, die von `Base` erben. Spalten in der Tabelle werden als Attribute der Klasse definiert.


```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

Base.metadata.create_all(bind=engine) # erstelle die Tabellen in der DB
```

### Erstellen von Sitzungen und Hinzufügen von Objekten

Sitzungen in SQLAlchemy ermöglichen es uns, Objekte zu erstellen, zu ändern und zu löschen. Sie fungieren als eine Art Puffer zwischen den Python-Objekten und der Datenbank.

#### 1. **Erstellen einer Session**

   Um mit der Datenbank zu interagieren, erstellen eine Session.

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

#### 2. **Hinzufügen von Objekten**

   Neue Objekte (Zeilen) können zur Datenbank hinzugefügt werden, indem sie zur Session hinzugefügt werden.

```python
new_user = User(name='Alice', age=30)
session.add(new_user)
```

#### 3. **Speichern von Änderungen**

   Änderungen werden in der Datenbank gespeichert, indem die `commit()`-Methode der Session aufgerufen wird.

```python
session.commit()
```

#### 4. **Schließen der Session**

   Nachdem wir mit der Datenbankinteraktion fertig sind, sollten wir die Session schließen.

```python
session.close()
```

### Übungsaufgabe: Erstellen und Verwalten von Daten mit SQLAlchemy ORM 🌶️️🌶️️

[60 min]

1.**Definiere ein Modell 'Book'** 🌶️️:

- Erstelle eine Klasse `Book`, die von `Base` erbt.
- Definiere die Tabelle `books` mit folgenden Spalten:
  - `id`: Integer, Primärschlüssel
  - `title`: String, Titel des Buches
  - `author`: String, Autor des Buches
  - `published_year`: Integer, Jahr der Veröffentlichung

<details>
<summary>Lösung</summary>

<pre><code>
# Importieren der notwendigen Bibliotheken
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Definieren des Basismodells
Base = declarative_base()

# Definition des Book-Modells
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    published_year = Column(Integer)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', published_year={self.published_year})>"
</code></pre>
</details>

<br />

2.**Erstellen eine SQLite-Datenbank** 🌶️️:

- Verwende eine SQLite-Datenbank (`sqlite:///books.db`).
- Erstelle die Tabelle `books` in der Datenbank.

<details>
<summary>Lösung</summary>

<pre><code>
# Erstellen einer SQLite-Datenbank
engine = create_engine('sqlite:///books.db')
# Erstelle die Tabelle in der Datenbank
Base.metadata.create_all(engine)
</code></pre>
</details>

<br />

3.**Füge neue Bücher hinzu** 🌶️️️:

- Erstelle mindestens drei Buch-Objekte mit unterschiedlichen Attributen.
- Füge diese Objekte zur Session hinzu und speicher sie in der Datenbank.

<details>
<summary>Lösung</summary>

<pre><code>
# Erstellen einer Session
Session = sessionmaker(bind=engine)
session = Session()

# Hinzufügen neuer Bücher
book1 = Book(title="1984", author="George Orwell", published_year=1949)
book2 = Book(title="Brave New World", author="Aldous Huxley", published_year=1932)
book3 = Book(title="Fahrenheit 451", author="Ray Bradbury", published_year=1953)

session.add_all([book1, book2, book3])
session.commit()
# Schließen der Session
session.close()
</code></pre>
</details>

<br />

4.**Abfragen von Büchern** 🌶️️🌶️️:

- Führe eine Abfrage durch, um alle Bücher auszugeben
- Führe eine Abfrage durch, um alle Bücher eines bestimmten Autors zu finden.
- Führe eine Abfrage durch, um alle Bücher zu finden, die vor dem Jahr 2000 veröffentlicht wurden.

<details>
<summary>Lösung</summary>

<pre><code>
# Abfrage aller Bücher
all_books = session.query(Book).all()

# Ausgabe aller Bücher
print("Alle Bücher:")
for book in all_books:
    print(f"{book.title} von {book.author}, veröffentlicht {book.published_year}")
# Orwells Bücher
books_by_orwell = session.query(Book).filter_by(author="George Orwell").all()
print("Bücher von George Orwell:", books_by_orwell)
# Bücher vor 2000
books_before_2000 = session.query(Book).filter(Book.published_year < 2000).all()
print("Bücher veröffentlicht vor 2000:", books_before_2000)
</code></pre>
</details>

<br />

5.**Aktualisieren eines Buches** 🌶️️🌶️️:

- Wähle eines der Bücher aus und aktualisiere dessen `published_year`.
- Speicher die Änderungen in der Datenbank.
- Führe eine einfache Abfrage durch, um dieses Buch auszugeben.

<details>
<summary>Lösung</summary>

<pre><code>
# Aktualisieren eines Buches
book_to_update = session.query(Book).filter_by(title="Fahrenheit 451").first()
if book_to_update:
    book_to_update.published_year = 1954
    session.commit()

# Beispielhafte Ausgabe dieses Buches
books_after_1953 = session.query(Book).filter(Book.published_year > 1953).all()
print("Bücher veröffentlicht nach 1953:", books_after_1953)
</code></pre>
</details>

<br />

6.**Bonus** 🌶️️🌶️️🌶️️: Implementiere eine Funktion, um ein Buch anhand seiner ID zu löschen.

<details>
<summary>Lösung</summary>

<pre><code>
# Löschen eines Buches
def delete_book(book_id):
    book_to_delete = session.query(Book).filter_by(id=book_id).first()
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()

# Beispiel für das Löschen eines Buches
delete_book(1)
</code></pre>
</details>

<br />

### Hinweis zur Lösung

- Nutze die [SQLAlchemy-Dokumentation](https://docs.sqlalchemy.org/en/20/), falls du zusätzliche Informationen benötigst.

### Gesamtlösung

<details>
<summary>Lösung</summary>

<pre><code>
# Importieren der notwendigen Bibliotheken
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Definieren des Basismodells
Base = declarative_base()

# Definition des Book-Modells
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    published_year = Column(Integer)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', published_year={self.published_year})>"

# Erstellen einer SQLite-Datenbank
engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)

# Erstellen einer Session
Session = sessionmaker(bind=engine)
session = Session()

# Hinzufügen neuer Bücher
book1 = Book(title="1984", author="George Orwell", published_year=1949)
book2 = Book(title="Brave New World", author="Aldous Huxley", published_year=1932)
book3 = Book(title="Fahrenheit 451", author="Ray Bradbury", published_year=1953)

session.add_all([book1, book2, book3])
session.commit()

# Abfragen von Büchern eines bestimmten Autors
books_by_orwell = session.query(Book).filter_by(author="George Orwell").all()
print("Bücher von George Orwell:", books_by_orwell)

# Abfragen von Büchern, die vor dem Jahr 2000 veröffentlicht wurden
books_before_2000 = session.query(Book).filter(Book.published_year < 2000).all()
print("Bücher veröffentlicht vor 2000:", books_before_2000)

# Aktualisieren eines Buches
book_to_update = session.query(Book).filter_by(title="Fahrenheit 451").first()
if book_to_update:
    book_to_update.published_year = 1954
    session.commit()

# Bonus: Löschen eines Buches anhand seiner ID
def delete_book(book_id):
    book_to_delete = session.query(Book).filter_by(id=book_id).first()
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()

# Beispiel für das Löschen eines Buches
delete_book(1)

# Schließen der Session
session.close()
</code></pre>

```bash
Bücher von George Orwell: [<Book(title='1984', author='George Orwell', published_year=1949)>]
Bücher veröffentlicht vor 2000: [<Book(title='1984', author='George Orwell', published_year=1949)>, <Book(title='Brave New World', author='Aldous Huxley', published_year=1932)>, <Book(title='Fahrenheit 451', author='Ray Bradbury', published_year=1953)>]


/var/folders/n9/5zsytn3s4hj75c26k015w8080000gp/T/ipykernel_95677/2235682494.py:7: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()
```

</details>
