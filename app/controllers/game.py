from random import choice, choice, randint

from app.models.labyrinth import Labyrinth
from app.models.hero import Hero


class Game:
    def __init__(self):
        self.victory = False
        self.defeat = False
        self.path_enemy = ""
        self.needle = ""
        self.tube = ""
        self.ether = ""
        self.path_used = []

    def convert(self, path: str):
        i, j = 0, 0
        for direction in path:
            if direction == "l":
                i += -1
            elif direction == "r":
                i += 1
            elif direction == "d":
                j += -1
            elif direction == "u":
                j += 1
        return i, j

    def place_enemy(self, leaves: list):
        """
        input : all the paths to the leaves in the labyrinth
        Appends path_used with the path drawn, preventing it to be used later
        """
        self.path_enemy = choice(leaves)
        self.path_used.append(self.path_enemy)

    def place_objects(self, leaves: list):
        """
        Remove the path drawn for the enemy
        Draw 3 paths among the list leaves for the objects
        """
        tmp = leaves[:]
        tmp.remove(self.path_used[0])
        self.needle = choice(tmp)
        tmp.remove(self.needle)
        self.tube = choice(tmp)
        tmp.remove(self.tube)
        self.ether = choice(tmp)

    def test_position(self, tree: "Tree", hero: "Hero", direction: str):
        current = tree.huffman_traversal(hero.path.path)

        if direction == "l":
            if current.left:
                return True
            else:
                return False
        elif direction == "r":
            if current.right:
                return True
            else:
                return False
        elif direction == "u":
            if current.up:
                return True
            else:
                return False
        elif direction == "d":
            if current.down:
                return True
            else:
                return False

    def test_victory(self, hero: "Hero") -> bool:
        coord_hero = self.convert(hero.path.path)
        coord_enemy = self.convert(self.path_enemy)

        if coord_hero == coord_enemy and hero.items == 3:
            return True
        elif coord_hero == coord_enemy and hero.items != 3:
            return "defeat"
        else:
            return False

    def test_item(self, hero: "Hero"):
        """
        If the hero's path equals one of the objects, delete it from
        the dictionnary and return True. Else, return False.
        """
        path_items = [self.ether, self.needle, self.tube]

        if hero.path in path_items:
            return True
        else:
            return False
