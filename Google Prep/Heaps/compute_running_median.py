# Compute the Running Median
# Daily Coding Problem: Page 107

"""Compute the running median of a sequence of numbers.
That is given a stream of numbers, print out the median of the list so far after each new
element.
Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your
algorithm should print out:
2
1.5
2
3.5
2
2
2
"""

"""
SOLUTION
We'll use two heaps: min-heap and max-heap in our implementation.
We'll keep all the element larger than the median in a min-heap
and all the element smaller than the median in a max-heap.
As long as we keep these heaps the same size, we can guarantee that the
median is either the root of the min-heap or max-heap (or both).

Whenever, we encounter a new element from the stream, we'll first add it to one of our heaps:
the max-heap if the element is smaller than the median, or the min-heap
if it is bigger. If the element is equals to median, we'll arbitrarily choose to
add it to the min-heap.

Then we re-balance if necessary by moving the root of the larger heap to the smaller one.
This is only necessary if one heap is larger than the other by more than 1 element.

Finally, we can print our median. This will either be the root of the larger heap, 
or the average of the two roots if they're of equal size. We can save ourselves some trouble here by noting that
since the root of a heap occupies the initial index of the underlying array, geting the median simply involves
accessing heap[0].

COMPLEXITIES
Time: O(nlogn), since for each element we perform a constant number of 
heappush and heappop operations, each of which takes O(log n) in the 
worst case.
"""

import heapq

def get_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        return min_heap[0]

    elif len(min_heap) < len(max_heap):
        return -1 * max_heap[0]
    
    else:
        return (min_heap[0] + -1 * max_heap[0]) / 2.0
    


def add(num, min_heap, max_heap):
    # If empty, add to min_heap
    if len(min_heap) + len(max_heap) < 1:
        heapq.heappush(min_heap, num)
        return

    median = get_median(min_heap, max_heap)

    if num > median:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -1 * num)


def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * root)

    elif len(min_heap) < len(max_heap) + 1:
        root = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -1 * root)


def print_median(min_heap, max_heap):
    print(get_median(min_heap, max_heap))

def running_median(stream):
    min_heap = []
    max_heap = []
    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(max_heap, max_heap)