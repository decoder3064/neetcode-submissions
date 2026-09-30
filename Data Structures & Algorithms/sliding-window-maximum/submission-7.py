from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k > len(nums):
            return []
        l = 0 
        q = deque()
        toReturn = []
        for r in range(len(nums)): 
            to_add = nums[r]
            if q: 
                    back = len(q)
                    while back > 0 and to_add >= q[back-1][0]:
                        q.pop()
                        back-=1
                    q.append((to_add,r))
            else:
                q.append((to_add,r))

            if r-l+1 == k:
                    toReturn.append(q[0][0])
                    l+=1
            if l > q[0][1]:
                q.popleft() 

        return toReturn 


            




        

        