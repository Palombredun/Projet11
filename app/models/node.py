class Node:
    def __init__(self, data: str):
        self.data = data
        self.right = None
        self.left = None
        self.up = None
        self.down = None

    def __str__(self):
        return self.data
