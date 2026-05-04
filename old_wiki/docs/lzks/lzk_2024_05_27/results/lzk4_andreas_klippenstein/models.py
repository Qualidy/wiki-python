from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True, nullable=False)
    name_eng = Column(String)
    name_translation = Column(String)
    name_language = Column(String)
