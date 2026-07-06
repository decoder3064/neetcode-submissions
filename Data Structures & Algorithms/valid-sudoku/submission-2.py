class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = {}

        for row in range(len(board)): 
            for col in range(len(board[row])):
                num = board[row][col]
                if num != '.' and num not in seen: 
                    seen[num] = [(row,col)]
                elif num != '.':
                    if not self.validate(seen[num],row,col):
                        return False 
                    seen[num].append((row,col))

        return True 
                    
    def validate(self, coord_list: List[int], row: int, col: int) -> bool:

        for coords in coord_list:
            if coords[0] == row or coords[1] == col:
                return False
            if ((row // 3) * 3 + (col // 3)) == ((coords[0] // 3) * 3 + (coords[1] //3)):
                return False 
        return True 

            

