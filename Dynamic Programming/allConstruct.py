"""
Write a function `allConstruct(target, wordBank)` that accepts
a target string and an array of strings.

The function should return a 2D array containing all of the ways
that the `target` can be constructed by concatenating elements of
the `wordBank` array.

Each element of the 2D array should represent one combination that
constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.
"""

from typing import List

class Solve:
    def allConstruct(self, target: str, wordBank: List[str]) -> List[List[str]]: 
        if target == "": return [[]]
        
        res = []
        for word in wordBank:
            if target.find(word) == 0:
                suffix = target[len(word):]
                suffixWays = self.allConstruct(suffix, wordBank)
                targetWays = list(map(lambda way: [word, *way], suffixWays))
                res.extend(targetWays)
                
        return res
    
    def allConstruct_memo(self, target: str, wordBank: List[str], memo = {}) -> List[List[str]]:
        if target in memo: return memo[target]
        
        if target == "": return [[]]
        res = []
        
        for word in wordBank:
            if target.find(word) == 0:
                suffix = target[len(word):]
                suffixWays = self.allConstruct_memo(suffix, wordBank, memo)
                targetWays = list(map(lambda way: [word, *way], suffixWays))
                res.extend(targetWays)
        memo[target] = res
        return res
    

sol = Solve()

target = "purple"
wordBank = ["purp", "p", "ur", "le", "purpl"]

print(sol.allConstruct(target, wordBank))
                
        
        