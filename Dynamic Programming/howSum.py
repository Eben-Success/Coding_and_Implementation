"""
Write a function `howSum(targetSum, numbers)`
that takes in a p targetSum and an array of numbers as arguments.

The function should return an array containing any combination
of elements that add up to exactly the targetSum.
If there is no combination that addes up the taragetSum, then return null.

If there are multiple combinations possible, you may return any 
single one.

m = targetSum
n = array length
"""

from typing import List

# Brute Force
# Time: O(n^m * m) | Space: O(m)

def howSum(nums: List[int], targetSum: int):
    
    if targetSum < 0: return None
    if targetSum == 0: return []
    
    for num in nums:
        remainder = targetSum - num
        remain_res = howSum(nums, remainder)
        if remain_res is not None:
            return remain_res + [num]
    return None


# Time: O(n*m*m) -> O(n*m^2) | Space: O(m*m) -> O(m^2)
def howSum_optimized(nums: List[int], targetSum: int, memo = {}) -> List[int]:
    
    if targetSum in memo: return memo[targetSum]
    
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    for num in nums:
        remainder = targetSum - num
        remain_res = howSum_optimized(nums, remainder, memo)
        if remain_res is not None:
            memo[targetSum] = remain_res + [num]
            return memo[targetSum]
    memo[targetSum] = None  
    return None
   

nums = [5, 3, 4, 7]
targetSum = 7

nums = [7, 14]


print(howSum_optimized(nums, 300))