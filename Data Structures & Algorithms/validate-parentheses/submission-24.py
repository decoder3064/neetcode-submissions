class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(':')', '{':'}','[':']'}
        stack = []

        if len(s) <= 1 or s[0] not in pars:
            return False 

        for i in range(len(s)): 
            if s[i] in pars:
                stack.append(s[i])
            elif stack: 
                comp = stack.pop()
                if pars[comp] != s[i]:
                    return False 
            else:
                return False
                
        return len(stack) == 0
                
    
        
       
        