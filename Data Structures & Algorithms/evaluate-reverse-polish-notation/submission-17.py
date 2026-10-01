class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+','-','*','/'}

        for i in range(len(tokens)): 
            if tokens[i] not in operands: 
                stack.append(int(tokens[i]))
            else:

                to_process1= stack.pop()
                to_process2 = stack.pop()

                if tokens[i] == '+': 
                    stack.append(to_process2 + to_process1)
                if tokens[i] == '*':
                    stack.append(to_process2 * to_process1)
                if tokens[i] == '-':
                    stack.append(to_process2 - to_process1)
                if tokens[i] == '/':
                    stack.append(int(to_process2 / to_process1))
        return stack[0]
                        
                    
            
            
        