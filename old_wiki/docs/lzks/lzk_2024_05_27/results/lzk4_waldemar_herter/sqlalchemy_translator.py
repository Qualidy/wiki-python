from sqlalchemy import Column, Integer, engine, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///pokemon.db')

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
    return 

class Pokemon(Base):
    __tablename__ = "pakimoni"
    id = Column(Integer, primary_key=True)
    
    

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
