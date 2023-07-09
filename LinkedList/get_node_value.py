# Question: https://structy.net/problems/get-node-value
# Time O(n)
# Space O(1)

# Iterative Approah

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_node_value(head, index):
    count = 0
    current = head
    while current is not None:
        if index == count:
            return current.val
        current = current.next
        count +=1

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2))