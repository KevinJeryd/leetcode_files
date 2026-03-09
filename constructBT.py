from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])

        splitIdx = 0

        for i in inorder:
            if i == preorder[0]:
                break

            splitIdx += 1

        root.left = self.buildTree(preorder[1:splitIdx+1], inorder[:splitIdx])
        root.right = self.buildTree(preorder[splitIdx+1:], inorder[splitIdx+1:])

        return root

