# Time O(n)
# Space O(1)
# Question: https://structy.net/problems/linked-list-find
# Return True if target in linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Iterative Approach
def linked_list_find(head, target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_find(a, 'c'))