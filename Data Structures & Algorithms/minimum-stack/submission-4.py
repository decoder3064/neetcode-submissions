class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        self.minima = []
        

    def push(self, val: int) -> None:
        if val <= self.minimum:
            self.minimum = val
            self.minima.append(val)

        self.stack.append(val)
        

    def pop(self) -> None:
        evl = self.stack.pop()
        if len(self.stack) == 1: 
            self.minimum == self.stack[0]
        if evl == self.minimum:
            self.minima.pop()
            if self.minima:
                self.minimum = self.minima[-1]
            else:
                self.minimum = float('inf')
        

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
         

