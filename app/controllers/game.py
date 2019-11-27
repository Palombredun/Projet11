from random import choice, choices, randint

from app.models.labyrinth import Labyrinth
from app.models.hero import Hero


class Game:
    def __init__(self):
        self.victory = False
        self.path_enemy = str()
        self.path_objects = {}
        self.path_used = []

    def place_enemy(self, leaves: list):
        if len(leaves) < 4:
            index = choice(len(leaves[0]))
            self.path_enemy = leaves[:index]
            self.path_used.append(self.path_enemy)
        else:
            self.path_enemy = ''.join(choices(leaves))
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
                self.path_objects[obj] = self.draw_path(leaves, 1)
            elif len(leaves) == 2:
                self.path_objects[obj] = self.draw_path(leaves, 2)
            else:
                self.path_objects[obj] = self.draw_path(leaves, 3)

    def draw_path(self, leaves: list, nb_leaves: int):
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
        if nb_leaves == 3:
            while True:
                path = choice(leaves)
                if path not in self.path_used:
                    break
            return path

        i = randint(0, nb_leaves-1)
        path = ""
        while True:
            index = randint(0, len(leaves[i]))
            path = leaves[i][:index]
            if path not in self.path_used:
                break
        return path


    def test_victory(self, hero):
        if (hero.path == self.path_enemy) and (
            hero.items == {"needle", "tube", "ether"}
        ):
            return True
        else:
            return False
