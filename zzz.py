from app.models.tree import Tree


tree = Tree('root')

tree.add_node([], 'l', 'path')
print(tree.root.left)
tree.add_node(['l'], 'l', 'wall')
print(tree.root.left.left)
print(tree.root.left.right)