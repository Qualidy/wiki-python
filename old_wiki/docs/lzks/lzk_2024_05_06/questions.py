import sqlite3
from unittest import main, TestCase

DATABASE_URL = "datenbank.sqLite"


def execute_sql(query, params, database_url=DATABASE_URL):
    cursor = sqlite3.connect(database_url).cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

def count_teachers_dql() -> str:
    """⭐Gibt den SQL-Ausdruck zurück, die Anzahl der Lehrkräfte zu erhalten."""
    return "SELECT COUNT(*) FROM lehrkraft"


class TestCountTeachers(TestCase):
    def test_count_teachers_0(self):
        count_teacher = execute_sql(count_teachers_dql(), [])
        self.assertEqual(count_teacher[0][0], 20)

def class_sizes_dql() -> str:
    """Gibt den SQL-Ausdruck zurück, um für einen Klassennamen die Größe der Klasse zu erhalten."""
    return "SELECT COUNT(*) FROM schuelerin JOIN klasse ON schuelerin.klasse_id = klasse.id WHERE klasse.name = ?"


class TestClassSizesDql(TestCase):
    def test_class_sizes_0(self):
        anzahl_schueler = execute_sql(class_sizes_dql(), ["7a"])
        self.assertEqual(anzahl_schueler[0][0], 28)

    def test_class_sizes_2(self):
        anzahl_schueler = execute_sql(class_sizes_dql(), ["5b"])
        self.assertEqual(anzahl_schueler[0][0], 21)

    def test_class_sizes_3(self):
        anzahl_schueler = execute_sql(class_sizes_dql(), ["6c"])
        self.assertEqual(anzahl_schueler[0][0], 0)


def list_of_names_dql():
    """⭐Gibt den SQL-Ausdruck zurück, um für eine Namensliste (Rufname und Familienname)
    aller Schüler einer Klasse zu erhalten."""
    return """select rufname, familienname
        from schuelerin, klasse
        where schuelerin.klasse_id = klasse.id and klasse.name = ?
        """


class TestListOfNamesDql(TestCase):
    def test_class_sizes_0(self):
        list_of_names = execute_sql(list_of_names_dql(), ["7a"])
        self.assertCountEqual(list_of_names, [
            ('Stephanie', 'Shaw'), ('Melissa', 'Walters'), ('Lydia', 'Meredith'), ('Maria', 'Regina'),
            ('Jeremy', 'Mathis'), ('Tammy', 'Giles'), ('Matthew', 'Calderon'), ('Breanna', 'Thompson'),
            ('Michael', 'Mcdonald'), ('Austin', 'Wright'), ('Daniel', 'Curtis'), ('Michael', 'Briggs'),
            ('Kimberly', 'Russell'), ('David', 'Hudson'), ('Yolanda', 'Deleon'), ('Rebecca', 'Mejia'),
            ('Jason', 'Carpenter'), ('Jack', 'Stevens'), ('Kimberly', 'Evans'), ('Phillip', 'Chambers'),
            ('Ruth', 'Greene'), ('Jennifer', 'Bailey'), ('Jeffrey', 'Mcmillan'), ('Bradley', 'Navarro'),
            ('Cynthia', 'Salinas'), ('Bailey', 'Nguyen'), ('Heather', 'Calderon'), ('Jeffrey', 'Howell')
        ])

def list_of_names_sorted_dql():
    """⭐⭐Gibt den SQL-Ausdruck zurück, um für eine Namensliste (Rufname und Familienname)
    aller Schüler einer Klasse zu erhalten. Diese Liste ist nach dem Nachnamen aufsteigend sortiert."""
    return """select rufname, familienname
        from schuelerin, klasse
        where schuelerin.klasse_id = klasse.id and klasse.name = ?
        order by familienname ASC
        """

