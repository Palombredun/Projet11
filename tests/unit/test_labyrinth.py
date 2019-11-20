import pytest

from app.models.position import Position
from app.models.path import Path
from app.models.labyrinth import Labyrinth
from app.models.tree import Tree

import config.settings as constants


@pytest.fixture(scope="module")
def base_lab():
    return Labyrinth()


def test_init_labyrinth(base_lab):
    assert base_lab.length == constants.LENGTH
    assert base_lab.width == constants.WIDTH
    assert base_lab.maze.root.data == "p"


def test_has_neigbor_method(base_lab):
    pos = Position(5, 5)
    dirs = base_lab._has_unvisited_neighbors(pos, [])
    assert dirs == [(1, 0), (-1, 0), (0, 1), (0, -1)]


def test_has_neighbor_method_near_x0(base_lab):
    pos = Position(0, 3)
    dirs = base_lab._has_unvisited_neighbors(pos, [])
    assert dirs == [(1, 0), (0, 1), (0, -1)]


def test_has_neighbor_method_near_xf(base_lab):
    pos = Position(0, 14)
    dirs = base_lab._has_unvisited_neighbors(pos, [])
    assert dirs == [(1, 0), (0, -1)]


def test_has_neighbor_method_near_y0(base_lab):
    pos = Position(3, 0)
    dirs = base_lab._has_unvisited_neighbors(pos, [])
    assert dirs == [(1, 0), (-1, 0), (0, 1)]


def test_has_neighbor_method_near_yf(base_lab):
    pos = Position(14, 0)
    dirs = base_lab._has_unvisited_neighbors(pos, [])
    assert dirs == [(-1, 0), (0, 1)]


def test_has_neighbor_method_near_x0y0(base_lab):
    pos = Position(0, 0)
    dirs = base_lab._has_unvisited_neighbors(pos, [])
    assert dirs == [(1, 0), (0, 1)]


def test_has_neighbor_method_all_visited(base_lab):
    pos = Position(1, 1)
    dirs = base_lab._has_unvisited_neighbors(pos, [(2, 1), (0, 1), (1, 2), (1, 0)])
    assert dirs == []
