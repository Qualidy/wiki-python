from sqlalchemy import create_engine,MetaData,ForeignKey,Column,Integer,String,func
from sqlalchemy.orm import sessionmaker, declarative_base

import os
os.chdir((r'/Users/aschmid/python_f73/lzk4'))

Base= declarative_base()

class Pokemon(Base):

    __tablename__ = 'pokemon'
    id = Column(Integer,primary_key=True)
    english_name = Column(String)
    translation= Column(String)
    language=Column(String)




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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
