class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row =[set() for _ in range(9)]
        cols=[set()  for _ in range(9)]
        sq=[set()  for _ in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                index = (i//3)*3 +(j//3)
                if board[i][j] in row[i] or board[i][j] in cols[j] or board[i][j] in sq[index]:
                    return False
                else :
                    row[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sq[index].add(board[i][j])  
        return True