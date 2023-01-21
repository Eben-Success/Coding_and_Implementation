class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            inorder_successor = find_min(root.right)
            root.data = inorder_successor.data
            root.right = delete_node(root.right, inorder_successor.data)
    return root


def find_min(root):
    while root.left:
        root = root.left
    return root
