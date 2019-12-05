from random import choice

import config.settings as constants

from .position import Position
from .path import Path
from .tree import Tree

import config.settings as constants


class Labyrinth:
    def __init__(self):
        """
        Creates a labyrinth based on the recursive backtracker algorithm.
        """
        self.length = constants.LENGTH
        self.width = constants.WIDTH
        self.tree = Tree("p")

        self.create()

    def create(self):
        """
        output :
        The structure of a labyrinth as a Tree composed of nodes with 4 branches
        (one for each direction). It is randomly generated based on
        """
        pos = Position(0, 0)
        path = Path("")
        visited_cells = set()
        visited_cells.add((pos.x, pos.y))
        grid = set([(x, y) for x in range(self.length) for y in range(self.width)])
        stack = [(pos.x, pos.y)]
        leaves = set()

        while stack:
            directions = []        
            if (pos.x - 1, pos.y) not in visited_cells and (pos.x - 1, pos.y) in grid:
                directions.append((-1, 0))
            if (pos.x + 1, pos.y) not in visited_cells and (pos.x + 1, pos.y) in grid:
                directions.append((1, 0))
            if (pos.x, pos.y - 1) not in visited_cells and (pos.x, pos.y - 1) in grid:
                directions.append((0, -1))
            if (pos.x, pos.y + 1) not in visited_cells and (pos.x, pos.y + 1) in grid:
                directions.append((0, 1))

            if len(directions) > 0: 
                next_dir = choice(directions)
                self.tree.add_node(path.path, next_dir, "p")
                pos += next_dir
                path += next_dir

                visited_cells.add((pos.x, pos.y))
                stack.append((pos, path))
            
            else:
                leaves.add(path.path)
                pos, path = stack.pop()

        self.tree.leaves= list(leaves)