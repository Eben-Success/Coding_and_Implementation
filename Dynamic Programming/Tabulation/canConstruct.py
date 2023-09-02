# Time: O(m^2 * n) | Space: O(m)

from typing import List

def canConstruct(targetString: str, wordBank: List[str]) -> bool:
    
    n = len(targetString)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(n):
        if dp[i]:
            for word in wordBank:
                if targetString[i:len(word)] == word:
                    dp[i+len(word)] = True
                    
    return dp[n]
    
    
    
targetString = "abcdef"
wordBank = ["ab", "abc", "cd", "def", "abcd"]

targetString = "skateboard"
wordBank = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]

# True
targetString = "eeee"
wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]
print(canConstruct(targetString, wordBank))
    