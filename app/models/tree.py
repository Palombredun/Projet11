from .node import Node


class Tree:
    def __init__(self, value):
        """
        Creates an object Tree, made of Nodes (with 4 directions).
        """
        self.root = Node(value)
        self.leaves = list()

    def huffman_traversal(self, path: str) -> Node:
        """
        input : position of the current node
        output : node at the position in parameter
        The function is based on the huffman decoding algorithm, thus its name
        """
        if type(path) is not str:
            raise TypeError("path is not a string")

        current = self.root

        if not path:
            return current

        for branch in path:

            if not current:
                raise ValueError("Error in the path : {} is not valid", branch)

            if branch == "l":
                current = current.left
            elif branch == "r":
                current = current.right
            elif branch == "u":
                current = current.up
            elif branch == "d":
                current = current.down
            else:
                raise ValueError("Wrong direction")
        return current

    def add_node(self, path: str, direction: tuple, value: str) -> None:
        """
        input : 
            - path of the node to add
            - direction of the new node
            - value of the node
        output: None
        Adds a new node at the path in parameter, in the direction
        given, with the value (type of the square)
        """
        if type(path) is not str:
            raise TypeError("path is not a str")
        if type(direction) is not tuple:
            raise TypeError("direction is not a tuple")
        if type(direction[0]) is not int or type(direction[1]) is not int:
            raise TypeError("One of the elements of direction is not an int")
        if direction not in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            raise ValueError("Wrong value for the direction")
        if type(value) is not str:
            raise TypeError("Wrong type for the value")

        current = self.huffman_traversal(path)

        new_node = Node(value)

        if direction == (0, -1):
            current.left = new_node
            new_node.right = current
        elif direction == (0, 1):
            current.right = new_node
            new_node.left = current
        elif direction == (-1, 0):
            current.up = new_node
            new_node.down = current
        elif direction == (1, 0):
            current.down = new_node
            new_node.up = current