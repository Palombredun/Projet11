import pytest

from app.models.tree import Tree
from app.models.hero import Hero

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


@pytest.fixture(scope="module")
def hero():
    return Hero()


def test_base_game(base_game):
    assert base_game.victory == False
    assert base_game.path_enemy == str()
    assert base_game.path_used == []
    assert base_game.needle == ""
    assert base_game.tube == ""
    assert base_game.ether == ""


def test_convert_up(base_game):
    path = "uuu"
    (i, j) = base_game.convert(path)
    assert (i, j) == (0, 3)


def test_convert_down(base_game):
    path = "dddd"
    (i, j) = base_game.convert(path)
    assert (i, j) == (0, -4)


def test_convert_left(base_game):
    path = "ll"
    (i, j) = base_game.convert(path)
    assert (i, j) == (-2, 0)


def test_convert_right(base_game):
    path = "rrrrr"
    (i, j) = base_game.convert(path)
    assert (i, j) == (5, 0)


def test_convert_complex_path(base_game):
    path = "rrruluurrd"
    (i, j) = base_game.convert(path)
    assert (i, j) == (4, 2)


def test_place_enemy(base_game, leaves):
    base_game.place_enemy(leaves)
    assert base_game.path_enemy in leaves
    assert base_game.path_used[0] == base_game.path_enemy


def test_place_objects(base_game, leaves):
    base_game.place_objects(leaves)
    assert base_game.needle in leaves
    assert base_game.tube in leaves
    assert base_game.ether in leaves


def test_test_position(base_game, hero):
    tree = Tree("p")
    tree.add_node(path="", direction=(1, 0), value="p")
    res = base_game.test_position(tree, hero, "u")
    assert res == True


def test_test_victory(base_game, hero):
    hero.items = 3
    base_game.place_enemy(["ur"])
    hero.path.path = "ur"
    res = base_game.test_victory(hero)
    assert res == True


def test_victory_missing_items(base_game, hero):
    hero.items = 2
    base_game.place_enemy(["ur"])
    hero.path.path = "ur"
    res = base_game.test_victory(hero)
    assert res == "defeat"


def test_victory_wrong_tile(base_game, hero):
    hero.items = 3
    base_game.place_enemy(["ur"])
    hero.path.path = "uuurrrddl"
    res = base_game.test_victory(hero)
    assert res == False
