
from collections import deque

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


    # edges
    # edges = [
    #     ['w', 'x'],
    #     ['x', 'y'], 
    #     ['z', 'y'],
    #     ['w', 'v']
    # ]

def has_cycle(edges, start, visited=set()):

    graph = build_graph(edges)
    visited.add(start)

    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor in visited:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False
