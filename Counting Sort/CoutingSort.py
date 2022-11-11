def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cumulative count
    for i in range(1, 10):
        count[i] += count[i-1]

    # Find the index of each element of the original arrayin count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into orginal array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 1 ,5, 6, 2,5,7]
countingSort(data)
print("Sorted Array using Counting Sort: ")
print(data)