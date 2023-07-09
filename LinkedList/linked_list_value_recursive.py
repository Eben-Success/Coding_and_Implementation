# Time complexity is O(n)
# Space complexity is O(n)

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
    values = []
    _linked_list_values(head, values)
    return values

def _linked_list_values(head, values):
    if head is None:
        return
    values.append(head.val)
    _linked_list_values(head.next, values)


print(linked_list_values(a))
