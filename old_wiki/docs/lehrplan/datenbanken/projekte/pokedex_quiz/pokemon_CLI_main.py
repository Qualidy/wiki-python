import click
from controllers.pokemon_query_click_controller import cli as query_cli
from controllers.pokemon_load_csv_click_controller import load_csv as load_csv_cli
from controllers.pokemon_quiz_click_controller import start_quiz as quiz_cli

@click.group()
def main_cli():
    """
    Haupt-CLI für das Pokémon-Projekt.
    Dieses Tool ermöglicht die Verwaltung von Pokémon-Daten,
    das Laden von Daten über CSV und das Durchführen eines Pokémon-Quiz.
    """
    pass

# Integriere die verschiedenen CLI-Kommandos aus den Controller-Modulen
main_cli.add_command(query_cli, name="query")
main_cli.add_command(load_csv_cli, name="load-csv")
main_cli.add_command(quiz_cli, name="quiz")

if __name__ == '__main__':
    main_cli()
