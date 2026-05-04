from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)

engine = create_engine('sqlite:///pokemon.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

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
    return session.query(Pokemon.english_name).where(Pokemon.translation == name).first()[0].title()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
