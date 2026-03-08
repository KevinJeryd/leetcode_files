import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            m = l + (r - l) // 2

            # If we manage to eat all within current eatSpeed, let's try to lower the eatSpeed
            if self.hasEatenUp(piles, m, h):
                r = m - 1
            else: # If not, try to increase it and see again
                l = m + 1
            
        return l


    def hasEatenUp(self, piles, eatSpeed, limit):
        sum = 0

        # Amount of hours to eat each pile at current eat speed
        for i in piles:
            sum += math.ceil(i / eatSpeed)
        
        # Return if we managed to eat all bananes within the limit or not
        return sum <= limit

