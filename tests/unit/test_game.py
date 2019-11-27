import pytest

from app.controllers.game import Game


@pytest.fixture(scope="module")
def base_game():
    return Game()


def test_base_game(base_game):
    assert base_game.victory == False
    assert base_game.path_enemy == str()
    assert base_game.path_objects == {}
    assert base_game.path_used == []


def test_place_enemy(base_game):
    leaves = [
        "drrdldlluu",
        "ddrddlrlrlrulruuurdl",
        "rlrrlldddrl",
        "drrdldlffrld",
        "lrrrdldlldlruulldl",
    ]
    base_game.place_enemy(leaves)
    assert base_game.path_enemy in leaves


def test_place_object(base_game):
    leaves = [
        "drrdldlluu",
        "ddrddlrlrlrulruuurdl",
        "drrdldlffrld",
        "lrrrdldlldlruulldl",
    ]
    base_game.place_objects(leaves)
    assert base_game.path_objects["ether"] in leaves
    assert base_game.path_objects["needle"] in leaves
    assert base_game.path_objects["tube"] in leaves
