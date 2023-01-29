def findRedundantConnection(edges):

    parent = [-1] * (len(edges) + 1)

    def find(x):
        if parent[x] != -1:
            find(parent[x])
        return x

    def union(x, y):
        x_set = find(x)
        y_set = find(y)

        if x_set != y_set:
            parent[x_set] = y_set
        else:
            return [x, y]

    for edge in edges:
        if union(edge[0], edge[1]):
            return union(edge[0], edge[1])

    

edges = [[1,2],[1,3],[2,3]]

print(findRedundantConnection(edges))