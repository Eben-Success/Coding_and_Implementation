def isCousin(root, x, y):
    results = []

    def dfs(node, parent, depth):
        if not node or len(results) == 0:
            return
        else:
            if node.val == x or node.val == y:
                results.append((parent, depth))
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

    dfs(root, None, 0)
    return results[0][0] != results[1][0] and results[0][1] == results[1][1]
