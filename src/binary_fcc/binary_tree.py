from enum import Enum
from typing import Callable, List, Union

from src.linked_list import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        left_null = self.left is None
        right_null = self.right is None 
        return f"Node. Value: {self.value}. Left null: {left_null}. Right null: {right_null}"


class SearchStrategyEnum(str, Enum):
    DEPTH_FIRST = "DEPTH_FIRST"
    BREADTH_FIRST = "BREADTH_FIRST"


class ImplementationStrategyEnum(str, Enum):
    ITERATIVE = "ITERATIVE"
    RECURSIVE = "RECURSIVE"


class Tree:
    def __init__(self, root: Node):
        self.root = root

class TreeSearcher:
    def __init__(self, tree: Tree):
        self.tree = tree

    def get_values(self):
        raise NotImplementedError("Must be implemented by subclass.")


class TreeSearcherIterative(TreeSearcher):
    def _reduce(self):
        raise NotImplementedError("Must be subclassed.")
    
    def get_values(self):
        return self._reduce(self._reduce_get_values, [])

    def _reduce_get_values(self, node: Node, accum):
        return accum + [node.value]

    def sum(self):
        return self._reduce(self._reduce_sum, 0)

    def _reduce_sum(self, node: Node, accum):
        return node.value + accum
    
    def min(self):
        return self._reduce(self._reduce_min, None)
    
    def _reduce_min(self, node: Node, accum):
        if accum == None or node.value < accum:
            return node.value
        return accum


class TreeSearcherDepthIterative(TreeSearcherIterative):
    """This is implemented with a Stack DS.
    
    It's O(N) T (navigates all nodes once), O(N) M (for the stack).
    """
    def get_values_full(self):
        values = []
        stack = []
        current_node = self.tree.root
        stack.append(current_node)
        while len(stack) > 0:
            values.append(current_node.value)
            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)
            current_node = stack.pop()
        
        return values

    def includes(self, value):
        stack = [self.tree.root]
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.value == value:
                return True
            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)

        return False

    def _reduce(self, reduce_func: Callable, accum):
        stack = [self.tree.root]
        while len(stack) > 0:
            current_node = stack.pop()
            accum = reduce_func(current_node, accum)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        
        return accum


class TreeSearcherDepthRecursive(TreeSearcher):
    """This uses recursion to implement the stack (i.e., the call stack is the search stack).
    
    It's O(N) T (navigates all nodes once), O(N) S (for the stack).
    """
    def get_values(self):
        return self._search_node_values(self.tree.root)

    def _search_node_values(self, node: Node) -> list:
        left_values = [] if node.left == None else self._search_node_values(node.left)
        right_values = [] if node.right == None else self._search_node_values(node.right)
        return [node.value] + left_values + right_values

    def includes(self, value):
        return self._node_includes(self.tree.root, value)
    
    def _node_includes(self, node: Node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        
        right_includes = self._node_includes(node.right, value)
        left_includes = self._node_includes(node.left, value)

        return right_includes or left_includes

    def sum(self):
        return self._sum_node(self.tree.root)

    def _sum_node(self, node: Node):
        if node is None:
            return 0
        right_sum = self._sum_node(node.right)
        left_sum = self._sum_node(node.left)

        return node.value + right_sum + left_sum

    def min(self):
        return self._node_min(self.tree.root)
    
    def _node_min(self, node: Node) -> float:
        values = [node.value]
        if node.left is not None:
            values.append(self._node_min(node.left))
        if node.right is not None:
            values.append(self._node_min(node.right))

        return min(values)
    
    def max_root_to_leaf_sum(self):
        return self._max_root_to_leaf_sum_rec(self.tree.root, 0)

    def _max_root_to_leaf_sum_rec(self, node: Node, accum: float):
        new_accum: float = accum + node.value
        
        if node.left is None and node.right is None:
            return new_accum

        if node.left is None:
            return self._max_root_to_leaf_sum_rec(node.right, new_accum)
        
        if node.right is None:
            return self._max_root_to_leaf_sum_rec(node.left, new_accum)
        
        return max([
            self._max_root_to_leaf_sum_rec(node.left, new_accum),
            self._max_root_to_leaf_sum_rec(node.right, new_accum),
        ])


class TreeSearcherBreadthIterative(TreeSearcherIterative):
    """Uses a queue DS.
    
    O(N) time, O(N) memory (for the queue)
    """
    def get_values_full(self):
        values = []
        current_node = self.tree.root
        queue = Queue()
        queue.enqueue(current_node)
        while not queue.is_empty():
            current_node = queue.dequeue()
            values.append(current_node.value)
            
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)
        
        return values

    def _reduce(self, reduce_func: Callable, accum):
        queue = Queue()
        queue.enqueue(self.tree.root)
        while not queue.is_empty():
            current_node = queue.dequeue()
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)
            accum = reduce_func(current_node, accum)

        
        return accum
    
    def includes(self, value):
        current_node = self.tree.root
        queue = Queue()
        queue.enqueue(current_node)
        while not queue.is_empty():
            current_node = queue.dequeue()
            if current_node.value == value:
                return True 
            
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)
        
        return False



