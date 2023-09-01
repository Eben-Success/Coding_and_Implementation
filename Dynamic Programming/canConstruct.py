"""
Write a function canConstruct(target, wordBank) that accepts
a target string and an array of strings.

The function should return a boolean indicating whether or not
the `target` can be constructed by concatenating elements of
`wordBank` array.

You may reuse elements of `wordBank` as many times as needed.
"""


# Time: O(n^m * m) time | Space: O(m^2) 
from typing import List

class Solution:

    def canConstruct(self, target: str, wordBank: List[str]) -> bool:
    
        if target == "": return True
        
        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                if self.canConstruct(suffix, wordBank):
                    return True
        return False
    
    
    def canConstruct_memo(self, target: str, wordBank: List[str], memo = {}) -> bool:
        if target in memo: return memo[target]
        
        if target == "": return True
        
        for word in wordBank:
            if target.find(word) == 0:
                suffix = target[len(word):]
                if self.canConstruct_memo(suffix, wordBank):
                    memo[target] = True
        memo[target] = False
        return False            
                    



sol = Solution()

target = "abcdef"
wordBank = ["ab", "abc", "cd", "def", "abcd"]

target2 = "skateboard"
wordBank2 = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]

# print(sol.canConstruct(target, wordBank))   # True

# print(sol.canConstruct(target2, wordBank2)) # False

target3 = "eeeeeeeeeee"
wordBank3 = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]

print(sol.canConstruct_memo("a", ["b"]))