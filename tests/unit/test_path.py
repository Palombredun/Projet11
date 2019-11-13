import pytest

from app.models.path import Path


class TestPath:
    current = Path([])

    def test_init_path(self):
        assert self.current.path == []

    def test_append_path(self):
        self.current.path.append("l")
        assert self.current.path == ["l"]

    def test_add_direction_right(self):
        current = Path([])
        current += (0, 1)
        assert current.path == ["r"]

    def test_add_direction_left(self):
        current = Path([])
        current += (0, -1)
        assert current.path == ["l"]

    def test_add_direction_up(self):
        current = Path([])
        current += (-1, 0)
        assert current.path == ["u"]

    def test_add_direction_down(self):
        current = Path([])
        current += (1, 0)
        assert current.path == ["d"]

    def test_wrong_direction(self):
        current = Path([])
        with pytest.raises(ValueError):
            current += "toto"
            assert current.path == []