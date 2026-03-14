from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0

        maxPrice = 0
        while r < len(prices):
            # Means we have a lower buy than sell, which means more profit
            if prices[l] < prices[r]:
                maxPrice = max(maxPrice, prices[r] - prices[l])
            else: # We have found a cheaper buy option
                l = r
            r += 1
        
        return maxPrice

