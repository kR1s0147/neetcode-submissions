class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDia = set()
        negDia = set()

        res= []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in cols or (r + c) in posDia or (r-c) in negDia:
                    continue
                cols.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] ="Q"
                backtrack(r+1)
                cols.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] ="."
        backtrack(0)
        return res