# Time: O(m^2 * n) | Space: O(n)

from typing import List

def countConstruct(targetString: str, wordBank: List[str]) -> int:
    
    n = len(targetString)
    dp = [0] * (n + 1)
    dp[0] = 1
    count = 0
    
    for i in range(n):
        if dp[i]:
            for word in wordBank:
                if targetString[i:i+len(word)] == word:
                    dp[i+len(word)] += dp[i]
                    
    return dp[n]

targetString = "purple"
wordBank = ["purp", "p", "ur", "le", "purpl"]

print(countConstruct(targetString, wordBank))
                    