# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        st = set()
        while curr:
            print
            if curr in st:
                return True  
            else:
                st.add(curr)
            curr = curr.next

        return False 

            
