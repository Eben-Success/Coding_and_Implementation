# Time: O()

from typing import List

def allConstruct(targetString, wordBank: List[str]) -> List[List[str]]:
    
    n = len(targetString)
    dp = [[] for _ in range(n + 1)]
    dp[0] = [[]]
    
    for i in range(n):
        if dp[i]:
            for word in wordBank:
                if targetString[i:i+len(word)] == word:
                    dp[i+len(word)] += [combination + [word] for combination in dp[i]]
                    
    return dp[n]


targetString = "purple"
wordBank = ["purp", "p", "ur", "le", "purpl"]
print(allConstruct(targetString, wordBank))