# It has no explicit base case

def depth_first_recursive(graph:dict, source:str):
    print(source)
    for neighbor in graph[source]:
        depth_first_recursive(graph, neighbor)

graph = {
    'a' : ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f': [],
}

depth_first_recursive(graph, 'a')