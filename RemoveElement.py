from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

def test(nums, val, expected):
    answer = Solution().removeElement(nums, val)
    assert nums[:answer] == expected, f"Expected {expected}, got {nums[:answer]}"
    print(f"PASSED: {nums[:answer]}")

test([1,1,2,3,4], 1, [2,3,4])
test([0,1,2,2,3,0,4,2], 2, [0,1,3,0,4])

"""
Pattern: Two pointers

Why: The array is not sorted so we can't skip duplicates early, like in remove duplicates from sorted array.
     However, we only need to preserve relative order of non-val elements. 
     Two pointers lets us do this in-place in O(n) time and O(1) space.
     This is because the right pointer scans for non-val elements, and the left pointer keeps track where to put it

How: Have one pointer iterate through the list, for each position, check if it is the removal element,
     if it's not the removal element, we want to put it in our list. 
     The left pointer keeps track of where to put it in our list, increase with 1 for every non removal element
     If element == val we skip it, but don't advance the left pointer, effectively overwriting it when next non-val element comes
     Repeat and return leftmost pointer in the end since it will be equal to valid elements.
"""
