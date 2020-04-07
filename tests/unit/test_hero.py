import pytest

from app.models.hero import Hero
from app.models.path import Path


class TestHero:
    @pytest.fixture(scope="function", autouse=True)
    def base_hero(self):
        return Hero()

    def test_init_hero(self, base_hero):
        assert base_hero.path.path == ""
        assert base_hero.items == 0

    def test_add_item(self, base_hero):
        base_hero.items += 1
        assert base_hero.items == 1