# Time O(n)
# Space O(n)

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def dfs(root):
    if root is None:
        return 0
    return dfs(root.left) + dfs(root.right) + root.val

    # left_sum = dfs(root.left)
    # right_sum = dfs(root.right)
    # return left_sum + right_sum + root.val

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

print(dfs(a))
