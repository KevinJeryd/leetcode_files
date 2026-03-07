from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 0:
            return []
        
        self.quickSortRec(pairs, 0, len(pairs) - 1)
        
        return pairs
    
    def quickSortRec(self, pairs, start, end):
        if end - start + 1 <= 1:
            return 

        pivot = pairs[end]

        leftPointer = start

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                tmp = pairs[leftPointer]
                pairs[leftPointer] = pairs[i]
                pairs[i] = tmp
                leftPointer += 1
        
        pairs[end] = pairs[leftPointer]
        pairs[leftPointer] = pivot

        self.quickSortRec(pairs, start, leftPointer -1)
        self.quickSortRec(pairs, leftPointer + 1, end)

