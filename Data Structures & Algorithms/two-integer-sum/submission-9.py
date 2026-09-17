class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i,v in enumerate(nums):
            dic[v] = i
        print(dic)

        for i in range(len(nums)):
            if target - nums[i] in dic and dic[target - nums[i]] != i:
                return [i,dic[target - nums[i]]]
        return []