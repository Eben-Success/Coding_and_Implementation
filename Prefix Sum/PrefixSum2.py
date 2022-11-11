def find_prefix_sum(nums):
    prefix_sum= [0]

    for i in range(len(nums)):
        prefix_sum.append(prefix_sum[i] + nums[i])
    return prefix_sum

n = find_prefix_sum([2, 3, 4, 5, 6, 7, 5, 4, 5])
print(n)