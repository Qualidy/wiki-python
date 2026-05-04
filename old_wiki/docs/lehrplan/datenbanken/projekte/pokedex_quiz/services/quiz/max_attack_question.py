from database.models import Pokemon
from services.quiz.question import Question

class MaxAttackQuestion(Question):
    def generate_question(self):
        max_attack_pokemon = self.session.query(Pokemon).order_by(Pokemon.attack.desc()).first()
        return {
            "id": max_attack_pokemon.id,
            "text": "Welches Pokémon hat den höchsten Angriffswert?",
            "type": 'max_attack_question'
        }, max_attack_pokemon.name