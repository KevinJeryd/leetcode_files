from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        # Hardcode first cell
        queue.append((0, 0))
        visit.add((0, 0))

        # Define which cell is destination
        destinationCell = (rows-1, cols-1)

        # Define all possible movements
        neighbors = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]]

        # Length = 1 since we already appended 0, 0
        length = 1

        while len(queue) > 0:
            # Go through current layer
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # If current cell is destination
                if (r, c) == destinationCell:
                    return length

                # Add all viable neighbors for the next layer
                for dr, dc in neighbors:
                    # Check if neighbor is outside, then skip
                    if min(r + dr, c + dc) < 0 or r + dr > rows - 1 or c + dc > cols - 1:
                        continue
                    
                    # Check if pos is 1, then skip
                    if grid[r + dr][c + dc] == 1:
                        continue
                    
                    #Check if already visited
                    if (r + dr, c + dc) in visit:
                        continue

                    visit.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
            length += 1
        
        return -1

