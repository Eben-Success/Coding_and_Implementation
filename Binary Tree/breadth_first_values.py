# Travel across before you go deep.
# Time O(n)
# Space: O(n)

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def breadth_first_traversal(root):
    if root is None:
        return []
    queue = deque([root])
    result = []

    while len(queue) > 0:
        current = queue.popleft()
        result.append(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
        return result


a = Node("a")
b = Node("b")
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(breadth_first_traversal(a))