# max-root-to-leaf-path-sum

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path_sum(root):
    if root is None:
        # return - float("inf")
        return 0
    if root.left is None and root.right is None:
        return root.val
    max_child = max(max_path_sum(root.left),
                    max_path_sum(root.right))
    return root.val + max_child


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

print(max_path_sum(a))





















