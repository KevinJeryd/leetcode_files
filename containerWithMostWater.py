from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPillar = 0
        rightPillar = len(heights) - 1

        maxArea = -1

        while leftPillar < rightPillar:
            currentArea = min(heights[leftPillar], heights[rightPillar]) * (rightPillar - leftPillar)

            if currentArea > maxArea:
                maxArea = currentArea
            
            if heights[leftPillar] < heights[rightPillar]:
                leftPillar += 1
            else:
                rightPillar -= 1
        
        return maxArea
