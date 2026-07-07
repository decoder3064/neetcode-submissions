class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        block = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):

                x = r // 3 
                y = c // 3

                if board[r][c] in rows[r]:
                    return False 
                if board[r][c] in cols[c]:
                    return False 
                if board[r][c] in block[(x,y)]: 
                    return False 
                if board[r][c] != '.':
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    block[(x,y)].add(board[r][c])
        return True 
            

