from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):

    graph = [[] for _ in range(numCourses)]

    indegrees = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegrees[a] += 1

    queue = deque()
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()

        for nei in graph[course]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                queue.append(nei)

    return sum(indegrees) == 0
