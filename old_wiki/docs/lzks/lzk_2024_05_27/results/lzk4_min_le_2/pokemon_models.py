from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
class Pokemon(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String)
    translation = Column(String)
    language = Column(String)

engine = create_engine('sqlite:///pokemon.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()