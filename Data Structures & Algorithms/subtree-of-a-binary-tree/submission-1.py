# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def check(root, subroot):
            if not root and not subroot:
                return True 
            if root and subroot and root.val == subroot.val:
                return (check(root.right, subroot.right) 
                        and check(root.left, subroot.left))
            return False 

        if check(root, subroot):
            return True 

        r = root.right 
        l = root.left 

        while r:
            if check(r, subroot):
                return True 
            r = r.right 
        while l:
            if check(l, subroot):
                return True 
            l = l.left
        return False 