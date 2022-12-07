from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def dfs(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return dfs(root.left, target) or dfs(root.right, target)


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

print(dfs(a, 'b'))