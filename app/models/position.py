
class Position:
    def __init__(self, x: int, y: int) -> None:
        """
        Creates an object Position, used temporarily for constructing 
        the labyrinth.
        """
        if type(x) is not int or type(y) is not int:
            raise TypeError("Wrong type for x or y")
            
        self.x = x
        self.y = y

    def __str__(self):
        string = "(" + str(self.x) + ", " + str(self.y) + ")"
        return string

    def __add__(self, direction: tuple) -> "Position":
        """
        input :
        a tuple direction, contained in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        which matches a direction (left, right, up, down). 
        """

        x = self.x + direction[0]
        y = self.y + direction[1]
        new_position = Position(x, y)
        return new_position
