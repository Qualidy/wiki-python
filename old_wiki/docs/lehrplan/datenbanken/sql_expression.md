# Exkurs: Fortgeschrittene ORM-Konzepte

## Einführung in die SQL Expression Language

[15 min]

SQLAlchemy's SQL Expression Language ermöglicht eine detaillierte Erstellung von SQL-Statements in Python. Im Gegensatz zum ORM, das eine höhere Abstraktionsebene bietet, ermöglicht die SQL Expression Language eine präzisere und spezifischere Interaktion mit der Datenbank. In diesem Abschnitt werden wir die Grundlagen der SQL Expression Language in SQLAlchemy kennenlernen.

Die SQL Expression Language aus SQLAlchemy unterscheidet zwei grundlegende Konzepte: Ausdrücke und Statements. Ein Ausdruck ist ein einzelnes Element, das in SQL verwendet werden kann, wie z.B. eine Spalte oder ein mathematischer Ausdruck. Ein Statement ist ein SQL-Befehl, der eine oder mehrere Ausdrücke enthält.

- **Ausdrücke und Statements**: Jedes Element in der SQL Expression Language ist entweder ein Ausdruck (wie eine Spalte oder ein mathematischer Ausdruck) oder ein Statement (wie ein SQL-Befehl).
  
- **Tabellen und Spalten**: Tabellen werden als `Table`-Objekte repräsentiert, während Spalten als `Column`-Objekte dargestellt werden. Ein `Table`-Objekt wird einer `MetaData`-Instanz zugeordnet, die die Strukturinformationen enthält.

```python
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()
user_table = Table('user', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String))
```

- **Select-Statement**: Ein SELECT-Statement wird in SQLAlchemy 1.4+ direkt mit der `select()`-Funktion erstellt, wobei die Spalten direkt als Argumente übergeben werden, ohne eine Liste zu verwenden.

```python
from sqlalchemy.sql import select

select_statement = select(user_table.c.name).where(user_table.c.name == 'Alice')
```

## Unterschiede und Gemeinsamkeiten mit dem ORM

[15 min]

### Gemeinsamkeiten

- **Gleiche Datenbank-Abstraktion**: Beide Ansätze basieren auf SQLAlchemy's Engine und Connection-Objekten für die Datenbankinteraktion.
  
- **Transaktionsmanagement**: Sowohl in der SQL Expression Language als auch im ORM können Transaktionen verwendet werden, um die Datenintegrität zu gewährleisten.

### Unterschiede

- **Abstraktionsgrad**: Das ORM bietet ein höheres Abstraktionsniveau, indem es die Datenbanktabellen als Klassen und die Zeilen als Objektinstanzen abbildet. Die SQL Expression Language bleibt näher an der eigentlichen SQL-Syntax und ermöglicht präzisere und spezifischere Abfragen.

- **Flexibilität vs. Einfachheit**: Das ORM ist für Standard-Operationen einfacher und schneller, während die SQL Expression Language bei komplexen oder speziellen Abfragen mehr Flexibilität bietet.

### Beispiel: Unterschiede in der Anwendung

- **ORM-Abfrage**:

```python
for user in session.query(User).filter(User.name == 'Alice'):
    print(user.id, user.name)
```

- **SQL Expression Language-Abfrage**:

```python
  # SQL Expression Language
conn = engine.connect()
select_statement = select(user_table.c.id, user_table.c.name).where(user_table.c.name == 'Alice')
result = conn.execute(select_statement)
for row in result:
    print(row.id, row.name)
```

Die SQL Expression Language in SQLAlchemy ermöglicht es, SQL-Statements direkt in Python zu erstellen, und bietet eine leistungsfähige Alternative zum ORM für komplexe Abfragen und spezielle Datenbankoperationen. Mit der Einführung von SQLAlchemy 1.4+ hat sich die Syntax leicht verändert, wobei die `select()`-Funktion nun direkt Spalten als Argumente akzeptiert, was die Nutzung intuitiver und Pythonischer macht.

### Übungsaufgabe: Erkundung der SQL Expression Language in SQLAlchemy 🌶️️🌶️️🌶️️
[60 min]

1. **Vorbereitung der Umgebung und Tabellendefinition**:
    - Erstelle eine neue SQLite-Datenbank und definieren Sie eine Tabelle `user` mit den Spalten `id` (Integer, Primärschlüssel) und `name` (String).
    - Füge einige Einträge in die `user`-Tabelle ein.

2. **Erstellen von Select-Statements**:
    - Schreibe ein Select-Statement, um alle Nutzer aus der `user`-Tabelle abzurufen.
    - Schreibe ein weiteres Select-Statement, um nur Nutzer mit einem bestimmten Namen (z.B. "Alice") abzurufen.

