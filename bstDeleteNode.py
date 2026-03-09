from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSuccessor(self, root):
        if root.left == None:
            return root

        return self.findSuccessor(root.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # Find node to be deleted
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # Found node
            # Check if it's scenario where delete node only has 1 or 0 children
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else: # Delete node has 2 children, have to find the smallest node in the right subtree to replace deletion node
                successor = self.findSuccessor(root.right)
                root.val = successor.val # We don't set root = successor because we lose the pointers to the rest of the tree
                root.right = self.deleteNode(root.right, successor.val) # Delete the node after we switched it out

        return root

