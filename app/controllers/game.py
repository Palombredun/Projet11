from random import choice, choices

from app.models.labyrinth import Labyrinth
from app.models.hero import Hero


class Game:
    def __init__(self):
        self.path_enemy = None
        self.path_objects = {}
        self.is_victory = False

    def place_enemy(self, maze: "Labyrinth"):
        self.path_enemy = choice(maze.leafs)
        if len(maze.leafs) == 1:
            maze.leafs = maze.leafs[:-1]
        else:
            maze.leafs.remove(self.path_enemy)

    def place_objects(self, maze: "Labyrinth"):
        if len(maze.leafs) == 1:
            path = maze.leafs[0]
            indexes = choices(range(0, len(path)), k=3)
            self.path_objects['ether'] = path[: indexes[0]]
            self.path_objects['tube'] = path[:indexes[1]]
            self.path_objects['needle'] = path[:indexes[2]]
        else:
            indexes = choices(maze.leafs)
            self.path_objects['ether'] = path[indexes]
            self.path_objects['tube'] = path[indexes]
            self.path_objects['needle'] = path[indexes]

    def test_victory(self, hero):
        if (hero.path == self.path_enemy) and (
            hero.items == {"needle", "tube", "ether"}
        ):
            return True
        else:
            return False
