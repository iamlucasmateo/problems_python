from enum import Enum

from src.linked_list import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


class TreeSearcherDepthIterative(TreeSearcher):
    """This is implemented with a Stack DS.
    
    It's O(N) T (navigates all nodes once), O(N) M (for the stack).
    """
    def get_values(self):
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



class TreeSearcherBreadthRecursive(TreeSearcher):
    def get_values(self):
        return self._search_node_values(self.tree.root)
    
    def _search_node_values(self, node: Node):
        values = [node.value]
        if node.left is not None:
            values.append(node.left.value)
        if node.right is not None:
            values.append(node.right.value)



class TreeSearcherBreadthIterative(TreeSearcher):
    """Uses a queue DS.
    
    O(N) time, O(N) memory (for the queue)
    """
    def get_values(self):
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

