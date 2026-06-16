class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()

        if not nums:
            return False
            
        for i in range(len(nums)):
            if nums[i] in d: 
                return True 
            else:
                d.add(nums[i])

        return False 

        