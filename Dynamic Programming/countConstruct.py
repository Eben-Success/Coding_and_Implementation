"""
Write a function countConstruct(target, wordBank) that accepts
a target string and an array of strings.

The function should return the number of ways that the `target`
can be constructed by concatenating elements of `wordBank` array.
You can reuse elements of `wordBank` as many times as needed.
"""


from typing import List

class Solution:
    def countConstruct(self, target: str, wordBank: List[str]) -> int:
        if target == "": return 1
        count = 0
        
        for word in wordBank:
            if target.find(word) == 0:
                suffix = target[len(word):]
                if self.countConstruct(suffix, wordBank):
                    count += 1
        return count
    
    def countConstruct_memo(self, target: str, wordBank: List[str], memo = {}) -> int:
        if target in memo: return memo[target]
        
        # Edge Base
        if target == "": return 1
        
        count = 0
        
        for word in wordBank:
            if target.find(word) == 0:
                suffix = target[len(word):]
                if self.countConstruct_memo(suffix, wordBank):
                    count += 1
        memo[target] = count
        return count
                
                
                
soln = Solution()
target = "purple"
wordBank = ["purp", "p", "ur", "le", "purpl"]

print(soln.countConstruct(target, wordBank)) # 2

target2 = "abcdef"
wordBank2 = ["ab", "abc", "cd", "def", "abcd"]

target3 = "eeeeeeeeeee"
wordBank3 = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]

print(soln.countConstruct(target3, wordBank3)) # 1

target4 = "eeeeeeeeeeeeeeeeeeeeeef"
wordBank4 = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]
print(soln.countConstruct_memo(target4, wordBank4))