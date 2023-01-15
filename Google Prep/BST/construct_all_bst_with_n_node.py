# Construct all BSTs with n nodes
# Daily Coding Problem Page: 90

"""
Given an integer n, construct all possible binary
search tree with n nodes where all values from [1, .., n] are used

For example, given n = 3, return the following trees.
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def make_tree(low, high):
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high + 1):
        left = make_tree(low, i - 1)
        right = make_tree(i+1, high)


        for l in left:
            for r in right:
                node = TreeNode(i, left=l, right=r)
                trees.append(node)

    return trees