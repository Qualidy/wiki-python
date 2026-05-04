from random import choice
from database.models import Pokemon
from services.quiz.question import Question

class TypeQuestion(Question):
    def generate_question(self):
        pokemon = choice(self.session.query(Pokemon).all())
        correct_answer = ', '.join([t.type_name for t in pokemon.types])
        return {
            "id": pokemon.id,
            "text": f"Welchen Typ hat das Pokémon {pokemon.name}?",
            "type": 'type_question'
        }, correct_answer
