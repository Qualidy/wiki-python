from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Many-to-Many Beziehungstabelle für Pokémon-Typen
pokemon_types_table = Table('pokemon_types', Base.metadata,
                            Column('pokemon_id', Integer, ForeignKey('pokemons.id'), primary_key=True),
                            Column('type_id', Integer, ForeignKey('types.id'), primary_key=True))

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    name = Column(String, unique=True)
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    sp_attack = Column(Integer)
    sp_defense = Column(Integer)
    speed = Column(Integer)
    generation = Column(Integer)
    legendary = Column(Boolean)
    description = Column(String)
    previous_evolution_id = Column(Integer, ForeignKey('pokemons.id'))
    
    types = relationship('Type', secondary=pokemon_types_table, back_populates="pokemons")
    previous_evolution = relationship('Pokemon', remote_side=[id], uselist=False, backref='next_evolution')


class Type(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True)
    type_name = Column(String, unique=True)

    pokemons = relationship('Pokemon', secondary=pokemon_types_table, back_populates="types")

    def __str__(self):
        return self.type_name

def init_db():
    engine = create_engine('sqlite:///pokedex.db', echo=False)
    Base.metadata.create_all(engine)
    return engine

engine = init_db()
