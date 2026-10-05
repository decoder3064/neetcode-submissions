class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL = len(matrix), len(matrix[0])


        
        bot, top = 0,ROW-1 
        while bot<=top:
            row = (bot+top)//2
            if target > matrix[row][-1]:
                bot = row+1
            elif target < matrix[row][0]: 
                top = row-1 
            else:
                break

        print(row)
        if not (bot <=top):
            return False 

        l , r = 0, COL-1
        while l <= r:
            mid = (r+l )// 2 
            if matrix[row][mid] < target:
                l = mid+1 
            elif matrix[row][mid] > target:
                r = mid -1
            else:
                return True 
        return False 
                    
