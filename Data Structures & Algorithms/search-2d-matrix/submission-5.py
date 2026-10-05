class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        


        for i in range(len(matrix)):
            

            if matrix[i][0]<= target and matrix[i][-1] >= target:
                print(matrix[i])

                r = len(matrix[i])-1
                l = 0 
                while l <= r:
                    mid = (r+l )// 2 
                    if matrix[i][mid] < target:
                        l = mid+1 
                    elif matrix[i][mid] > target:
                        r = mid -1
                    else:
                        return True 
        return False 
                    
