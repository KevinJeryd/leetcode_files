from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        startRottenFruits = []

        # Find first rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    startRottenFruits.append((r, c))
        
        # No rotten fruit
        if len(startRottenFruits) == 0:
            # Check if there are any fresh fruits
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        return -1
            return 0

        queue = deque()
        visited = set()

        queue.extend(startRottenFruits)
        visited.update(startRottenFruits)

        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        time = 0

        while len(queue) > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                for dr, dc in neighbors:
                    # Check if out of bounds
                    if min(r + dr, c + dc) < 0 or r + dr > rows - 1 or c + dc > cols - 1:
                        continue
                    
                    # Skip if 0, don't care about it
                    if grid[r + dr][c + dc] != 1:
                        continue
                    
                    # If already visited, skip
                    if (r + dr, c + dc) in visited:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            time += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time - 1


