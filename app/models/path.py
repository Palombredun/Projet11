class Path:
    def __init__(self, path: list) -> 'Path':
        self.path = path

    def __add__(self, direction: tuple) -> "Position":
        if direction == (1, 0):
            self.path.append("d")
        elif direction == (-1, 0):
            self.path.append("u")
        elif direction == (0, -1):
            self.path.append("l")
        elif direction == (0, 1):
            self.path.append("r")
        else:
            raise ValueError("Wrong direction")
        return self