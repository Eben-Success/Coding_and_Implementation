def oneMinusZeros(grid):
    m, n = len(grid), len(grid[0])

    # takes extra space
    row = [0] * m
    col = [0] * n

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row[i] += grid[i][j]
            col[j] += grid[i][j]

    res = []

    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            temp.append(row[i] + col[j] - (n - row[i]) - (m - col[j]))
        res.append(temp)
    return res


grid = [[0,1,1],[1,0,1],[0,0,1]]
print(oneMinusZeros(grid))