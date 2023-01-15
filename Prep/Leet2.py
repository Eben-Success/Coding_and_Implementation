from collections import defaultdict

nums = [2,2,4,4,5,5,6,6,7,8,7]

check = defaultdict(set)

for idx, num in enumerate(nums):
    check.append(idx, num)