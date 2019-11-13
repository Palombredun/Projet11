from app.models.node import Node


class TestNode:
    node = Node("foo")

    def test_create_node(self):
        assert self.node.data == "foo"
        assert self.node.left == None
        assert self.node.right == None
        assert self.node.up == None
        assert self.node.down == None

    def test_change_node_data(self):
        self.node.data = "bar"
        assert self.node.data == "bar"

    def test_connect_node_on_left(self):
        new_node = Node("bar")
        self.node.left = new_node
        assert self.node.left == new_node

    def test_connect_node_on_right(self):
        new_node = Node("bar")
        self.node.right = new_node
        assert self.node.right == new_node

    def test_connect_node_on_up(self):
        new_node = Node("bar")
        self.node.up = new_node
        assert self.node.up == new_node

    def test_connect_node_on_down(self):
        new_node = Node("bar")
        self.node.down = new_node
        assert self.node.down == new_node
