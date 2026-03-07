from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 1 or len(pairs) == 0:
            return pairs

        firstHalf = pairs[:len(pairs)//2]
        secondHalf = pairs[len(pairs)//2:]

        sortedFirstHalf = Solution.mergeSort(self, firstHalf)
        sortedSecondHalf = Solution.mergeSort(self, secondHalf)

        return Solution.merge(self, sortedFirstHalf, sortedSecondHalf)

    def merge(self, list1, list2):
        output = []

        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if list1[i].key <= list2[j].key:
                output.append(list1[i])
                i += 1
            else:
                output.append(list2[j])
                j += 1

        output.extend(list1[i:] or list2[j:])

        return output


            

