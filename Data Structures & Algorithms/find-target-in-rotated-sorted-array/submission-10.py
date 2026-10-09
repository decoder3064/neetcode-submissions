class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums) -1     
        while l<=r:
            mid = (l+r)//2
            pivot = mid
            if nums[l] < nums[r]:
                pivot = l
                break 
            if nums[l] <= nums[mid]: 
                l = mid+1 
            else: 
                r= mid 

        print(f"pivot {pivot}")

        if nums[pivot] <= target and target <= nums[-1]:
            print(nums[pivot])
            print(nums[-1])
            l = pivot 
            r = len(nums)-1
        else:
            r = pivot 
            l = 0

        print(f"l {l}")
        print(f"r {r}")

        while l <=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid - 1
            else: 
                return mid 
        return -1

            