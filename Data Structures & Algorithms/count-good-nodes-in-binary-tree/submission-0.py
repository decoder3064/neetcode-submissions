# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        node = root 
        toReturn = 0
        count = [0]
        mx = -9999999

        def dfs(self, node, mx, count):
            if node == None:
                return 0

            if node.val >= mx:
                mx = node.val
                count[0] += 1
                
            dfs(self, node.right,mx,count)
            dfs(self, node.left,mx,count)
    
        
        dfs(self, root,mx,count)
        return count[0]
                
        

   
            



        