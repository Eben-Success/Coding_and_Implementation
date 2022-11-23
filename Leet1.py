def findMedian(nums1, nums2):
    nums1 = nums1 + nums2

    mid = len(nums1) / 2

    if len(nums1) % 2 == 0:
        median = nums1[mid] + nums1[mid+1]
        print(median)

    else:
        median = nums1[mid]
        print(median)



nums1 = [2,3,4,5]
nums2 = [6,7]

print(findMedian(nums1, nums2))