import pytest

from app.models.path import Path


class TestPath:
    @pytest.fixture(scope="class")
    def start_path(self):
        current = Path("")
        return current

    def test_init_path(self, start_path):
        assert type(start_path) == Path

    def test_add_direction_right(self, start_path):
        new_path = start_path + (0, 1)
        assert new_path.path == "r"

    def test_add_direction_left(self, start_path):
        new_path = start_path + (0, -1)
        assert new_path.path == "l"

    def test_add_direction_up(self, start_path):
        new_path = start_path + (-1, 0)
        assert new_path.path == "u"

    def test_add_direction_down(self, start_path):
        new_path = start_path + (1, 0)
        assert new_path.path == "d"

    def test_add_multiple_directions(self, start_path):
        new_path = start_path + (0, 1) + (0, 1)
        assert new_path.path == "rr"

    def test_wrong_direction(self, start_path):
        with pytest.raises(ValueError):
            start_path += "toto"
            assert start_path.path == str()
