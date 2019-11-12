from random import choice

# import config.settings as constants

from .tree import Tree
from .position import Position
from .path import Path


class Labyrinth:
    def __init__(self):
        self.length = 15
        self.width = 15
        self.tree = Tree("P")
        self.generate_labyrinth(self.length, self.width)

    def _has_unvisited_neighbors(
        self, cell: list, length: int, width: int, visited_cells: set
    ) -> list:
        directions = [
            (cell[0] + x, cell[1] + y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if cell[0] + x < length
            if cell[0] + x >= 0
            if cell[1] + y < width
            if cell[1] + y >= 0
            if abs(x) + abs(y) not in [0, 2]
        ]
        unvisited_directions = []
        for direction in directions:
            if direction not in visited_cells:
                unvisited_directions.append(direction)
        return unvisited_directions

    def generate_labyrinth(self, length: int, width: int) -> Tree:
        """
        input :
        - length of the labyrinth
        - width of the labyrinth

        output :
        The structure of a labyrinth as a Tree composed of nodes with 4 branches
        (one for each direction). It is randomly generated based on
        """
        unvisited_cells = set([(x, y) for x in range(length) for y in range(width)])
        visited_cells = set()
        stack = []
        current = Position()

        while len(visited_cells) < length * width:
            directions = self._has_unvisited_neighbors(
                current.coordinates, length, width, visited_cells
            )
            if len(directions) > 0:
                next_direction = choice(directions)
                if len(directions) > 1:
                    stack.append(current.coordinates)
                self.tree.add_node(current.path, next_direction, "P")
                current = current.__add__(current, next_direction)
            elif stack:
                current = stack.pop()


if __name__ == "__main__":
    lab = Labyrinth()
