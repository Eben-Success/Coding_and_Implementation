# Return true if the source and the destination nodes exist.
# Time complexity is O(e)
# n = nodes
# n**2 = edges.
# So time complexity is O(n**2)
# Space complexity is O(n)

# Question Link: https://structy.net/problems/has-path

def has_path(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        return True if has_path(graph, neighbor, dst) else False




graph = {
    'a' : ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f': [],
}

print(has_path(graph, 'a', 'z'))


