# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

def longestIncreasingPath(matrix):
    res = 1
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            res = max(res, dfs(matrix, r, c))
            

def dfs(matrix, r, c):
    memo = {}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if (r, c) in memo:
        return memo[(r, c)]
    
    memo[(r, c)] = 1
    
    for r_inc, c_inc in directions:
        new_r = r_inc + r
        new_c = c_inc + c
        
        if (0 <= new_r < len(matrix)) and (0 <= new_c < len(matrix[0])) and matrix[r][c] < matrix[new_r][new_c]:
            memo[(r,c)] = max(memo[(r, c)] + 1 + dfs(matrix, new_r, new_c))
            
    return memo[(r, c)]
    
    


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))      