import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d =  {}
      
        toReturn = []

        for ana in strs: 
            count  = [0] * 26 
            for letter in ana: 
                count[ord(letter) - ord('a')] += 1

            key = tuple(count)
            if key in d: 
                d[key].append(ana)
            else:
                d[key] = [ana]

        for k,v in d.items(): 
            toReturn.append(v)

        return toReturn




            


        