from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target > nums[m]: # We know that target is in right half, move left to midway point to cut list in half
                l = m + 1
            elif target < nums[m]: # We know that target is in left half
                r = m - 1
            else:
                return m # If it's neither, it means it's equal so we found
            
        return -1 # If we didn't find target throughout the loop, it doesn't exist
