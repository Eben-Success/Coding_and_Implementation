# Question https://structy.net/problems/undirected-path
# Count for cases where there are cycles in graphs

# Solving the question
# Convert edges to adjacency list


def undirected_path(edges, node_A, node_B):
    graph = buildGraph(edges)
    print(graph)
    return has_path(graph, node_A, node_B, set())

def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
        return True if has_path(graph, neighbor, dst, visited) else False

edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'j', 'i'))