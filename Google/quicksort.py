# Time: O(nlogn)
# In worst case, quicksort takes O(n^2)
# In the average case, quicksort takes O(nlogn).

"""If merge sort and quicksort are both O(nlogn) time, quicksort is faster.
Quicksort is faster because it hits the average case way more often than the worst case.
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = [0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)



