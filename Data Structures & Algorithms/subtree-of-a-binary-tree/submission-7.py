# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        
        def equalTrees(node, subRoot):
            queue1 = deque([node])
            queue2 = deque([subRoot])

            while queue1 or queue2:
                levelp = len(queue1)
                levelq = len(queue2)

                if levelp != levelq:
                    return False
                
                for i in range(levelp):
                    node1 = queue1.popleft()
                    node2 = queue2.popleft()
                    if (node1 == None and node2 != None) or (node1 != None and node2 == None):
                        return False
                    if node1 == None and node2 == None:
                        continue
                    if node1.val != node2.val:
                        return False
                    if node1.left:
                        queue1.append(node1.left)
                    else:
                        queue1.append(None)
                    if node1.right:
                        queue1.append(node1.right)
                    else:
                        queue1.append(None)
                    if node2.left:
                        queue2.append(node2.left)
                    else:
                        queue2.append(None)
                    if node2.right:
                        queue2.append(node2.right)
                    else:
                        queue2.append(None)
            return True


        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if node == None:
                    continue
                if node.val == subRoot.val:
                    if equalTrees(node, subRoot):
                        return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False