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
    assert base_game.path_objects == {}
    assert base_game.path_used == []


def test_place_enemy(base_game, leaves):
    base_game.place_enemy(leaves)
    assert base_game.path_enemy in leaves


def test_draw_objects(base_game, leaves):
    tmp = base_game._draw_path(leaves, 4)
    assert tmp in leaves


def test_place_object(base_game, leaves):
    base_game.place_objects(leaves)
    assert base_game.path_objects["ether"] in leaves
    assert base_game.path_objects["needle"] in leaves
    assert base_game.path_objects["tube"] in leaves
