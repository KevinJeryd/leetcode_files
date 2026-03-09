from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        levels = []

        queue = deque([root])

        while len(queue) > 0:
            newLevel = []
            
            for _ in range(len(queue)):
                root = queue.popleft()
                newLevel.append(root.val)
                
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
                
            levels.append(newLevel)

        res = []
        for level in levels:
            res.append(level[0])

        return res

