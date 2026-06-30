import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        d = {}

        for i in range(len(nums)+1):
            buckets.append([])

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] = 1
        
        for num in d: 
            buckets[d[num]].append(num)
       
        print(buckets)
        

        toReturn = []
        for i in range(len(buckets)-1, 0, -1): 
            for num in buckets[i]: 
                toReturn.append(num)
                if len(toReturn) == k:
                    return toReturn
        return toReturn 
      
       

        