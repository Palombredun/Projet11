import pytest

from app.models.path import Path


@pytest.fixture(scope="module")
def start_path():
    current = Path("")
    return current


def test_init_path(start_path):
    assert type(start_path) == Path


def test_add_direction_right(start_path):
    new_path = start_path + (0, 1)
    assert new_path.path == "r"


def test_add_direction_left(start_path):
    new_path = start_path + (0, -1)
    assert new_path.path == "l"


def test_add_direction_up(start_path):
    new_path = start_path + (-1, 0)
    assert new_path.path == "u"


def test_add_direction_down(start_path):
    new_path = start_path + (1, 0)
    assert new_path.path == "d"


def test_add_multiple_directions(start_path):
    new_path = start_path + (0, 1) + (0, 1)
    assert new_path.path == "rr"