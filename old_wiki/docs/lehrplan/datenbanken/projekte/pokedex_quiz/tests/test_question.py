import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from database.models import Pokemon, Type
from services.quiz.type_question import TypeQuestion
from services.quiz.max_attack_question import MaxAttackQuestion

class TestTypeQuestion(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.type_question = TypeQuestion(self.session)
        self.pokemon = Pokemon(id=1, name="Bulbasaur", types=[Type(type_name="Grass"), Type(type_name="Poison")])

    @patch('services.quiz.type_question.choice', return_value=Pokemon(id=1, name="Bulbasaur", types=[Type(type_name="Grass"), Type(type_name="Poison")]))
    def test_generate_question(self, _):
        """Testet, ob eine Typ-Frage richtig generiert wird."""
        question, answer = self.type_question.generate_question()
        self.assertIn("Welchen Typ hat das Pokémon Bulbasaur?", question['text'])
        self.assertEqual("Grass, Poison", answer)