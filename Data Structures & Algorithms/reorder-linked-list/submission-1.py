from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s = head 
        f = head.next 

        while f and f.next: 
            s = s.next
            if f.next: 
                f = f.next.next 
       

        prev = None 
        curr = s.next
        s.next = None 

        while  curr:
            #print(curr.val)
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp 
        
     
        start = head
        first_half = start.next 
        sec_half = prev

        switch = 1

        while first_half and sec_half: 
            if switch % 2 == 0: 
                start.next = first_half
                first_half = first_half.next
                start = start.next 
            else: 
                start.next = sec_half
                sec_half = sec_half.next 
                start = start.next 
            switch+=1

        while first_half: 
            start.next = first_half
            first_half = first_half.next
            start = start.next 

        while sec_half:
            start.next = sec_half
            sec_half = sec_half.next 
            start = start.next 

      


        #while first_half: 



        



            
            



     
        
        
            
            


    



        
        
       
        




        


   
            
            
            
            
        
        

        
        