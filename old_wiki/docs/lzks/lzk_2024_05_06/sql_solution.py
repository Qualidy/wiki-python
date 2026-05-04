import sqlite3
from unittest import main, TestCase

DATABASE_URL = "datenbank.sqLite"

# 🟥AUFGABE: Fülle alle Funktionen mit einem passenden SQL-Statement.🟥


def execute_sql(query, params, database_url=DATABASE_URL):
    cursor = sqlite3.connect(database_url).cursor()
    cursor.execute(query, params)
    return cursor.fetchall()


def count_teachers() -> str:
    """⭐Gibt den SQL-Ausdruck zurück, die Anzahl der Lehrkräfte zu erhalten."""
    return "SELECT COUNT(*) FROM lehrkraft"


class TestCountTeachers(TestCase):
    def test_count_teachers_0(self):
        count_teacher = execute_sql(count_teachers(), [])
        self.assertEqual(count_teacher[0][0], 20)


def size_of_class() -> str:
    """⭐⭐Gibt den SQL-Ausdruck zurück, um die Anzahl der Schüler in einer Klasse zu erhalten."""
    return "select count(*) from schuelerin join klasse on klasse.id = schuelerin.klasse_id where klasse.name = ?"


class TestSizeOfClass(TestCase):
    def test_count_teachers_0(self):
        size_class = execute_sql(size_of_class(), ['6a'])
        self.assertEqual(size_class[0][0], 27)

    def test_count_teachers_1(self):
        size_class = execute_sql(size_of_class(), ['8b'])
        self.assertEqual(size_class[0][0], 24)

    def test_count_teachers_not_existing(self):
        size_class = execute_sql(size_of_class(), ['14a'])
        self.assertEqual(size_class[0][0], 0)


def exams_in_timeframe():
    """⭐⭐Gibt den SQL-Ausdruck zurück, um die Anzahl Prüfungen in einem Zeitfenster zu erhalten.
    Beide Zeitpunkte sind inklusive. Es sollen nur Prüfungen vom Typ 'Ex' betrachtet werden."""
    return """select count(*) from pruefung WHERE ? <= datum and datum <= ? and typ = 'Ex'"""


class TestExamsInTimeframe(TestCase):
    def test_exams_in_timeframe_0(self):
        exam_count = execute_sql(exams_in_timeframe(), ['2022-11-03', '2022-11-05'])
        self.assertEqual(exam_count[0][0], 3)

    def test_exams_in_timeframe_1(self):
        exam_count = execute_sql(exams_in_timeframe(), ['2022-11-11', '2022-12-05'])
        self.assertEqual(exam_count[0][0], 43)

    def test_exams_in_timeframe_invalid_window(self):
        exam_count = execute_sql(exams_in_timeframe(), ['2022-11-05', '2022-11-03'])
        self.assertEqual(exam_count[0][0], 0)


def all_klassensprecher():
    """⭐Gibt den SQL-Ausdruck zurück, um die Ruf- und Familiennamen aller Klassensprecher zu finden."""
    return """select rufname, familienname from schuelerin where ist_klassensprecher = 1"""


class TestAllKlassensprecher(TestCase):
    def test_all_klassensprecher_0(self):
        klassensprecher = execute_sql(all_klassensprecher(), [])
        self.assertEqual(len(klassensprecher), 12)

    def test_all_klassensprecher_1(self):
        klassensprecher = execute_sql(all_klassensprecher(), [])
        self.assertCountEqual(klassensprecher,
                              [('Hannah', 'Rivera'), ('Jessica', 'Moore'), ('Zachary', 'Pearson'), ('Kimberly', 'Vega'),
                               ('Jeffrey', 'Mcmillan'), ('Casey', 'Campbell'), ('Elizabeth', 'Singleton'),
                               ('Paul', 'Mueller'), ('Donald', 'Hunter'), ('Jeanne', 'Moss'), ('Teresa', 'James'),
                               ('Lauren', 'Wells')])


def all_klassensprecher_sorted():
    """⭐⭐Gibt den SQL-Ausdruck zurück, um die Ruf- und Familiennamen und Klasse aller Klassensprecher zu finden.
    Die Rückgabe soll aufsteigend absteigend nach dem Familiennamen der Klasse sein."""
    return """select rufname, familienname, name from schuelerin
    join klasse on klasse.id = klasse_id where ist_klassensprecher = 1 
    order by familienname desc"""


class TestAllKlassensprecherSorted(TestCase):
    def test_all_klassensprecher_0(self):
        klassensprecher = execute_sql(all_klassensprecher_sorted(), [])
        self.assertEqual(len(klassensprecher), 12)

    def test_all_klassensprecher_1(self):
        klassensprecher = execute_sql(all_klassensprecher_sorted(), [])
        self.assertCountEqual(klassensprecher,
                              [('Lauren', 'Wells', '10b'), ('Kimberly', 'Vega', '6b'), ('Elizabeth', 'Singleton', '8a'),
                               ('Hannah', 'Rivera', '5a'), ('Zachary', 'Pearson', '6a'), ('Paul', 'Mueller', '8b'),
                               ('Jeanne', 'Moss', '9b'), ('Jessica', 'Moore', '5b'), ('Jeffrey', 'Mcmillan', '7a'),
                               ('Teresa', 'James', '10a'), ('Donald', 'Hunter', '9a'), ('Casey', 'Campbell', '7b')])


def youngest_student():
    """⭐⭐⭐Gibt den SQL-Ausdruck zurück, um Ruf- und Familiennamen des jüngsten Schülers einer
    Klasse zu erhalten."""
    return """select rufname, familienname 
    from schuelerin 
    where geburtsdatum = 
        (select min(geburtsdatum)
        from schuelerin 
        join klasse on klasse.id = schuelerin.klasse_id
        where klasse.name = ?)"""


class TestYoungestStudent(TestCase):
    def test_youngest_student_0(self):
        youngest = execute_sql(youngest_student(), ['6a'])
        self.assertCountEqual(youngest, [('John', 'Walker')])

    def test_youngest_student_1(self):
        youngest = execute_sql(youngest_student(), ['7a'])
        self.assertCountEqual(youngest, [('Heather', 'Calderon')])

    def test_youngest_student_invalid_class(self):
        youngest = execute_sql(youngest_student(), ['14f'])
        self.assertCountEqual(youngest, [])


def average_value():
    """⭐⭐Gibt den SQL-Ausdruck zurück, um die Durchschnittsnote einer Prüfung zu erhalten.
    Übergeben wird die ID einer Prüfung."""
    return """select avg(wert) from note where pruefung_id = ?"""


class TestAverageValue(TestCase):
    def test_average_value_0(self):
        avg_value = execute_sql(average_value(), [1])
        self.assertAlmostEqual(avg_value[0][0], 2.8333333333335)

    def test_average_value_1(self):
        avg_value = execute_sql(average_value(), [3])
        self.assertAlmostEqual(avg_value[0][0], 3.037037037037037)


if __name__ == '__main__':
    main()
