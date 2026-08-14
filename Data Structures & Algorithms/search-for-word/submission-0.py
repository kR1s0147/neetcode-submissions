class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return  False

        self.matched = False
        rows = len(board)
        cols = len(board[0])
        visited = []
        def dfs(r,c,k):
            if k == len(word):
                self.matched = True
                return
            if r <0 or c<0 or r >=rows or c >= cols  or board[r][c] != word[k] or [r,c] in visited:
                return 
            visited.append([r,c])
            dfs(r-1,c,k+1)
            dfs(r+1,c,k+1)
            dfs(r,c-1,k+1)
            dfs(r,c+1,k+1)
            visited.pop()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    dfs(r,c,0)
        return self.matched