3. **Erstellen und Ausführen einer Insert-Operation**:
    - Füge einen neuen Nutzer in die `user`-Tabelle ein.

4. **Update- und Delete-Operationen**:
    - Aktualisiere den Namen eines Nutzers in der `user`-Tabelle.
    - Lösch einen Nutzer aus der `user`-Tabelle.

5. **Bonus**: Erstelle eine Unterabfrage, die eine aggregierte Information zurückgibt (z.B. die Gesamtanzahl der Nutzer).

<details>
<summary>Lösung</summary>

<pre><code>
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, func

# Datenbank in memory und Tabelle erstellen
engine = create_engine('sqlite://')
metadata = MetaData()
user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String))
metadata.create_all(engine)

# Einige Nutzer einfügen
with engine.connect() as conn:
    conn.execute(user_table.insert(), [{'name': 'Alice'}, {'name': 'Bob'}])

# Select-Statements
with engine.connect() as conn:
    # Alle Nutzer abrufen
    all_users = conn.execute(select(user_table)).fetchall()
    print("Alle Nutzer:", all_users)

    # Nutzer mit dem Namen 'Alice' abrufen
    alice = conn.execute(select(user_table).where(user_table.c.name == 'Alice')).fetchall()
    print("Nutzer namens Alice:", alice)

# Einen neuen Nutzer einfügen
with engine.connect() as conn:
    conn.execute(user_table.insert(), {'name': 'Charlie'})

# Einen Nutzer aktualisieren
with engine.connect() as conn:
    conn.execute(user_table.update().where(user_table.c.name == 'Bob').values(name='Robert'))

# Einen Nutzer löschen
with engine.connect() as conn:
    conn.execute(user_table.delete().where(user_table.c.name == 'Charlie'))

# Bonus: Unterabfrage für aggregierte Information
with engine.connect() as conn:
    user_count = conn.execute(select(func.count()).select_from(user_table)).scalar()
    print("Gesamtanzahl der Nutzer:", user_count)

Alle Nutzer: []
Nutzer namens Alice: []
Gesamtanzahl der Nutzer: 0
</code></pre>
</details>

## CRUD-Operationen mit Expression Language
[30 min]

In diesem Abschnitt konzentrieren wir uns auf CRUD-Operationen (Create, Read, Update, Delete) unter Verwendung der SQL Expression Language in SQLAlchemy. Diese Operationen sind das Herzstück der Interaktion mit jeder Datenbank und ermöglichen es Ihnen, Daten effektiv zu verwalten.

### Erstellen von Daten (Create)

Das Erstellen neuer Daten in der Datenbank erfolgt über das `insert`-Statement. Wir können einzelne Datensätze oder mehrere auf einmal einfügen.

```python
from sqlalchemy import insert

# Einzelnen Datensatz einfügen
insert_stmt = insert(user_table).values(name='Alice')
conn.execute(insert_stmt)

# Mehrere Datensätze gleichzeitig einfügen
conn.execute(user_table.insert(), [
    {'name': 'Bob'},
    {'name': 'Carol'}
])
```

### Lesen von Daten (Read)

Das Lesen von Daten, bekannt als Abfrage oder Query, wird mit dem `select`-Statement durchgeführt. Wir können spezifische Spalten auswählen und Bedingungen für die Abfrage festlegen.

```python
from sqlalchemy.sql import select

# Alle Datensätze abfragen
select_stmt = select(user_table)
result = conn.execute(select_stmt)
for row in result:
    print(row)

# Abfrage mit Bedingung
select_stmt = select(user_table).where(user_table.c.name == 'Alice')
result = conn.execute(select_stmt)
for row in result:
    print(row)
```

### Aktualisieren von Daten (Update)

Das Aktualisieren vorhandener Daten erfolgt über das `update`-Statement. Wir können spezifizieren, welche Spalten aktualisiert werden sollen und unter welchen Bedingungen.

```python
from sqlalchemy import update

# Datensatz aktualisieren
update_stmt = update(user_table).where(user_table.c.name == 'Alice').values(name='Alicia')
conn.execute(update_stmt)
```

### Löschen von Daten (Delete)

Das Löschen von Daten aus der Datenbank wird mit dem `delete`-Statement ausgeführt. Wir können Bedingungen angeben, um zu steuern, welche Datensätze gelöscht werden.

```python
from sqlalchemy import delete

# Datensatz löschen
delete_stmt = delete(user_table).where(user_table.c.name == 'Alicia')
conn.execute(delete_stmt)
```

### Umgang mit Bulk-Operationen

