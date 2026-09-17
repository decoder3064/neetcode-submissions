class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = -1

        r= len(heights)-1
        l= 0

        while l < r: 
            height = min(heights[l],heights[r]) 
            width = r - l 

            if height * width > mx:
                mx = height * width 
            
            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else: 
                r-=1
                l+=1
        return mx
                
            



        