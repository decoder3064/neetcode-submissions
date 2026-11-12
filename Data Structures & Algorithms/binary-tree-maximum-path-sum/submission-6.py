# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        global_max = float("-inf")


        def dfs(root): 
            nonlocal global_max

            if not root:
                return 0

            left_sum  = max(dfs(root.left),0)
            right_sum = max(dfs(root.right),0)

            global_max = max(global_max, root.val + left_sum + right_sum)

            return root.val + max(right_sum, left_sum)
            
            
         

           
           

        dfs(root)

        return global_max
            


        