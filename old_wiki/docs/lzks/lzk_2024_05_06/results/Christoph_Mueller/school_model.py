from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# 🟨Diese Datei musst du nicht anfassen.🟨

class Fach(Base):
    __tablename__ = 'fach'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    kuerzel = Column(String(10), nullable=False)
    ist_kernfach = Column(Boolean, nullable=False)
    ist_vorrueckungsfach = Column(Boolean, nullable=False)


class Klasse(Base):
    __tablename__ = 'klasse'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    jahrgangsstufe = Column(Integer, nullable=False)
    klassenleitung_id = Column(Integer, ForeignKey('lehrkraft.id'))

    klassenleitung = relationship('Lehrkraft')


class Lehrbefaehigung(Base):
    __tablename__ = 'lehrbefaehigung'

    lehrkraft_id = Column(Integer, ForeignKey('lehrkraft.id'), primary_key=True)
    fach_id = Column(Integer, ForeignKey('fach.id'), primary_key=True)


class Lehrkraft(Base):
    __tablename__ = 'lehrkraft'

    id = Column(Integer, primary_key=True)
    familienname = Column(String(100), nullable=False)
    rufname = Column(String(50), nullable=False)
    geburtsdatum = Column(Date, nullable=False)
    geschlecht = Column(String(1), nullable=False)


class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    wert = Column(Integer, nullable=False)
    datum = Column(Date)
    gewicht = Column(Integer, default=1)
    schueler_id = Column(Integer, ForeignKey('schuelerin.id'))
    lehrkraft_id = Column(Integer, ForeignKey('lehrkraft.id'))
    fach_id = Column(Integer, ForeignKey('fach.id'))
    pruefung_id = Column(Integer, ForeignKey('pruefung.id'))

    schueler = relationship('Schuelerin')
    lehrkraft = relationship('Lehrkraft')
    fach = relationship('Fach')
    pruefung = relationship('Pruefung')


class Pruefung(Base):
    __tablename__ = 'pruefung'

    id = Column(Integer, primary_key=True)
    typ = Column(String(50))
    laufende_nr = Column(Integer, nullable=False)
    klasse = Column(Integer, ForeignKey('klasse.id'))
    datum = Column(Date)
    fach_id = Column(Integer, ForeignKey('fach.id'))
    lehrkraft_id = Column(Integer, ForeignKey('lehrkraft.id'))

    klasse_obj = relationship('Klasse')
    fach = relationship('Fach')
    lehrkraft = relationship('Lehrkraft')


class Schuelerin(Base):
    __tablename__ = 'schuelerin'

    id = Column(Integer, primary_key=True)
    familienname = Column(String(100), nullable=False)
    rufname = Column(String(50), nullable=False)
    geburtsdatum = Column(Date, nullable=False)
    geschlecht = Column(String(1), nullable=False)
    ist_klassensprecher = Column(Boolean, nullable=False, default=False)
    klasse_id = Column(Integer, ForeignKey('klasse.id'))

    klasse = relationship('Klasse')


class Unterrichtet(Base):
    __tablename__ = 'unterrichtet'

    lehrkraft_id = Column(Integer, ForeignKey('lehrkraft.id'), primary_key=True)
    fach_id = Column(Integer, ForeignKey('fach.id'), primary_key=True)
    klasse_id = Column(Integer, ForeignKey('klasse.id'), primary_key=True)
