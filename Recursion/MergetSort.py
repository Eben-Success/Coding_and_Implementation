def MergeSort(arr):
    if len(arr) < 2:
        return arr
    
    result = []
    mid = arr // 2
    y = MergeSort(arr[:mid])
    z = MergeSort(arr[mid:])
    
    i, j  = 0, 0
    
    while (i < len(y) and j < len(z)):
        if y[i] < z[j]:
            result.append(y[i])
            i+=1
        else:
            result.append(z[j])
            j+=1
    
    result += y[i:]
    result += z[j:]
    return result
    