from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)



engine = create_engine('sqlite:///Pokemon.db')
Base.metadata.create_all(engine)
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
        'bulbasaur'
        >>> translate_to_eng('bisasam')
        'bulbasaur'
        >>> translate_to_eng('bulbizarre')
        'bulbasaur'
        >>> translate_to_eng('bulbasaur')
        'bulbasaur'
    """
    session = Session()
    english_pokemon = session.query(Pokemon.english_name).filter(Pokemon.english_name==name).first()


    translated_pokemon = session.query(Pokemon.english_name).filter(Pokemon.translation==name).first()

    if translated_pokemon == None:
        return name

    return translated_pokemon[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
