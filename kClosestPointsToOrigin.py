from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for pair in points:
            dist = pow(pair[0] - 0, 2) + pow(pair[1] - 0, 2)
            heapq.heappush(maxHeap, (-dist, pair))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for _ in range(len(maxHeap)):
            dist, pair = heapq.heappop(maxHeap)
            res.append(pair)

        return res
