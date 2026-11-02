# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        toReturn = [True]
        def dfs (p, q):

            if p and q:
                dfs(p.right,q.right)
                dfs(p.left, q.left)
                if p.val == q.val:
                    return True 

            if not p and not q:
                return True 
            toReturn[0] = False 
            return False 
        dfs(p, q)
        return toReturn[0]
          



        