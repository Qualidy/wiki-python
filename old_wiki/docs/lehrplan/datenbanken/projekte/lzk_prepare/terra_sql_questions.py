import sqlite3
from unittest import TestCase, main

DATABASE_URL = "terra.sqlite"


def execute_sql(query, params, database_url=DATABASE_URL):
    """Führe eine SQL-Query aus mit den übergebenen Parametern aus."""
    cursor = sqlite3.connect(database_url).cursor()
    cursor.execute(query, params)
    return cursor.fetchall()


def find_countries_starting_with() -> str:
    """Gibt den SQL-Ausdruck zurück, um eine Liste (Land, Kontinent) von Ländern zu erhalten,
     die mit einem bestimmten Buchstaben beginnen."""
    return """..."""


class TestCountriesStartingWith(TestCase):
    def test_countries_starting_with_B(self):
        query = find_countries_starting_with()
        countries = execute_sql(query, ['B%'])
        expected = [
            ('Belgien', 'Europa'), ('Bahrein', 'Asien'), ('Barbados', 'Nordamerika'),
            ('Bangladesch', 'Asien'), ('Bahamas', 'Afrika'), ('Bulgarien', 'Europa'),
            ('Belize', 'Nordamerika'), ('Bhutan', 'Asien'), ('Bosnien-Herzegowina', 'Europa'),
            ('Bolivien', 'Südamerika'), ('Brasilien', 'Südamerika'), ('Brunei', 'Asien'),
            ('Burundi', 'Afrika'), ('Birma', 'Asien'), ('Bophuthatswana', 'Afrika'),
            ('Botswana', 'Afrika'), ('Benin', 'Afrika'), ('Burkina Faso', 'Afrika')]
        self.assertCountEqual(countries, expected)

    def test_countries_starting_with_C(self):
        query = find_countries_starting_with()
        countries = execute_sql(query, ['C%'])
        expected = [
            ('Costa Rica', 'Nordamerika'), ('Chile', 'Südamerika'), ('China', 'Asien')]
        self.assertCountEqual(countries, expected)


def find_places_with_countries() -> str:
    """Gibt den SQL-Ausdruck zurück, um eine Liste (Ort, Land) zu erhalten."""
    return """..."""


class TestPlacesWithCountries(TestCase):
    def test_places_with_countries(self):
        query = find_places_with_countries()
        places = execute_sql(query, [])
        self.assertIn(('Berlin', 'Deutschland'), places)
        self.assertIn(('Wien', 'Österreich'), places)
        self.assertEqual(26205, len(places))


def find_places_with_countries_and_continents() -> str:
    """Gibt den SQL-Ausdruck zurück, um eine Liste (Ort, Land, Kontinent) zu erhalten."""
    return """..."""


class TestPlacesWithCountriesAndContinents(TestCase):
    def test_places_with_countries_and_continents(self):
        query = find_places_with_countries_and_continents()
        places = execute_sql(query, [])
        self.assertIn(('Berlin', 'Deutschland', 'Europa'), places)
        self.assertIn(('Wien', 'Österreich', 'Europa'), places)
        self.assertEqual(26205, len(places))


def find_rivers_flowing_into() -> str:
    """Gibt den SQL-Ausdruck zurück, um Flüsse zu finden, die in einen bestimmten Fluss münden."""
    return """..."""


class TestRiversFlowingInto(TestCase):
    def test_rivers_flowing_into_donau(self):
        query = find_rivers_flowing_into()
        rivers = execute_sql(query, ['Donau'])
        expected = [('Altmühl',), ('Drau',), ('Enns',), ('Ilz',), ('Inn',), ('Isar',), ('Lech',), ('Leitha',),
                    ('Save',), ('Theiß',), ('Traun',), ('Ybbs',)]
        self.assertCountEqual(rivers, expected)


def find_continent_of_city() -> str:
    """Gibt den SQL-Ausdruck zurück, um den Kontinent zu finden, auf dem eine bestimmte Stadt liegt."""
    return """..."""


class TestContinentOfCity(TestCase):
    def test_continent_of_city_bangkok(self):
        query = find_continent_of_city()
        continent = execute_sql(query, ['Bangkok'])
        expected = [('Asien',)]
        self.assertEqual(continent, expected)


def find_languages_spoken_in_country() -> str:
    """Gibt den SQL-Ausdruck zurück, um Sprachen und ihre Häufigkeiten zu finden,
    die in einem bestimmten Land gesprochen werden. Die Liste ist absteigend sortiert, nach der Häufigkeit."""
    return """..."""


class TestLanguagesSpokenInCountry(TestCase):
    def test_languages_spoken_in_switzerland(self):
        query = find_languages_spoken_in_country()
        languages = execute_sql(query, ['Schweiz'])
        expected = [('Deutsch', 65), ('Französisch', 18), ('Italienisch', 12), ('Rätoromanisch', 1)]
        self.assertListEqual(languages, expected)


def find_neighbors_of_country() -> str:
    """Gibt den SQL-Ausdruck zurück, um Nachbarländer eines bestimmten Landes zu finden."""
    return """..."""


class TestNeighborsOfCountry(TestCase):
    def test_neighbors_of_germany(self):
        query = find_neighbors_of_country()
        neighbors = execute_sql(query, ['Deutschland'])
        expected = [('Österreich',), ('Belgien',), ('Schweiz',), ('Tschechische Republik',), ('Frankreich',)]
        self.assertCountEqual(neighbors, expected)


if __name__ == '__main__':
    main()
