from typing import List

"""
You are given an array nums consisting of n elements where each element is an integer representing a color:

    0 represents red
    1 represents white
    2 represents blue

Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        countArr = [0, 0, 0]

        for num in nums:
            countArr[num] += 1

        counter = 0
        for i in range(len(countArr)):
            for _ in range(0, countArr[i]):
                nums[counter] = i
                counter += 1

