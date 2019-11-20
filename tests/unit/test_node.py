import pytest

from app.models.node import Node


class TestNode:
    @pytest.fixture(scope="class")
    def base_node(self):
        return Node("foo")

    def test_create_node(self, base_node):
        assert base_node.data == "foo"
        assert base_node.left == None
        assert base_node.right == None
        assert base_node.up == None
        assert base_node.down == None

    def test_change_node_data(self, base_node):
        base_node.data = "bar"
        assert base_node.data == "bar"

    def test_connect_node_on_left(self, base_node):
        new_node = Node("bar")
        base_node.left = new_node
        assert base_node.left == new_node

    def test_connect_node_on_right(self, base_node):
        new_node = Node("bar")
        base_node.right = new_node
        assert base_node.right == new_node

    def test_connect_node_on_up(self, base_node):
        new_node = Node("bar")
        base_node.up = new_node
        assert base_node.up == new_node

    def test_connect_node_on_down(self, base_node):
        new_node = Node("bar")
        base_node.down = new_node
        assert base_node.down == new_node
