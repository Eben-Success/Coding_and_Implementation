# Determine if a cylce exists
"""
Given an undirected graph, determine if it contains cycles.
"""

"""
Suppose we are traversing the graph's edges, starting from the 
a given vertex. If, for some vertex, we find that one of its
neighbors has already been visited, then we know that there are two 
ways to reach that neighbor from the same point, which indicates a
cycle.

We can implement this solution uisng depth first search. For each 
vertex in the graph, if it has not already been visited, we call our search 
funtion on it. This function will recursively traverse unvisited neighbors of the vertex, and return 
True if we come across the situation described above.
If we are able to visit all vertices without finding a duplicate path, 
we return False.

COMPLEXITIES
Time: O(V + E), since in the worst case we will have to traverse all edges of the graph.
Space: O(V) space in the worst case to store the vertices in a given traversal on the stack. """

def search(graph, vertex, visited, parent):
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if search(graph, neighbor, visited, vertex):
                return True

            elif parent != neighbor:
                return True

    return False


def has_cycle(graph):
    visited = {v: False for v in graph.keys()}

    for vertex in graph.keys():
        if not visited[vertex]:
            if search(graph, vertex, visited, None):
                return True
    return False