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


def level_order(root):
    if not root:
        return []

    queue = deque([root])
    res = []
    while queue:
        level_order = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_order.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_order)
    return res
            


