from typing import List

def searchmatrix(matrix: List[List[int]], target: int) -> bool:
    
    n = len(matrix)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (right - left) // 2 + (left)
        r = mid//n
        c = mid%n
        cur_pos = matrix[r][c]
        
        if cur_pos == target:
            return True
        
        elif cur_pos > target:
            right = left - 1
        else:
            left = right + 1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

print(searchmatrix(matrix, target))