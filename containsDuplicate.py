from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                return True
            
        return False
