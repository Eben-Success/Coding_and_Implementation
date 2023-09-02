# Time: O(m^2 * n) | Space: O(m^2): Every table could contain a 2D array

from typing import List

def bestSum(targetSum: int, nums: List[int]) -> List[int]:
    
    dp = [None] * (targetSum +1 )
    
    dp[0] = []
    
    for i in range(targetSum):
        if dp[i] != None:
            for num in nums:
                if i + num <= targetSum:
                    combination = dp[i] + [num]
                    # if current combination is shorter than what is alreay
                    #stored.
                    if not dp[i+num] or len(dp[i+num]) > len(combination):
                        dp[i+num] = combination
    
    return dp[targetSum]



targetSum = 7
nums = [5, 3, 4, 7]

targetSum = 8
nums = [2, 3, 5]

print(bestSum(targetSum, nums))