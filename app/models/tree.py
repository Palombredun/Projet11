from .node import Node


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def huffman_traversal(self, path: list) -> Node:
        """
        input : position of the current node
        output : node at the position in parameter

        The function is based on the huffman decoding algorithm, thus its name
        """
        current = self.root
        for cell in path:
            if cell == "l":
                current = current.left
            elif cell == "r":
                current = current.right
            elif cell == "u":
                current = current.up
            elif cell == "d":
                current = current.down
            else:
                raise ValueError("Wrong direction")
        return current

    def add_node(self, position: list, direction: tuple, value: str) -> None:
        """
        input : 
            - position of the node to add
            - direction of the new node
            - value of the node
        output: None

        Adds a new node at the position in parameter, in the direction
        given, with the value (type of the square)
        """
        current = self.huffman_traversal(position)
        new_node = Node(value)
        if direction == (-1, 0):
            current.left = new_node
            new_node.right = current
        elif direction == (1, 0):
            current.right = new_node
            new_node.left = current
        elif direction == (0, 1):
            current.up = new_node
            new_node.down = current
        elif direction == (0, -1):
            current.down = new_node
            new_node.up = current

    def inorderTraversal(self, root):
        if root:
            print(root.data)
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
            self.inorderTraversal(root.up)
            self.inorderTraversal(root.down)
