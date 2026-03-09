from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)

    def helper(self, root, targetSum, currentSum):
        if root is None:
            return False

        # We are at leaf node
        if root.left is None and root.right is None:
            return currentSum + root.val == targetSum
        
        resLeft = self.helper(root.left, targetSum, currentSum + root.val)
        resRight = self.helper(root.right, targetSum, currentSum + root.val)

        return resLeft or resRight
