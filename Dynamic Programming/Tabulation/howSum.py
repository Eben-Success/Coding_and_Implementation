def howSum(targetSum, nums):
    table = [None] * (targetSum + 1)
    table[0] = []
    
    for i in range(targetSum):
        if table[i] != None:
            for num in nums:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]
                    
    return table[targetSum]



targetSum = 7
nums = [2, 3]

print(howSum(targetSum, nums))