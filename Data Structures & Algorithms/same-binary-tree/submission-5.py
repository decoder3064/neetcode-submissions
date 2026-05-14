# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = [] 

        if q == None and p == None:
            return True 
        elif q == None and p:
            return False 
        elif q and p == None:
            return False 
        
      

        stack1.append(p)
        stack2.append(q)

        while stack1 or stack2:
            node1 = stack1.pop() 
            node2 = stack2.pop()

            if node1.val != node2.val:
                return False 

            if node1.left and not node2.left: 
                return False 
            elif not node1.left and node2.left: 
                return False
            else:
                if(node1.left != None and node2.left != None):
                    stack1.append(node1.left)
                    stack2.append(node2.left)
                    
            if node1.right and not node2.right: 
                return False 
            elif not node1.right and node2.right: 
                return False 
            else:
                if(node1.right != None and node2.right != None):
                    stack1.append(node1.right)
                    stack2.append(node2.right)

        return True 

       

            


            

            
            
        