def bisect_left(nums, target):
    
    low, high = 0, len(nums) - 1
    leftmost = -1
    
    while low <= high:
        mid = (low + high)
        
        if nums[mid] > target:
            high = mid - 1
            
        elif nums[mid] < target:
            low = mid + 1
            
        else:
            leftmost = mid
            high = mid - 1
            
    return leftmost
            