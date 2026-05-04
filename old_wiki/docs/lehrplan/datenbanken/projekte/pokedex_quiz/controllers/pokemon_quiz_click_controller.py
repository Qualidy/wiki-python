import click
from services.pokemon_quiz_service import PokemonQuizService

# Erstelle eine Instanz des Quiz-Services
quiz_service = PokemonQuizService()

@click.command()
def start_quiz():
    """Startet das Quiz mit einer zufälligen Frage."""
    question, correct_answer = quiz_service.get_random_question()
    click.echo(f'Frage: {question["text"]}')
    user_answer = click.prompt('Deine Antwort')
    is_correct = quiz_service.check_answer(user_answer, correct_answer)

    if is_correct:
        click.echo('Richtig! Sehr gut gemacht!')
    else:
        click.echo(f'Leider falsch. Die richtige Antwort wäre: {correct_answer}')
