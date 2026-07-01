class Solution:
    
    

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for st in strs: 
            ln = f"{len(st)}"
            encoded +=  ln + '#' + st

        print(encoded)
        return encoded
            
        
        
        

    def decode(self, s: str) -> List[str]:
        ln = len(s)
        ct = 0
        toReturn = []
        while ct < ln: 
            num = ''
            char = s[ct]
            print('char ' + char)
            while char != '#':
                if s[ct] != '#':
                    num += s[ct]
                    print(num)
                ct +=1
                char = s[ct]

            print('AFTER ' + num)
            print(f'count {ct}')
         
            decoded = ''
            for i in range(int(num)): 
                decoded += s[ct+1]
                ct +=1
                print(f'count {ct}')
            toReturn.append(decoded)
            ct+=1
        
        
        return toReturn 
