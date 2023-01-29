"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from heapq import heappop, heappush
def min_path_sum(grid):
    ROW, COL = len(grid), len(grid[0])

    visited = set()
    heap = [(grid[0][0], 0, 0)]

    while heap:
        val, r, c = heappop(heap)

        if r == ROW - 1 and c == COL - 1:
            return val

        if (r, c) in visited:
            continue
        visited.add(r, c)

        if r + 1 < ROW:
            heappush(heap, (val + grid[r+1][c], r + 1, c))

        if c + 1 < COL:
            heappush(heap, (val + grid[r][c+1], r, c+1))

    return 0
    