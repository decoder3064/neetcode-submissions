class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        sort= nums
        sort.sort()


        for i in range(len(sort)):
            
            init = sort[i]
            if i > 0  and sort[i-1] == init:
                continue 
            l = i+1
            r = len(sort)-1

            targ = -init
            while l < r: 
                if sort[l] + sort[r] == targ:
                    toReturn.append([sort[l], sort[r], init])
                    r-=1
                    l+=1
                    while l < r and sort[l] == sort[l-1]:
                        l+=1
                    while l< r and sort[r] == sort[r+1]:
                        r-=1
                elif sort[l] + sort[r] + init > 0:
                    r-=1
                else:
                    l+=1


        return toReturn




        