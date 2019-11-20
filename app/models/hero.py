# from .position import Position
from .path import Path


class Hero:
    def __init__(self):
        self.path = Path("")
        self.items = set()

    def add_item(self, item):
        if item in ["needle", "tube", "ether"]:
            self.items.add(item)
        else:
            raise ValueError("This item is not needed")
