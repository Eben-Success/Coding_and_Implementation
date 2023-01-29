# Time: O(r * c)
# Space Complexity: O(r * C)

"""
0: empty cell
1. fruit
2. rotten oranges

converting fruits(1s) to rotten oranges(2s) and return 
the minimum time it takes to do that else return -1
"""

from collections import deque
def rotten_orange(grid):
    if not grid:
        return

    time_taken = 0
    visited = set()
    queue = deque()
    fruit = 0

    # set directions to move up, down, left and right of the grid
    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    # traverse the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fruit += 1
            if grid[r][c] == 2:
                queue.append((r, c, 0))

            # process the node in the queue
            while queue:
                r, c, cur_time = queue.popleft()

                time_taken = max(time_taken, cur_time)

                if (r, c) not in visited:
                    visited.add((r, c))

                for row_inc, col_inc in directions:
                    new_row = row_inc + r
                    new_col = col_inc + c

                    # check for rows and columns in bounds and validity
                    row_inbound = 0 <= new_row < len(grid)
                    col_inbound = 0 <= new_col < len(grid[0])

                    if not row_inbound or not col_inbound or grid[new_row][new_col] != 2:
                        continue

                    cur_pos = (new_row, new_col)

                    if cur_pos not in visited:
                        visited.add(cur_pos)

                    fruit -= 1
                    queue.append(cur_pos)

        return time_taken if fruit == 0 else -1

                


    