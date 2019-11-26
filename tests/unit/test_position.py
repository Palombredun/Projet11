import pytest

from app.models.position import Position

@pytest.fixture(scope="module")
def base_position():
    return Position(0,0)

def test_init_position(base_position):
    assert base_position.x == 0
    assert base_position.y == 0

def test_add_position_in_y(base_position):
    new_position = base_position + (1, 0)
    assert new_position.x == 1
    assert new_position.y == 0

def test_add_position_in_y(base_position):
    new_position = base_position + (0, -1)
    assert new_position.x == 0
    assert new_position.y == -1

def test_wrong_type_position():
    with pytest.raises(TypeError):
        position = Position('r', 0)

def test_wrong_type_direction(base_position):
    with pytest.raises(TypeError):
        new_position = base_position + ('r', 'r')

def test_wrong_value_direction(base_position):
    with pytest.raises(ValueError):
        new_position = base_position + (50, 50)