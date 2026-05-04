from sqlalchemy  import create_engine, Column,String,Integer
from sqlalchemy.orm import declarative_base,sessionmaker
import os

Base = declarative_base()
class Pokemon(Base):
    __tablename__="pokemon"
    id = Column(Integer, primary_key = True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)

os.chdir(r'/Users/dsi3abe/Desktop/Programmierung/Python_Programme/Python_Mai-24/LZK_270524/')
engine=create_engine('sqlite:///pokemon.db')






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
    with sessionmaker(bind=engine)() as session:
        test = session.query(Pokemon.english_name).filter((Pokemon.translation == name.upper()) | (Pokemon.english_name== name.upper())).first()
    return test[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(translate_to_eng('glurak'))
