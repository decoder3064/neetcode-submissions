import string 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        d = {}
        toRet = []

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1 

            if tuple(count) in d:
                print(count) 
                d[tuple(count)].append(word)
            else: 
                d[tuple(count)] = [word]
        
        for key in d: 
            toRet.append(d[key])

        return toRet
            
        
        
     



             
                





    