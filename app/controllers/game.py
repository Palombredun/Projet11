from random import choice, choices

from app.models.labyrinth import Labyrinth
from app.models.hero import Hero


class Game:
    def __init__(self):
        self.path_enemy = None
        self.path_objects = {}
        self.victory = False
        self.path_used = []

    def place_enemy(self, maze: "Labyrinth"):
        if len(maze.leafs) < 4:
            index = choice(len(maze.leafs[0]))
            self.path_enemy = maze.leafs[:index]
            self.path_used.append(self.path_enemy)
        else:
            self.path_enemy = ''.join(choices(maze.leafs))
            self.path_used.append(self.path_enemy)


    def place_objects(self, maze: "Labyrinth"):
        """
        If there is only one path, draw the position of the position between
        the start and the position in front of the enemy.
        If the number of leafs is equal to 2 or 3, draw the path of the objects
        in their path.
        Else, the objects are placed on a leaf of the tree.
        """

        if len(maze.leafs) == 1:
            self.path_objects['ether'] = self.draw_path(maze.leafs, 1)
            self.path_objects['needle'] = self.draw_path(maze.leafs, 1)
            self.path_objects['tube'] = self.draw_path(maze.leafs, 1)
        elif len(maze.leafs) == 2:
            self.path_objects['ether'] = self.draw_path(maze.leafs, 2)
            self.path_objects['needle'] = self.draw_path(maze.leafs, 2)
            self.path_objects['tube'] = self.draw_path(maze.leafs, 2)
        elif len(maze.leafs) == 3:
            self.path_objects['ether'] = self.draw_path(maze.leafs, 3)
            self.path_objects['needle'] = self.draw_path(maze.leafs, 3)
            self.path_objects['tube'] = self.draw_path(maze.leafs, 3)
        else:
            # CHOIX
        
        elif len(maze.leafs) == 3:
            leaf = choice([1, 2, 3])
            if leaf == 1:
                index = choice(range(0, len(maze.leafs[0])))
                self.path_objects["ether"] = maze.leafs[0][:index]
            elif leaf == 2:
                index = choice(range(0, len(maze.leafs[1])))
                self.path_objects["ether"] = maze.leafs[1][:index]
            else:
                index = choice(range(0, len(maze.leafs[1])))
                self.path_objects["ether"] = maze.leafs[1][:index]

            leaf = choice([1, 2, 3])
            if leaf == 1:
                index = choice(range(0, len(maze.leafs[0])))
                self.path_objects["ether"] = maze.leafs[0][:index]
            elif leaf == 2:
                index = choice(range(0, len(maze.leafs[1])))
                self.path_objects["ether"] = maze.leafs[1][:index]
            else:
                index = choice(range(0, len(maze.leafs[1])))
                self.path_objects["ether"] = maze.leafs[1][:index]

            leaf = choice([1, 2, 3])
            if leaf == 1:
                index = choice(range(0, len(maze.leafs[0])))
                self.path_objects["ether"] = maze.leafs[0][:index]
            elif leaf == 2:
                index = choice(range(0, len(maze.leafs[1])))
                self.path_objects["ether"] = maze.leafs[1][:index]
            else:
                index = choice(range(0, len(maze.leafs[1])))
                self.path_objects["ether"] = maze.leafs[1][:index]


        else:
            indexes = choices(maze.leafs)
            self.path_objects["ether"] = path[indexes]
            self.path_objects["tube"] = path[indexes]
            self.path_objects["needle"] = path[indexes]

    def test_victory(self, hero):
        if (hero.path == self.path_enemy) and (
            hero.items == {"needle", "tube", "ether"}
        ):
            return True
        else:
            return False
