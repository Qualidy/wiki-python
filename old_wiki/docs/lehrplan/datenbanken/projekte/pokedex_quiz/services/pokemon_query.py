from database.init_db import get_session
from database.models import Pokemon, Type

class PokemonQueryService:
    """Service-Klasse für Abfragen und Änderungen an der Pokémon-Datenbank."""

    def __init__(self):
        """Initialisiert die Datenbankverbindung."""
        self.session = get_session()

    def add_pokemon(self, name, hp, attack, defense, sp_attack, sp_defense, speed, generation, legendary, description, types):
        """Fügt ein neues Pokémon der Datenbank hinzu."""
        new_pokemon = Pokemon(name=name, hp=hp, 
                              attack=attack, defense=defense,
                              sp_attack=sp_attack, sp_defense=sp_defense,
                              speed=speed, generation=generation,
                              legendary=legendary, description=description)
        for type_name in types:
            type_instance = self.session.query(Type).filter_by(type_name=type_name).first()
            if not type_instance:
                type_instance = Type(type_name=type_name)
                self.session.add(type_instance)
                self.session.commit()  # Sicherstellen, dass der Typ in der DB vorhanden ist
            new_pokemon.types.append(type_instance)
        self.session.add(new_pokemon)
        self.session.commit()
        return new_pokemon

    def get_pokemon_by_name(self, name):
        """Liefert ein Pokémon anhand seines Namens."""
        return self.session.query(Pokemon).filter_by(name=name).first()

    def update_pokemon(self, name, **kwargs):
        """Aktualisiert die Eigenschaften eines Pokémon."""
        pokemon = self.session.query(Pokemon).filter_by(name=name).first()
        if pokemon:
            for key, value in kwargs.items():
                setattr(pokemon, key, value)
            self.session.commit()
            return pokemon
        return None

    def remove_pokemon(self, name):
        """Entfernt ein Pokémon aus der Datenbank anhand seines Namens."""
        pokemon = self.session.query(Pokemon).filter_by(name=name).first()
        if pokemon:
            self.session.delete(pokemon)
            self.session.commit()
            return True
        return False

    def list_pokemons(self):
        """Gibt eine Liste aller Pokémon in der Datenbank zurück."""
        return self.session.query(Pokemon).all()
