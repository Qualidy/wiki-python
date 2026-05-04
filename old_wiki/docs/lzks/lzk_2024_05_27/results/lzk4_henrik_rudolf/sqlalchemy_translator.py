from sqlalchemy import MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)

engine = create_engine("sqlite:///pokemon.db")
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
        'Bulbasaur'
        >>> translate_to_eng('bisasam')
        'Bulbasaur'
        >>> translate_to_eng('Bulbizarre')
        'Bulbasaur'
        >>> translate_to_eng('Bulbasaur')
        'Bulbasaur'
    """
    session = Session()
    name_lower = name.lower()
    result = session.query(Pokemon).filter_by(translation=name_lower).first()
    if not result:
        result = session.query(Pokemon).filter_by(english_name=name_lower).first()
    if not result:
        return None
    session.close()
    return result.english_name.capitalize()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
