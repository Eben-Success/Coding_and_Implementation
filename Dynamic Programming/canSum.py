"""
Write a function `canSum(targetSum, numbers)` that takes in a targetSum 
and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is 
possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.
You may assume that all input numbers are non negative..

"""

from typing import List

# def canSum(targetSum: int, nums: List[int]):
    
#     n = len(nums)
#     for i in range(n):
#         sum_ = nums[i]
#         for j in range(i+1, n):
#             sum_  += nums[j]
#             if sum_ == targetSum:
#                 return True         
#     return False


# print(canSum(7, [2]))

#Brute Force

# O(n^m) time | O(m) space
# def canSum(nums: List[int], targetSum: int) -> bool:
    
#     if targetSum == 0: return True
#     if targetSum < 0: return False
    
#     for num in nums:
#         remainder = targetSum - num
#         if canSum(nums, remainder):
#             return True
#     return False


# print(canSum([2, 3], 7))
# print(canSum([5, 3, 4, 7], 7))

# Time: O(m*n) | Space: O(m)
# Memoization
from typing import List
def canSum(nums: List[int], targetSum: int, memo = {}) -> bool:
    if targetSum in memo: return memo[targetSum]
    
    if targetSum == 0: return True
    if targetSum < 0: return False
    
    for num in nums:
        remainder:int  = targetSum - num
        
        if canSum(nums, remainder, memo):
            memo[targetSum] = True
            return True
        
    memo[targetSum] = False
    return False    


print(canSum([2, 3], 7))
print(canSum([5, 3, 4, 7], 7))
print(canSum([7, 14], 300))


