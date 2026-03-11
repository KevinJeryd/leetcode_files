from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        row = col = 0
        while row < len(grid):
            while col < len(grid[0]):
                if grid[row][col] == '1':
                    islands += 1
                    self.sinkConnected(grid, row, col)
                col += 1
            col = 0
            row += 1
        
        return islands

        
    def sinkConnected(self, grid, row, col):
        # Check if out of bounds, then move on
        if min(row, col) < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
            return

        # Check if it is a 0, then move on
        if grid[row][col] == '0':
            return
        
        # Check if it is a 1, then flip
        if grid[row][col] == '1':
            grid[row][col] = '0'
        
        self.sinkConnected(grid, row+1, col)
        self.sinkConnected(grid, row-1, col)
        self.sinkConnected(grid, row, col+1)
        self.sinkConnected(grid, row, col-1)
        

