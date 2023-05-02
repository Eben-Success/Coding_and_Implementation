"""
Given an m x n binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.
"""

from collections import deque


def maximal_square(matrix):
    # if matrix is empty

    queue = deque([])

    max_area = 0

    if not matrix:
        return 0
    
    len_row, len_col = len(matrix), len(matrix[0])

    # Add all 1's in the first row to the queue
    for i in range(len_col):
        if matrix[0][i] == 1:
            queue.append((0, i, 1)) # Add a tuple of (row, col, side(area))

    # Add the elements in the queue to a visited set
    visited = set(queue)

    # Process the queue while it is not empty
    while queue:
        row, col, size = queue.popleft()

        # Update the max_area
        max_area = max(max_area, size ** 2)

        # Enqueue all the neighboring cells that are 1 and not visited
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row_inc, col_inc in directions:
            new_row, new_col = row + row_inc, col + col_inc

            if 0 <= new_row < len_row and 0 <= new_col < len_col and matrix[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, min(size + 1, min(len_row - new_row, len_col - new_col))))
                # Add the new cell to the visited set
                visited.add((new_row, new_col))

    return max_area

