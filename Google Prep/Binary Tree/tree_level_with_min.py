# Get tree level with minimum sum
# Daily Coding Problem Page: 83

"""
Given a binary tree, return the level of the tree
that has the minimum sum. The level of a node is defined
as the number of connections required to get to the root,
with the root having level zero.

For example:
In this tree, level 0 has a sum of 1, level 1 has a sum of 5,\
and level 2 has a sum of 9, so the level with the minimum sum is 0
"""

"""
SOLUTION
Edge cases
1. Binary tree is empty.
2. The left and right of a binary tree is null, return root.

Time: O(n): traverse the neighbors of the node
Space: O(n): queue and level_sum

"""

from collections import deque, defaultdict

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def min_level(root):
    queue = deque([(root, 0)])

    # Create a map to accumulate the sum at each
    # level

    level_sum = defaultdict(int)

    # process the queue while it is not empty
    while queue:
        node, level = queue.popleft()

        level_sum[level] += node.data

        if node.left:
            queue.append((node.left, level+1))

        if node.right:
            queue.append((node.right, level+1))

        return min(level_sum, key=level_sum.get)





