

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}
        counts = [[]] 

        for i in range(len(nums)+1):
            counts.append([])

        
        for i in range(len(nums)): 
            if nums[i] in hmap: 
                hmap[nums[i]] +=1
            else:
                hmap[nums[i]] = 1

        for key,val in hmap.items():
            counts[val].append(key)


        
        toReturn = []

        for i in range(len(counts), 0, -1): 
            for j in range(len(counts[i-1])):
                print(counts[i-1])
                toReturn.append(counts[i-1][j])
                if len(toReturn) == k:
                    return toReturn
                

        return []
                

                



            

        


        
