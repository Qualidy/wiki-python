from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def generate_question(self):
        """Generiere eine spezifische Frage und gib diese samt Antwort zurück."""
        pass
