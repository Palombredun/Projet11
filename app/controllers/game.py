from random import choice, choices, randint

from app.models.labyrinth import Labyrinth
from app.models.hero import Hero


class Game:
    def __init__(self):
        self.victory = False
        self.defeat = False
        self.path_enemy = str()
        self.path_items = {}
        self.path_used = []

    def place_enemy(self, leaves: list):
        """
        input :
            - list of the path to the leaves of the tree
        If the tree possesses less than 4 leaves, the enemy is randomly
        placed on one of them.
        """
        if len(leaves) < 4:
            index = randint(0, len(leaves[0]))
            self.path_enemy = leaves[:index]
            self.path_used.append(self.path_enemy)
        else:
            self.path_enemy = "".join(choices(leaves))
            self.path_used.append(self.path_enemy)

    def place_objects(self, leaves: list):
        """
        If there is only one path, draw the position of the position between
        the start and the position in front of the enemy.
        If the number of leaves is equal to 2 or 3, draw the path of the objects
        in their path.
        Else, the objects are placed on a leaf of the 
        """
        for obj in ["ether", "needle", "tube"]:
            if len(leaves) == 1:
                self.path_items[obj] = self._draw_path(leaves, 1)
            elif len(leaves) == 2:
                self.path_items[obj] = self._draw_path(leaves, 2)
            else:
                self.path_items[obj] = self._draw_path(leaves, 3)

    def _draw_path(self, leaves: list, nb_leaves: int):
        """
        input : 
          - list of leaves
          - number of leaves in the list
        If the number of leaves is equal or superior to three, 
        each object is placed on one of the leaves.
        If this number is smaller, the objects are randomly placed on
        the path of the leaves.
        
        output :
        path chosen randomly, it cannot have been previously drawn.
        """
        if nb_leaves >= 3:
            while True:
                path = choice(leaves)
                if path not in self.path_used:
                    break
            return path

        i = randint(0, nb_leaves - 1)
        path = ""
        while True:
            index = randint(0, len(leaves[i]))
            path = leaves[i][:index]
            if path not in self.path_used:
                break
        return path

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
