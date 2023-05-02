# find the smallest element in array >= target element.

def ceiling_number(arr, target):
    low = 0
    high = len(arr) - 1

    # if target > high:
    #     return -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [2,3,5,9,14,16,18]

print(ceiling_number(arr, 4))