class TreeSearcherFactory:
    def __init__(self, search_strategy: SearchStrategyEnum, implementation_strategy: ImplementationStrategyEnum):
        self.search_strategy = search_strategy
        self.implementation_strategy = implementation_strategy
    
    def get(self):
        class_map = {
            (SearchStrategyEnum.DEPTH_FIRST, ImplementationStrategyEnum.ITERATIVE): TreeSearcherDepthIterative,
            (SearchStrategyEnum.DEPTH_FIRST, ImplementationStrategyEnum.RECURSIVE): TreeSearcherDepthRecursive,
            (SearchStrategyEnum.BREADTH_FIRST, ImplementationStrategyEnum.ITERATIVE): TreeSearcherBreadthIterative,
        }

        return class_map[(self.search_strategy, self.implementation_strategy)]


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")
j = Node("j")
k = Node("k")


a.left = b
a.right = c
b.left = d
b.right = e
e.right = j
d.right = i
d.left = h
c.right = g
c.left = f
f.right = k 

tree = Tree(root=a)


#             a
#        /        \
#       b           c
#      /  \       /   \
#     d    e      f    g
#    / \    \      \
#   h   i    j      k

# Depth first: a, b, d, h, i, e, j, c, f, k, g
# Breadth first: a, b, c, d, e, f, g, h, i, j, k


a_n = Node(1)
b_n = Node(2)
c_n = Node(3)
d_n = Node(4)
e_n = Node(7)
f_n = Node(50)
g_n = Node(5)
h_n = Node(3)
i_n = Node(8)
j_n = Node(2)
k_n = Node(-1)


a_n.left = b_n
a_n.right = c_n
b_n.left = d_n
b_n.right = e_n
e_n.right = j_n
d_n.right = i_n
d_n.left = h_n
c_n.right = g_n
c_n.left = f_n
f_n.right = k_n 

tree_n = Tree(root=a_n)


if __name__ == "__main__":
    includes_g = TreeSearcherBreadthIterative(tree).includes("g")
    print(includes_g)
    includes_z = TreeSearcherBreadthIterative(tree).includes("z")
    print(includes_z)

    includes_g = TreeSearcherDepthIterative(tree).includes("g")
    print(includes_g)
    includes_z = TreeSearcherDepthIterative(tree).includes("z")
    print(includes_z)

    includes_g = TreeSearcherDepthRecursive(tree).includes("g")
    print(includes_g)
    includes_z = TreeSearcherDepthRecursive(tree).includes("z")
    print(includes_z)

    suma = TreeSearcherDepthRecursive(tree_n).sum()
    print(suma)
    suma = TreeSearcherBreadthIterative(tree_n).sum()
    print(suma)
    suma = TreeSearcherDepthIterative(tree_n).sum()
    print(suma)
    values = TreeSearcherBreadthIterative(tree).get_values()
    print(values)
    values = TreeSearcherDepthIterative(tree).get_values()
    print(values)
    _min = TreeSearcherBreadthIterative(tree_n).min()
    print(_min)
    _min = TreeSearcherDepthIterative(tree_n).min()
    print(_min)
    _min = TreeSearcherDepthRecursive(tree_n).min()
    print(_min)

    max_branch = TreeSearcherDepthRecursive(tree_n).max_root_to_leaf_sum()
    print(max_branch)
