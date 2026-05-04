from random import choice

from database.models import Pokemon
from services.quiz.question import Question

class DescriptionQuestion(Question):
    def generate_question(self):
        # Wähle zufällig ein Pokémon aus
        pokemon = choice(self.session.query(Pokemon).all())
        return {
            "text": f"Wie heißt das Pokémon, auf das folgende Beschreibung zutrifft: {pokemon.description}?",
            "type": 'description_question'
        }, pokemon.name
