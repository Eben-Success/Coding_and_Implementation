

class Solution:
    # def __init__(self):

    def swap(self,nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp


    def reverse(self,nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1


    def nextPermutation(self,nums):
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums, 0, 1)

        dec = len(nums) - 2
        check1 = dec + 1
        while dec >= 0 and nums[dec] >= nums[check1]:
            dec -= 1
        self.reverse(nums, dec + 1, len(nums) - 1)

        if dec == -1:
            return

        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap(nums, next_num, dec)


a = Solution()

nums = [3,2,1]

print(a.nextPermutation(nums))


