class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def find_node(self, x):
      
        if x == self.root:
            return True

        if x < self.root and self.left:
            return self.left.find_node(x)

        if x > self.root and self.right:
            return self.right.find_node(x)

    def insert_node(self, x):
        if x <= self.root and self.left:
            return self.left.insert_node(x)
        elif x <= self.root:
            self.left = TreeNode(x)

        elif x >= self.root and self.right:
            return self.left.insert_node(x)
        else:
            self.right = TreeNode(x)

# Alternate code to insert into tree

    def insert_left(self, val):
        if self.left is None:
            self.left = TreeNode(val)
        else:
            new_node = TreeNode(val)
            new_node.self.left = self.left
            self.left = new_node

    def insert_right(self, val):
        if self.right is None:
            self.right = TreeNode(val)
        else:
            new_node = TreeNode(val)
            new_node.self.right = self.right
            self.right = new_node
