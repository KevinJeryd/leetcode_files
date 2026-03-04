from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

# Test cases
sol = Solution()

# Test 1
nums = [1, 1, 2]
k = sol.removeDuplicates(nums)
print(f"k={k}, nums={nums[:k]}")  # Expected: k=2, nums=[1,2]

# Test 2
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)
print(f"k={k}, nums={nums[:k]}")  # Expected: k=5, nums=[0,1,2,3,4]

"""
Pattern: Two pointers

Why: The pattern works perfect because one pointer is used to check for duplicates, 
     and one is used to keep track on where to put the next unique number.

How: We now that the 0th index will always be unique, so we start iterating from 1.
     Check the current with the previous, if it's not the same we know it's unique because the list is ordered.
     If it's unique, insert it at the left pointer position and increase the left pointer.
     Repeat and return leftmost pointer in the end.
"""
