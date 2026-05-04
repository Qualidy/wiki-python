from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Klasse, Pruefung, Note


def durchschnittsnote_klasse_klausur(klassen_id, pruefungs_id):
    engine = create_engine('sqlite:///datenbank.sqLite')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Gesamtpunktzahl und Anzahl der Schüler für die Klasse und die Prüfung abrufen
    query = session.query(func.sum(Note.wert), func.count(Note.id)) \
        .join(Pruefung) \
        .filter(Pruefung.id == pruefungs_id) \
        .filter(Note.pruefung_id == Pruefung.id) \
        .filter(Pruefung.klasse == klassen_id)

    summe, anzahl = query.first()

    # Durchschnittsnote berechnen
    durchschnittsnote = summe / anzahl if anzahl else None

    session.close()

    return durchschnittsnote

import sqlite3

def anzahl_schueler_klasse(klassen_name):
    connection = sqlite3.connect('datenbank.sqLite')
    cursor = connection.cursor()

    # SQLite-Abfrage, um die Anzahl der Schüler in der Klasse zu erhalten
    cursor.execute("SELECT COUNT(*) FROM schuelerin JOIN klasse ON schuelerin.klasse_id = klasse.id WHERE klasse.name = ?", (klassen_name,))
    anzahl_schueler = cursor.fetchone()[0]

    connection.close()

    return anzahl_schueler

# Beispielaufruf der Funktion

if __name__ == '__main__':
    # Beispielaufruf der Funktion
    klassen_id = 1  # Hier die ID der Klasse einsetzen
    pruefungs_id = 1  # Hier die ID der Prüfung (Klausur) einsetzen
    durchschnittsnote = durchschnittsnote_klasse_klausur(klassen_id, pruefungs_id)
    print(f"Durchschnittsnote der Klasse in der Klausur: {durchschnittsnote}")

    klassen_name = '7a'  # Hier den Namen der Klasse einsetzen
    anzahl_schueler = anzahl_schueler_klasse(klassen_name)
    print(f"Die Klasse {klassen_name} hat {anzahl_schueler} Schüler/innen.")


