from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        my_deque = deque()
        next = head.next

        while next:
            my_deque.append(next)
            print(next.val)
            next = next.next 

        marker = head 
        switch = 1
        while my_deque: 
            if switch % 2 == 1: 
                to_add = my_deque.pop()
                print(f"pass {to_add.val}")
            else:
                to_add = my_deque.popleft()
                print(f"not pass {to_add.val}")
                
            to_add.next = None 
            marker.next = to_add
            if marker.next: 
                marker = marker.next
            switch +=1

        print(marker.val)



        
        
       
        




        


   
            
            
            
            
        
        

        
        