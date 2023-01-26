class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return 

    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = buildTree(preorder[], inorder[])