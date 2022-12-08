from heapq import heappushpop, heappush


def topKFrequent(nums, k):
    
    res = []
    dic = {}
    
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
            
    for key, val in dic.items():
        if len(res) < k:
            heappush(res, [val, key])
        else:
            heappushpop(res, [val, key])
    return [key for value, key in res]

    

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))