Bulk-Operationen sind nützlich, um eine große Anzahl von Datensätzen einzufügen, zu aktualisieren oder zu löschen. SQLAlchemy bietet Methoden, um solche Operationen effizient zu handhaben.

```python
# Bulk-Insert
conn.execute(user_table.insert(), [
    {'name': 'Dave'},
    {'name': 'Eve'},
    {'name': 'Frank'}
])

# Bulk-Update (vorsicht, aktualisiert alle Zeilen, wenn keine Where-Bedingung angegeben ist)
conn.execute(update(user_table).values(name='Unknown'))

# Bulk-Delete
conn.execute(delete(user_table).where(user_table.c.name == 'Unknown'))
```

CRUD-Operationen bilden die Grundlage der Datenbankinteraktion in SQLAlchemy's SQL Expression Language. Sie ermöglichen es uns, Daten effizient zu erstellen, abzufragen, zu aktualisieren und zu löschen. Bulk-Operationen erweitern diese Funktionalität, indem sie die Bearbeitung großer Datensätze optimieren. Durch das Erlernen dieser Grundlagen können wir die Daten in unser Anwendung effektiv verwalten und manipulieren.

### Übungsaufgabe: CRUD-Operationen mit SQL Expression Language 🌶️️🌶️️
[60 min]

1. **Tabellenerstellung**:
    - Definiere eine Tabelle `book` mit den Spalten `id` (Integer, Primärschlüssel) und `title` (String).
    - Erstelle die Tabelle in einer SQLite-Datenbank.

2. **Daten einfügen (Create)**:
    - Füge mindestens drei Bücher in die `book`-Tabelle ein.

3. **Daten abfragen (Read)**:
    - Führe eine Abfrage durch, um alle Bücher in der Tabelle anzuzeigen.

4. **Daten aktualisieren (Update)**:
    - Aktualisiere den Titel eines Buches.

5. **Daten löschen (Delete)**:
    - Lösche ein Buch aus der Tabelle.

6. **Ausgabe der Daten**:
    - Führe eine Abfrage durch, um alle Bücher in der Tabelle anzuzeigen.

7. **Bonus**: Führe eine Bulk-Insert-Operation durch, um mehrere Bücher gleichzeitig hinzuzufügen.

<details>
<summary>Lösung</summary>

<pre><code>
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, insert, update, delete

