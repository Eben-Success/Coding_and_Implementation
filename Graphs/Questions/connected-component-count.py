# Question: https://structy.net/problems/connected-components-count

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True


a = connected_components_count({
    0: [4, 7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
})  # -> 5

print(a)
