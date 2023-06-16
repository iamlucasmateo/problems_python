class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, root: Node):
        self.root = root


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

tree = Tree(root=a)


#         a
#        / \
#       b   c
#      / \   \
#     d   e   f

# Depth first: a, b, d, e, c, f
def get_depth_first_values(tree: Tree):
    values = []
    stack = []
    current_node = tree.root
    stack.append(current_node)
    while len(stack) > 0:
        values.append(current_node.value)
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)
        current_node = stack.pop()
    
    return values

# Breadth first: a, b, c, d, e, f

