# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            levelp = len(queue1)
            levelq = len(queue2)
            if levelp != levelq:
                return False
            
            for i in range(levelp):
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                if node1 == None and node2 != None:
                    return False
                if node1 != None and node2 == None:
                    return False
                if node1 == None and node2 == None:
                    break
                if node1.val != node2.val:
                    return False
                queue1.append(node1.left)
                queue2.append(node2.left)
                queue1.append(node1.right)
                queue2.append(node2.right)
        
        return True