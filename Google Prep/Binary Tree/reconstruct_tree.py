"""Given pre-order and in-order traversal of a
binary tree, write a function to reconstruct
the tree

For example, given the following pre-order traversal:
[a, b, d, e, c, f, g]

And the following in-order traversal:
[d, b, e, a, f, c, g]

"""


"""
SOLUTOIN

re-order:
Root, then left node, right node, right


In-order:
left node, root node, right node

"""


"""
Root node: from the pre-order traveral,
the root node is a

In-order

1. Find the root node from the pre-order list: O(1)
2. Run a binary search on the in-order list to locate the 
root node.
3. All nodes before the root node are the left node,
all nodes after the root node are the right nodes.

Edge cases:
if not in_order and not pre_order: return None

If the length of the in_order or length of pre_order
is 1: return any [0]
"""


def reconstruct(pre_order, in_order):

    if not pre_order and not in_order:
        return None

    if len(pre_order) == len(in_order) == 1:
        return pre_order[0]

    # Run reconstruct recursively to build the 
    # tree

    root = pre_order[0]
    root_idx = in_order.index(root)

    root.left = reconstruct(pre_order[1:1+root_idx], in_order[:root_idx])

    root.right = reconstruct(pre_order[1+root_idx:], in_order[root_idx+1:])

    return root


