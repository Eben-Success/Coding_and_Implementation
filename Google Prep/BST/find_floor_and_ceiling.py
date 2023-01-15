# Find floor and ceil
# Daily Coding Problem Page: 87

"""
Given a binary search tree, find the floor and ceiling
of a given integer. The floor is the highest element in the tree less than
or equal to an integer, while the ceil is the lowest element in the tree greater than
or equal to an integer. 

If either does not exist, return None
"""

"""
SOLUTION

1. If value < node.data, we know the ceiling can be no
greater than node.data

2. If value > node.data, we know the floor can be no less than
node.data

COMPLEXITIES
This algorithm requires a single traversal from top to bottom of the tree.
Therefore, the time complexity is O(n), where n is the height of the tree. 
If the tree is balanced, this is equal to O(logn).
Similarly, the space complexity is O(n), where n is the call stacks.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_bounds(root, x, floor=None, ceil=None):
    if not root:
        return floor, ceil

    if x == root.val:
        return x, x

    elif x < root.val:
        floor, ceil = get_bounds(root.left, x, floor, root.val)

    elif x > root.val:
        floor, ceil = get_bounds(root.right, x, root.val, ceil)
        
    return floor, ceil