class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        suffix = [0] * (len(nums)+1)
        toRet = []
        suffix[len(suffix)-1] = 1

        for i in range(len(nums)):
            prefix.append(nums[i] * prefix[i])
        
        for i in range(len(nums)-1, -1, -1):
            print(i)
            suffix[i] = nums[i] * suffix[i+1]
      
        for i in range(1, len(nums)+1): 
      
            toRet.append(prefix[i-1] * suffix[i])

        return toRet




        
