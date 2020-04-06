from random import choice, choices, randint

from app.models.labyrinth import Labyrinth
from app.models.hero import Hero


class Game:
    def __init__(self):
        self.victory = False
        self.defeat = False
        self.path_enemy = str()
        self.needle = ""
        self.tube = ""
        self.ether = ""
        self.path_used = []

    def place_enemy(self, leaves: list):
        """
        input : all the paths to the leaves in the labyrinth
        Appends path_used with the path drawn, preventing it to be used later
        """
        self.path_enemy = choices(leaves)[0]
        self.path_used.append(self.path_enemy)

    def place_objects(self, leaves: list):
        """
        Remove the path drawn for the enemy
        Draw 3 paths among the list leaves for the objects
        """
        tmp = leaves[:]
        tmp.remove(self.path_used[0])
        self.needle, self.tube, self.ether = choices(tmp, k=3)


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

    def test_victory(hero: "Hero") -> bool:
        if hero.path == self.path_enemy and len(hero.items) == 3:
            return True
        else:
            return False

    def test_defeat(self, hero: "Hero") -> bool:
        if hero.path == self.path_enemy and len(hero.items) < 3:
            return True
        else:
            return False

    def test_item(self, hero: "Hero"):
        """
        If the hero's path equals one of the objects, delete it from
        the dictionnary and return True. Else, return False.
        """
        key_list = list(self.path_items.keys())
        val_list = list(self.path_items.values())

        if hero.path in val_list:
            key = key_list[val_list.index(hero.path)]
            del self.path_items[key]
            return True
        else:
            return False
