from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


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

    Base = declarative_base()

    class Pokemon(Base):
        __tablename__ = "pokemon"
        id = Column(Integer, primary_key=True)
        english_name = Column(String, nullable=False)
        translation = Column(String, nullable=False)
        language = Column(String, nullable=False)

    engine = create_engine('sqlite:///pokemon.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    #Übersetzung ermitteln
    session.commit()
    vorbereitet = name.lower()
    uebersetzung = session.query(Pokemon.english_name).filter_by(translation=vorbereitet).scalar()
    if uebersetzung is None:
        uebersetzung = name

    return uebersetzung


if __name__ == "__main__":
    import doctest

    doctest.testmod()
