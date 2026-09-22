# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.val = True
        def maxDepth(root):
            if not root:
                return 0
            leftdepth = maxDepth(root.left)
            rightdepth = maxDepth(root.right)

            if abs(leftdepth - rightdepth) > 1:
                self.val = False
            return 1 + max(leftdepth, rightdepth)
        
        maxDepth(root)
        return self.val