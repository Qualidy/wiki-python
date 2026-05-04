import click
from services.pokemon_query import PokemonQueryService

# Initialisiere den Query Service
service = PokemonQueryService()

@click.group()
def cli():
    """CLI Tool zur Verwaltung der Pokémon-Datenbank."""
    pass

@cli.command()
@click.option('--name', prompt='Name des Pokémon', help='Name des Pokémon')
@click.option('--hp', prompt='HP', type=int, help='HP des Pokémon')
@click.option('--attack', prompt='Attacke', type=int, help='Angriffswert des Pokémon')
@click.option('--defense', prompt='Verteidigung', type=int, help='Verteidigungswert des Pokémon')
@click.option('--sp_attack', prompt='Spez. Angriff', type=int, help='Spezial-Angriffswert des Pokémon')
@click.option('--sp_defense', prompt='Spez. Verteidigung', type=int, help='Spezial-Verteidigungswert des Pokémon')
@click.option('--speed', prompt='Geschwindigkeit', type=int, help='Geschwindigkeit des Pokémon')
@click.option('--generation', prompt='Generation', type=int, help='Generation des Pokémon')
@click.option('--legendary', prompt='Legendär (Ja/Nein)', help='Ist das Pokémon legendär?')
@click.option('--description', prompt='Beschreibung', help='Beschreibung des Pokémon')
@click.option('--types', prompt='Typen (durch Komma getrennt)', help='Typen des Pokémon')
def add(name, hp, attack, defense, sp_attack, sp_defense, speed, generation, legendary, description, types):
    """Fügt ein neues Pokémon hinzu."""
    types_list = types.split(',')
    legendary_status = True if legendary.lower() == 'ja' else False
    pokemon = service.add_pokemon(
        name=name,
        hp=hp,
        attack=attack,
        defense=defense,
        sp_attack=sp_attack,
        sp_defense=sp_defense,
        speed=speed,
        generation=generation,
        legendary=legendary_status,
        description=description,
        types=types_list
    )
    click.echo(f'Pokémon {pokemon.name} erfolgreich hinzugefügt.')
    
@cli.command()
@click.argument('name')
def remove(name):
    """Entfernt ein Pokémon aus der Datenbank."""
    if service.remove_pokemon(name):
        click.echo(f'Pokémon {name} erfolgreich entfernt.')
    else:
        click.echo('Pokémon nicht gefunden oder Entfernen fehlgeschlagen.')

@cli.command()
@click.argument('name')
def get(name):
    """Gibt Informationen zu einem Pokémon zurück."""
    pokemon = service.get_pokemon_by_name(name)
    if pokemon:
        click.echo(f'Name: {pokemon.name}')
        click.echo(f'HP: {pokemon.hp}')
        click.echo(f'Attack: {pokemon.attack}')
        click.echo(f'Defense: {pokemon.defense}')
        click.echo(f'Sp. Attack: {pokemon.sp_attack}')
        click.echo(f'Sp. Defense: {pokemon.sp_defense}')
        click.echo(f'Speed: {pokemon.speed}')
        click.echo(f'Generation: {pokemon.generation}')
        click.echo(f'Legendary: {"Yes" if pokemon.legendary else "No"}')
        click.echo(f'Description: {pokemon.description}')
        types = ', '.join([t.type_name for t in pokemon.types])
        click.echo(f'Types: {types}')
        if pokemon.previous_evolution:
            click.echo(f'Previous Evolution: {pokemon.previous_evolution.name}')
    else:
        click.echo('Pokémon not found.')

@cli.command()
@click.argument('name')
@click.option('--hp', type=int, help='Neuer HP-Wert')
@click.option('--attack', type=int, help='Neuer Angriffswert')
@click.option('--defense', type=int, help='Neuer Verteidigungswert')
@click.option('--sp_attack', type=int, help='Neuer Spez. Angriffswert')
@click.option('--sp_defense', type=int, help='Neuer Spez. Verteidigungswert')
@click.option('--speed', type=int, help='Neue Geschwindigkeit')
@click.option('--generation', type=int, help='Neue Generation')
@click.option('--legendary', type=click.Choice(['Ja', 'Nein']), help='Legendarität ändern (Ja/Nein)')
@click.option('--description', type=str, help='Neue Beschreibung')
@click.option('--types', type=str, help='Typen aktualisieren (durch Komma getrennt)')
def update(name, **kwargs):
    """Aktualisiert die Eigenschaften eines Pokémon."""
    # Verarbeiten der legendären Option
    if 'legendary' in kwargs:
        kwargs['legendary'] = True if kwargs['legendary'].lower() == 'ja' else False
    # Verarbeiten der Typen, falls gegeben
    if 'types' in kwargs:
        types_list = kwargs['types'].split(',')
        kwargs['types'] = types_list
    
    updated = service.update_pokemon(name, **kwargs)
    if updated:
        click.echo(f'Pokémon {name} wurde aktualisiert.')
    else:
        click.echo('Pokémon nicht gefunden oder Update fehlgeschlagen.')

@cli.command()
def list_all():
    """Listet alle Pokémon in der Datenbank auf."""
    pokemons = service.list_pokemons()
    if pokemons:
        for pokemon in pokemons:
            click.echo(f'Name: {pokemon.name}')
            click.echo(f'HP: {pokemon.hp}')
            click.echo(f'Attack: {pokemon.attack}')
            click.echo(f'Defense: {pokemon.defense}')
            click.echo(f'Sp. Attack: {pokemon.sp_attack}')
            click.echo(f'Sp. Defense: {pokemon.sp_defense}')
            click.echo(f'Speed: {pokemon.speed}')
            click.echo(f'Generation: {pokemon.generation}')
            click.echo(f'Legendary: {"Yes" if pokemon.legendary else "No"}')
            click.echo(f'Description: {pokemon.description}')
            types = ', '.join([t.type_name for t in pokemon.types])
            click.echo(f'Types: {types}')
            if pokemon.previous_evolution:
                click.echo(f'Previous Evolution: {pokemon.previous_evolution.name}')
            click.echo('----------')
    else:
        click.echo('No Pokémon found in the database.')