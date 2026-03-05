from typing import List

"""
You are given an integer array nums of length n. 
Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n * 2
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans


def test(nums, expected):
    answer = Solution().getConcatenation(nums)
    assert answer == expected, f"Expected {expected}, got {answer}"
    print(f"PASSED: {answer}")

test([1,4,1,2], [1,4,1,2,1,4,1,2])
test([22,21,20,1], [22,21,20,1,22,21,20,1])
