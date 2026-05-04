# Fortgeschrittene ORM- Konzepte

Bisher haben wir SQLAlchemy verwendet, um einfache Datenbankoperationen durchzuführen. In realen Anwendungen werden wir jedoch schnell komplexere Abfragen erstellen, beispielsweise um unsere Datenbank zu durchsuchen. Abfreagen aus der Datenbank werden häufig auch als queries bezeichnet. Im folgenden werden wir uns einigen queries in SQLAlchemy widmen, die es uns ermöglichen, komplexe Abfragen zu erstellen.

## Erstellen von Abfragen mit SQLAlchemy

[10 min]

Eine Abfrage wird in SQLAlchemy mit der `query()`-Methode erstellt. als Attribut geben wir der Methode die zu abfragende Tabelle an. Die `query()`-Methode gibt ein `Query`-Objekt zurück, das die Abfrage repräsentiert. Das `Query`-Objekt kann dann verwendet werden, um die Abfrage zu verfeinern und die Ergebnisse abzurufen.

```python
result = session.query(MyModel).all()
```

Hierbei ist `MyModel` ein SQLAlchemy-Modell, das eine Datenbanktabelle repräsentiert. Die `all()`-Methode gibt alle Datensätze in der Tabelle zurück. Wir können auch andere Methoden verwenden, um die Abfrage zu verfeinern und die Ergebnisse zu filtern, zu sortieren oder zu aggregieren.

### Aufgabe:🌶️️

[10min]

Suche in der SQLAlchemy-Dokumentation nach weiteren Methoden, um die Datensätze eines `Query`-Objektes zurückzugeben.

Neben dem Abfragen einer ganzen Tabelle können wir auch nur bestimmte Spalten abfragen. Dies wird erreicht, indem wir die gewünschten Spalten als Argumente an die `query()`-Methode übergeben.

<details>
<summary>Lösung</summary>

<pre><code>
result = session.query(MyModel.column1, MyModel.column2).all()
</code></pre>
</details>

## Arbeiten mit Filtern, Sortierung und Aggregation

[15 min]

- **Filtern**: Wir können Abfragen mit Bedingungen filtern, um nur Datensätze abzurufen, die bestimmten Kriterien entsprechen.

```python
result = session.query(MyModel).filter(MyModel.column == 'wert').all()
```

  Es ist auch möglich, mehrere Filterbedingungen zu kombinieren.

- **Sortierung**: SQLAlchemy ermöglicht es uns, die Ergebnisse einer Abfrage zu sortieren.

```python
result = session.query(MyModel).order_by(MyModel.column).all()
```

- **Aggregation**: SQLAlchemy bietet Funktionen zur Durchführung von Aggregationsoperationen wie `count`, `sum`, `avg`, etc.

```python
result = session.query(func.count(MyModel.column)).all()
```

Hierbei ist `func` ein Modul in SQLAlchemy, das SQL-Funktionen wie `count` bereitstellt.

## Definition und Verwendung von Beziehungen zwischen Tabellen

[15 min]

Aus der Einführung in SQL wissen wir bereits, dass Beziehungen bzw. Relationen ein Zentrales Konzept relationaler Datenbanken sind. SQLAlchemy ermöglicht es uns, Beziehungen zwischen Tabellen auf einfache und Pythonische Weise zu definieren und zu nutzen.

- **Definition einer Beziehung**: Eine Beziehung wird in SQLAlchemy mit der `relationship`-Funktion definiert.

```python
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import ForeignKey, Column, Integer

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
```

In diesem Beispiel hat ein `Parent` mehrere `Children`. Die `relationship`-Funktion erstellt eine Verbindung zwischen `Parent` und `Child`.

- **Verwenden von Beziehungen in Abfragen**: Sobald eine Beziehung definiert ist, können wir diese in unseren Abfragen verwenden.

```python
result = session.query(Parent).join(Child).filter(Child.column == 'wert').all()
```

  Dies ermöglicht das effiziente Abfragen von Daten über Tabellengrenzen hinweg unter Ausnutzung der relationalen Struktur Ihrer Datenbank.

