# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        count = 0 
        counter = head

        while counter: 
            counter = counter.next 
            count+=1

        cycles = count//k 

        curr = head 
        join = curr 
        for cycle in range(cycles):
            start = curr 
            count = 0
            prev = None 
            while count < k and curr: 
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp 
                count+=1  

            
            if cycle == 0: 
                toReturn = prev
            else:
                join.next = prev

            join = start 
            
        join.next = curr
        return toReturn 

            

        
                


            
      


        




        