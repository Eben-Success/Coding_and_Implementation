def BinarySearchRecursion(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high ) // 2
    
    if target == arr[mid]:
        return mid
    
    if target < arr[mid]:
        return BinarySearchRecursion(arr, low, mid - 1, target)
    
    return BinarySearchRecursion(arr, mid + 1, high, target)


arr = [2,3,4,5,6,7,8,8,9]
print(BinarySearchRecursion(arr, 0, len(arr) -1, 7))