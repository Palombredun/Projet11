import pytest

from app.models.path import Path


@pytest.fixture(scope="module")
def start_path():
    current = Path("")
    return current

def test_init_path(start_path):
    assert type(start_path) == Path

def test_init_path_wrong_type(start_path):
    with pytest.raises(TypeError):
        path = Path(562)

def test_add_direction_wrong_type(start_path):
    with pytest.raises(TypeError):
        new_path = start_path + "toto"

def test_add_direction_wrong_length(start_path):
    with pytest.raises(ValueError):
        new_path = start_path + (0, 1, 1)

def test_add_direction_wrong_direction_types(start_path):
    with pytest.raises(TypeError):
        new_path = start_path + ('a', 'b')

def test_add_direction_wrong_direction_values(start_path):
    with pytest.raises(ValueError):
        new_path = start_path + (99, 99)

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