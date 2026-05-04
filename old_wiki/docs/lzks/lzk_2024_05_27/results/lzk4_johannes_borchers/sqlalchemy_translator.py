from sqlite3 import *
from sqlalchemy import * 
from sqlalchemy.orm import * 

engine = create_engine('sqlite:///pokemon.db', echo=True)

Base = declarative_base()
session = create_session(engine)

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    english_name = Column(String)
    language = Column(String)
    translation = Column(String)


con = connect('pokemon.db')

cur = con.cursor()
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

    data = cur.execute(f"select * from pokemon as p").fetchall()
    for row in data:
        if row[2] == name:
            return row[1]
        
def orm_translate_to_eng(name):
    return session.query(Pokemon.english_name).filter(Pokemon.translation == name).first()[0]

print(f"{orm_translate_to_eng(name='bisasam')}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
