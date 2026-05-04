from unittest import TestCase, main

from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, DECIMAL, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased

Base = declarative_base()
engine = create_engine('sqlite:///terra.sqlite')
Session = sessionmaker(bind=engine)
session = Session()


class Fluss(Base):
    __tablename__ = 'fluss'
    FNR = Column(String(3), primary_key=True)
    Name = Column(String(30), nullable=False)
    ZielFNR = Column(String(3), ForeignKey('fluss.FNR'))
    Meer = Column(String(25))
    Laenge = Column(Float)


class Kontinent(Base):
    __tablename__ = 'kontinent'
    KNR = Column(String(2), primary_key=True)
    Name = Column(String(15))
    Flaeche = Column(Float)
    Einwohner = Column(Float, nullable=False)
    AnteilErdoberflaeche = Column(DECIMAL(4, 2), nullable=False)


class Land(Base):
    __tablename__ = 'land'
    LNR = Column(String(4), primary_key=True)
    Name = Column(String(50))
    KNR = Column(String(3), ForeignKey('kontinent.KNR'))
    Einwohner = Column(Float)
    Flaeche = Column(Float)
    HauptONR = Column(String(6))


class Sprache(Base):
    __tablename__ = 'sprache'
    SNR = Column(String(3), primary_key=True)
    Name = Column(String(50), nullable=False)


class Gesprochen(Base):
    __tablename__ = 'gesprochen'
    SNR = Column(String(3), ForeignKey('sprache.SNR'), primary_key=True)
    LNR = Column(String(4), ForeignKey('land.LNR'), primary_key=True)
    Anteil = Column(Integer)


class Nachbarland(Base):
    __tablename__ = 'nachbarland'
    LNR1 = Column(String(4), ForeignKey('land.LNR'), primary_key=True)
    LNR2 = Column(String(4), ForeignKey('land.LNR'), primary_key=True)


class Ort(Base):
    __tablename__ = 'ort'
    ONR = Column(String(6), primary_key=True)
    Name = Column(String(30))
    LNR = Column(String(4), ForeignKey('land.LNR'))
    Landesteil = Column(String(30))
    Einwohner = Column(Integer)
    Breite = Column(Float)
    Laenge = Column(Float)
    Done = Column(String(3))


class Stadtfluss(Base):
    __tablename__ = 'stadtfluss'
    ONR = Column(String(6), ForeignKey('ort.ONR'), primary_key=True)
    FNR = Column(String(3), ForeignKey('fluss.FNR'), primary_key=True)
    Done = Column(String(5))


class Weg(Base):
    __tablename__ = 'weg'
    ONR1 = Column(String(6), ForeignKey('ort.ONR'), primary_key=True)
    ONR2 = Column(String(6), ForeignKey('ort.ONR'), primary_key=True)
    Strecke = Column(Float, nullable=False)
    Dauer = Column(Integer, nullable=False)
    Sperrung = Column(Integer, nullable=False, default=0)


Base.metadata.create_all(engine)


def find_countries_starting_with(letter):
    ...


class TestCountriesStartingWith(TestCase):
    def test_countries_starting_with_B(self):
        countries = find_countries_starting_with('B')
        expected = [
            ('Belgien', 'Europa'), ('Bahrein', 'Asien'), ('Barbados', 'Nordamerika'),
            ('Bangladesch', 'Asien'), ('Bahamas', 'Afrika'), ('Bulgarien', 'Europa'),
            ('Belize', 'Nordamerika'), ('Bhutan', 'Asien'), ('Bosnien-Herzegowina', 'Europa'),
            ('Bolivien', 'Südamerika'), ('Brasilien', 'Südamerika'), ('Brunei', 'Asien'),
            ('Burundi', 'Afrika'), ('Birma', 'Asien'), ('Bophuthatswana', 'Afrika'),
            ('Botswana', 'Afrika'), ('Benin', 'Afrika'), ('Burkina Faso', 'Afrika')]
        self.assertCountEqual(countries, expected)


def find_places_with_countries():
    ...


class TestPlacesWithCountries(TestCase):
    def test_places_with_countries(self):
        places = find_places_with_countries()
        self.assertIn(('Berlin', 'Deutschland'), places)
        self.assertIn(('Wien', 'Österreich'), places)
        self.assertEqual(26205, len(places))


def find_places_with_countries_and_continents():
    ...


class TestPlacesWithCountriesAndContinents(TestCase):
    def test_places_with_countries_and_continents(self):
        places = find_places_with_countries_and_continents()
        self.assertIn(('Berlin', 'Deutschland', 'Europa'), places)
        self.assertIn(('Wien', 'Österreich', 'Europa'), places)


def find_rivers_flowing_into(flussname):
    ...


class TestRiversFlowingInto(TestCase):
    def test_rivers_flowing_into_donau(self):
        rivers = find_rivers_flowing_into('Donau')
        expected = [('Altmühl',), ('Drau',), ('Enns',), ('Ilz',), ('Inn',), ('Isar',), ('Lech',), ('Leitha',),
                    ('Save',), ('Theiß',), ('Traun',), ('Ybbs',)]
        self.assertListEqual(rivers, expected)


def find_continent_of_city(stadtname):
    ...


class TestContinentOfCity(TestCase):
    def test_continent_of_city_bangkok(self):
        continent = find_continent_of_city('Bangkok')
        expected = [('Asien',)]
        self.assertEqual(continent, expected)


def find_languages_spoken_in_country(landname):
    ...


class TestLanguagesSpokenInCountry(TestCase):
    def test_languages_spoken_in_switzerland(self):
        languages = find_languages_spoken_in_country('Schweiz')
        expected = [('Deutsch', 65), ('Französisch', 18), ('Italienisch', 12), ('Rätoromanisch', 1)]
        self.assertListEqual(languages, expected)


def find_neighbors_of_country(landname):
    ...


class TestNeighborsOfCountry(TestCase):
    def test_neighbors_of_germany(self):
        neighbors = find_neighbors_of_country('Deutschland')
        expected = [('Österreich',), ('Belgien',), ('Schweiz',), ('Tschechische Republik',), ('Frankreich',)]
        self.assertListEqual(neighbors, expected)


if __name__ == '__main__':
    main()