## Komplex Aufgaben

### Übungsaufgabe: Abfragen und Beziehungen in SQLAlchemy 🌶️️🌶️️🌶️️

[60 min]

1.Definiere zwei Modelle: `Author` und `Book`. `Author` soll die Felder `id` und `name` haben, `Book` die Felder `id`, `title`, `published_year` und `author_id`.

<details>
<summary>Lösung</summary>
<pre><code>
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    published_year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
</code></pre>
</details>

<br />

2.Füge eine Beziehung zwischen `Author` und `Book` hinzu, sodass ein Autor mehrere Bücher haben kann.

<details>
<summary>Lösung</summary>
<pre><code>
class Author(Base):
    __tablename__ = 'authors'
    books = relationship("Book", backref="author")
</code></pre>
</details>

<br />

3.Erstelle mehrere Autoren und Bücher. Stelle  sicher, dass die Bücher Autoren zugewiesen sind.

<details>
<summary>Lösung</summary>
<pre><code>
author1 = Author(name="Autor 1")
author2 = Author(name="Autor 2")
book1 = Book(title="Buch 1", published_year=1995, author=author1)
book2 = Book(title="Buch 2", published_year=1999, author=author1)
book3 = Book(title="Buch 3", published_year=2001, author=author2)
session.add_all([author1, author2, book1, book2, book3])
session.commit()
</code></pre>
</details>

<br />

4.Schreibe eine Abfrage, um alle Bücher eines bestimmten Autors abzurufen.

<details>
<summary>Lösung</summary>
<pre><code>
books_by_author1 = session.query(Book).filter(Book.author == author1).all()
</code></pre>
</details>

<br />

5.Schreibe eine Abfrage, um alle Bücher zu finden, die zwischen 1990 und 2000 veröffentlicht wurden.

<details>
<summary>Lösung</summary>
<pre><code>
books_1990s = session.query(Book).filter(Book.published_year.between(1990, 2000)).all()
</code></pre>
</details>

<br />

6.Schreibe eine Abfrage, um alle Bücher eines Autors, sortiert nach ihrem Veröffentlichungsjahr, abzurufen.

<details>
<summary>Lösung</summary>
<pre><code>
sorted_books = session.query(Book).filter(Book.author == author1).order_by(Book.published_year).all()
</code></pre>
</details>

<br />

7.**Bonus**: Implementiere eine Aggregationsabfrage, um die Anzahl der Bücher zu zählen, die jeder Autor geschrieben hat.

<details>
<summary>Lösung</summary>
<pre><code>
author_book_counts = session.query(
    Author.name, 
    func.count(Book.id)
).join(Book).group_by(Author.id).all()
</code></pre>
</details>

#### Gesamte Lösung

<details>
<summary>Lösung</summary>

<pre><code>
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func

# Definieren der Basis
Base = declarative_base()

# Definition des Author-Modells
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", backref="author")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

# Definition des Book-Modells
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    published_year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', published_year={self.published_year}, author_id={self.author_id})>"

# Erstellen einer SQLite-Datenbank
engine = create_engine('sqlite:///db/library.db')
Base.metadata.create_all(engine)

# Erstellen einer Session
Session = sessionmaker(bind=engine)
session = Session()

# Füllen der Datenbank
# Autoren hinzufügen
author1 = Author(name="Autor 1")
author2 = Author(name="Autor 2")

# Bücher hinzufügen
book1 = Book(title="Buch 1", published_year=1995, author=author1)
book2 = Book(title="Buch 2", published_year=1999, author=author1)
book3 = Book(title="Buch 3", published_year=2001, author=author2)

session.add_all([author1, author2, book1, book2, book3])
session.commit()

# Abfragen der Datenbank
# Abfrage von Büchern eines bestimmten Autors
books_by_author1 = session.query(Book).filter(Book.author == author1).all()
print("Bücher von Autor 1:", books_by_author1)

