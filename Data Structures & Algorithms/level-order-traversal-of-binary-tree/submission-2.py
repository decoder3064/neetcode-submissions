from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        q.append(root)
        toReturn = []
        if not root:
            return toReturn
    
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node and node.left:
                    q.append(node.left)
                if node and  node.right:
                    q.append(node.right)

            toReturn.append(level)
        return toReturn
                

            
            
            
        


        
        
        