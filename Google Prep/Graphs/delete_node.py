class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def findNode(self, root, to_delete):
        self.forest = []

        self.dfs(root, to_delete, True)
        return self.forest

    def dfs(self, node, to_delete, is_root):
        if not node:
            return 

        if node.val in to_delete:
            self.dfs(node.left, to_delete, True)
            self.dfs(node.right, to_delete, True)

        if node.left:
            if node.left.val in to_delete:
                self.dfs(node.left, to_delete, True)
                node.left = None

            else:
                self.dfs(node.left, to_delete, False)

            if node.right:
                if node.right.val in to_delete:
                    self.dfs(node.right, to_delete, True)
                    node.right = None

                else:
                    self.dfs(node.right, to_delete, False)

            if is_root:
                self.forest.append(node)