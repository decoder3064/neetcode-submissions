class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          
        if len(nums) == 0:
            return 0
            
        new_nums = set(nums)
        longest = 0
        for i in range(len(nums)):
            verify = nums[i] - 1
            count = 0
            while verify in new_nums:
                verify = verify -1
                count +=1
                if count > longest: 
                    longest = count

        return longest +1

        
        

            
            
        
        
            
            
                
            
            

