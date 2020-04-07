import pytest

from app.controllers.game import Game


@pytest.fixture(scope="module")
def base_game():
    return Game()


@pytest.fixture(scope="module")
def leaves():
    return [
        "drrdldlluu",
        "ddrddlrlrlrulruuurdl",
        "rlrrlldddrl",
        "drrdldlffrld",
        "lrrrdldlldlruulldl",
    ]


def test_base_game(base_game):
    assert base_game.victory == False
    assert base_game.path_enemy == str()
    assert base_game.path_used == []
    assert base_game.needle == ""
    assert base_game.tube == ""
    assert base_game.ether == ""


def test_place_enemy(base_game, leaves):
    base_game.place_enemy(leaves)
    assert base_game.path_enemy in leaves
    assert base_game.path_used[0] == base_game.path_enemy


def test_place_objects(base_game, leaves):
    base_game.place_objects(leaves)
    assert base_game.needle in leaves
    assert base_game.tube in leaves
    assert base_game.ether in leaves
