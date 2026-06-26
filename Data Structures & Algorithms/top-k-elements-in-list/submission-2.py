import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] = 1

        pq = []
        for num in d: 
            heapq.heappush(pq, (-d[num], num ))

        print(pq)
        toReturn = []
        for top in range(k): 
           toReturn.append(heapq.heappop(pq)[1])
        
        return toReturn
      
       

        