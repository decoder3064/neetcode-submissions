class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        if len(s) != len(t):
            return False 

        ct1 = 0
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]]=1

            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]]=1

        for i in range(len(s)):
            if s[i] not in d2 or d1[s[i]] != d2[s[i]]:
                return False 

        return True 
