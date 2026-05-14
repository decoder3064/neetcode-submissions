# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
   

        def dfs(self, node, mn, mx):
            if not node:
                return True    
            if not (mn < node.val < mx):
                return False  

            return dfs(self, node.left, mn, node.val) and dfs(self, node.right, node.val, mx) 


        return dfs(self,root, -99999999, 9999999999)



            



        