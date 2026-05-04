from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(url="sqlite:///LZK_Montag/lzk4/database.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()