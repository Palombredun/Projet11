import pytest

from app.controllers.game import Game


@pytest.fixture(scope="module")
def base_game():
    return Game()

def test_base_game(base_game):
	assert base_game.victory == False
	assert base_game.path_enemy == None
	assert base_game.path_objects == {}

def test_place_enemy(base_game):
	base_game.place_enemy(['ddrrddllurdl', 'rddrdrdluu', 'rrddlluuudr'])
	assert base_game.path_enemy in ['ddrrddllurdl', 'rddrdrdluu', 'rrddlluuudr']

def test_place_enemy_one_leaf(base_game):
	base_game.place_enemy(['ddrllullrlrrdlluudlr'])
	assert base_game.path_enemy in 'ddrllullrlrrdlluudlr'