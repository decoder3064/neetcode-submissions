import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_piles = max(piles)
        sm = 0
        mn = max_piles

        l, r = 1,max_piles
        while  l <= r: 
            k = (l+r)//2
            sm = sum(math.ceil(x/k) for x in piles)
            if sm > h:
                l = k + 1
            else:
                mn = k
                r = k - 1
               
        return mn 

           


                 

        

        



                
        