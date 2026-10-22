"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':



        curr = head 
        new_node= Node(0,None, None)
        new_head = new_node
        store = {}
    
        while curr: 
            new_node.next = Node(curr.val,None,None)
            new_node = new_node.next 
            if curr not in store: 
                store[curr] = new_node
            curr = curr.next 
            
        for key,val in store.items(): 
            if key.random:
                val.random = store[key.random]
            else:
                val.random = None

        return new_head.next 
        
       


        

    



        