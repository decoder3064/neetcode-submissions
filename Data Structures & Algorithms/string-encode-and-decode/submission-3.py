class Solution:
    
    

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for st in strs: 
            ln = f"{len(st)}"
            encoded +=  ln + '#' + st

        return encoded
            
        
    
    def decode(self, s: str) -> List[str]:
        ln = len(s)
        ct = 0
        toReturn = []
        while ct < ln: 
            num = ''
            char = s[ct]
            while char != '#':
                if s[ct] != '#':
                    num += s[ct]
                ct +=1
                char = s[ct]
         
            decoded = ''
            for i in range(int(num)): 
                decoded += s[ct+1]
                ct +=1
            toReturn.append(decoded)
            ct+=1
        return toReturn 
