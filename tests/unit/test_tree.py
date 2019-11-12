from app.models.node import Node
from app.models.tree import Tree


class TestTree:
    tree = Tree("start")

    def test_init_tree(self):
        assert type(self.tree.root) is Node
        assert self.tree.root.data == "start"

    def test_add_node_left(self):
        self.tree.add_node(position=[], direction=(-1, 0), value='path')
        assert type(self.tree.root.left) is Node
        assert self.tree.root.left.data == "path"
        assert self.tree.root.left.right.data == "start"
        assert type(self.tree.root.left.right) is Node

    def test_add_node_right(self):
        self.tree.add_node(position=[], direction=(1, 0), value='path')
        assert type(self.tree.root.right) is Node
        assert self.tree.root.right.data == "path"
        assert self.tree.root.right.left.data == "start"
        assert type(self.tree.root.right.left) is Node

    def test_add_node_up(self):
        self.tree.add_node(position=[], direction=(0, 1), value='path')
        assert type(self.tree.root.up) is Node
        assert self.tree.root.up.data == "path"
        assert self.tree.root.up.down.data == "start"
        assert type(self.tree.root.up.down) is Node

    def test_add_node_down(self):
        self.tree.add_node(position=[], direction=(0, -1), value='path')
        assert type(self.tree.root.down) is Node
        assert self.tree.root.down.data == "path"
        assert self.tree.root.down.up.data == "start"
        assert type(self.tree.root.down.up) is Node