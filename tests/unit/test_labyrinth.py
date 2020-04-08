import pytest

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
    assert base_lab.tree.root.data == "p"
    assert base_lab.tree.leaves == []


def test_in_limit_outlimit(base_lab):
    cell = (-5, -5)
    in_limit = base_lab.in_limits(cell)
    assert in_limit == False


def test_in_limit_inlimit(base_lab):
    cell = (5, 5)
    in_limit = base_lab.in_limits(cell)
    assert in_limit == True


def test_unvisited_neighbors_no_neighbors(base_lab):
    cell = (1, 1)
    visited_cells = [(0, 1), (2, 1), (1, 0), (1, 2)]
    neighbors = base_lab.unvisited_neighbors(visited_cells, cell)
    assert neighbors == []


def test_unvisited_neighbors_all_neighbors(base_lab):
    cell = (1, 1)
    visited_cells = []
    neighbors = base_lab.unvisited_neighbors(visited_cells, cell)
    assert neighbors == [(0, 1), (2, 1), (1, 0), (1, 2)]


def test_unvisited_neuigbors_corner(base_lab):
    cell = (0, 0)
    visited_cells = [(1, 0)]
    neighbors = base_lab.unvisited_neighbors(visited_cells, cell)
    assert neighbors == [(0, 1)]


def test_generate_lab(base_lab):
    base_lab.generate_maze()
    # assert list of leaves is not longer empty
    assert base_lab.tree.leaves != []
    # assert number of tiles equal to LENGTH * WIDTH
    tiles = set((0, 0))
    for leaf in base_lab.tree.leaves:
        i, j = 0, 0
        for direction in leaf:
            if direction == "l":
                i += -1
            elif direction == "r":
                i += 1
            elif direction == "u":
                j += 1
            elif direction == "d":
                j += -1
            tiles.add((i, j))
    assert len(tiles) == 225
