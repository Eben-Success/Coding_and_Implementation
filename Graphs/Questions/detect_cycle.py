from collections import deque

def detect_cycle(grid):

    ROW, COL = len(grid), len(grid[0])

    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]:
                continue
            visited[r][c] = True

            queue = deque([(r, c, 1)])

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                r, c, pathLen = queue.popleft()

                for row_inc, col_inc in directions:
                    new_row = r + row_inc
                    new_col = c + col_inc

                    if not (0 <= new_row < ROW and 0 <=  new_col < COL) or grid[new_row][new_col] != grid[r][c]:
                        continue

                    if (new_row, new_col) == (r, c):
                        return True

                    if grid[new_row][new_col]:
                        continue
                    visited[new_row][new_col] = True

                    queue.append((new_row, new_col, pathLen+ 1))

    return False
