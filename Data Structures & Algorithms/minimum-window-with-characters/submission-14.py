class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)  < len(t):
            return ""


        need = {}
        matches = {}
        subs = set()

        for i in range(len(t)):
            need[t[i]] = need.get(t[i],0)+1
            matches[t[i]] = matches.get(t[i],0)

        have = 0
        l = 0
        min_len = float("inf")
        min_idxs = [0,0] 
        for r in range(len(s)): 
            if s[r] in need:
                matches[s[r]]+=1
                if matches[s[r]] <= need[s[r]]:
                    have+=1
            #print(f"have {have}")
            while have == len(t):
                if r-l+1 < min_len: 
                    min_len = r-l+1
                    min_idxs = [l,r]
                if s[l] in need:
                    matches[s[l]]-=1
                    if matches[s[l]] < need[s[l]]:
                        have-=1
                l+=1
        if min_len == float("inf"):
            return ""

        return s[min_idxs[0]: min_idxs[1]+1]
        

           
                


                



            
        

        

                



