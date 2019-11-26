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
        """
        input :
        a tuple direction, contained in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        which matches a direction (left, right, up, down). 
        It is added to the current path.    
        """
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
