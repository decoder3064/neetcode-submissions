import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
     
        normal = self.normalize(s)
        left = 0
        right = len(normal)-1

        if len(normal) <= 1:
            return True

        if normal[left] != normal[right]:
            return False

        
        while right > left:
            comp1 = normal[left]
            comp2 = normal[right]
            if  comp1 != comp2:
                return False

            right-=1
            left+=1
        return True 
            
            
    def is_char(self, s:str)->bool:
        full_alphabet = string.ascii_letters
        if s in full_alphabet or s in "0123456789":
            return True 
        return False

    def normalize(self, s:str)->str:
        toReturn = ""

        for char in s:
            if self.is_char(char):
                toReturn+=char.lower()
        return toReturn

