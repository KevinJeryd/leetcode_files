from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            for j in range(len(res)): 
                newSet = res[j].copy()
                newSet.append(i)
                res.append(newSet)
                
        return res
