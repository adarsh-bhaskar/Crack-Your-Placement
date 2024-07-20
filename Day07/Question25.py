# Leetcode 1499

from typing import List
import math
import heapq

# Approach 1: Using Max Heap
def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
    ans = -math.inf
    maxHeap = [] # (y - x, x)

    for x, y in points:
        while maxHeap and x + maxHeap[0][1] > k:
            heapq.heappop(maxHeap)
        if maxHeap:
            ans = max(ans, x + y - maxHeap[0][0])
        heapq.heappush(maxHeap, (x - y, -x))
    
    return ans

points = [[1, 3], [2, 0], [5, 10], [6, -10]]
k = 1
print(findMaxValueOfEquation(points, k))