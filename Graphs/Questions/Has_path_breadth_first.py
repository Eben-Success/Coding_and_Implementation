from collections import deque
def Has_path(graph, src, dst):
    queue = deque([src])
    while len(queue) > 0:
        current = queue.popleft()
        if current == dst:
            return True

        for neigbor in graph[current]:
            queue.append(neigbor)
    return False

graph = {
    'a' : ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f': [],
}

print(Has_path(graph, 'a', 'd'))