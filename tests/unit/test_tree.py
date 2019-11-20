import pytest

from app.models.node import Node
from app.models.tree import Tree


class TestTree:
    @pytest.fixture(scope="class")
    def basic_tree(self):
        tree = Tree("start")
        return tree

    def test_init_tree(self, basic_tree):
        assert type(basic_tree.root) is Node
        assert basic_tree.root.data == "start"

    def test_huffman_traversal(self, basic_tree):
        basic_tree.add_node(path="", direction=(0, -1), value="path")
        basic_tree.add_node(path="l", direction=(0, -1), value="path")
        basic_tree.add_node(path="ll", direction=(-1, 0), value="path")
        basic_tree.add_node(path="llu", direction=(-1, 0), value="path")
        current = basic_tree.huffman_traversal("lluu")
        assert current.data == "path"

    def test_add_node_left(self, basic_tree):
        basic_tree.add_node(path="", direction=(0, -1), value="path")
        assert type(basic_tree.root.left) is Node
        assert basic_tree.root.left.data == "path"
        assert basic_tree.root.left.right.data == "start"
        assert type(basic_tree.root.left.right) is Node

    def test_add_node_right(self, basic_tree):
        basic_tree.add_node(path="", direction=(0, 1), value="path")
        assert type(basic_tree.root.right) is Node
        assert basic_tree.root.right.data == "path"
        assert basic_tree.root.right.left.data == "start"
        assert type(basic_tree.root.right.left) is Node

    def test_add_node_up(self, basic_tree):
        basic_tree.add_node(path="", direction=(-1, 0), value="path")
        assert type(basic_tree.root.up) is Node
        assert basic_tree.root.up.data == "path"
        assert basic_tree.root.up.down.data == "start"
        assert type(basic_tree.root.up.down) is Node

    def test_add_node_down(self, basic_tree):
        basic_tree.add_node(path="", direction=(1, 0), value="path")
        assert type(basic_tree.root.down) is Node
        assert basic_tree.root.down.data == "path"
        assert basic_tree.root.down.up.data == "start"
        assert type(basic_tree.root.down.up) is Node
