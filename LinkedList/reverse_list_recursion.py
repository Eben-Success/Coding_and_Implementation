# Question https://structy.net/problems/reverse-list

# Time O(n)
# Space O(n)

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a))