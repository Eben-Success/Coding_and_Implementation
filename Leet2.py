def largestNumber(nums):
    ans = []
    for num in nums:
        if num % 10 == num:
            ans.append(num)
            ans = sorted(ans, reverse=True)
        else:
            res = []
            res.append(num)
            res = sorted(res, reverse=True)
            ans.append(res)
    return ans

xrange


nums = [3,30,34,5,9]
p = largestNumber(nums)

print(p)
