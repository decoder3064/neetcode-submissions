class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        st = set()

        for i in range(len(nums)):
            if nums[i] in st:
                st.remove(nums[i])
            else: 
                st.add(nums[i])
            
        

        return st.pop()
            
        