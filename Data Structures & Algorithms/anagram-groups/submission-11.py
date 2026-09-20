import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d =  {}
      
        toReturn = []

        for ana in strs: 
            count  = [0] * 26 
            for letter in ana: 
                count[ord(letter) - ord('a')] += 1

            if tuple(count) in d: 
                d[tuple(count)].append(ana)
            else:
                d[tuple(count)] = [ana]

        for k,v in d.items(): 
            toReturn.append(v)

        return toReturn




            


        