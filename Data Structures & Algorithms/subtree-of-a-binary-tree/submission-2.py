# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    check = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(p, q):
            if not p and not q:
                return True 
            if not p or not q or p.val != q.val:
                return False 
            return isSame(p.right, q.right) and isSame(p.left, q.left)

        if not root:
            return False

        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)
    
        if(isSame(root,subRoot)):
            self.check = True 
        return self.check
        
    
        
