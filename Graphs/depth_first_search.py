def depth_first_search(graph:dict, source:str):

    # initialize stack
    # feed stack with source
    # while stack not empty, stack.pop()
    # visit neighbors and append them to stack

    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbors in graph[current]:
            stack.append(neighbors)

graph = {
    'a' : ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f': [],
}

depth_first_search(graph, 'a')

