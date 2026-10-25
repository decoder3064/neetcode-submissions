# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr_1 = l1
        curr_2 = l2
        carry = 0
        toReturn = ListNode(0,None)
        prev = toReturn
        
        while curr_1 and curr_2: 
            sm = curr_1.val + curr_2.val + carry
            print(sm)
            if sm > 9: 
                carry = sm // 10 
                sm = sm % 10 
            else: 
                carry = 0 

            new_node = ListNode(sm, None)
            prev.next = new_node 
            prev = new_node

            curr_1 = curr_1.next 
            curr_2 = curr_2.next 
        
        while curr_1: 
            sm = curr_1.val + carry
            print(sm)
            if sm > 9: 
                carry = sm // 10 
                sm = sm % 10 
            else: 
                carry = 0 

            new_node = ListNode(sm, None)
            prev.next = new_node 
            prev = new_node

            curr_1 = curr_1.next 

        while curr_2: 
            sm = curr_2.val + carry
            print(sm)
            if sm > 9: 
                carry = sm // 10 
                sm = sm % 10 
            else: 
                carry = 0 

            new_node = ListNode(sm, None)
            prev.next = new_node 
            prev = new_node

            curr_2 = curr_2.next 

        
        if carry > 0: 
            new_node = ListNode(carry, None)
            prev.next = new_node 
            prev = new_node
            
        return toReturn.next 

                
            
            
       