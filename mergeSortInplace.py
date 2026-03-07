from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return Solution.mergeSortHelper(self, pairs, 0, len(pairs)-1)


    def mergeSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2

        self.mergeSortHelper(arr, s, m)
        self.mergeSortHelper(arr, m+1, e)

        self.merge(arr, s, m, e)

        return arr


    def merge(self, arr, s, m, e):
        leftArr = arr[:m+1]
        rightArr = arr[m+1:e+1]

        l = r = 0 # Counter for leftArr and rightArr
        i = s

        while l < len(leftArr) and r < len(rightArr):
            if leftArr[l].key <= rightArr[r].key:
                arr[i] = leftArr[l]
                l += 1
            else:
                arr[i] = rightArr[r]
                r += 1

            i += 1

        while l < len(leftArr):
            arr[i] = leftArr[l]
            l += 1
            i += 1

        while r < len(rightArr):
            arr[i] = rightArr[r]
            r += 1
            i += 1

        
