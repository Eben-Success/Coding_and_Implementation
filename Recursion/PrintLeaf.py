def print_leaf_node(Node root):
    if (root == None): return
    
    if (root.left == None and root.right == None):
        print(root.val + ", ")
    
    if (root.left != None):
        print_leaf_node(root.left)
    
    if (root.right != None):
        print_leaf_node(root.right)