class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_min_recursion(root):
    if root is None:
        return float("inf")
    left_min = tree_min_recursion(root.left)
    right_min = tree_min_recursion(root.right)
    return min(left_min, right_min, root.val)

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

print(tree_min_recursion(a))