# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_height = [float('-inf')]

        def traverse(root:Optional[TreeNode]) -> int: 
            if not root: 
                return 0

            left = traverse(root.left)
            right = traverse(root.right)
           
            if left+right > max_height[0]:
                max_height[0] = left+right

            return max(right, left)+1

      

        trav = traverse(root)
        return max_height[0]


            
        

        




        