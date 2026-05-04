from unittest import main, TestCase

from sqlalchemy import create_engine,func,and_,desc
from sqlalchemy.orm import sessionmaker

from school_model import *

engine = create_engine('sqlite:///datenbank.sqLite')

Session = sessionmaker(bind=engine)
session = Session()

# 🟥AUFGABE: Fülle alle Funktionen mit einem passenden sqlalchemy-Querries.🟥


def count_teachers_sqlalchemy():
    """⭐Gibt die Anzahl der Lehrkräfte zurück, implementiert mit SQLAlchemy."""
    return session.query(Lehrkraft).count()

class TestCountTeachersSqlalchemy(TestCase):
    def test_count_teachers(self):
        self.assertEqual(count_teachers_sqlalchemy(), 20)


def size_of_class_sqlalchemy(class_name):
    """⭐⭐Gibt die Anzahl der Schüler in einer Klasse zurück."""
    return session.query(func.count(Schuelerin.id)) \
      .join(Klasse, Schuelerin.klasse_id == Klasse.id) \
      .filter(Klasse.name == class_name) \
      .order_by(Klasse.name) \
      .scalar()

class TestSizeOfClassSqlalchemy(TestCase):
    def test_size_of_class_0(self):
        self.assertEqual(size_of_class_sqlalchemy('6a'), 27)

    def test_size_of_class_1(self):
        self.assertEqual(size_of_class_sqlalchemy('8b'), 24)

    def test_size_of_class_2(self):
        self.assertEqual(size_of_class_sqlalchemy('14a'), 0)


def exams_in_timeframe_sqlalchemy(start_date, end_date):
    """⭐⭐Gibt die Anzahl der Prüfungen in einem Zeitfenster zurück.
    Beide Zeitpunkte sind inklusive. Es sollen nur Prüfungen vom Typ 'Ex' betrachtet werden."""
    return session.query(Pruefung).filter(
        and_(
            Pruefung.datum >= start_date,
            Pruefung.datum <= end_date,
            Pruefung.typ == 'Ex'
            )
        ).count()

class TestExamsInTimeframeSqlalchemy(TestCase):
    def test_exams_in_timeframe_0(self):
        self.assertEqual(exams_in_timeframe_sqlalchemy('2022-11-03', '2022-11-05'), 3)

    def test_exams_in_timeframe_1(self):
        self.assertEqual(exams_in_timeframe_sqlalchemy('2022-11-11', '2022-12-05'), 43)

    def test_exams_in_timeframe_2(self):
        self.assertEqual(exams_in_timeframe_sqlalchemy('2022-11-05', '2022-11-03'), 0)


def all_klassensprecher_sqlalchemy():
    """⭐Gibt die Ruf- und Familiennamen aller Klassensprecher zurück."""
    return session.query(Schuelerin).filter(Schuelerin.ist_klassensprecher=='1').all()

class TestAllKlassensprecherSqlalchemy(TestCase):
    def test_all_klassensprecher_0(self):
        klassensprecher = all_klassensprecher_sqlalchemy()
        self.assertEqual(len(klassensprecher), 12)

    def test_all_klassensprecher_1(self):
        klassensprecher = all_klassensprecher_sqlalchemy()
        self.assertCountEqual(klassensprecher,
                              [('Hannah', 'Rivera'), ('Jessica', 'Moore'), ('Zachary', 'Pearson'), ('Kimberly', 'Vega'),
                               ('Jeffrey', 'Mcmillan'), ('Casey', 'Campbell'), ('Elizabeth', 'Singleton'),
                               ('Paul', 'Mueller'), ('Donald', 'Hunter'), ('Jeanne', 'Moss'), ('Teresa', 'James'),
                               ('Lauren', 'Wells')])


def all_klassensprecher_sorted_sqlalchemy():
    """⭐⭐Gibt die Ruf- und Familiennamen sowie die Klasse aller Klassensprecher zurück,
    sortiert absteigend nach dem Familiennamen."""

    return ...


class TestAllKlassensprecherSortedSqlalchemy(TestCase):
    def test_all_klassensprecher_0(self):
        klassensprecher = all_klassensprecher_sorted_sqlalchemy()
        self.assertEqual(len(klassensprecher), 12)

    def test_all_klassensprecher_1(self):
        klassensprecher = all_klassensprecher_sorted_sqlalchemy()
        self.assertEqual(klassensprecher,
                         [('Lauren', 'Wells', '10b'), ('Kimberly', 'Vega', '6b'), ('Elizabeth', 'Singleton', '8a'),
                          ('Hannah', 'Rivera', '5a'), ('Zachary', 'Pearson', '6a'), ('Paul', 'Mueller', '8b'),
                          ('Jeanne', 'Moss', '9b'), ('Jessica', 'Moore', '5b'), ('Jeffrey', 'Mcmillan', '7a'),
                          ('Teresa', 'James', '10a'), ('Donald', 'Hunter', '9a'), ('Casey', 'Campbell', '7b')])


def youngest_student_sqlalchemy(class_name):
    """⭐⭐⭐Gibt den Ruf- und Familiennamen des jüngsten Schülers einer Klasse zurück."""
    return session.query(Schuelerin.rufname,Schuelerin.familienname).filter_by(klasse=class_name).order_by(desc(Schuelerin.geburtsdatum)).first()


class TestYoungestStudentSqlalchemy(TestCase):
    def test_youngest_student_0(self):
        self.assertCountEqual(youngest_student_sqlalchemy('6a'), [('John', 'Walker')])

    def test_youngest_student_1(self):
        self.assertCountEqual(youngest_student_sqlalchemy('7a'), [('Heather', 'Calderon')])

    def test_youngest_student_2(self):
        self.assertCountEqual(youngest_student_sqlalchemy('14f'), [])


def average_value_sqlalchemy(exam_id):
    """⭐⭐⭐Gibt die Durchschnitsnote einer Prüfung zurück"""
    return ...


class TestAverageValueSqlalchemy(TestCase):
    def test_average_value_0(self):
        self.assertAlmostEqual(average_value_sqlalchemy(1), 2.8333333333335)

    def test_average_value_1(self):
        self.assertAlmostEqual(average_value_sqlalchemy(3), 3.037037037037037)


if __name__ == '__main__':
    main()
