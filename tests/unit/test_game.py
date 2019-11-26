import pytest

from app.controllers.game import Game

@pytest.fixture(scope="module")
def base_game():
	return Game()

