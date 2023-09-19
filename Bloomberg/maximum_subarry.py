from typing import List

def maximum_subarray(nums: List[int]) -> int:
    global_max = float("-inf")
    cur_sum = 0
    
    for num in nums:
        cur_sum += num
        temp = num
        cur_sum = max(cur_sum, temp)
        global_max = max(global_max, cur_sum)
    return global_max




nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maximum_subarray(nums))