class TestListOfNamesSortedDql(TestCase):
    def test_class_sizes_sorted_0(self):
        list_of_names = execute_sql(list_of_names_sorted_dql(), ["7a"])
        print(list_of_names)
        self.assertListEqual(list_of_names, [
            ('Jennifer', 'Bailey'), ('Michael', 'Briggs'), ('Matthew', 'Calderon'), ('Heather', 'Calderon'),
            ('Jason', 'Carpenter'), ('Phillip', 'Chambers'), ('Daniel', 'Curtis'), ('Yolanda', 'Deleon'),
            ('Kimberly', 'Evans'), ('Tammy', 'Giles'), ('Ruth', 'Greene'), ('Jeffrey', 'Howell'),
            ('David', 'Hudson'), ('Jeremy', 'Mathis'), ('Michael', 'Mcdonald'), ('Jeffrey', 'Mcmillan'),
            ('Rebecca', 'Mejia'), ('Lydia', 'Meredith'), ('Bradley', 'Navarro'), ('Bailey', 'Nguyen'),
            ('Maria', 'Regina'), ('Kimberly', 'Russell'), ('Cynthia', 'Salinas'), ('Stephanie', 'Shaw'),
            ('Jack', 'Stevens'), ('Breanna', 'Thompson'), ('Melissa', 'Walters'), ('Austin', 'Wright')
        ])


def teachers_of_class_dql() -> str:
    """⭐⭐⭐Gibt den SQL-Ausdruck zurück, um einer Liste aller Lehrkräfte zu erhalten (Rufname, Familienname),
    die eine Klasse unterrichten."""
    return """select distinct rufname, familienname
from lehrkraft, unterrichtet, klasse
where unterrichtet.lehrkraft_id = lehrkraft.id and unterrichtet.klasse_id = klasse.id
and klasse.name = ?"""


class TestTeachersOfClass(TestCase):
    def test_count_teachers_0(self):
        teachers_of_class = execute_sql(teachers_of_class_dql(), ['6a'])
        self.assertCountEqual(teachers_of_class,
                              [('Elise', 'Byrne'), ('Nadia', 'Graham'), ('Lydia', 'Austin'),
                               ('Eliza', 'Day'), ('Albert', 'Spangler'), ('Ray', 'Mills'), ('Harvey', 'Ball')])


def teachers_of_class_with_topic_dql() -> str:
    """⭐⭐⭐Gibt den SQL-Ausdruck zurück, um einer Liste aller Lehrkräfte mit ihrem Fach zu erhalten
    (Rufname, Familienname, Fach),
    die eine Klasse unterrichten."""
    return """select rufname, familienname, fach.name
from lehrkraft, unterrichtet, klasse, fach
where unterrichtet.lehrkraft_id = lehrkraft.id and unterrichtet.klasse_id = klasse.id
and unterrichtet.fach_id = fach.id
and klasse.name = ?"""


class TestTeachersOfClass(TestCase):
    def test_count_teachers_0(self):
        teachers_of_class = execute_sql(teachers_of_class_with_topic_dql(), ['6a'])
        self.assertCountEqual(teachers_of_class,
       [('Elise', 'Byrne', 'Deutsch'), ('Nadia', 'Graham', 'Kunst'), ('Lydia', 'Austin', 'Physik'),
        ('Eliza', 'Day', 'Biologie'), ('Albert', 'Spangler', 'Mathematik'), ('Ray', 'Mills', 'Englisch'),
        ('Ray', 'Mills', 'Geographie'), ('Harvey', 'Ball', 'Sport'), ('Harvey', 'Ball', 'Geschichte')])


def score_jason_carpenter_english() -> str:
    """⭐⭐Gibt den SQL-Ausdruck zurück, um die Durchschnitsnote vom Schüler 'Jason Carpenter' im Fach 'Englisch' zu erhalten"""
    return """select avg(wert)
from schuelerin, note, fach
where
note.schueler_id = schuelerin.id and note.fach_id = fach.id
and fach.name = 'Englisch' 
and schuelerin.rufname = 'Jason' and schuelerin.familienname = 'Carpenter'
"""


class TestScoreJasonCarpenterEnglish(TestCase):
    def test_count_teachers_0(self):
        score = execute_sql(score_jason_carpenter_english(), [])
        print(score)
        self.assertEqual(score[0][0], 3.75)

def average_score() -> str:
    """⭐⭐Gibt den SQL-Ausdruck zurück, um die Durchschnittsnote eines Schülers in einem Fach zu erhalten.
    Es werden (Fach, Rufname, Familienname) übergeben."""
    return """select avg(wert)
from schuelerin, note, fach
where
note.schueler_id = schuelerin.id and note.fach_id = fach.id
and fach.name = ? 
and schuelerin.rufname = ? and schuelerin.familienname = ?
"""


class TestAverageScore(TestCase):
    def test_count_teachers_0(self):
        score = execute_sql(average_score(), ['Englisch', 'Jason', 'Carpenter'])
        print(score)
        self.assertEqual(score[0][0], 3.75)