# Abfrage nach Büchern innerhalb eines bestimmten Zeitraums
books_1990s = session.query(Book).filter(Book.published_year.between(1990, 2000)).all()
print("Bücher veröffentlicht zwischen 1990 und 2000:", books_1990s)

# Sortieren von Büchern nach Veröffentlichungsjahr
sorted_books = session.query(Book).filter(Book.author == author1).order_by(Book.published_year).all()
print("Sortierte Bücher von Autor 1:", sorted_books)

# Bonus: Aggregationsabfrage
author_book_counts = session.query(
    Author.name, 
    func.count(Book.id)
).join(Book).group_by(Author.id).all()
print("Anzahl der Bücher pro Autor:", author_book_counts)

# Schließen der Session
session.close()
</code></pre>

<pre><code>
Bücher von Autor 1: [<Book(id=1, title='Buch 1', published_year=1995, author_id=1)>, <Book(id=2, title='Buch 2', published_year=1999, author_id=1)>]
Bücher veröffentlicht zwischen 1990 und 2000: [<Book(id=1, title='Buch 1', published_year=1995, author_id=1)>, <Book(id=2, title='Buch 2', published_year=1999, author_id=1)>]
Sortierte Bücher von Autor 1: [<Book(id=1, title='Buch 1', published_year=1995, author_id=1)>, <Book(id=2, title='Buch 2', published_year=1999, author_id=1)>]
Anzahl der Bücher pro Autor: [('Autor 1', 2), ('Autor 2', 1)]
</code></pre>

</details>

### Übungsaufgabe: Komplexe Abfragen und Joins in SQLAlchemy 🌶️️🌶️️🌶️️

[60 min]

### Aufgabenstellung

1.**Modelldefinitionen**:

- Definiere drei Modelle: `Department`, `Employee` und `Project`.
- `Department` sollte Felder für `id` und `name` haben.
- `Employee` sollte Felder für `id`, `name`, `department_id` (Fremdschlüssel zu `Department`) und `manager_id` (selbstreferenzierender Fremdschlüssel) haben.
- `Project` sollte Felder für `id`, `name` und `department_id` haben.

<details>
<summary>Lösung</summary>
<pre><code>
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", backref="department")

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('department.id'))
    manager_id = Column(Integer, ForeignKey('employee.id'))
    manager = relationship("Employee", remote_side=[id])

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String)
</code></pre>
</details>

<br />

2.**Erstelle Beziehungen**:

- Zwischen `Department` und `Employee` (One-to-Many).
- Zwischen `Employee` und `Project` über eine Assoziationstabelle (Many-to-Many).

<details>
<summary>Lösung</summary>
<pre><code>
# Definiere die Many-to-Many-Beziehung zwischen Employee und Project
employee_project_table = Table('employee_project', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employee.id')),
    Column('project_id', Integer, ForeignKey('project.id'))
)
Employee.projects = relationship("Project", secondary=employee_project_table, backref="employees")
</code></pre>
</details>

<br />

3.**Datenbank befüllen**:

- Erstelle einige Beispieldatensätze für jedes Modell.

<details>
<summary>Lösung</summary>
<pre><code>
# Erstellen von Abteilungen
dept1 = Department(name="Entwicklung")
dept2 = Department(name="Marketing")

# Erstellen von Mitarbeitern
emp1 = Employee(name="Alice", department=dept1)
emp2 = Employee(name="Bob", department=dept1, manager=emp1)
emp3 = Employee(name="Charlie", department=dept2, manager=emp2)

# Erstellen von Projekten
proj1 = Project(name="Projekt Alpha")
proj2 = Project(name="Projekt Beta")

# Zuweisung von Projekten zu Mitarbeitern
emp1.projects.append(proj1)
emp2.projects.append(proj2)
emp3.projects.append(proj1)
emp3.projects.append(proj2)

# Daten zur Session hinzufügen und commiten
session.add_all([dept1, dept2, emp1, emp2, emp3, proj1, proj2])
session.commit()
</code></pre>
</details>

<br />

4.**Komplexe Abfragen**:

