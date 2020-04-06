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
        current = self.root

        if not path:
            return current

        for branch in path:
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
        current = self.huffman_traversal(path)

        new_node = Node(value)

        if direction == (0, -1):
            current.left = new_node
            new_node.right = current
        elif direction == (0, 1):
            current.right = new_node
            new_node.left = current
        elif direction == (-1, 0):
            current.down = new_node
            new_node.up = current
        elif direction == (1, 0):
            current.up = new_node
            new_node.down = current

    def is_leaf(self, path: str) -> bool:
        if path == "":
            return False

        node = self.huffman_traversal(path)

        if node.left and not node.right and not node.up and not node.down:
            return True
        elif node.up and not node.left and not node.right and not node.down:
            return True
        elif node.right and not node.left and not node.up and not node.down:
            return True
        elif node.down and not node.left and not node.right and not node.up:
            return True
        else:
            return False
