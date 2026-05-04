import pandas as pd
from database.init_db import get_session
from database.models import Pokemon, Type

class PokemonLoadCSVService:
    """Service-Klasse zum Laden von Pokémon-Daten aus einer CSV-Datei in die Datenbank."""

    def __init__(self):
        self.session = get_session()

    def load_csv(self, filepath):
        """
        Liest Pokémon-Daten aus einer CSV-Datei und fügt sie in die Datenbank ein.
        Erwartet, dass die CSV-Datei Spalten für Pokémon-Eigenschaften einschließlich der Typen enthält.
        """
        df = pd.read_csv(filepath)
        for _, row in df.iterrows():
            type1 = self.session.query(Type).filter_by(type_name=row['Typ 1']).first()
            if not type1:
                type1 = Type(type_name=row['Typ 1'])
                self.session.add(type1)
                self.session.commit()  # Sicherstellen, dass der Typ gespeichert wird, bevor er verwendet wird

            type2 = None
            if pd.notna(row['Typ 2']):
                type2 = self.session.query(Type).filter_by(type_name=row['Typ 2']).first()
                if not type2:
                    type2 = Type(type_name=row['Typ 2'])
                    self.session.add(type2)
                self.session.commit()  # Ebenso für Typ 2

            prev_pokemon = None
            if pd.notna(row['Vorherige Evolution']):
                prev_pokemon = self.session.query(Pokemon).filter_by(name=row['Vorherige Evolution']).first()

            pokemon = Pokemon(
                name=row['Name'],
                total=row['Gesamt'],
                hp=row['KP'],
                attack=row['Angriff'],
                defense=row['Verteidigung'],
                sp_attack=row['Spez. Angr'],
                sp_defense=row['Spez. Vert'],
                speed=row['Tempo'],
                generation=row['Generation'],
                legendary=row['Legendär'] == 'Ja',
                description=row['Beschreibung'],
                previous_evolution=prev_pokemon
            )
            pokemon.types.append(type1)
            if type2:
                pokemon.types.append(type2)
            self.session.add(pokemon)
        self.session.commit()