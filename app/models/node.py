class Node:
    def __init__(self, data: str) -> "Node":
        """
        Creates an object Node, which contains 4 directions and a attribute data.
        The 4 directions are later used to be linked to other nodes.
        """
        
        self.data = data
        self.right = None
        self.left = None
        self.up = None
        self.down = None

    def __str__(self):
        return str(self.data)
