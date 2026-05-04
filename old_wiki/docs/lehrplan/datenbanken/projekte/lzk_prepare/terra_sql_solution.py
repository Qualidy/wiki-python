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
    return """
    SELECT land.name, kontinent.name
    FROM land
    JOIN kontinent ON land.knr = kontinent.knr
    WHERE land.name LIKE ?
    """


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
    return """
    SELECT ort.name, land.name
    FROM ort
    JOIN land ON ort.lnr = land.lnr
    """


class TestPlacesWithCountries(TestCase):
    def test_places_with_countries(self):
        query = find_places_with_countries()
        places = execute_sql(query, [])
        self.assertIn(('Berlin', 'Deutschland'), places)
        self.assertIn(('Wien', 'Österreich'), places)
        self.assertEqual(26205, len(places))


def find_places_with_countries_and_continents() -> str:
    """Gibt den SQL-Ausdruck zurück, um eine Liste (Ort, Land, Kontinent) zu erhalten."""
    return """
    SELECT ort.name, land.name, kontinent.name
    FROM ort
    JOIN land ON ort.lnr = land.lnr
    JOIN kontinent ON land.knr = kontinent.knr
    """


class TestPlacesWithCountriesAndContinents(TestCase):
    def test_places_with_countries_and_continents(self):
        query = find_places_with_countries_and_continents()
        places = execute_sql(query, [])
        self.assertIn(('Berlin', 'Deutschland', 'Europa'), places)
        self.assertIn(('Wien', 'Österreich', 'Europa'), places)
        self.assertEqual(26205, len(places))


def find_rivers_flowing_into() -> str:
    """Gibt den SQL-Ausdruck zurück, um Flüsse zu finden, die in einen bestimmten Fluss münden."""
    return """
    SELECT fluss.name
    FROM fluss
    JOIN fluss ziel ON fluss.zielfnr = ziel.fnr
    WHERE ziel.name = ?
    """


class TestRiversFlowingInto(TestCase):
    def test_rivers_flowing_into_donau(self):
        query = find_rivers_flowing_into()
        rivers = execute_sql(query, ['Donau'])
        print(rivers)
        expected = [('Altmühl',), ('Drau',), ('Enns',), ('Ilz',), ('Inn',), ('Isar',), ('Lech',), ('Leitha',),
                    ('Save',), ('Theiß',), ('Traun',), ('Ybbs',)]
        self.assertCountEqual(rivers, expected)


def find_continent_of_city() -> str:
    """Gibt den SQL-Ausdruck zurück, um den Kontinent zu finden, auf dem eine bestimmte Stadt liegt."""
    return """
    SELECT kontinent.name
    FROM ort
    JOIN land ON ort.lnr = land.lnr
    JOIN kontinent ON land.knr = kontinent.knr
    WHERE ort.name = ?
    """


class TestContinentOfCity(TestCase):
    def test_continent_of_city_bangkok(self):
        query = find_continent_of_city()
        continent = execute_sql(query, ['Bangkok'])
        expected = [('Asien',)]
        self.assertEqual(continent, expected)


def find_languages_spoken_in_country() -> str:
    """Gibt den SQL-Ausdruck zurück, um Sprachen und ihre Häufigkeiten zu finden,
    die in einem bestimmten Land gesprochen werden. Die Liste ist absteigend sortiert, nach der Häufigkeit."""
    return """
    SELECT sprache.name, gesprochen.anteil
    FROM gesprochen
    JOIN sprache ON gesprochen.snr = sprache.snr
    JOIN land ON gesprochen.lnr = land.lnr
    WHERE land.name = ?
    ORDER BY gesprochen.anteil DESC
    """


class TestLanguagesSpokenInCountry(TestCase):
    def test_languages_spoken_in_switzerland(self):
        query = find_languages_spoken_in_country()
        languages = execute_sql(query, ['Schweiz'])
        print(languages)
        expected = [('Deutsch', 65), ('Französisch', 18), ('Italienisch', 12), ('Rätoromanisch', 1)]
        self.assertListEqual(languages, expected)


def find_neighbors_of_country() -> str:
    """Gibt den SQL-Ausdruck zurück, um Nachbarländer eines bestimmten Landes zu finden."""
    return """
    select l2.name from land as l1, nachbarland, land as l2
    where l1.lnr = nachbarland.lnr1 and nachbarland.lnr2 = l2.lnr 
    and l1.name = ?
    """


class TestNeighborsOfCountry(TestCase):
    def test_neighbors_of_germany(self):
        query = find_neighbors_of_country()
        neighbors = execute_sql(query, ['Deutschland'])
        expected = [('Österreich',), ('Belgien',), ('Schweiz',), ('Tschechische Republik',), ('Frankreich',)]
        self.assertCountEqual(neighbors, expected)


if __name__ == '__main__':
    main()
