from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        if k == 0:
            return root.val
            
        orderedArr = []

        self.inorderTraversal(root, orderedArr)

        return orderedArr[k-1]
    

    def inorderTraversal(self, root, arr):
        if root is None:
            return

        self.inorderTraversal(root.left, arr)
        arr.append(root.val)
        self.inorderTraversal(root.right, arr)
