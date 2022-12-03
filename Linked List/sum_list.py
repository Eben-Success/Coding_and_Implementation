# Time O(n)
# Space O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_list(head):
    current = head
    res = 0

    while current is not None:
        res += current.val
        current = current.next
    return res

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

print(sum_list(a))