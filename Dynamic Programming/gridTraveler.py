"""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your
goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?
Write a function gridTraveler(n, m) that calculates this
"""

# Time: O(2^(n + m)) | Space: O(n + m)
# def gridTraveler(n, m):
#     if n == 0 or m == 0:
#         return 0
    
#     if n == 1 and m == 1:
#         return 1
    
#     return gridTraveler(n - 1, m) + gridTraveler(n, m - 1)


# print(gridTraveler(2, 3))

# Memoization
# Time: O(n + m) | Space: O(n + m)
def gridTraveler(n, m, memo = {}):
    key = str(m) + "," + str(n)
    if key in memo: return memo[key]
    
    if n == 1 and m == 1: return 1
    if n == 0 or m == 0:  return 0
    
    memo[key] = gridTraveler(n - 1, m, memo) + gridTraveler(n, m - 1, memo)
    return memo[key]
        
        
print(gridTraveler(18, 18))



 

