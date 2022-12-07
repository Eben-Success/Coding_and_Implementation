from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_min_vale(root):
    queue = deque([root])
    value = float("inf")
    while queue:
        current = queue.popleft()
        value = min(current.val, value)

        if current.right is not None:
            queue.append(current.right)

        if current.left is not None:
            queue.append(current.left)
    return value


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_min_vale(a))