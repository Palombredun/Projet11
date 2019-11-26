class Path:
    def __init__(self, path: str) -> "Path":
        """
        Creates an object Path, used to translate the movement
        of the hero in the tree with the huffman decoding method.
        """
        if type(path) is not str:
            raise TypeError("Wrong type for the path")

        self.path = path

    def __add__(self, direction: tuple) -> "Path":
        if type(direction) is not tuple:
            raise TypeError("Wrong type for the direction")

        if len(direction) != 2:
            raise ValueError("Wrong number of arguments for the direction")

        if type(direction[0]) is not int or type(direction[1]) is not int:
            raise TypeError("Wrong type for one of the value of the direction")

        if direction not in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            raise ValueError("Wrong direction")

        if direction == (1, 0):
            new_path = self.path + "d"
            return Path(new_path)
        elif direction == (-1, 0):
            new_path = self.path + "u"
            return Path(new_path)
        elif direction == (0, -1):
            new_path = self.path + "l"
            return Path(new_path)
        elif direction == (0, 1):
            new_path = self.path + "r"
            return Path(new_path)
        else:
            raise ValueError("Wrong direction")
        return self

    def __str__(self):
        return self.path
