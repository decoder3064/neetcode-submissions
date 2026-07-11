class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        new_nums = set(nums)
        longest = 0

        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            if curr - 1 not in new_nums:
                while curr in new_nums:
                    if count > longest:
                        longest = count
                    count+=1
                    curr +=1
                    

        return longest 

        
        

            
            
        
        
            
            
                
            
            

