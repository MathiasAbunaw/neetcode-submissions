class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            res = set()
            for j in board[i]:
                if j == ".":
                    continue
                elif j in res:
                    return False
                res.add(j)

        for i in range(9):
            res = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in res:
                    return False
                res.add(board[j][i])

        for square in range(9):
            res = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] ==  ".":
                        continue
                    elif board[row][col] in res:
                        return False
                    res.add(board[row][col])
        return True

        
                    