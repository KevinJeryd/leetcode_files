from typing import List

"""
The solution basically banks on "flattening the matrix" and treating it as an array, without actually doing the flattening
Instead we calculate which row and col a index WOULD be on. So if we have index 12 in a matrix with 3 rows and 4 cols
We would calculate it's matrix index as row = 12 // cols, and col = 12 % cols
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        leftIndex = 0

        numRows = len(matrix)
        numCols = len(matrix[0])
        rightIndex = numRows * numCols - 1

        while leftIndex <= rightIndex:
            midIndex = leftIndex + (rightIndex - leftIndex) // 2

            midRow = midIndex // numCols
            midCol = midIndex % numCols

            if target > matrix[midRow][midCol]:
                leftIndex = midIndex + 1
            elif target < matrix[midRow][midCol]:
                rightIndex = midIndex - 1
            else:
                return True
        
        return False

