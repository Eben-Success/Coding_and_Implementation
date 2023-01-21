class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def insert_left(self, val):
        if self.left == None:
            self.left = BinaryTree(val)
        else:
            new_node = BinaryTree(val)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, val):
        if self.right == None:
            self.right = BinaryTree(val)
        else:
            new_node = BinaryTree(val)
            new_node.right = self.right
            self.right = new_node

    def insert_node(self, root, val):
        new_node = BinaryTree(val)
        if val < root.val:
            if self.left == None:
                self.left = BinaryTree(val)
            else:
                new_node.left = self.left
                self.left = new_node

        else:
            if self.right == None:
                self.right = BinaryTree(val)
            else:
                new_node.right = self.left
                self.left = new_node

    def find_node(self, val):
        pass

    def remove_node(self, val, parent):
        pass

    def clear_node(self):
        pass

    def find_minimum_value(self):
        pass