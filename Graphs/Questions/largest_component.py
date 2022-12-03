# Question: https://structy.net/problems/largest-component

# Time complexity O(e)
# Space complexity O(n)

# def largest_component(graph)
# def explore_size(graph, node, visited)
# depth first search

# Time complexity O(e)
# Space complexity O(n)

def largest_component(graph):
    visited = set() # undirected graph and we need to avoid cycles
    largest = 0

    for node in graph:
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size
    return largest


def explore_size(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1

    for neigbor in graph[node]:
        size += explore_size(graph, neigbor, visited)
    return size

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) )