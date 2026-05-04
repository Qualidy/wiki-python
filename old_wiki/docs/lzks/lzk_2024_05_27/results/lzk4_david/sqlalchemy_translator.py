from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///pokemon.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    english_name = Column(String)
    language = Column(String)
    translation = Column(String)

def translate_to_eng(name: str):
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

    return session.query(Pokemon).filter_by(translation=name).first().english_name


def __del__():
    session.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
