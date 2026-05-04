from models import Pokemon
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy import create_engine

engine = create_engine('sqlite///pokemon.db')
Session = sessionmaker(bind=engine)


def translate_to_eng(name):
    """
    Gibt den englischen Namen eines Pokémon zurück, basierend auf einem beliebigen Namen in einer unterstützten Sprache.

    Args:
        name (str): Der Name des Pokémon in einer beliebigen unterstützten Sprache.

    Returns:
        str: Der englische Name des Pokémon, wenn gefunden, sonst None.

    Examples:
        >>> translate_to_eng('フシギダネ')
        'Bulbasaur'
        >>> translate_to_eng('bisasam')
        'Bulbasaur'
        >>> translate_to_eng('Bulbizarre')
        'Bulbasaur'
        >>> translate_to_eng('Bulbasaur')
        'Bulbasaur'
    """
    return ...


def test_database(searched_name):
    with Session as session:
        return session.query(Pokemon).filter(Pokemon.name_eng == searched_name).all()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
