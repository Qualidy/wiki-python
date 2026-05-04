import unittest
from click.testing import CliRunner
from controllers.pokemon_query_click_controller import cli
from services.pokemon_query import PokemonQueryService
from unittest.mock import patch

class TestPokemonQueryClickController(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('controllers.pokemon_query_click_controller.service.get_pokemon_by_name')
    def test_query_pokemon_not_found(self, mock_get_pokemon_by_name):
        """Testet die CLI-Funktion, die versucht, ein nicht existierendes Pokémon abzufragen."""
        mock_get_pokemon_by_name.return_value = None
        result = self.runner.invoke(cli, ['get', 'Pikachu'])
        self.assertIn('Pokémon not found', result.output)