# Question https://structy.net/problems/reverse-list
# Time complexity O(n)
# Space O(1)

# Iterative Approach

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev



if __name__ == '__main__':

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