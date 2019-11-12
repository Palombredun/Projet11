from .position import Position


class Hero(Position):
    def __init__(self, position: list = []):
        super().__init__(position)
        self.items = set()

    def up(self):
        return self.position.append("u")

    def down(self):
        return self.position.append("d")

    def right(self):
        return self.position.append("r")

    def left(self):
        return self.position.append("l")

    def add_item(self, item):
        if item in ["needle", "tube", "ether"]:
            self.items.add(item)
