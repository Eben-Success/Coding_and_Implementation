"""
Write a function `bestSum(targetSum, numbers)` that takes in 
a targetSum and an array of numbers as arguments.

The function should return an array containing the shortest 
combination of numbers that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may 
return any one of the shortest.
"""

from typing import List

class Solve:
    def bestSum(self, nums: List[int], targetSum: int):
        
        if targetSum == 0: return []
        if targetSum < 0: return None
        
        min_len = None
        
        for num in nums:
            remainder = targetSum - num
            res = self.bestSum(nums, remainder)
            if res is not None:
                ans = res + [num]
                if min_len == None or len(ans) < len(min_len):
                    min_len = ans
                
        return min_len
    
    
sol = Solve()

nums = [5, 3, 4, 7]
targetSum = 7

# nums = [5, 3, 4, 7]
# targetSum = 7

print(sol.bestSum(nums, targetSum))
                