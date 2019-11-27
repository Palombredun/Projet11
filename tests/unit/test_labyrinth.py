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
    assert base_lab.tree.root.data == "p"
