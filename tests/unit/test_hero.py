from app.models.hero import Hero
from app.models.position import Position

class TestHero:
    hero = Hero()

    def test_start_at_root(self):
        assert self.hero.position == []
        assert self.hero.items == set()

    def test_movement_left(self):
        self.hero.left()
        assert self.hero.position == ['l']

    def test_movement_right(self):
        self.hero.position = []
        self.hero.right()
        assert self.hero.position == ['r']

    def test_movement_up(self):
        self.hero.position = []
        self.hero.up()
        assert self.hero.position == ['u']

    def test_movement_down(self):
        self.hero.position = []
        self.hero.down()
        assert self.hero.position == ['d']

    def test_add_item(self):
        self.hero.add_item('ether')
        assert self.hero.items == {'ether'}