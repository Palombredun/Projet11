import pytest

from app.models.hero import Hero
from app.models.path import Path


class TestHero:
    @pytest.fixture(scope="function", autouse=True)
    def base_hero(self):
        return Hero()

    def test_init_hero(self, base_hero):
        assert base_hero.path.path == ""
        assert base_hero.items == set()

    def test_add_authorized_item(self, base_hero):
        base_hero.add_item("needle")
        assert base_hero.items == {"needle"}

    def test_add_wrong_item(self, base_hero):
        with pytest.raises(ValueError):
            base_hero.add_item("foo")
            assert base_hero.items == {"needle"}