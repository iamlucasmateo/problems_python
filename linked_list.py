import random
import typing

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

        return self
        
    def insert(self, node):
        node.next = self.head
        self.head = node

        return self
    
    def delete_position(self, position: int):
        if position == 0:
            self.head = self.head.next
            return self
        
        i = 0
        previous_node = None
        current_node = self.head
        while current_node.next is not None:
            if i == position:
                previous_node.next = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next
            i += 1
        
        if i < position:
            raise ValueError(f"Linked list does not have {position} nodes.")

        return self

    def aggregate_nodes(self, agg_func: typing.Callable, init_value: typing.Any):
        agg_value = init_value
        current_node = self.head
        while current_node is not None:
            agg_value = agg_func(current_node, agg_value)
            current_node = current_node.next
        
        return agg_value

    def count_nodes(self):
        def _count(node: Node, agg_value: int):
            return agg_value + 1
        
        return self.aggregate_nodes(_count, 0)

    def sum_nodes(self):
        def _sum(node: Node, agg_value: int):
            return node.value + agg_value
        
        return self.aggregate_nodes(_sum, 0)
    def reverse(self, in_place: bool = True):
        return self._reverse_in_place() if in_place else self._reverse_copy()

    def _reverse_in_place(self):
        current_node = self.head
        next_node = current_node.next
        node_after_next = next_node.next
        current_node.next = None
        while node_after_next.next is not None:
            next_node.next = current_node
            current_node = next_node
            next_node = node_after_next
            node_after_next = node_after_next.next
        
        next_node.next = current_node
        node_after_next.next = next_node
        self.head = node_after_next

        return self

    def _reverse_cropy(self):
        raise NotImplementedError("Method not implemented")
    
    def __str__(self):
        result = ""
        current = self.head
        i = 0
        while current is not None and i < 10:
            result += str(current.value) + " -> "
            current = current.next
            i += 1
        return result[:-4]

    @classmethod
    def create_random(cls, nodes: int):
        ll = cls()
        for _ in range(nodes):
            node = Node(random.randint(0, 25))
            ll.add(node)
        
        return ll