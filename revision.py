

def bubble_sort(arr):
    
    # swap = False
    
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                
                # swap = True
                
        # if not swap:
        #     break
        
    return arr

arr = [112, -9, 45, 3, 2, 56]

print(bubble_sort(arr))