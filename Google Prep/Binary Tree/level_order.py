# Level order traversal is also known as breadth-first traversal

from collections import deque

def level_order_traversal(root):
    if root is None:
        return 

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)