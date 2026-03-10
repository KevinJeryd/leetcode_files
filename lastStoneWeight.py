from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap by negating all values, largest value will now become smallest value
        # Then un-negate when popping
        for i  in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            stoneX = -heapq.heappop(stones)
            stoneY = -heapq.heappop(stones)

            if stoneX < stoneY:
                stoneY = stoneY - stoneX
                heapq.heappush(stones, -stoneY)
            elif stoneY < stoneX:
                stoneX = stoneX - stoneY
                heapq.heappush(stones, -stoneX)

        stones.append(0)

        return -stones[0]
