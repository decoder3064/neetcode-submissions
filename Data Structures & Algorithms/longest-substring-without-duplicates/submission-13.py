class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        if len(s) == 0:
            return 0

        p1 , p2 = 0,0
        mx = -1
        seen = set()
        while p2 < len(s):
            if s[p2] not in seen:
                seen.add(s[p2])
                p2+=1
                mx = max(mx, p2 - p1)
            else:
                seen.remove(s[p1])
                p1+=1
                


           
        return mx 



