from linked_list import Node

class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, value: int):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1

        return self

    def dequeue(self):
        if self.head is None:
            return None

        self.head = self.head.next
        self.size -= 1

        return self
    
    def pop(self):
        if self.head is None:
            return None
        
        to_pop = self.head
        self.head = self.head.next
        self.size -= 1

        return to_pop

    def peek(self):
        return self.head
    
    def __str__(self):
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        
        return " -> ".join(values)