class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        toReturn = {}
        vocab = 'abcdefghijklmnopqrstuvwxyz'

        index = 0
        for s in strs:
            count = [0]* 26
            for i in range(len(s)):
                for j in range(len(vocab)): 
                    if s[i] == vocab[j]:
                        count[j] +=1
            
            if tuple(count) in toReturn:
                toReturn[tuple(count)].append(s)
            else:
                ls = []
                ls.append(s)
                toReturn[tuple(count)] = ls 

        list2r = []
        for entry in toReturn:
            list2r.append(toReturn[entry])

        return list2r
                
               


                

        