# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.curr_dia = 0

        def maxDepth(root):
            if not root:
                return 0
            leftdepth = maxDepth(root.left)
            rightdepth = maxDepth(root.right)
            total = leftdepth + rightdepth
            if total > self.curr_dia:
                self.curr_dia = total
            return 1 + max(leftdepth, rightdepth)
        
        maxDepth(root)
        return self.curr_dia
        