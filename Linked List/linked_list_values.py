# Time complexity is O(n)
# Space complexity is O(n): number of nodes.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def linked_list_values(head):
    res = []
    current = head
    while current is not None:
        res.append(current.val)
        current = current.next
    return res


print(linked_list_values(a))
