from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base= declarative_base()

engine= create_engine('sqlite:///pokemon.db')

def translate_to_eng(name):
    with sessionmaker(bind=engine)() as session:
    # """
    # Gibt den englischen Namen eines Pokémon zurück, basierend auf einem beliebigen Namen in einer unterstützten Sprache.

    # Args:
    #     name (str): Der Name des Pokémon in einer beliebigen unterstützten Sprache.

    # Returns:
    #     str: Der englische Name des Pokémon, wenn gefunden, sonst None.

    # Examples:
    #     >>> translate_to_eng('フシギダネ')
    #     'Bulbasaur'
    #     >>> translate_to_eng('bisasam')
    #     'Bulbasaur'
    #     >>> translate_to_eng('Bulbizarre')
    #     'Bulbasaur'
    #     >>> translate_to_eng('Bulbasaur')
    #     'Bulbasaur'
    # """
        return ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()




























