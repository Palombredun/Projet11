class Path:
    def __init__(self, path: str) -> "Path":
        self.path = path

    def __iadd__(self, direction: tuple) -> "Path":
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