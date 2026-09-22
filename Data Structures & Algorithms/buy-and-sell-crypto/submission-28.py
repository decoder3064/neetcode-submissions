class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l , r = 0 , 1

        mn = prices[l]
        mx = -999
        toReturn = 0
    
        while r < len(prices) and l < len(prices):    
            if prices[l] > prices[r]: 
                if  (r+1) < len(prices):
                    if prices[r] < mn:
                        mx = -1
                    mn = min (prices[r], mn)
                    l = r
                r+=1
            else:
                mx = max(prices[r], mx)
                r+=1

            toReturn = max(toReturn, mx-mn)

        return toReturn
            
        
      



            

            

                



            
        


            
        



        