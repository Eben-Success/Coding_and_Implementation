import heapq

# Has Time complexity of O(logn)

nums = [10, 20, 43, 1,2 ,65, 17, 44 ,2, 3,1]

heapq.heapify(nums)

print(nums)

# heap is min heap by default.
print(heapq.heappop(nums))

heapq.heappush(nums, 978)
heapq.heappush(nums, 6)
print(nums)

# MAX HEAP
# Invert the numbers to turn them into max heap.
heapq._heapify_max(nums)
heapq.heappop(nums)
print(nums)
