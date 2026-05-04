from random import choice

from database.init_db import get_session
from services.quiz.description_question import DescriptionQuestion
from services.quiz.max_attack_question import MaxAttackQuestion
from services.quiz.type_question import TypeQuestion

class PokemonQuizService:
    def __init__(self):
        self.session = get_session()
        self.question_types = [
            TypeQuestion(self.session),
            MaxAttackQuestion(self.session),
            DescriptionQuestion(self.session)
            # Weitere Frageklassen können hier hinzugefügt werden
        ]

    def get_random_question(self):
        question_instance = choice(self.question_types)
        question, correct_answer = question_instance.generate_question()
        return question, correct_answer

    def check_answer(self, user_answer, correct_answer):
        """Überprüft die Benutzerantwort gegen die korrekte Antwort."""
        return user_answer.lower().strip() == correct_answer.lower().strip()

