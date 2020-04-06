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
        if not self.path:
            if isinstance(direction, tuple):
                if direction == (-1, 0):
                    new_path = self.path + 'd'
    
                if direction == (1, 0):
                    new_path = self.path + 'u'
        
                if direction == (0, -1):
                    new_path = self.path + 'l'
        
                if direction == (0, 1):
                    new_path = self.path + 'r'
            elif isinstance(direction, str):
                new_path = self.path + direction
            return Path(new_path)
        
        if isinstance(direction, tuple):
            #up
            if direction == (1, 0):
                if self.path[-1] == 'd':
                    return Path(self.path[:-1])
                return Path(self.path + "u")
            
            #down
            elif direction == (-1, 0):
                if self.path[-1] == 'u':
                    return Path(self.path[:-1])
                return Path(self.path + "d")

            #left
            elif direction == (0, -1):
                if self.path[-1] == "r":
                    return Path(self.path[:-1])
                return Path(self.path + 'l')
            
            #right
            elif direction == (0, 1):
                if self.path[-1] == "l":
                    return Path(self.path[:-1])
                return Path(self.path + 'r')

        elif isinstance(direction, str):
            if direction == "u":
                if self.path[-1] == "d":
                    new_path = self.path[:-1]
                else:
                    new_path = self.path + direction
            
            elif direction == "d":
                if self.path[-1] == "u":
                    new_path = self.path[:-1]
                else:
                    new_path = self.path + direction
            
            elif direction == "l":
                if self.path[-1] == "r":
                    new_path = self.path[:-1]
                else:
                    new_path = self.path + direction
            
            elif direction == "r":
                if self.path[-1] == "l":
                    new_path = self.path[:-1]
                else:
                    new_path = self.path + direction
            return Path(new_path)

    def __str__(self):
        return self.path

    def __len__(self):
        return len(self.path)