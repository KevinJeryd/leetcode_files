from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        tmp = deque([root])

        while len(tmp) > 0:
            newLevel = []
            for _ in range(len(tmp)):
                root = tmp.popleft()
                newLevel.append(root.val)
                if root.left:
                    tmp.append(root.left)
                if root.right:
                    tmp.append(root.right)

            res.append(newLevel)

        return res
        
