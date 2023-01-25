from collections import deque

def canFinish(numCourses, prerequisites):

    # create an adjacency list to represent the graph of coures.
    graph = [[] for _ in range(numCourses)]

    # create an array to store the number of incoming edges for each node (courses)
    indegrees = [0] * numCourses

    # Fill the adjacency list and indegrees array based on the input prerequisites
    for a, b in prerequisites:
        graph[b].append(a)
        indegrees[a] += 1

    # create a queue to store the nodes (coures) with no incoming edges
    queue = deque()
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)

    # Traverse the graph starting from the node (coures) with not incoming edges
    while queue:
        course = queue.popleft()
        for neighbor in graph[course]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return sum(indegrees) == 0