from random import choice

import config.settings as constants

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

    def in_limits(self, cell):
        if (cell[0] < self.length and cell[0] >= 0) and (
            cell[1] < self.width and cell[1] >= 0
        ):
            return True
        else:
            return False

    def unvisited_neighbors(self, visited_cells, cell):
        neighbors = []
        possibilities = [
            (cell[0] - 1, cell[1]),
            (cell[0] + 1, cell[1]),
            (cell[0], cell[1] - 1),
            (cell[0], cell[1] + 1),
        ]

        for cell in possibilities:
            if cell not in visited_cells and self.in_limits(cell):
                neighbors.append(cell)
        return neighbors

    def create(self):
        """
        output :
        The structure of a labyrinth as a Tree composed of nodes with 4 branches
        (one for each direction). It is randomly generated based on
        """
        start = (0, 0)
        path = Path("")
        visited_cells = set()
        visited_cells.add(start)
        stack = [
            (start, path),
        ]

        while stack:
            curr, path = stack.pop()
            neighbors = self.unvisited_neighbors(visited_cells, curr)
            if neighbors:
                stack.append((curr, path))
                chosen = choice(neighbors)
                direction = (chosen[0] - curr[0], chosen[1] - curr[1])
                self.tree.add_node(path.path, direction, "p")
                path += direction
                visited_cells.add(chosen)
                curr = chosen
                stack.append((curr, path))
            else:
                if self.tree.is_leaf(path.path):
                    self.tree.leaves.append(path.path)
