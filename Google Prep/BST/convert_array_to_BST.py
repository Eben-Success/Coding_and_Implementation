# Convert sorted array to BST
# Daily Coding Problem Page: 88


"""Given a sorted array, convert it into a
height-balanced binary search tree.
"""

"""SOLUTION
If the tree did not have to be balanced, we could
initialize the first element as the root of the tree,
the add each subsequent element as a right child.

However, keeping the BST balanced is crucial to ensuing the efficiency
of its operations.

Since the array is sorted, the root (m) could be found at the middle of the array.
All element before m forms the root.left and all
element after m forms the root.right

COMPLEXITIES:
Time: O(n)
Space: O(n)
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_bst(array):
    if not array:
        return None

    mid = len(array) // 2

    root = TreeNode(array[mid])

    root.left = make_bst(array[:mid])
    root.right = make_bst(array[mid+1:])

    return root