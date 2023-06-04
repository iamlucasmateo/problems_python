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
    
    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.value) + " -> "
            current = current.next
        return result[:-4]


