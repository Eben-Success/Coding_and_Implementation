# Evaluate arithmetic tree
# Daily coding page: 81

"""Suppose an arithmetic expressions is given as a binary tree.
Each leaft is an integer and each internal node is one of +, -, *, or /.

Given the root to such a tree, write a function to evaluate it.
"""

"""SOLUTION

This type of tree is formally known as expression tree.
We use a form of post-order traversal to evaluate it.

Edge Cases
1. if not root, return root.val

APPROACH
1. We check the parent node for the operation to perform,
and apply the operate to the child nodes.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

plus = "+"
minus = "-"
times = "*"
divide = "/"

def evaluate(root):
    if not root:
        return 0

    if not root.left or not root.right:
        return root.val

    if root.val == plus:
        return evaluate(root.left) + evaluate(root.right)

    if root.val == minus:
        return evaluate(root.left) - evaluate(root.right)

    if root.val == times:
        return evaluate(root.left) * evaluate(root.right)

    if root.val == divide:
        return evaluate(root.left) // evaluate(root.right)

"""This algorithm runs in O(n) and O(n) space.
Reason: We have to traverse all nodes.
And our call stack will hold at most a number of elements
equal to the tree's height."""
