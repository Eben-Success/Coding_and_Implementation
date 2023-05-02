# Tree-sum
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def bfs(root):
    queue = deque([root])
    tree_sum = 0

    while queue:
        current = queue.popleft()
        tree_sum += current.val

        if current.right is not None:
            queue.append(current.right)
        if current.left is not None:
            queue.append(current.left)
    return tree_sum



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

print(bfs(a))
