# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = [0]
        toReturn = [root]

        def  countNodes(root,k):
            if not root:
                return 
            left = countNodes(root.left,k)
            count[0]+=1
            if count[0] == k:
                toReturn[0] = root
            right = countNodes(root.right,k)
    
           


        countNodes(root,k)
        return toReturn[0].val



        