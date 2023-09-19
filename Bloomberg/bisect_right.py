def bisect_right(nums, target):
    low, high = 0, len(nums) - 1
    rightmost = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] > target:
            high = mid - 1
            
        elif nums[mid] < target:
            low = mid + 1
        
        else:
            rightmost = mid
            low = mid + 1
    return rightmost