# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return 

        curr = head
        prev = None 
        while curr: 
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp 

        count = 1
        back = prev 
        before = None

        while count < n:
            before = back 
            back = back.next  
            count +=1
        
        if before: 
            before.next = back.next 
            back.next = None 
        else:
            prev = back.next
            back.next = None 

        

        
        curr = prev
        prev = None 
        while curr: 
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp 

        return prev 


        

        



        