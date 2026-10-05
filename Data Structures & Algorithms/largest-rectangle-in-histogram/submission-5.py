class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = float("-inf")
        stack = []
        for i in range(len(heights)):
            if stack: 
                if heights[i] < stack[-1][1]: 
                    while stack and heights[i] < stack[-1][1]: 
                        area = max(area, (i - stack[-1][0]) * stack[-1][1])
                        temp= stack.pop()
                    stack.append((temp[0], heights[i]))
                else: 
                    stack.append((i, heights[i]))
            else: 
                stack.append((i, heights[i]))

        print(stack)
        
        for i in range(len(stack),-1,-1): 
            area = max(area , (stack[i-1][1])*(len(heights)-stack[i-1][0]))
            

        return area

    

             



            
           

        