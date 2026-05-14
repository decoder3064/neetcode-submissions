class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dic1 = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in dic1:
                dic1[char] = dic1[char]+1
            else:
                dic1[char] = 1
        
        dic2 = {}
        for char in t:
            if char in dic2:
                dic2[char] = dic2[char]+1
            else:
                dic2[char] = 1
        
        for entry in dic1:
            if entry not in dic2:
                return False 
            if dic1[entry] != dic2[entry]:
                return False 

            
                
            
        
        return True 


        