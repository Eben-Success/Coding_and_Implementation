class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert a new value into the BST.
        Time complexity: O(log n) in average case, O(n) in worst case (when tree is skewed)
        Space complexity: O(1)
        """
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

    def search(self, val):
        """Search for a value in the BST.
        Time complexity: O(log n) in average case, O(n) in worst case (when tree is skewed)
        Space complexity: O(1)
        """
        current = self.root
        while current:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, val):
        """Delete a value from the BST.
        Time complexity: O(log n) in average case, O(n) in worst case (when tree is skewed)
        Space complexity: O(1)
        """
        # Helper function to find the node with the minimum value in a subtree
        def find_min(node):
            current = node
            while current.left:
                current = current.left
            return current

        def delete_node(node, val):
            if not node:
                return None
            if val == node.val:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_right = find_min(node.right)
                    node.val = min_right.val
                    node.right = delete_node(node.right, min_right.val)
                    return node
            elif val < node.val:
                node.left = delete_node(node.left, val)
                return node
            else:
                node.right = delete_node(node.right, val)
                return node

        self.root = delete_node(self.root, val)
