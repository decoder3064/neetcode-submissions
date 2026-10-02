class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        toReturn = [0] * len(temperatures)
        

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                past_i = stack.pop()
                toReturn[past_i] =  i-past_i 
            stack.append(i)


            
        return toReturn 
            
            
        