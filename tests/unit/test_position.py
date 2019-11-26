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