# Datenbank in memory und Tabelle erstellen
engine = create_engine('sqlite://')
metadata = MetaData()
book_table = Table('book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('title', String))
metadata.create_all(engine)

# Verbindung zur Datenbank herstellen
conn = engine.connect()

# Einige Bücher einfügen
conn.execute(insert(book_table), [{'title': 'Book 1'}, {'title': 'Book 2'}, {'title': 'Book 3'}])

# Alle Bücher abfragen und ausgeben
result = conn.execute(select(book_table))
print("Vor Update und Delete:")
for row in result:
    print(row)

# Einen Buchtitel aktualisieren
conn.execute(update(book_table).where(book_table.c.title == 'Book 1').values(title='Updated Book 1'))

# Ein Buch löschen
conn.execute(delete(book_table).where(book_table.c.title == 'Book 2'))

# Bonus: Bulk-Insert
conn.execute(insert(book_table), [{'title': 'Book 4'}, {'title': 'Book 5'}])

# Ausgabe der Daten nach Update und Delete
result = conn.execute(select(book_table))
print("Nach Update und Delete:")
for row in result:
    print(row)

# Verbindung schließen
conn.close()

Vor Update und Delete:
(1, 'Book 1')
(2, 'Book 2')
(3, 'Book 3')
Nach Update und Delete:
(1, 'Updated Book 1')
(3, 'Book 3')
(4, 'Book 4')
(5, 'Book 5')
</code></pre>
</details>

## Erweiterte Funktionen und Performance
[30 min]

In diesem Abschnitt befassen wir uns mit fortgeschrittenen Techniken in SQLAlchemy, die darauf abzielen, die Performance zu optimieren und erweiterte Datenbankfunktionen zu nutzen. Dazu gehören die Indexierung zur Beschleunigung von Abfragen, das Performance-Tuning und die Verwendung von Funktionen und Stored Procedures.

### Einsatz von Indexierung und Performance-Tuning

#### Indexierung

Indexe in einer Datenbank verbessern die Geschwindigkeit der Datenabrufe, können aber das Einfügen, Löschen und Aktualisieren von Daten verlangsamen. SQLAlchemy ermöglicht es, Indexe in Ihren Tabellendefinitionen zu spezifizieren.

```python
from sqlalchemy import Index

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)  # Einen Index für die Spalte 'name' erstellen

# Erstellen eines expliziten Indexes
Index('my_index', User.name)
```

#### Performance-Tuning

- **Eager Loading**: SQLAlchemy lädt standardmäßig Beziehungen "lazy", d.h., es werden separate Queries ausgeführt, wenn auf eine Beziehung zugegriffen wird. Eager Loading kann diese Abfragen reduzieren.


```python
from sqlalchemy.orm import joinedload

users = session.query(User).options(joinedload(User.posts)).all()
```

- **Batching**: Beim Einfügen oder Aktualisieren vieler Datensätze können Batch-Operationen die Performance verbessern.


```python
session.bulk_insert_mappings(User, [{'name': 'name1'}, {'name': 'name2'}])
```

### Verwendung von Funktionen und Stored Procedures

#### Funktionen

SQLAlchemy ermöglicht den Aufruf von Datenbankfunktionen direkt aus dem Query. Dies kann für Aggregationsfunktionen oder spezifische Datenbankoperationen genutzt werden.

```python
from sqlalchemy.sql import func

# Aggregationsfunktion verwenden
user_count = session.query(func.count(User.id)).scalar()
```

#### Stored Procedures

Stored Procedures sind auf der Datenbank gespeicherte Programme, die mit SQLAlchemy aufgerufen werden können. Dies erfolgt meist über rohe SQL-Statements.

```python
# Stored Procedure aufrufen
conn = engine.connect()
result = conn.execute("CALL my_stored_procedure()")
for row in result:
    print(row)
```


Die Verwendung von Indexierung und Performance-Tuning-Techniken kann die Effizienz Ihrer Anwendung erheblich verbessern, insbesondere bei großen Datenmengen. Ebenso ermöglicht die Nutzung von Funktionen und Stored Procedures eine erweiterte Interaktion mit der Datenbank, die über einfache CRUD-Operationen hinausgeht. SQLAlchemy bietet eine reichhaltige Palette an Möglichkeiten, um diese fortgeschrittenen Features effektiv zu nutzen.

### Übungsaufgabe: Erweiterte Funktionen und Performance in SQLAlchemy 🌶️️🌶️️🌶️️
[60 min]

1. **Tabellenerstellung mit Index**:
    - Erstelle eine Tabelle `employee` mit den Spalten `id`, `name` und `department`.
    - Füge einen Index auf die Spalte `department` hinzu und beobachte die Auswirkungen auf Abfragegeschwindigkeiten.

2. **Eager Loading vs. Lazy Loading**:
    - Erstelle zwei Tabellen `author` und `book`, wobei `author` eine One-to-Many-Beziehung zu `book` hat.
    - Führe Abfragen durch, um alle Autoren und ihre Bücher zu laden, einmal mit Lazy Loading und einmal mit Eager Loading (verwenden `joinedload`).

3. **Performance-Messung**:
    - Mess die Ausführungszeit für beide Abfragen (Lazy Loading und Eager Loading) und vergleiche die Ergebnisse.

<details>
<summary>Lösung</summary>

<pre><code>
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData, Index
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload
import time

# Datenbank-Engine in memory und Metadaten-Objekt erstellen
engine = create_engine('sqlite://')
metadata = MetaData()

# Basis für ORM-Modelle definieren
Base = declarative_base()

# Tabellendefinitionen
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", backref="author")

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))

# Tabellen erstellen
Base.metadata.create_all(engine)

# Session-Setup
Session = sessionmaker(bind=engine)
session = Session()

# Beispieldaten hinzufügen
author1 = Author(name='Autor 1')
author2 = Author(name='Autor 2')
session.add_all([author1, author2])
session.commit()

book1 = Book(title='Buch 1 von Autor 1', author_id=author1.id)
book2 = Book(title='Buch 2 von Autor 1', author_id=author1.id)
book3 = Book(title='Buch 1 von Autor 2', author_id=author2.id)
session.add_all([book1, book2, book3])
session.commit()

# Lazy Loading Zeit messen
start_time = time.time()
lazy_authors = session.query(Author).all()
lazy_loading_time = (time.time() - start_time) * 1000
print("Lazy Loading Zeit:", lazy_loading_time, " ms")

# Eager Loading Zeit messen
start_time = time.time()
eager_authors = session.query(Author).options(joinedload(Author.books)).all()
eager_loading_time = (time.time() - start_time) * 1000
print("Eager Loading Zeit:", eager_loading_time, " ms")

# Session schließen
session.close()

Lazy Loading Zeit: 1.1391639709472656  ms
Eager Loading Zeit: 2.4099349975585938  ms
</code></pre>
</details>