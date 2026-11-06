# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        mn = float('-inf')
        mx = float('inf')

        def dfs(root,mx,mn):
            if not root:
                return True 

            if mx <= root.val or mn >= root.val:
                return False 
            
            return  dfs(root.right,mx,root.val) and dfs(root.left,root.val,mn)

        return dfs(root,mx,mn)
        
        

        



        

           
           
        