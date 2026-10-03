class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        


        combined = []
        for i in range(len(position)): 
            car = (position[i],speed[i])
            combined.append(car)
        
        combined.sort(reverse=True)

        stack = []

        for i in range(len(combined)):
            compute = (target - combined[i][0])/combined[i][1]
            if stack and compute <= stack[-1]:
                pass
            else:
                stack.append(compute)
        print(stack)
        
        return len(stack)

