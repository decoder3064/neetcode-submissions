class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1 


        total = len(nums1) + len(nums2)
        half = (total)//2 

       
        l = 0
        r = len(A)  

        while True: 

            mid_a = ((l+r) //2) 
            b_bound = half - mid_a  
            
            Aleft = A[mid_a-1] if mid_a > 0 else float("-inf")
            Aright = A[mid_a] if mid_a < len(A) else float("inf")
            Bleft = B[b_bound-1] if b_bound > 0 else float("-inf")
            Bright = B[b_bound] if b_bound < len(B) else float('inf')

            

            if  not Bleft <= Aright:
                l = mid_a  +1
            elif not Aleft <= Bright:
                r = mid_a -1
            else:
                break 
 
        
        if total %2 == 1:
            median = min(Aright, Bright)
        else: 
            mx = max(Aleft, Bleft)
            mn = min(Aright, Bright)
            median = (mx+mn)/2


        return median 

        


            

