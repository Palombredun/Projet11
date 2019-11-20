from .node import Node


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def huffman_traversal(self, path: str) -> Node:
        """
        input : position of the current node
        output : node at the position in parameter

        The function is based on the huffman decoding algorithm, thus its name
        """
        current = self.root
        print(path)
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

    def add_node(self, path: str, direction: str, value: str) -> None:
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
            current.up = new_node
            new_node.down = current
        elif direction == (1, 0):
            current.down = new_node
            new_node.up = current

    def inorderTraversal(self, root):
        if root:
            print(root.data)
            self.inorderTraversal(root.right)
            self.inorderTraversal(root.down)
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.up)