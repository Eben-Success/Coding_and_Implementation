# Question https://structy.net/problems/shortest-path

# def build_graph(edges): convert edges to adjacency list
# implement breadth first search
# explore_paths btwn nodes

# Time complexity O(e)
# Space complexity O(n)

from collections import deque

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == node_B:
            return distance

        for neigbor in graph[node]:
            if neigbor not in visited:
                visited.add(neigbor)
                queue.append((neigbor, distance+1))
    return -1

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'v'))