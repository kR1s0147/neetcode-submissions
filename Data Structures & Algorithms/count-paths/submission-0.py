class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.paths = 0

        def go(r,c):
            if r >= m or c >= n:
                return 
            if r == (m-1) and c == (n-1):
                self.paths+=1
            go(r+1,c)
            go(r,c+1)
        go(0,0)
        return self.paths