from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Leetcode expects [] as answer on empty input, not [[]]
        if len(pairs) == 0:
            return []
        
        # First state of intermediate state is the list in its initial state
        result = [list(pairs)]

        # We treat the first index as solved, since it's only itself
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                tmp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = tmp
                j -= 1
            result.append(list(pairs))

        return result
