import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Pokemon, Type
from sqlalchemy.exc import IntegrityError

class TestDatabaseModels(unittest.TestCase):
    def setUp(self):
        """ Memory-only SQLite Datenbank vor jedem Test. """
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_pokemon_creation(self):
        """ Testet die Erstellung und die Abfrage von Pokémon. """
        pokemon = Pokemon(name="Bulbasaur", hp=45, attack=49, defense=49)
        self.session.add(pokemon)
        self.session.commit()

        retrieved_pokemon = self.session.query(Pokemon).filter_by(name="Bulbasaur").one()
        self.assertEqual(retrieved_pokemon.name, "Bulbasaur")
        self.assertEqual(retrieved_pokemon.hp, 45)
        self.assertEqual(retrieved_pokemon.attack, 49)
        self.assertEqual(retrieved_pokemon.defense, 49)

    def test_type_relationship(self):
        """ Testet die Beziehung zwischen Pokémon und deren Typ. """
        type_grass = Type(type_name="Grass")
        type_poison = Type(type_name="Poison")
        pokemon = Pokemon(name="Bulbasaur", types=[type_grass, type_poison])
        self.session.add(pokemon)
        self.session.commit()

        retrieved_pokemon = self.session.query(Pokemon).filter_by(name="Bulbasaur").one()
        self.assertEqual(len(retrieved_pokemon.types), 2)
        self.assertListEqual([t.type_name for t in retrieved_pokemon.types], ["Grass", "Poison"])

    def test_unique_pokemon_name(self):
        """ Testet dass Pokémon Namen unique sind. """
        pokemon1 = Pokemon(name="Charmander", hp=39, attack=52)
        self.session.add(pokemon1)
        self.session.commit()

        pokemon2 = Pokemon(name="Charmander", hp=39, attack=52)
        self.session.add(pokemon2)
        with self.assertRaises(IntegrityError):
            self.session.commit()

        # Rollback session after integrity error
        self.session.rollback()

    def test_pokemon_with_no_types(self):
        """ Testet die Erstellung eines Pokémon ohne Typ. """
        pokemon = Pokemon(name="Pikachu")
        self.session.add(pokemon)
        self.session.commit()

        retrieved_pokemon = self.session.query(Pokemon).filter_by(name="Pikachu").one()
        self.assertEqual(len(retrieved_pokemon.types), 0)

    def test_delete_pokemon(self):
        """ Testet das Löschen eines Pokémon. """
        pokemon = Pokemon(name="Squirtle", hp=44, attack=48)
        self.session.add(pokemon)
        self.session.commit()

        self.session.delete(pokemon)
        self.session.commit()

        retrieved_pokemon = self.session.query(Pokemon).filter_by(name="Squirtle").all()
        self.assertEqual(len(retrieved_pokemon), 0)

    def tearDown(self):
        """ Droppt alle Tables nach jedem Test für einen Cleanen State. """
        Base.metadata.drop_all(self.engine)