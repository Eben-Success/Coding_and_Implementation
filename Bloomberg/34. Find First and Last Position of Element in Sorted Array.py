"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

0 <= len(nums) <= 105
-109 <= target < 109
 -109<= nums[i] <= 109
"""

from typing import List
from bisect_left import bisect_left
from bisect_right import bisect_right

class FirstLast:
    
    def binarySearch(self, nums: List[int], target: int) -> List[int]:
        # Edge case: if nums is empty
        # if not nums:
        #     return [-1, -1]
        
        # first = self.bisect_left(nums, target)
        # last = self.bisect_right(nums, target)
        # return [first, last]
    
        first = bisect_left(nums, target)
        last = bisect_right(nums, target)
        
        return [first, last]
    
    def bisect_left(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    first = mid
                high = mid - 1
            else:
                low = mid + 1
        return first
                
    
    def bisect_right(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                last = mid
                low = mid + 1
        return last
    

    
nums = [5, 8, 8, 8, 8, 8, 8, 8, 8, 10]
target = 8

soln = FirstLast()
print(soln.binarySearch(nums, target))