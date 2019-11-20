from random import choice, seed

import config.settings as constants

from .position import Position
from .path import Path
from .tree import Tree

import config.settings as constants


class Labyrinth:
    def __init__(self):
        self.length = constants.LENGTH
        self.width = constants.WIDTH
        self.maze = Tree("p")

        self.generate_labyrinth()

    def _has_unvisited_neighbors(self, cell: "Position", visited_cells: set) -> list:
        """
        input :
          - the current position
          - the visited cells in the grid
        output :
          - all directions (minimum 0, maximum 3) where there is a cell available
        A cell is considered available if its position is comprised between 0 (included)
        and self.length or self.width respectively. It must also not be part of the
        visited_cells set.
        """
        unvisited_directions = []

        if (cell.x - 1, cell.y) not in visited_cells and cell.x - 1 >= 0:
            unvisited_directions.append((-1, 0))
        
        if (cell.x + 1, cell.y) not in visited_cells and cell.x + 1 < self.length:
            unvisited_directions.append((1, 0))

        if (cell.x, cell.y - 1) not in visited_cells and cell.y - 1 >= 0:
            unvisited_directions.append((0, -1))

        if (cell.x, cell.y + 1) not in visited_cells and cell.y + 1 < self.width:
            unvisited_directions.append((0, 1))

        return unvisited_directions

    def generate_labyrinth(self) -> Tree:
        """
        output :
        The structure of a labyrinth as a Tree composed of nodes with 4 branches
        (one for each direction). It is randomly generated based on
        """
        visited_cells = set()
        current_pos = Position(0, 0)
        current_path = Path("")
        stack = [(current_pos, current_path)]

        while len(stack) > 0:
            
            directions = self._has_unvisited_neighbors(current_pos, visited_cells)
            if directions:

                next_direction = choice(directions)
                if len(directions) > 1:
                    stack.append((current_pos, current_path))
                    _stack_.append((current_pos.x, current_pos.y))
                
                self.maze.add_node(current_path.path, next_direction, "p")
                
                visited_cells.add((current_pos.x, current_pos.y))
                current_pos += next_direction
                current_path += next_direction
            else:
                current_pos, current_path = stack.pop()


if __name__ == "__main__":
    lab = Labyrinth()