- Schreibe eine Abfrage, um alle Mitarbeiter eines bestimmten Departments anzuzeigen.
- Schreibe eine Abfrage, um alle Projekte zu finden, an denen ein bestimmter Mitarbeiter arbeitet.
- Schreibe eine Abfrage, um den Manager jedes Mitarbeiters (falls vorhanden) zu finden.

<details>
<summary>Lösung für alle Mitarbeiter eines bestimmten Departments anzeigen</summary>
<pre><code>
employees_in_dept = session.query(Employee).filter(Employee.department == dept1).all()
</code></pre>
</details>
<details>
<summary>Lösung für alle Projekte, an denen ein bestimmter Mitarbeiter arbeitet</summary>
<pre><code>
projects_of_emp = session.query(Project).join(employee_project_table).join(Employee).filter(Employee.id == emp1.id).all()
</code></pre>
</details>
<details>
<summary>Lösung für den Manager jedes Mitarbeiters finden</summary>
<pre><code>
employee_managers = session.query(Employee.name, Employee.manager.has()).all()
</code></pre>
</details>

#### Gesamte Lösung

<details>
<summary>Lösung</summary>
<pre><code>
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# Assoziationstabelle für die Many-to-Many-Beziehung zwischen Employee und Project
employee_project_table = Table('employee_project', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employee.id')),
    Column('project_id', Integer, ForeignKey('project.id'))
)

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", backref="department")

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('department.id'))
    manager_id = Column(Integer, ForeignKey('employee.id'))
    manager = relationship("Employee", remote_side=[id])
    projects = relationship("Project", secondary=employee_project_table, backref="employees")

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', department_id={self.department_id}, manager_id={self.manager_id})>"

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}')>"

# Verbindung zur Datenbank herstellen
engine = create_engine('sqlite:///db/company.db')
Base.metadata.create_all(engine)

# Erstellen einer Session
Session = sessionmaker(bind=engine)
session = Session()

# Erstellen von Abteilungen
dept1 = Department(name="Entwicklung")
dept2 = Department(name="Marketing")

# Erstellen von Mitarbeitern
emp1 = Employee(name="Alice", department=dept1)
emp2 = Employee(name="Bob", department=dept1, manager=emp1)
emp3 = Employee(name="Charlie", department=dept2, manager=emp2)

# Erstellen von Projekten
proj1 = Project(name="Projekt Alpha")
proj2 = Project(name="Projekt Beta")

# Zuweisung von Projekten zu Mitarbeitern
emp1.projects.append(proj1)
emp2.projects.append(proj2)
emp3.projects.append(proj1)
emp3.projects.append(proj2)

# Daten zur Session hinzufügen und commiten
session.add_all([dept1, dept2, emp1, emp2, emp3, proj1, proj2])
session.commit()

# Abfrage aller Mitarbeiter eines bestimmten Departments
employees_in_dept = session.query(Employee).filter(Employee.department == dept1).all()
print("Mitarbeiter in der Entwicklungsabteilung:", employees_in_dept)

# Abfrage aller Projekte, an denen ein bestimmter Mitarbeiter arbeitet
projects_of_emp = session.query(Project).join(employee_project_table).join(Employee).filter(Employee.id == emp1.id).all()
print("Projekte von Alice:", projects_of_emp)
</code></pre>

<pre><code>
Mitarbeiter in der Entwicklungsabteilung: [<Employee(id=1, name='Alice', department_id=1, manager_id=None)>, <Employee(id=2, name='Bob', department_id=1, manager_id=1)>]
Projekte von Alice: [<Project(id=1, name='Projekt Alpha')>]
</code></pre>
</details>

## Transaktionen und Sitzungsmanagement
[10 min]

In SQLAlchemy spielt das Konzept von Transaktionen und Sitzungen (Sessions) eine zentrale Rolle. Eine Session in SQLAlchemy dient als Zwischenpuffer zwischen dem Objektmodell (Ihren Python-Klassen) und der Datenbank.

### Grundlagen der Sitzungsverwaltung

