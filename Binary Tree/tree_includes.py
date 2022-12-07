from collections import deque

# Time O(n)
# Space O(n)

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# TREE INCLUDE
# depth first search
def bfs(root, target):
    if root is None:
        return False
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.right is not None:
            queue.append(current.right)
        if current.left is not None:
            queue.append(current.left)
    return False


a = Node("a")
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(bfs(a, 'b'))