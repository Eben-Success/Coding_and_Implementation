def sliding_window(arr, k):
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    for i in range(1, len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray - arr[i+k-1]

        result.append(curr_subarray)

    return result