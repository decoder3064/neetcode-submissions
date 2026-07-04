class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count_zeros = 0
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zeros += 1
            else:
                print(f'prod {prod}')
                prod *= nums[i]

    
        if count_zeros > 1:
            return [0] * len(nums)
        

        res = []
        
        for i in range(len(nums)):
            if count_zeros == 1:
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // nums[i])
        return res 
            
            
            

            

                
            
        
            
    
          
        return toReturn 

            