- **Erstellen einer Session**: Eine Session wird in SQLAlchemy mit der `sessionmaker`-Funktion erstellt. Sie ist der Startpunkt für alle Operationen mit der Datenbank.

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

- **Verwenden einer Session**: Über die Session interagieren wir mit der Datenbank. Wir können Objekte hinzufügen, aktualisieren, abfragen und löschen.

```python
new_object = MyModel(name='Beispiel')
session.add(new_object)
session.commit()
```

- **Schließen einer Session**: Es ist wichtig, eine Session zu schließen, um Ressourcen freizugeben und die Verbindung zur Datenbank ordnungsgemäß zu beenden.

```python
session.close()
```

### Transaktionsmanagement

[10 min]

Jede Session in SQLAlchemy ist an eine Transaktion gebunden. Eine Transaktion umfasst eine Sequenz von Operationen, die als eine Einheit behandelt werden.

- **Commit einer Transaktion**: Mit `session.commit()` werden alle Änderungen, die in der Session gemacht wurden, in die Datenbank übernommen.

```python
session.commit()
```

- **Zurückrollen einer Transaktion**: Wenn während einer Transaktion ein Fehler auftritt, können Sie die Transaktion mit `session.rollback()` zurückrollen.

```python
try:
    session.add(new_object)
    session.commit()
except:
    session.rollback()
    raise
```

## Verständnis des Unit-of-Work-Musters

[10 min]

Das Unit-of-Work-Muster ist ein Entwurfsmuster, das sicherstellt, dass alle Änderungen an den Objekten in einer Transaktion entweder komplett in die Datenbank übernommen oder komplett verworfen werden. In SQLAlchemy wird dies durch die Session-Implementierung erreicht.

- **Unit of Work**: Eine Session in SQLAlchemy repräsentiert ein "Unit of Work". Sie hält eine Liste aller Objekte fest, die geändert wurden (neu hinzugefügt, modifiziert, gelöscht).
- **Automatisches Tracking von Änderungen**: SQLAlchemy trackt automatisch Änderungen an Objekten, die zur Session hinzugefügt wurden. Dies umfasst das Verfolgen von Änderungen an Feldwerten, das Hinzufügen oder Löschen von Objekten usw.
- **Commit des Unit of Work**: Beim Commit einer Session werden alle gesammelten Änderungen in einer einzigen Transaktion an die Datenbank übermittelt.

Das Verständnis von Sitzungen und Transaktionen sowie des Unit-of-Work-Musters ist entscheidend für die effektive Nutzung von SQLAlchemy. Es ermöglicht uns, Änderungen an den Daten auf konsistente und kontrollierte Weise zu verwalten. Durch die Verwendung von Sessions können wir sicherstellen, dass unsere Datenbankoperationen atomar, konsistent, isoliert und dauerhaft (ACID-Eigenschaften) sind.

## Komplex Aufgaben (Transaktionen)

### Übungsaufgabe: Transaktionen und Sitzungsmanagement in SQLAlchemy 🌶️️🌶️️🌶️️

[60 min]

1.**Modell- und Datenbanksetup**:

- Definiere ein einfaches Modell `Person` mit den Feldern `id` (Primärschlüssel) und `name`.
- Erstelle eine SQLite-Datenbank und füge einige Einträge in die `Person`-Tabelle ein.

<details>
<summary>Lösung</summary>
<pre><code>
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Hinzufügen einiger Personen
session.add_all([Person(name="Alice"), Person(name="Bob")])
session.commit()
</code></pre>
</details>

<br />

2.**Transaktionsmanagement**:

- Schreibe eine Funktion `add_person`, die eine neue `Person` hinzufügt. Nutze Transaktionsmanagement, um  sicherzustellen, dass Änderungen nur bei Erfolg commitet werden.
- Simuliere innerhalb der Funktion einen Fehler (z.B. durch Einfügen eines Duplikats) und stelle sicher, dass die Transaktion zurückgerollt wird.

