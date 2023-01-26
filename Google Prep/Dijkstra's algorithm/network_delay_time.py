# times = (u, v, w)
 # u = source node
 # v = target node
 # w = time taken


# Dijskstra's Algorithm

from collections import defaultdict
import heapq

class Solution:
    def network_time_delay(times, n, k):
        
        # create adjacency list to store the times
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = ([0, k])
        time_taken = 0
        visited = set((0, k))

        while minHeap:
            cur_time, cur_node = heapq.heappop(minHeap)

            if cur_node in visited:
                continue
            visited.add(cur_node)

            time_taken = max(time_taken, cur_time)

            for nei, next_time in edges[cur_node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (cur_time + next_time, nei))

        return time_taken if len(visited) == n else -1
