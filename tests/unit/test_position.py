from app.models.position import Position


class TestPosition:
    position = Position(0, 0)

    def test_init_position(self):
        assert self.position.x == 0
        assert self.position.y == 0

    def test_position_up(self):
        new_position = self.position.up()
        assert new_position.x == -1
        assert new_position.y == 0

    def test_position_down(self):
        new_position = self.position.down()
        assert new_position.x == 1
        assert new_position.y == 0

    def test_position_left(self):
        new_position = self.position.left()
        assert new_position.x == 0
        assert new_position.y == -1

    def test_position_right(self):
        new_position = self.position.right()
        assert new_position.x == 0
        assert new_position.y == 1

    def test_add_position(self):
        new_position = self.position + (0, 1)
        assert new_position.x == 0
        assert new_position.y == 1
