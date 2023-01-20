# Time: O(V + E)
# Space: O(V)

from collections import deque

def bfs(graph, start, visited=set()):

    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited