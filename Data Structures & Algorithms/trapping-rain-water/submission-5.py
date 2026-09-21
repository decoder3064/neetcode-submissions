class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1 

        maxL = height[l]
        maxR = height[r]
    
        total = 0

        while l < r:

            if height[l] <= height[r]:
                l+=1
                water = maxL - height[l]
                if water >=0:
                    total+= water
                maxL = max(maxL, height[l])
            else:
                r-=1
                water = maxR - height[r]
                if water >=0:
                    total+= water
                maxR = max(maxR, height[r])

                

        
        return total 

            





        
             