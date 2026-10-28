import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        toReturn = ListNode()
        min_heap = []
        if not lists:
            return

        for head in lists: 
            if head:
                heapq.heappush(min_heap, (head.val, id(head),head))

        curr = toReturn
        while min_heap:
            smallest = heapq.heappop(min_heap)[2]
            curr.next = smallest 
            curr = smallest 
            if smallest.next: 
                heapq.heappush(min_heap, (smallest.next.val,id(smallest.next) ,smallest.next))

        return toReturn.next 
            




        
            
            



        