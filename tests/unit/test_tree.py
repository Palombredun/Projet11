import pytest

from app.models.node import Node
from app.models.tree import Tree


@pytest.fixture(scope="module")
def basic_tree():
    tree = Tree("start")
    return tree


def test_init_tree(basic_tree):
    assert type(basic_tree.root) is Node
    assert basic_tree.root.data == "start"
    assert basic_tree.leafs == set()


def test_huffman_traversal(basic_tree):
    basic_tree.add_node(path="", direction=(0, -1), value="path")
    basic_tree.add_node(path="l", direction=(0, -1), value="path")
    basic_tree.add_node(path="ll", direction=(-1, 0), value="path")
    basic_tree.add_node(path="llu", direction=(-1, 0), value="path")
    current = basic_tree.huffman_traversal("lluu")
    assert current.data == "path"


def test_huffman_traversal_wrong_path_type(basic_tree):
    with pytest.raises(TypeError):
        basic_tree.huffman_traversal(255)


def test_huffman_traversal_wrong_path(basic_tree):
    basic_tree.add_node(path="", direction=(0, -1), value="path")
    basic_tree.add_node(path="l", direction=(0, -1), value="path")
    basic_tree.add_node(path="ll", direction=(-1, 0), value="path")
    basic_tree.add_node(path="llu", direction=(-1, 0), value="path")
    with pytest.raises(ValueError):
        current = basic_tree.huffman_traversal("lduu")


def test_add_node_left(basic_tree):
    basic_tree.add_node(path="", direction=(0, -1), value="path")
    assert type(basic_tree.root.left) is Node
    assert basic_tree.root.left.data == "path"
    assert basic_tree.root.left.right.data == "start"
    assert type(basic_tree.root.left.right) is Node


def test_add_node_right(basic_tree):
    basic_tree.add_node(path="", direction=(0, 1), value="path")
    assert type(basic_tree.root.right) is Node
    assert basic_tree.root.right.data == "path"
    assert basic_tree.root.right.left.data == "start"
    assert type(basic_tree.root.right.left) is Node


def test_add_node_up(basic_tree):
    basic_tree.add_node(path="", direction=(-1, 0), value="path")
    assert type(basic_tree.root.up) is Node
    assert basic_tree.root.up.data == "path"
    assert basic_tree.root.up.down.data == "start"
    assert type(basic_tree.root.up.down) is Node


def test_add_node_down(basic_tree):
    basic_tree.add_node(path="", direction=(1, 0), value="path")
    assert type(basic_tree.root.down) is Node
    assert basic_tree.root.down.data == "path"
    assert basic_tree.root.down.up.data == "start"
    assert type(basic_tree.root.down.up) is Node
