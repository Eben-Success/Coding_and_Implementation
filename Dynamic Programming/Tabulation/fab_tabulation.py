"""
Write a function fib(n) that takes in a number as an argument.
The function should return the nth number of the Fibonacci sequence.

The 0th number of the sequence is 0.
The 1st number of the sequence is 1.   

To generate the next number of the sequence, we sum the previous two.
"""
from typing import List

class Solution:
    def fib_tab(self, n):
        dp = [0] * (n + 1)
        
        dp[1] = 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    
soln = Solution()
print(soln.fib_tab(200))