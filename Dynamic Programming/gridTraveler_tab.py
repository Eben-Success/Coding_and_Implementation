"""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your
goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?
Write a function gridTraveler(n, m) that calculates this
"""

from typing import List

class Solution:
    def gridTraveler(self, m: int, n: int) -> int:
        
        dp = [[0] * (n+1) for _ in range(m+1)]
  
        dp[1][1] = 1
        dp_len = len(dp)
        
        for i in range(dp_len):
            for j in range(dp_len):
                cur = dp[i][j]
                if i + 1<= m: dp[i+1][j] += cur
                if j + 1<= n: dp[i][j+1] += cur
                    
        return dp[m][n]
        
        
soln = Solution()

print(soln.gridTraveler(10, 10))

print(soln.gridTraveler(18, 18))