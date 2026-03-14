from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index, fixedNum in enumerate(nums):
            # We can break if fixedNum is larger than 0, because it is guaranteed to be the smallest num in the array
            # So we can never get 0 if fixedNum is larger.
            if fixedNum > 0:
                break
            
            if index > 0 and fixedNum == nums[index - 1]:
                continue
            
            left = index + 1
            right = len(nums) - 1

            while left < right:
                sum = fixedNum + nums[left] + nums[right]
                if sum == 0:
                    res.append([fixedNum, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
            
        return res
