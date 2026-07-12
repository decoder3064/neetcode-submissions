import string

class Solution:

    def normalize(self, s:str) -> str:
            vocab = string.ascii_letters + string.digits
            toReturn = []
            for char in s:
                if char in vocab:
                    toReturn.append(char.lower())
            return toReturn

    def isPalindrome(self, s: str) -> bool:

        normalized = self.normalize(s)
        right = len(normalized)-1
        left = 0

        print(normalized)
        alphan= string.ascii_letters + string.digits

        while right > left:
            if normalized[right] != normalized[left]:
                return False
            right-=1
            left+=1
    
        return True

        