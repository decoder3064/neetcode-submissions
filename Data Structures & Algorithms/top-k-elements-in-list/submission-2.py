class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]]  += 1
            else:
                count[nums[i]] = 1

        for num in count: 
            arr[count[num]].append(num)

        toReturn = []
        count = 0
        for i in range(len(arr)-1, -1, -1):
            j = 0
            if arr[i] != []:
                while count < k and j < len(arr[i]):
                    toReturn.append(arr[i][j])
                    count+=1
                    j+=1
                
        return toReturn
            
