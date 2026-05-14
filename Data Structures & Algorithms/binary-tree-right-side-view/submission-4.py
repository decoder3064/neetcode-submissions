# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        q = deque()
        q.append(root)
        toReturn = []
        while q: 
            rightSide = None 
            levelLen = len(q)
            print(q)
            for i in range(levelLen):
                node = q.popleft()
                if node: 
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:        
                toReturn.append(rightSide.val)
            
        return toReturn
            

            
                

            
            
            
                
            
        


        
        

        


        
            
            
        