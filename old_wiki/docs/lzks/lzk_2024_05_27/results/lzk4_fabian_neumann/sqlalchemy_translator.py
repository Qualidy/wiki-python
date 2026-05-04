from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()
engine = create_engine('sqlite:///pokemon.db')
Session = sessionmaker(bind=engine)
session = Session(bind=engine)


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)


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

    name = name.lower()
    english_names = [english_name[0] for english_name in session.query(Pokemon.english_name).all()]
    if name in english_names:
        return name[0].upper() + name[1:]

    translation = session.query(Pokemon).filter(Pokemon.translation == name).first()
    if translation:
        english_name = translation.english_name
        return english_name[0].upper() + english_name[1:]
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
