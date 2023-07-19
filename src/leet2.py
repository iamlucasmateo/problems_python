from linked_list import LinkedList, Node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        max_length = max(len(l1), len(l2))
        sum_list = []
        add_from_previous = 0
        for i in range(max_length):
            value_1 = l1[i] if i < len(l1) else 0
            value_2 = l2[i] if i < len(l2) else 0
            added_value = value_1 + value_2 + add_from_previous
            net_value = added_value if added_value < 10 else added_value - 10
            add_from_previous = 1 if added_value >= 10 else 0
            sum_list.append(net_value)
        
        if add_from_previous == 1:
            sum_list.append(1)

        return sum_list

class LLAdder:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    
    def addTwoLL(self):
        ll_sum = LinkedList()
        current_1 = self.l1.head
        current_2 = self.l2.head
        add_from_previous = 0

        while (current_1 is not None or current_2 is not None):
            value_1 = 0 if current_1 is None else current_1.value
            value_2 = 0 if current_2 is None else current_2.value
            current_sum = value_1 + value_2 + add_from_previous
            net_value = current_sum if current_sum < 10 else current_sum - 10
            add_from_previous = 1 if current_sum >= 10 else 0
            node = Node(net_value)
            ll_sum.add(node)
            current_1 = None if current_1 is None else current_1.next
            current_2 = None if current_2 is None else current_2.next

        
        if add_from_previous == 1:
            ll_sum.add(Node(1))
        
        return ll_sum



l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = [9, 9, 9, 9, 9]
l4 = [1, 2]

assert Solution().addTwoNumbers(l1, l2) == [7, 0, 8]
assert Solution().addTwoNumbers(l1, l4) == [3, 6, 3]
assert Solution().addTwoNumbers(l3, l4) == [0, 2, 0, 0, 0, 1]


ll1 = LinkedList()
ll1.add(Node(2)).add(Node(4)).add(Node(3))
ll2 = LinkedList()
ll2.add(Node(5)).add(Node(6)).add(Node(4))
ll3 = LinkedList()
ll3.add(Node(9)).add(Node(9)).add(Node(9)).add(Node(9)).add(Node(9))
ll4 = LinkedList()
ll4.add(Node(1)).add(Node(2))

print(LLAdder(ll1, ll2).addTwoLL())
print(LLAdder(ll1, ll4).addTwoLL())
print(LLAdder(ll3, ll4).addTwoLL())