class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self) :
        self.root = None


    
    def insert_node(self, val):
        """
        In average case, the time is O(logn): tree is balanced
        Time in worst case is O(n): height of the BST
        """
        new_node = Node(val)

        if self.root is None:
            self.root = new_node

        current = self.root

        if val < current.val:
            if current.left is None:
                current.left = new_node
                return 
            # traverses the left of the tree.
            current = current.left

        else:
            if current.right is None:
                current.right = new_node
                return 
            # traverse the right of the tree
            current = current.right

    def get_node(self, root, val):
        """Average time: O(logn) when tree is balanced.
        Worst case: O(n): height of the BST"""

        if root is None or root.val == val:
            return root

        if val < root.val:
            return self.get_node(root.left, val)
        else:
            return self.get_node(root.right, val)

    # Iterative Approach
    # Return boolean if node if found
    def search(self, root, key):
        while root is not None:
            if key == root:
                return True
            elif key < root:
                root = root.left
            else:
                root = root.right
        return False

    # Recursive Approach
    def search_recursive(self, root, key):
        if root is None or root.val == key:
            return root is not None
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)