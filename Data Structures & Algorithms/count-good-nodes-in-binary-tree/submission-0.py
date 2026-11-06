# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good = [0] 
        mx = float('-inf')

        def dfs(root, good, mx):
        
            if not root:
                return
            
            if root.val >= mx:
                good[0] +=1
                mx = root.val
          
            right = dfs(root.right,good, mx)
            left = dfs(root.left,good, mx)

            


        dfs(root, good,mx)
        return good[0]

        