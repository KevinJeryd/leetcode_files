from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = col = 0
        count = 0

        while row < len(grid):
            while col < len(grid[0]):
                if grid[row][col] == 1:
                    res = self.helper(grid, row, col)
                    count = max(count, res)
                col += 1
            col = 0
            row += 1

        return count

    def helper(self, grid, row, col):
        # Check out of bounds
        if min(row, col) < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
            return 0

        # Check if 0
        if grid[row][col] == 0:
            return 0

        currentArea = 0

        if grid[row][col] == 1:
            currentArea += 1
            grid[row][col] = 0
        
        currentArea += self.helper(grid, row+1, col)
        currentArea += self.helper(grid, row-1, col)
        currentArea += self.helper(grid, row, col+1)
        currentArea += self.helper(grid, row, col-1)

        return currentArea
