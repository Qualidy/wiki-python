from sqlalchemy import Column, String, Integer
from __init__ import Base, engine
from dataclasses import dataclass


@dataclass
class Pokemon(Base):
    __tablename__ = "pokemon"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    english_name: str = Column(String)
    translation: str = Column(String)
    language: str = Column(String)

Base.metadata.create_all(bind=engine)