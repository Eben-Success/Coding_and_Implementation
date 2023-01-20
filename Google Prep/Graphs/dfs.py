# Time: O(V + E)
# Space: O(V)

def dfs(graph, node, visited=set()):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, node, visited)

    return visited