<details>
<summary>Lösung</summary>
<pre><code>
def add_person(name):
    try:
        # Überprüfen, ob der Name bereits existiert
        existing_person = session.query(Person).filter_by(name=name).first()
        if existing_person:
            raise ValueError(f"Eine Person mit dem Namen '{name}' existiert bereits.")

        new_person = Person(name=name)
        session.add(new_person)
        session.commit()
        print(f"Person '{name}' erfolgreich hinzugefügt.")
    except Exception as e:
        session.rollback()
        print(f"Fehler: {e}")

# Test der Funktion
add_person("Charlie")
add_person("Alice")  # Dies sollte einen Fehler verursachen, da 'Alice' bereits existiert
</code></pre>
</details>

<br />

3.**Abfrage und Änderung von Daten**:

- Führe eine Abfrage aus, um alle Personen in der Datenbank zu finden.
- Ändere den Namen einer Person und committe die Änderung.

<details>
<summary>Lösung für Abfrage aller Personen</summary>
<pre><code>
people = session.query(Person).all()
for person in people:
    print(f"ID: {person.id}, Name: {person.name}")
</code></pre>
</details>
<details>
<summary>Lösung für Ändern des Namens einer Person</summary>
<pre><code>
person_to_update = session.query(Person).filter_by(name="Bob").first()
if person_to_update:
    person_to_update.name = "Robert"
    session.commit()

# Erneute Abfrage, um die Änderung zu bestätigen
people = session.query(Person).all()
for person in people:
    print(f"ID: {person.id}, Name: {person.name}")
</code></pre>
</details>

<br />

#### Gesamte Lösung

<details>
<summary>Lösung</summary>
<pre><code>
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Hinzufügen einiger Personen
session.add_all([Person(name="Alice"), Person(name="Bob")])
session.commit()

def add_person(name):
    try:
        # Überprüfen, ob der Name bereits existiert
        existing_person = session.query(Person).filter_by(name=name).first()
        if existing_person:
            raise ValueError(f"Eine Person mit dem Namen '{name}' existiert bereits.")

        new_person = Person(name=name)
        session.add(new_person)
        session.commit()
        print(f"Person '{name}' erfolgreich hinzugefügt.")
    except Exception as e:
        session.rollback()
        print(f"Fehler: {e}")

# Test der Funktion
add_person("Charlie")
add_person("Alice")  # Dies sollte einen Fehler verursachen, da 'Alice' bereits existiert


# Abfrage aller Personen
people = session.query(Person).all()
for person in people:
    print(f"ID: {person.id}, Name: {person.name}")

# Ändern des Namens einer Person
person_to_update = session.query(Person).filter_by(name="Bob").first()
if person_to_update:
    person_to_update.name = "Robert"
    session.commit()

# Erneute Abfrage, um die Änderung zu bestätigen
people = session.query(Person).all()
for person in people:
    print(f"ID: {person.id}, Name: {person.name}")

# Schließen der Session
session.close()
</code></pre>

<pre><code>
Fehler: Eine Person mit dem Namen 'Charlie' existiert bereits.
Fehler: Eine Person mit dem Namen 'Alice' existiert bereits.
ID: 1, Name: Alice
ID: 2, Name: Robert
ID: 3, Name: Charlie
ID: 4, Name: Alice
ID: 5, Name: Alice
ID: 6, Name: Robert
ID: 7, Name: Charlie
ID: 8, Name: Alice
ID: 9, Name: Alice
ID: 10, Name: Bob
ID: 11, Name: Charlie
ID: 12, Name: Alice
ID: 13, Name: Alice
ID: 14, Name: Bob
ID: 1, Name: Alice
ID: 2, Name: Robert
ID: 3, Name: Charlie
ID: 4, Name: Alice
ID: 5, Name: Alice
ID: 6, Name: Robert
ID: 7, Name: Charlie
ID: 8, Name: Alice
ID: 9, Name: Alice
ID: 10, Name: Robert
ID: 11, Name: Charlie
ID: 12, Name: Alice
ID: 13, Name: Alice
ID: 14, Name: Bob
</code></pre>
