# from .position import Position
from .path import Path


class Hero(Path):
    def __init__(self, path: list = []):
        super().__init__(path)
        self.items = set()

    def add_item(self, item):
        if item in ["needle", "tube", "ether"]:
            self.items.add(item)
