nums = ["3", "6", "7", "10"]

int_nums = [int(item) for item in nums]
print(int_nums)

srt = sorted(int_nums, reverse=True)
print(srt)


def kthLargestNumber(nums, k):
    int_nums = [int(item) for item in nums]

    srt = sorted(int_nums, reverse=True)

    return srt[k-1]


nums = ["3", "6", "7", "10"]

q = kthLargestNumber(nums, 4)
print(q)
