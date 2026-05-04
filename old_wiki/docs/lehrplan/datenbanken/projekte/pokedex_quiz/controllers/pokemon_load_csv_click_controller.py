import click
from services.pokemon_load_csv_service import PokemonLoadCSVService

# Erstelle eine Instanz des CSV-Lade-Services
csv_loader = PokemonLoadCSVService()

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def load_csv(filepath):
    """
    Lädt Pokémon-Daten aus einer angegebenen CSV-Datei.
    ARGUMENTS:
    filepath : Pfad zur CSV-Datei, die geladen werden soll.
    """
    try:
        csv_loader.load_csv(filepath)
        click.echo(f'Daten erfolgreich aus {filepath} geladen und in die Datenbank geschrieben.')
    except Exception as e:
        click.echo(f'Fehler beim Laden der Daten aus {filepath}: {e}')
